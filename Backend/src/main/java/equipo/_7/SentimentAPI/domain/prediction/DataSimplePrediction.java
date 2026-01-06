package equipo._7.SentimentAPI.prediction;

import jakarta.validation.constraints.NotBlank;

public record DataSimplePrediction(@NotBlank String text) {
}
