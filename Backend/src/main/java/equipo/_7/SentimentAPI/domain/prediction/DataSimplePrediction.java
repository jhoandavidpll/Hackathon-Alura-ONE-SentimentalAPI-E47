package equipo._7.SentimentAPI.domain.prediction;

import jakarta.validation.constraints.NotBlank;

public record DataSimplePrediction(@NotBlank String text) {
}
