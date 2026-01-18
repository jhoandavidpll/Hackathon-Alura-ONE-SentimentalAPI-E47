package equipo._7.SentimentAPI.domain.user;

import com.fasterxml.jackson.annotation.JsonAlias;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Pattern;

public record DataRegister(
        @NotBlank
        @Email
        String email,
        @NotBlank
        @JsonAlias("nombre")
        String name,
        @NotBlank
        @Pattern(
            regexp = "^(?=.*[A-Z])(?=.*\\d).{8,}$",
            message = "La contraseña debe tener al menos 8 caracteres, una mayúscula y un número"
        )
        @JsonAlias("contrasena")
        String password,
        @NotBlank
        @Pattern(
            regexp = "^(?=.*[A-Z])(?=.*\\d).{8,}$",
            message = "La contraseña debe tener al menos 8 caracteres, una mayúscula y un número"
        )
        @JsonAlias("confirmar_contrasena")
        String passwordConfirmation) {
}
