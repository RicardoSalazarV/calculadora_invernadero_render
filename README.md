AgriCalc

AgriCalc es una aplicación web interactiva desarrollada con Python y Streamlit que permite calcular de forma eficiente el consumo y requerimiento de agua en invernaderos, optimizando la toma de decisiones para sistemas de cultivo como hidroponía y goteo.

Objetivo

Ofrecer una herramienta intuitiva para agricultores, ingenieros agrónomos y responsables de producción agrícola que permita:

Dimensionar tanques de agua.

Estimar capacidad de riego.

Calcular necesidades hídricas por planta y por día.

Maximizar la eficiencia del recurso hídrico.


Funcionalidades

1. ¿Cuántas plantas puedo alimentar?
Ingresando los litros disponibles, el sistema calcula cuántas plantas pueden sostenerse durante un número de días.


2. ¿Cuánta agua necesito?
A partir del número de plantas y días, estima el volumen total requerido.


3. Calcular volumen del tanque
Introduciendo las dimensiones del tanque, se calcula su capacidad en litros.


4. Calcular plantas a partir del tanque
Con base en el tamaño del tanque y las condiciones del cultivo, se calcula cuántas plantas se pueden mantener.



Parámetros Considerados

Tipo de planta: Lechuga, jitomate, chile y espinaca.

Sistema de cultivo: Hidroponía o goteo.

Duración del soporte: Hasta 60 días.


Tecnologías Utilizadas

Python 3.10+

Streamlit para la interfaz web.

Lógica encapsulada en funciones para facilitar la reutilización y escalabilidad.


Requisitos de instalación

pip install streamlit

Ejecución

streamlit run app.py

Futuras mejoras

Exportación de reportes en PDF o Excel.

Almacenamiento de configuraciones y escenarios personalizados.

Simulación con pronóstico climático.

Conexión a sensores IoT para monitoreo en tiempo real.
