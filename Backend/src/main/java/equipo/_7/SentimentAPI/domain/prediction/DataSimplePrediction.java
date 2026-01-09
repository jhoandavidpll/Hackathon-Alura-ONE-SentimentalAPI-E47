package equipo._7.SentimentAPI.domain.prediction;

import com.fasterxml.jackson.annotation.JsonAlias;
import jakarta.validation.constraints.NotBlank;

public record DataSimplePrediction(@NotBlank @JsonAlias("comentario") String text) {
}
