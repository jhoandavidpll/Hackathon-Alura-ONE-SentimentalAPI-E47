package equipo._7.SentimentAPI.domain.prediction;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.time.LocalDateTime;
import java.util.List;

public interface PredictionRepository extends JpaRepository<Prediction, Long> {
    @Query(value = """
        WITH palabras AS (
            SELECT regexp_split_to_table(
                LOWER(TRIM(p.comentario_limpio)),
                    '[^a-zA-ZáéíóúÁÉÍÓÚñÑ]+') as palabra
            FROM predicciones p
            WHERE
                p.prevision = :clasificacion
                AND p.idioma = :lang
                AND TRIM(p.comentario_limpio) != ''
        )
        SELECT palabra, COUNT(*) as frecuencia
        FROM palabras
        WHERE LENGTH(palabra) > 2
        GROUP BY palabra
        ORDER BY frecuencia DESC
        LIMIT 5
    """, nativeQuery = true)
    List<Object[]> top5PalabrasMasRepetidas(String clasificacion, String lang);

    @Query(value = """
        WITH palabras AS (
            SELECT regexp_split_to_table(
                LOWER(TRIM(p.comentario_limpio)),
                    '[^a-zA-ZáéíóúÁÉÍÓÚñÑ]+') as palabra
            FROM predicciones p
            WHERE
                p.prevision = :clasificacion
                AND p.idioma = :lang
                AND p.fecha BETWEEN :fechaInicio AND :fechaFin
                AND TRIM(p.comentario_limpio) != ''
        )
        SELECT palabra, COUNT(*) as frecuencia
        FROM palabras
        WHERE LENGTH(palabra) > 2
        GROUP BY palabra
        ORDER BY frecuencia DESC
        LIMIT 5
    """, nativeQuery = true)
    List<Object[]> top5PalabrasMasRepetidasPorFecha(String clasificacion, String lang, LocalDateTime fechaInicio, LocalDateTime fechaFin);

    @Query(value = """
        SELECT prevision, COUNT(*) as cantidad
        FROM predicciones
        WHERE
            idioma = :lang
        GROUP BY prevision
        ORDER BY prevision
    """, nativeQuery = true)
    List<Object[]> cantidadSentimiento(String lang);

    @Query(value = """
        SELECT prevision, COUNT(*) as cantidad
        FROM predicciones
        WHERE
            idioma = :lang
            AND fecha BETWEEN :fechaInicio AND :fechaFin
        GROUP BY prevision
        ORDER BY prevision
    """, nativeQuery = true)
    List<Object[]> cantidadSentimientoPorFecha(String lang, LocalDateTime fechaInicio, LocalDateTime fechaFin);
}
