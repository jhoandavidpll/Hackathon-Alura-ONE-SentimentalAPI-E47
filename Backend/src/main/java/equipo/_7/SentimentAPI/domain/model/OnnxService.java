package equipo._7.SentimentAPI.domain.model;

import ai.onnxruntime.OnnxTensor;
import ai.onnxruntime.OrtEnvironment;
import ai.onnxruntime.OrtException;
import ai.onnxruntime.OrtSession;
import equipo._7.SentimentAPI.domain.prediction.Language;
import org.springframework.stereotype.Service;
import jakarta.annotation.PostConstruct; // Importante para Spring
import java.util.Collections;
import java.util.List;
import java.util.Map;
import ai.onnxruntime.OnnxMap;

@Service
public class OnnxService {
    private OrtEnvironment env;
    private OrtSession session;
    private Language currentModelLanguage;

    // Estructura para devolver a la entidad
    public record PredictionResult(long label, float probability) {}

    @PostConstruct
    public void init() throws Exception {
        this.env = OrtEnvironment.getEnvironment();
    }

    public void cargarModelo(Language tipoModelo) throws Exception {
        currentModelLanguage = tipoModelo;
        String pathModel = switch (tipoModelo) {
            case ES -> "resources/modelo_es.onnx";
            case PT -> "resources/modelo_pt.onnx";
        };

        byte[] modelBytes;
        try (var is = getClass().getClassLoader().getResourceAsStream(pathModel)) {
            if (is == null) throw new RuntimeException("No se encontró el modelo: " + pathModel);
            modelBytes = is.readAllBytes();
        }

        // Cerrar la sesión anterior para liberar memoria antes de crear la nueva
        if (this.session != null) {
            this.session.close();
        }

        this.session = env.createSession(modelBytes, new OrtSession.SessionOptions());
        System.out.println("Modelo ONNX cargado: " + tipoModelo);
    }

    public PredictionResult predict(String text) throws OrtException {

        String processedText = text;
        if (currentModelLanguage == Language.PT) {
            processedText = preprocessForPortugueseModel(text);
        }

        String[][] inputArray = new String[][]{{processedText}};

        try (OnnxTensor tensor = OnnxTensor.createTensor(env, inputArray);
             OrtSession.Result result = session.run(Collections.singletonMap("input_text", tensor))) {

            // 1. Obtener la etiqueta ganadora (index 0)
            long[] labels = (long[]) result.get(0).getValue();
            long winningLabel = labels[0];

            // 2. Obtener la probabilidad (index 1)
            Object outputValue = result.get(1).getValue();
            float winningProb = 0.0f;

            if (outputValue instanceof List<?> list) {
                // Estructura: List<OnnxMap> donde OnnxMap contiene las probabilidades
                if (!list.isEmpty()) {
                    Object firstElement = list.get(0);
                    if (firstElement instanceof OnnxMap) {
                        OnnxMap onnxMap = (OnnxMap) firstElement;

                        // OnnxMap puede devolver un Map directamente con getValue()
                        Object mapValue = onnxMap.getValue();

                        if (mapValue instanceof Map) {
                            @SuppressWarnings("unchecked")
                            Map<Number, Number> probMap = (Map<Number, Number>) mapValue;

                            // Buscar la probabilidad para la etiqueta ganadora
                            Number probNumber = probMap.get(winningLabel);
                            winningProb = (probNumber != null) ? probNumber.floatValue() : 0.0f;

                            System.out.println("DEBUG: Probability map: " + probMap);
                        }
                    }
                }
            } else if (outputValue instanceof float[][] rawScores) {
                float[] probs = softmax(rawScores[0]);
                winningProb = probs[(int) winningLabel];
            } else {
                throw new RuntimeException("Formato de salida del modelo no reconocido: " +
                        (outputValue != null ? outputValue.getClass().getName() : "null"));
            }

            System.out.println("DEBUG: Label=" + winningLabel + ", Probability=" + winningProb);
            return new PredictionResult(winningLabel, winningProb);
        }
    }

    private String preprocessForPortugueseModel(String text) {
        // Eliminar caracteres Unicode problemáticos (emojis)
        // Esto es un workaround temporal mientras se arregla el modelo
        if (text == null) return "";

        // Eliminar emojis y caracteres Unicode problemáticos
        String cleaned = text.replaceAll("[\\x{1F300}-\\x{1F9FF}\\x{1F600}-\\x{1F64F}]", "");

        // También eliminar cualquier otro carácter de 4 bytes (UTF-16 surrogate pairs)
        cleaned = cleaned.replaceAll("[\\uD800-\\uDBFF][\\uDC00-\\uDFFF]", "");

        if (!cleaned.equals(text)) {
            System.out.println("DEBUG: Texto preprocesado para modelo PT (emojis removidos)");
        }

        return cleaned;
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