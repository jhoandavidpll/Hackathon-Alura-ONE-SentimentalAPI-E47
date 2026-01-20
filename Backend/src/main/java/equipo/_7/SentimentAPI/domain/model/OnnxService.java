package equipo._7.SentimentAPI.domain.model;

import ai.onnxruntime.OnnxTensor;
import ai.onnxruntime.OrtEnvironment;
import ai.onnxruntime.OrtException;
import ai.onnxruntime.OrtSession;
import org.springframework.stereotype.Service;
import jakarta.annotation.PostConstruct; // Importante para Spring
import java.util.Collections;

@Service
public class OnnxService {
    private OrtEnvironment env;
    private OrtSession session;

    // Estructura para devolver a la entidad
    public record PredictionResult(long label, float probability) {}

    @PostConstruct
    public void init() throws Exception {
        this.env = OrtEnvironment.getEnvironment();

        // Usar el recurso de Spring para mayor compatibilidad
        byte[] modelBytes;
        try (var is = getClass().getClassLoader().getResourceAsStream("resources/modelo_con_vectorizer.onnx")) {
            if (is == null) {
                throw new RuntimeException("No se encontró el modelo en: resources/modelo_con_vectorizer.onnx");
            }
            modelBytes = is.readAllBytes();
        }

        // Crear la sesión usando los bytes del modelo en lugar de una ruta de archivo
        this.session = env.createSession(modelBytes, new OrtSession.SessionOptions());
        System.out.println("Modelo ONNX cargado exitosamente.");
    }

    public PredictionResult predict(String text) throws OrtException {
        String[][] inputArray = new String[][]{{text}};

        try (OnnxTensor tensor = OnnxTensor.createTensor(env, inputArray);
             OrtSession.Result result = session.run(Collections.singletonMap("input_text", tensor))) {

            // Obtener etiqueta
            long[] labels = (long[]) result.get(0).getValue();
            long label = labels[0];

            // Obtener probabilidades (Index 1) y aplicar Softmax
            float[][] rawScores = (float[][]) result.get(1).getValue();
            float[] probs = softmax(rawScores[0]);
            float winningProb = probs[(int) label];

            return new PredictionResult(label, winningProb);
        }
    }

    private float[] softmax(float[] logits) {
        float[] probabilities = new float[logits.length];
        float sum = 0;
        float max = Float.NEGATIVE_INFINITY;
        for (float val : logits) max = Math.max(max, val);
        for (int i = 0; i < logits.length; i++) {
            probabilities[i] = (float) Math.exp(logits[i] - max);
            sum += probabilities[i];
        }
        for (int i = 0; i < logits.length; i++) probabilities[i] /= sum;
        return probabilities;
    }
}