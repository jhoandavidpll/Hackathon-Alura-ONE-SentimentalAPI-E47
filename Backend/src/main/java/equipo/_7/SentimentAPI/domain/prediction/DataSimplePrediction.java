package equipo._7.SentimentAPI.domain.prediction;

import com.fasterxml.jackson.annotation.JsonAlias;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;

public record DataSimplePrediction(
        @NotBlank(message = "El texto para analizar no puede estar vacío")
        @Size(max = 300, message = "El texto es demasiado largo para la IA (máximo 300 caracteres)")
        @Size(min = 5, message = "El texto es demasiado corto para la IA (mínimo 5 caracteres)")
        @JsonAlias("comentario")
        String text
) {
}
