package equipo._7.SentimentAPI.controller;

import com.opencsv.CSVReader;
import com.opencsv.exceptions.CsvException;
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
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/predict")
public class PredictionController {

    @Autowired
    private PredictionRepository repository;

   @Transactional
@PostMapping
public ResponseEntity<DataPredictions> simplePrediction(@RequestBody @Valid DataSimplePrediction json, UriComponentsBuilder uriComponentsBuilder) {
    Prediction prediction = new Prediction(json);
    repository.save(prediction);
    var uri = uriComponentsBuilder.path("/predict/{id}").buildAndExpand(prediction.getId()).toUri();
    return ResponseEntity.created(uri).body(new DataPredictions(prediction));
}

    @GetMapping
    public ResponseEntity<Page<DataPredictions>> predictions(@PageableDefault(size=10, sort={"prevision"}) Pageable pageable) {
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
    public ResponseEntity<List<DataSimplePrediction>> csvPrediction(
            @RequestParam(value = "archivo")
            @NotNull(message = "Es necesario un arhivo del tipo csv")
            MultipartFile file) throws IOException {
       if (file.isEmpty()) {
           return ResponseEntity.badRequest().build();
       }
       if(!file.getOriginalFilename().endsWith(".csv")) {
           return ResponseEntity.status(HttpStatus.BAD_REQUEST).build();
       }

       List<DataSimplePrediction> predictions = new ArrayList<>();

       // Analizador del csv
        try (BufferedReader reader = new BufferedReader(
                new InputStreamReader(file.getInputStream(), StandardCharsets.UTF_8));
            CSVReader csvReader = new CSVReader(reader)
        ) {
            List<String[]> registros = csvReader.readAll();
            if (registros.isEmpty()) {
                return ResponseEntity.badRequest().build();
            }
            String[] header = registros.get(0);
            int headerIndex = -1;
            String columnName = "comentarios";
            for (int i = 0; i < header.length; i++) {
                if (header[i].trim().equalsIgnoreCase(columnName)) {
                    headerIndex = i;
                }
            }
            if (headerIndex == -1) {
                return ResponseEntity.badRequest().build();
            }
            for (int i = 1; i < registros.size(); i++) {
                String[] row = registros.get(i);
                if (row.length > headerIndex) {
                    String comentario = row[headerIndex];
                    if (!comentario.isEmpty()) {
                        var data = new DataSimplePrediction(comentario);
                        predictions.add(data);
                    }
                }
            }
        } catch (CsvException e) {
            throw new RuntimeException(e);
        }
        return ResponseEntity.ok(predictions);
    }
}
