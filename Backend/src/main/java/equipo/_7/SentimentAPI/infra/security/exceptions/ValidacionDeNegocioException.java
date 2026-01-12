package equipo._7.SentimentAPI.infra.security.exceptions;

public class ValidacionDeNegocioException extends RuntimeException {
    public ValidacionDeNegocioException(String mensaje) {
        super(mensaje);
    }
}