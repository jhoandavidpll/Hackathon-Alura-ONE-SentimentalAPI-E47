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

    // Clase para estructurar la respuesta
    public static class PredictionResult {
        public long label;
        public float[] probabilities;

        public PredictionResult(long label, float[] probabilities) {
            this.label = label;
            this.probabilities = probabilities;
        }
    }

    @PostConstruct // Ejecuta esto al levantar Spring
    public void init() throws Exception {
        this.env = OrtEnvironment.getEnvironment();

        // Cargar el modelo
        // Nota: Asegúrate que la ruta sea accesible desde el classpath compilado
        String modelPath = getClass().getClassLoader().getResource("resources/modelo_con_vectorizer.onnx").getPath();

        // CORRECCIÓN: Faltaba crear la sesión
        this.session = env.createSession(modelPath, new OrtSession.SessionOptions());
        System.out.println("Sesión ONNX iniciada correctamente en: " + modelPath);
    }

    public PredictionResult predict(String text) throws OrtException {
        String[][] inputArray = new String[1][1];
        inputArray[0][0] = text;

        try (OnnxTensor tensor = OnnxTensor.createTensor(env, inputArray);
             OrtSession.Result result = session.run(Collections.singletonMap("input_text", tensor))) {

            // 1. Obtener Etiqueta
            long[] labels = (long[]) result.get(0).getValue();

            // 2. Obtener Probabilidades
            float[][] rawScores = (float[][]) result.get(1).getValue();
            float[] probs = softmax(rawScores[0]);

            return new PredictionResult(labels[0], probs);
        }
    }

    // Misma utilidad de Softmax
    private float[] softmax(float[] logits) {
        float[] probabilities = new float[logits.length];
        float sum = 0;
        float max = Float.NEGATIVE_INFINITY;
        for (float val : logits) max = Math.max(max, val);

        for (int i = 0; i < logits.length; i++) {
            probabilities[i] = (float) Math.exp(logits[i] - max);
            sum += probabilities[i];
        }
        for (int i = 0; i < logits.length; i++) {
            probabilities[i] /= sum;
        }
        return probabilities;
    }
}