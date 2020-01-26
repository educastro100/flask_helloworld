# importando a classe Flask 
from flask import Flask

# Criando uma instância da classe Flask
app = Flask(__name__)

# Decorator serve pra applciar uma função em cima de outra
# Define uma rota para a página
@app.route("/")
def index(): # Uma página que está sendo criada (index)
    return "Hello World!"

# Verifica se o usuário está executando o arquivo principal
if __name__ == "__main__":
    app.run()
