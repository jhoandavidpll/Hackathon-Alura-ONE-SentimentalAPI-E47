package equipo._7.SentimentAPI.prediction;

public record DataPredictions(String prevision, float probabilidad, String topFeatures, String comentario) {
    public DataPredictions(Prediction prediction) {
        this(prediction.getPrevision(), prediction.getProbabilidad(),prediction.getTopFeatures(),
                prediction.getComentario());
    }
}
