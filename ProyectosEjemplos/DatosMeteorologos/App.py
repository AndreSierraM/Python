import pandas as pd
import matplotlib.pyplot as plt


def leer_archivo_csv(nombre_archivo):
    return pd.read_csv(nombre_archivo)


def limpiar_datos(datos):
    datos = datos.drop(columns=["STATION", "NAME", "LATITUDE", "LONGITUDE", "ELEVATION"])
    datos = datos.dropna()
    datos["DATE"] = pd.to_datetime(datos["DATE"])
    return datos


def graficar_temperaturas(datos):
    datos.plot(x="DATE", y=["TMAX", "TMIN"])
    plt.title("Temperaturas máximas y mínimas diarias")
    plt.xlabel("Fecha")
    plt.ylabel("Temperatura (°C)")
    plt.show()


def graficar_precipitaciones(datos):
    datos.plot(x="DATE", y="PRCP")
    plt.title("Precipitación diaria")
    plt.xlabel("Fecha")
    plt.ylabel("Precipitación (mm)")
    plt.show()


datos = leer_archivo_csv("weather.csv")
datos = limpiar_datos(datos)

graficar_temperaturas(datos)
graficar_precipitaciones(datos)
