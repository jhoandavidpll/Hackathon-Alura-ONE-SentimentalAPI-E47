package equipo._7.SentimentAPI.domain.prediction;

public record DataPredictions(Long id, String comentario,String prevision, float probabilidad, Language language) {
    public DataPredictions(Prediction prediction) {
        this(
            prediction.getId(),
            prediction.getComentario(),
            prediction.getPrevision(),
            prediction.getProbabilidad(),
            prediction.getLanguage()
        );
    }
}
