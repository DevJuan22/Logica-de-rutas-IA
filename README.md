# Sistema Inteligente de Rutas
## Abrir en Windows
1. Extrae el ZIP.
2. Entra en la carpeta `Front_Transporte_IA`.
3. En la barra de dirección del Explorador escribe `cmd` y pulsa Enter.
4. Ejecuta estos comandos, uno por uno:
```bat
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py
```
Si `python` no funciona, prueba `py` en los comandos.
5. Abre Chrome en http://127.0.0.1:5000

## Demostración
- **Planificador de ruta:** usa búsqueda BFS sobre la red de estaciones del proyecto original.
- **Predicción:** modifica seis variables y pulsa “Predecir recorrido”. Flask consulta el árbol de decisión de scikit-learn entrenado con el CSV.
- **Resumen:** muestra tamaño del conjunto, división entrenamiento/prueba y exactitud evaluada.

**Aviso:** el archivo CSV contiene datos sintéticos para una práctica; no son datos oficiales de TransMilenio ni recomendaciones para viajes reales.
