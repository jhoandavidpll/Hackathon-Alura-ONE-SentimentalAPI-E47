package equipo._7.SentimentAPI.domain.prediction;

public record DataPredictions(Long id,String prevision, float probabilidad, String comentario) {
    public DataPredictions(Prediction prediction) {
        this(
            prediction.getId(),
            prediction.getPrevision(),
            prediction.getProbabilidad(),
            prediction.getComentario()
        );
    }
}
