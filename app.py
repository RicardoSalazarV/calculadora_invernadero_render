import streamlit as st

def requerimiento_por_planta(tipo_planta, sistema):
    tabla_requerimientos = {
        "lechuga": {"hidroponía": 1.5, "goteo": 2.0},
        "jitomate": {"hidroponía": 3.5, "goteo": 4.5},
        "chile": {"hidroponía": 2.0, "goteo": 3.0},
        "espinaca": {"hidroponía": 1.2, "goteo": 1.8},
    }
    return tabla_requerimientos[tipo_planta][sistema]

def calcular_plantas_posibles(volumen_litros, tipo_planta, sistema, dias):
    consumo = requerimiento_por_planta(tipo_planta, sistema)
    return int(volumen_litros // (consumo * dias))

def calcular_agua_necesaria(num_plantas, tipo_planta, sistema, dias):
    consumo = requerimiento_por_planta(tipo_planta, sistema)
    return num_plantas * consumo * dias

def calcular_volumen_tanque(largo, ancho, alto):
    return largo * ancho * alto * 1000

def calcular_tanque_necesario(volumen_litros):
    lado = (volumen_litros / 1000) ** (1/3)
    return round(lado, 2)

st.set_page_config(page_title="Calculadora de Agua para Cultivos", layout="centered")

st.title("Calculadora Inteligente de Agua para Invernaderos")

menu = st.selectbox("Selecciona el cálculo que deseas realizar:", [
    "1. ¿Cuántas plantas puedo alimentar?",
    "2. ¿Cuánta agua necesito?",
    "3. Calcular volumen del tanque",
    "4. Calcular plantas a partir del tanque"
])

tipo_planta = st.selectbox("Tipo de planta:", ["lechuga", "jitomate", "chile", "espinaca"])
sistema = st.radio("Sistema de cultivo:", ["hidroponía", "goteo"])
dias = st.slider("Días de soporte:", min_value=1, max_value=60, value=7)

if menu == "1. ¿Cuántas plantas puedo alimentar?":
    litros = st.number_input("Litros de agua disponibles:", min_value=1.0)
    if litros and st.button("Calcular plantas posibles"):
        resultado = calcular_plantas_posibles(litros, tipo_planta, sistema, dias)
        st.success(f"Puedes alimentar **{resultado} plantas** de {tipo_planta} durante {dias} días.")

elif menu == "2. ¿Cuánta agua necesito?":
    plantas = st.number_input("Número de plantas:", min_value=1)
    if plantas and st.button("Calcular agua necesaria"):
        litros = calcular_agua_necesaria(plantas, tipo_planta, sistema, dias)
        st.success(f"Necesitas **{litros:.2f} litros** de agua para {plantas} plantas durante {dias} días.")

elif menu == "3. Calcular volumen del tanque":
    largo = st.number_input("Largo del tanque (m):", min_value=0.1)
    ancho = st.number_input("Ancho del tanque (m):", min_value=0.1)
    alto = st.number_input("Alto del tanque (m):", min_value=0.1)
    if largo and ancho and alto and st.button("Calcular volumen"):
        volumen = calcular_volumen_tanque(largo, ancho, alto)
        st.success(f"El tanque puede almacenar **{volumen:.2f} litros** de agua.")

elif menu == "4. Calcular plantas a partir del tanque":
    largo = st.number_input("Largo del tanque (m):", min_value=0.1, key="largo4")
    ancho = st.number_input("Ancho del tanque (m):", min_value=0.1, key="ancho4")
    alto = st.number_input("Alto del tanque (m):", min_value=0.1, key="alto4")
    if largo and ancho and alto and st.button("Calcular plantas posibles"):
        volumen = calcular_volumen_tanque(largo, ancho, alto)
        plantas = calcular_plantas_posibles(volumen, tipo_planta, sistema, dias)
        st.success(f"Con ese tanque puedes alimentar **{plantas} plantas** de {tipo_planta} durante {dias} días.")

st.markdown("---")
st.caption("Desarrollado por Ricardo - Optimizado con Streamlit")
