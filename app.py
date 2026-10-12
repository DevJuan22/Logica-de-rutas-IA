from pathlib import Path
import pandas as pd
from flask import Flask, render_template, request, jsonify
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
BASE=Path(__file__).resolve().parent
app=Flask(__name__)
cols=["numero_estaciones","tiempo_estimado_min","transbordos","ocupacion_pct","retraso_min","incidentes_reportados"]
df=pd.read_csv(BASE/"datos"/"recorridos_transporte.csv")
X=df[cols]; y=df["clasificacion"]
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)
modelo=DecisionTreeClassifier(max_depth=4,random_state=42,class_weight="balanced").fit(Xtr,ytr)
acc=modelo.score(Xte,yte)
@app.route("/")
def home(): return render_template("index.html",total=len(df),train=len(Xtr),test=len(Xte),accuracy=round(acc*100,2))
@app.route("/api/predecir",methods=["POST"])
def predecir():
 try:
  d=request.get_json(force=True); vals={c:int(d[c]) for c in cols}
  ranges={"numero_estaciones":(1,30),"tiempo_estimado_min":(1,240),"transbordos":(0,10),"ocupacion_pct":(0,100),"retraso_min":(0,180),"incidentes_reportados":(0,20)}
  if any(not ranges[k][0]<=v<=ranges[k][1] for k,v in vals.items()): return jsonify(error="Revisa los valores; alguno está fuera del rango permitido."),400
  xx=pd.DataFrame([vals],columns=cols); pred=modelo.predict(xx)[0]; probs=modelo.predict_proba(xx)[0]; confidence=float(probs[list(modelo.classes_).index(pred)])*100
  return jsonify(clasificacion=pred,confianza=round(confidence,1),accuracy=round(acc*100,2),mensaje="Predicción del árbol de decisión entrenado con el CSV.")
 except (KeyError,ValueError,TypeError): return jsonify(error="Completa todos los campos con números."),400
if __name__=="__main__": app.run(debug=True,port=5000)
