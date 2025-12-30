CREATE TABLE predicciones (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    prevision VARCHAR(10) NOT NULL,
    probabilidad DOUBLE PRECISION NOT NULL,
    comentario TEXT NOT NULL,
    top_features TEXT NOT NULL,
    fecha TIMESTAMP NOT NULL
);
