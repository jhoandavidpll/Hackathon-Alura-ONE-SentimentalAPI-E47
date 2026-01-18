package equipo._7.SentimentAPI.domain.user;

import com.fasterxml.jackson.annotation.JsonAlias;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;

public record DataAuth(
        @NotBlank
        @Email
        String email,
        @NotBlank
        @JsonAlias("contrasena")
        String password) {
}
