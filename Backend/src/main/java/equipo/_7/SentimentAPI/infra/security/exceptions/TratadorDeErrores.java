package equipo._7.SentimentAPI.infra.security.exceptions;

import jakarta.persistence.EntityNotFoundException;
import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.FieldError;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.http.converter.HttpMessageNotReadableException;
import com.auth0.jwt.exceptions.TokenExpiredException;

import java.util.List;

@RestControllerAdvice
public class TratadorDeErrores {

    @ExceptionHandler(TokenExpiredException.class)
    public ResponseEntity tratarErrorTokenExpirado() {
    return ResponseEntity.status(401)
    .body("Tu sesión ha expirado. Por favor, inicia sesión de nuevo para obtener un nuevo token.");
    }

    @ExceptionHandler(HttpMessageNotReadableException.class)
    public ResponseEntity tratarErrorReadable(HttpMessageNotReadableException e) {
    // Esto responde un 400 con un mensaje humano
    return ResponseEntity.badRequest().body(
        "El cuerpo de la solicitud (JSON) tiene un error de sintaxis o está mal formado.");
    }

    // 1. Error 404: Si intentan buscar algo que no existe en la BD
    @ExceptionHandler(EntityNotFoundException.class)
    public ResponseEntity tratarError404() {
        return ResponseEntity.notFound().build();
    }

    // 2. Error 400: Datos inválidos (ej. contraseña muy corta o email mal formado)
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity tratarError400(MethodArgumentNotValidException e) {
        var errores = e.getFieldErrors().stream()
                .map(DatosErrorValidacion::new)
                .toList();
        return ResponseEntity.badRequest().body(errores);
    }

    // 3. Error 409: Integridad de datos (ej. intentar registrar un email duplicado)
    @ExceptionHandler(DataIntegrityViolationException.class)
    public ResponseEntity tratarErrorDuplicado(DataIntegrityViolationException e) {
        return ResponseEntity.status(409).body("Error: El dato ingresado (probablemente el email) ya existe en el sistema.");
    }

    // 4. Error 401: Login fallido (contraseña o usuario incorrecto)
    @ExceptionHandler(org.springframework.security.authentication.BadCredentialsException.class)
    public ResponseEntity tratarErrorLogin() {
        return ResponseEntity.status(401).body("Error: Credenciales inválidas. Verifica tu correo y contraseña.");
    }

    // 5. Error 500: Errores inesperados del servidor
    @ExceptionHandler(Exception.class)
    public ResponseEntity tratarError500(Exception e) {
        return ResponseEntity.status(500).body("Error interno del servidor: " + e.getMessage());
    }

    // DTO interno para formatear los mensajes
    private record DatosErrorValidacion(String campo, String error) {
        public DatosErrorValidacion(FieldError error) {
            this(error.getField(), error.getDefaultMessage());
        }
    }

    @ExceptionHandler(ValidacionDeNegocioException.class)
    public ResponseEntity tratarErrorDeNegocio(ValidacionDeNegocioException e) {
    return ResponseEntity.badRequest().body(e.getMessage());
    }
}