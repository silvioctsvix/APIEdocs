from flask import Flask, render_template, request
#import requests

app = Flask(__name__)
# route -> hashtagtreinamentos.com/
# função -> o que você quer exibir naquela página
# template

class Requisicao:
    def __init__(self, code, state):
        self.code = code
        self.state = state

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

# @app.route("/GetCode")
# def GetCode():
#     requester_url = request.url
#     data = request.json()
#     if 'code' in data and 'state' in data:
#         codigo = data['code']
#         state = data['state']
#     requester_url = jsonify(data)
#     return render_template("GetCode.html", requester_url=requester_url)
#########################
# @app.route("/GetCode", methods=['POST'])
# def GetCode():
#     requester_url = request.url
#     return render_template("GetCode.html", requester_url=requester_url)

@app.route('/GetCode', methods=['POST'])
def code():
    data = request.get_json()
    html_response = f"<html><body>Dados recebidos: {data}</body></html>"
    return html_response, 200, {'Content-Type': 'text/html'}

#########################

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

    # servidor do heroku

