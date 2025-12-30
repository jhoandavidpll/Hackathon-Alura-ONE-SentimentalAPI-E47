package equipo._7.SentimentAPI.prediction;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.stringtemplate.v4.ST;

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

    public Prediction(DatosSimplePrediction json) {
        this.id = null;
        this.prevision = "Positivo";
        this.probabilidad = 0f;
        this.comentario = json.text();
        this.topFeatures = "['Hola', 'uwu']";
        this.fecha = LocalDateTime.now();
    }
}
