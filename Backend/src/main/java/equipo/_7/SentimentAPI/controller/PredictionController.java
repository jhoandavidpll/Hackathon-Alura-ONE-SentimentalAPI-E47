package equipo._7.SentimentAPI.controller;

import equipo._7.SentimentAPI.domain.prediction.DataPredictions;
import equipo._7.SentimentAPI.domain.prediction.DataSimplePrediction;
import equipo._7.SentimentAPI.domain.prediction.Prediction;
import equipo._7.SentimentAPI.domain.prediction.PredictionRepository;
import jakarta.transaction.Transactional;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.web.PageableDefault;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/predict")
public class PredictionController {

    @Autowired
    private PredictionRepository repository;

   @Transactional
@PostMapping
public ResponseEntity simplePrediction(@RequestBody @Valid DataSimplePrediction json) {

    Prediction prediction = new Prediction(json);

    repository.save(prediction);

    return ResponseEntity.ok(new DataPredictions(prediction));
}

    @GetMapping
    public Page<DataPredictions> predictions(@PageableDefault(size=10, sort={"prevision"}) Pageable pageable) {
        return repository.findAll(pageable).map(DataPredictions::new);
    }

    @Transactional
    @DeleteMapping("/{id}")
    public void deletePredictions(@PathVariable Long id) {
        repository.deleteById(id);
    }

    @GetMapping("/{id}")
    public DataPredictions singlePrediction(@PathVariable Long id) {
        var prediction =  repository.findById(id);
        if (prediction.isEmpty()) {
            throw new RuntimeException("Prediction not found");
        }
        return new DataPredictions(prediction.get());
    }
}
