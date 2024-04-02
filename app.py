from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/compras')
def compras():
    #return '<ul><li>arroz</li></ul>'
    return render_template('compras.html',item1 ='Cuscuz', item2 = 'Farinha')

@app.route('/mercados')
def mercados():
    return render_template('mercados.html')
'''
@app.route('/gastos')
def gastos():
    mes = 'fevereiro'
    valor = '843,00'
    return render_template('gastos.html',a = mes, b = valor)
'''

@app.route('/gastos', defaults = {'mes':'janeiro', 'valor': '0'})
@app.route('/gastos/<mes>/<valor>')
def gastos(mes, valor):
    return render_template('gastos.html',a = mes, b = valor)

@app.route('/dobro',defaults={'n':0})
@app.route('/dobro/<float:n>')
@app.route('/dobro/<int:n>')
def dobro(n):
    resultado = 2*n
    return render_template('dobro.html',n=n, resultado = resultado)

@app.route('/perfil/<usuario>')
def perfil(usuario):
    return render_template('perfil.html', usuario = usuario)

@app.route('/verificaridade/<int:idade>')
def verificaridade (idade):
    if idade >= 18:
        return 'Você é maior de idade'
    else: 
        return 'Você é menor de idade'

@app.route('/situacaofinal/<float:nota>')
def situacaofinal(nota):
    if nota >= 60.0:
        return 'Aprovado'
    elif nota >= 20.0:
        return 'Recuperação'
    else:
        return 'Reprovado'
    
@app.route('/login')
def login(): 
    return render_template('login.html')

@app.route('/verificarlogin', methods=['POST'])
def verificarlogin():
    usuario = request.form ['usuario']
    senha = request.form ['senha']

    if usuario == 'luanny' and senha == '123':
        return render_template('arearestrita.html', usuario=usuario, senha=senha)
    else:
        return 'Você nâo tem permissão'
    
@app.route('/verificaridade2/<int:idade>')
def verificaridade2 (idade):
    return render_template('verificaridade2.html', idade=idade)

@app.route('/usuario/<nome>')
def usuario(nome):
    return render_template('usuario.html', nome=nome)









