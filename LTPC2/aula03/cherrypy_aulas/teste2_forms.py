import random
import string

import cherrypy

#Abrimos a classe com objeto usando o framework cherrypy!
#Tem um texto em html com iframe aleatorio 2 inputs de dados e um botão para submeter os dados!
class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
          <body>
          <h1>Minha entrada de dados:<h1>
          <iframe>
          <p>Informe seu nome e opinião: </p>
            <form method="get" action="obrigado">
              <input type="text" value="Nome: " name="Nome" />
              <input type="text" value="Opiniao: " name="Opniao" />
              <button type="submit">Opinião</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def generate(self, length=8):
        return ''.join(random.sample(string.hexdigits, int(length)))
#importamos de novo um metodo construtor com o cherrypy com uma estrutura em html para gerar uma pagina de respostas aos dados gerados pelo usuario!
#contem agradecimento e uma imagem aleatoria!
    @cherrypy.expose
    def obrigado(self, Nome, Opniao):
        Nome = Nome.upper()
        Opniao = Opniao.upper()
        return f"""<html>
          <head></head>
          <body>
          <h1>Obrigado!<h1>
            <p>Obrigado {Nome} por sua opnião! </p>
            <p>Opinião: {Opniao}<p>
            <form method="get" action="obrigado">
            <img src = "">
              <a href = "http://localhost:8080">Voltar</a>
          </body>
        </html>"""

if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())
