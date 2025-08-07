from flask import Flask, render_template
from datetime import datetime
from scraper import obtener_titulos_hn, frutas_con_descripcion

app = Flask(__name__)

@app.route("/")
def home():
    titulos = obtener_titulos_hn()
    frutas = frutas_con_descripcion()
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return render_template(
        "index.html",
        titulos=titulos,
        frutas=frutas,
        fecha=fecha
    )

if __name__ == "__main__":
    app.run(debug=True)