package equipo._7.SentimentAPI.domain.prediction;

import java.time.LocalDateTime;

public record DataPredictions(Long id, String comentario, String prevision, float probabilidad, Language idioma, LocalDateTime fecha) {
    public DataPredictions(Prediction prediction) {
        this(
            prediction.getId(),
            prediction.getComentario(),
            prediction.getPrevision(),
            prediction.getProbabilidad(),
            prediction.getLanguage(),
            prediction.getFecha()
        );
    }
}
