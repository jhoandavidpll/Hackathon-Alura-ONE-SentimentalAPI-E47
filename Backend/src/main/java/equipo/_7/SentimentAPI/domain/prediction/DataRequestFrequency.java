package equipo._7.SentimentAPI.domain.prediction;

import com.fasterxml.jackson.annotation.JsonAlias;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Pattern;

import java.util.Date;

public record DataRequestFrequency(
        @NotBlank(message = "Debe de especificar el idioma (ES, PT)")
        @Pattern(regexp = "^(ES|PT)$",message = "El idioma debe ser: ES o PT")
        @JsonAlias("idioma")
        String language,
        @JsonAlias("fecha_inicio")
        Date fechaInicio,
        @JsonAlias("fecha_fin")
        Date fechaFin
) {
}
