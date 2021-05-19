import random
import string

import cherrypy

#Acrescentamos o uso do css Bulma no nosso pequeno projeto de site!

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """
        <!DOCTYPE html>
        <html>
          <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.2/css/bulma.min.css">
          <title>Minha primeira pagina web com python!</title>
          </head>
          <body>
          <h1>Minha entrada de dados:<h1>
          <iframe width="</iframe>
            <p>Informe seu nome e opinião: </p>
            <form method="get" action="obrigado">
            <input class="input" type="text" placeholder="Nome:"name = "Nome"><br>
            <input class="input is-rounded" type="text" placeholder="Opinião:"name="Opniao"><br>
            <button class="button is-info is-rounded"type="submit">Dar opnião</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def generate(self, length=8):
        return ''.join(random.sample(string.hexdigits, int(length)))

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
