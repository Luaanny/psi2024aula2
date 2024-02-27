from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/compras')
def compras():
    #return '<ul><li>arroz</li></ul>'
    return render_template('compras.html')

@app.route('/mercados')
def mercados():
    return render_template('mercados.html')

