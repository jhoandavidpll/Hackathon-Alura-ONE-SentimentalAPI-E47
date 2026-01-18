package equipo._7.SentimentAPI.infra.exceptions;

public class ValidacionDeNegocioException extends RuntimeException {
    public ValidacionDeNegocioException(String mensaje) {
        super(mensaje);
    }
}