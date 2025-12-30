package equipo._7.SentimentAPI.controller;

import equipo._7.SentimentAPI.prediction.DatosSimplePrediction;
import equipo._7.SentimentAPI.prediction.Prediction;
import equipo._7.SentimentAPI.prediction.PredictionRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/predict")
public class PredictionController {

    @Autowired
    private PredictionRepository repository;

    @PostMapping
    public void simplePrediction(@RequestBody DatosSimplePrediction json) {
        repository.save(new Prediction(json));
        System.out.println(json);
    }
}
