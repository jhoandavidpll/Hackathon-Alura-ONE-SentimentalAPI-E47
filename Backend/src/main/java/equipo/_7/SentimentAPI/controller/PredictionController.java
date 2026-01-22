package equipo._7.SentimentAPI.controller;

import ai.onnxruntime.OrtException;
import com.opencsv.CSVReader;
import com.opencsv.exceptions.CsvException;
import equipo._7.SentimentAPI.domain.model.OnnxService;
import equipo._7.SentimentAPI.domain.prediction.*;
import jakarta.transaction.Transactional;
import jakarta.validation.Valid;
import jakarta.validation.constraints.NotNull;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.web.PageableDefault;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.util.UriComponentsBuilder;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/predict")
public class PredictionController {

    @Autowired
    private PredictionRepository repository;

    @Autowired
    private OnnxService onnxService;

    @Transactional
    @PostMapping
    public ResponseEntity<?> simplePrediction(
            @RequestBody @Valid DataSimplePrediction json,
            UriComponentsBuilder uriComponentsBuilder) {
        try {
            // Cambiar el modelo antes de predecir
            onnxService.cargarModelo(json.model());

            Prediction prediction = new Prediction(json);
            var resultadoModelo = onnxService.predict(json.text());

            prediction.asignarResultado(resultadoModelo);
            repository.save(prediction);

            var uri = uriComponentsBuilder.path("/predict/{id}").buildAndExpand(prediction.getId()).toUri();
            return ResponseEntity.created(uri).body(new DataPredictions(prediction));
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body("Error: " + e.getMessage());
        }
    }

    @GetMapping
    public ResponseEntity<Page<DataPredictions>> predictions(@PageableDefault(size=10, sort={"id"}) Pageable pageable) {
        var page = repository.findAll(pageable).map(DataPredictions::new);
        return ResponseEntity.ok(page);
    }

    @Transactional
    @DeleteMapping("/{id}")
    public ResponseEntity deletePredictions(@PathVariable Long id) {
       repository.deleteById(id);
       return ResponseEntity.noContent().build();
    }

    @GetMapping("/{id}")
    public ResponseEntity<DataPredictions> singlePrediction(@PathVariable Long id) {
        var prediction =  repository.getReferenceById(id);
        return ResponseEntity.ok(new DataPredictions(prediction));
    }

    @PostMapping(value = "/csv", consumes = MediaType.MULTIPART_FORM_DATA_VALUE)
    public ResponseEntity<List<DataPredictions>> csvPrediction(
            @RequestParam(value = "archivo")
            @NotNull(message = "Es necesario un archivo del tipo csv")
            MultipartFile file,
            @RequestParam(value = "modelo")
            @NotNull(message = "Es necesario especificar el idioma (ES, PT)")
            Language model) throws Exception {
        onnxService.cargarModelo(model);

        if (file.isEmpty() || !file.getOriginalFilename().endsWith(".csv")) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).build();
        }

        List<DataPredictions> resultList = new ArrayList<>();

        try (BufferedReader reader = new BufferedReader(
                new InputStreamReader(file.getInputStream(), StandardCharsets.UTF_8));
             CSVReader csvReader = new CSVReader(reader)
        ) {
            List<String[]> registros = csvReader.readAll();
            if (registros.isEmpty()) return ResponseEntity.badRequest().build();

            // Localizar la columna "comentarios"
            String[] header = registros.get(0);
            int headerIndex = -1;
            for (int i = 0; i < header.length; i++) {
                if (header[i].trim().equalsIgnoreCase("comentarios")) {
                    headerIndex = i;
                    break;
                }
            }

            if (headerIndex == -1) return ResponseEntity.badRequest().build();

            // Procesar cada fila
            for (int i = 1; i < registros.size(); i++) {
                String[] row = registros.get(i);
                if (row.length > headerIndex && !row[headerIndex].isEmpty()) {
                    String comentario = row[headerIndex];

                    // 1. Crear entidad y DTO de entrada
                    DataSimplePrediction dataInput = new DataSimplePrediction(comentario, model);
                    Prediction prediction = new Prediction(dataInput);

                    // 2. Realizar inferencia con el modelo ONNX
                    try {
                        var resultadoModelo = onnxService.predict(comentario);
                        prediction.asignarResultado(resultadoModelo); // Asigna previsión y probabilidad
                    } catch (OrtException e) {
                        continue;
                    }

                    // 3. Persistir en la base de datos
                    repository.save(prediction);

                    // 4. Agregar a la lista de respuesta usando el DTO de salida
                    resultList.add(new DataPredictions(prediction));
                }
            }
        } catch (CsvException e) {
            throw new RuntimeException("Error al leer el archivo CSV", e);
        }

        return ResponseEntity.ok(resultList);
    }
}
