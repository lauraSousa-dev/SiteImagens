from flask import Flask, render_template,request,redirect
import requests
lista=[]

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', Titulo = 'COFFE images')

@app.route('/cadastro')
def cadastro():
    BASE_URL = "https://coffee.alexflipnote.dev/random.json"
    images = requests.get(BASE_URL).json()
    imagemdoCafe = images['file']
    return render_template('cadastro.html', Titulo = 'Cadastro', Imagem = imagemdoCafe)

@app.route('/galeria')
def galeria():
    return render_template('galeria.html', Titulo = 'Galeria COFFE', lista=lista)

@app.route('/criar', methods=['POST'])
def criar():
    imagem = request.form['url']
    descricao = request.form['descricao']
    fotos = [imagem, descricao]
    lista.append(fotos)
    return redirect('/cadastro')


if __name__ == '__main__':
    app.run()
