from kafka import KafkaProducer, KafkaConsumer
import pandas as pd 
import time
from services.Database import creating_engine, creating_session, Predicciones, Base
from json import dumps, loads
from joblib import load

kafka_topic = "kafka_workshop"

def kafka_producer():
    producer = KafkaProducer(
        value_serializer=lambda m: dumps(m).encode('utf-8'),
        bootstrap_servers=['localhost:9092'],
    )

    try:
        # Leer un csv con pandas
        data = pd.read_csv('services\data_result.csv')
        # Se obtiene el 30% de las filas de forma aleatoria
        n_samples = int(len(data) * 0.30)
        #Se usa el random_state para obtener los mismos resultados
        df = data.sample(n=n_samples, random_state=42)  


        for _, row in df.iterrows():
            message = {
            "GDP_per_capita": row["GDP_per_capita"],
            "life_expectancy": row["life_expectancy"],
            "freedom": row["freedom"],
            "perceptions_corruption": row["perceptions_corruption"],
            "generosity": row["generosity"],
            "happiness_score": row["happiness_score"]
            }
            producer.send(kafka_topic, value=message)
            print("Enviando registros desde el producer")
            #time.sleep(2)

    except Exception as e:
        print(f"Error al procesar y enviar datos: {str(e)}")



def kafka_consumer():

    # Cargar el modelo de regresión
    modelo_regresion = load("services\modelo_regresion.pkl")

    # Crea el engine y la sesión
    engine = creating_engine()
    session = creating_session(engine)

    # Crea la tabla si no existe
    Base.metadata.create_all(engine) 

    consumer = KafkaConsumer(
        'kafka_workshop',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group-1',
        value_deserializer=lambda m: loads(m.decode('utf-8')),
        bootstrap_servers=['localhost:9092']
    )

    for m in consumer:
        mensaje = m.value

        # Convertir el mensaje en un DataFrame temporal
        df1 = pd.DataFrame([mensaje])

        # Crear un df temporal exceptuando el happiness_score
        df_temporal = df1[["GDP_per_capita", "life_expectancy", 
                      "freedom", "perceptions_corruption", "generosity"]]
        
        #valores = df_temporal.values

        # Realiza predicciones con el modelo de regresión
        predicciones = modelo_regresion.predict(df_temporal)

        # Mostramos el resultado
        print("Happiness Score Predicted:", predicciones)

         # Crear un objeto Predicciones y asignar valores
        predicciones_obj = Predicciones(
            GDP_per_capita=mensaje["GDP_per_capita"],
            life_expectancy=mensaje["life_expectancy"],
            freedom=mensaje["freedom"],
            perceptions_corruption=mensaje["perceptions_corruption"],
            generosity=mensaje["generosity"],
            happiness_score=mensaje["happiness_score"],
            happiness_score_prediction=predicciones[0]  # Tomar la primera predicción del arreglo
        )

        # Agregar el objeto a la sesión y hacer commit
        session.add(predicciones_obj)
        session.commit()
        time.sleep(2)