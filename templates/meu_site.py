from flask import Flask, render_template, request

app = Flask(__name__)
# route -> hashtagtreinamentos.com/
# função -> o que você quer exibir naquela página
# template

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

@app.route("/GetCode")
def GetCode():
    requester_url = request.url
    data = request.html
    if 'code' in data and 'state' in data:
        code = data['code']
        state = data['state']
#        return jsonify(response), 200
# Inclua um script JavaScript na resposta para imprimir no console
    requester_url = data
    return render_template("GetCode.html", requester_url=requester_url)

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

    # servidor do heroku

