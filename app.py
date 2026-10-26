from flask import Flask

app= Flask(__name__)


@app.route('/')
def pagina_inicial ():
    return '<h1> teste </h1> <p> mais teste </p>'

@app.route("/cadastro")
def pagina_cadastro ():
    return '<h1> cadastre ou faça login aqui</h1> <p> clique aqui para se cadastrar </p> <p> clique aqui para logar </p>'


if __name__ == '__main__':
        app.run(debug=True)
