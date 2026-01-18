package equipo._7.SentimentAPI.domain.model;

import ai.onnxruntime.OnnxTensor;
import ai.onnxruntime.OrtEnvironment;
import ai.onnxruntime.OrtException;
import ai.onnxruntime.OrtSession;

import java.util.Arrays;
import java.util.Collections;

public class ModelTest {
    public static void main(String[] args) {
        String modelPath = "src/main/resources/resources/modelo_con_vectorizer.onnx";
        String textoPrueba = "Me parece genial que ya sea posible pedir todo desde casa.";

        try (OrtEnvironment env = OrtEnvironment.getEnvironment();
             OrtSession.SessionOptions options = new OrtSession.SessionOptions();
             OrtSession session = env.createSession(modelPath, options)) {

            System.out.println("--- Modelo Cargado ---");

            // 1. Preparar la entrada
            String[][] inputData = new String[][]{{textoPrueba}};

            try (OnnxTensor inputTensor = OnnxTensor.createTensor(env, inputData)) {

                // 2. Ejecutar Inferencia
                try (OrtSession.Result results = session.run(Collections.singletonMap("input_text", inputTensor))) {

                    // 3. Extraer ETIQUETA (Index 0)
                    long[] labels = (long[]) results.get(0).getValue();

                    // 4. Extraer PROBABILIDADES/LOGITS (Index 1)
                    // Nota: Si tu modelo devuelve una lista de mapas, esto lanzará error.
                    // Dado tu ejemplo numérico, asumo que es float[][] (Tensor)
                    float[][] rawScores = (float[][]) results.get(1).getValue();
                    float[] logits = rawScores[0]; // Tomamos el primer elemento del batch

                    // 5. Convertir Logits a Probabilidades (Softmax)
                    float[] probabilities = softmax(logits);

                    System.out.println("Texto: " + textoPrueba);
                    System.out.println("Predicción Ganadora: " + labels[0]);
                    System.out.println("Scores Crudos (Logits): " + Arrays.toString(logits));
                    System.out.println("Confianza Calculada (Softmax): " + Arrays.toString(probabilities));

                    // Imprimir bonito
                    System.out.printf("Confianza Negativa [0]: %.2f%%%n", probabilities[0] * 100);
                    System.out.printf("Confianza Neutra   [1]: %.2f%%%n", probabilities[1] * 100);
                    System.out.printf("Confianza Positiva [2]: %.2f%%%n", probabilities[2] * 100);
                }
            }

        } catch (OrtException e) {
            System.err.println("Error en ONNX Runtime: " + e.getMessage());
            e.printStackTrace();
        }
    }

    // Función auxiliar para convertir logits (ej: 2.22, -0.20) a probabilidad (0.8, 0.1)
    private static float[] softmax(float[] logits) {
        float[] probabilities = new float[logits.length];
        float sum = 0;
        float max = Float.NEGATIVE_INFINITY;

        // Estabilidad numérica (restar el max para evitar overflow en exp)
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