package equipo._7.SentimentAPI.domain.prediction;

import com.fasterxml.jackson.annotation.JsonAlias;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;

public record DataSimplePrediction(
        @NotBlank(message = "El texto para analizar no puede estar vacío")
        @Size(max = 3000, message = "El texto es demasiado largo para la IA (máximo 3000 caracteres)")
        @Size(min = 5, message = "El texto es demasiado corto para clasificarlo (mínimo 5 caracteres)")
        @JsonAlias("comentario")
        String text,
        @NotBlank(message = "El texto para analizar no puede estar vacío")
        @Size(max = 3000, message = "El texto es demasiado largo para la IA (máximo 3000 caracteres)")
        @Size(min = 5, message = "El texto es demasiado corto para clasificarlo (mínimo 5 caracteres)")
        @JsonAlias("comentario_limpio")
        String cleanText,
        @NotNull(message = "Es necesario especificar el idioma del modelo (ES, PT)")
        @JsonAlias("modelo")
        Language model
) {
}
