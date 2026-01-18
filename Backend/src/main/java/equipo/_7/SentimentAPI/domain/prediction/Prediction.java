package equipo._7.SentimentAPI.domain.prediction;

import equipo._7.SentimentAPI.domain.model.OnnxService;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

@Entity(name = "Prediction")
@Table(name = "predicciones")
@Getter
@NoArgsConstructor
@AllArgsConstructor
@EqualsAndHashCode(of = "id")
public class Prediction {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String prevision;
    private float probabilidad;
    private String comentario;
    @Column(name = "top_features")
    private String topFeatures;
    private LocalDateTime fecha;

    public Prediction(DataSimplePrediction json) {
        this.id = null;
        this.prevision = "Pendiente";
        this.probabilidad = 0f;
        this.comentario = json.text();
        this.topFeatures = "['Hola', 'uwu']";
        this.fecha = LocalDateTime.now();
    }

    // Método para inyectar el resultado del modelo
    public void asignarResultado(OnnxService.PredictionResult resultado){
        this.probabilidad = resultado.probability;

        // Mapeo directo: Número -> Texto
        switch ((int) resultado.label){
            case 0 -> this.prevision = "Negativo";
            case 1 -> this.prevision = "Neutral";
            case 2 -> this.prevision = "Positivo";
            default -> this.prevision = "Desconocido";
        }
    }
}
