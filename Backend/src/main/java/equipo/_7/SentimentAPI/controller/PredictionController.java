package equipo._7.SentimentAPI.controller;

import equipo._7.SentimentAPI.prediction.DatosSimplePrediction;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/predict")
public class PredictionController {
    @PostMapping
    public void simplePrediction(@RequestBody DatosSimplePrediction json) {
        System.out.println(json);
    }
}
