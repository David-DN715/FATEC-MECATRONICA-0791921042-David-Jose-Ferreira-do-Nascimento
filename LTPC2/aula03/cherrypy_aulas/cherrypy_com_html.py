#Terceiro progama com Cherrypy

# Importamos a Biblioteca
import cherrypy

#implementamos nossa aplicação WEB
class NossoSite(object):
#Colocamos o decorador para informar que é um site! @
    @cherrypy.expose
    def index(self):
        return "Olá Davidson!"
#Essa nova pagina não aparece de cara como link ou aprenstação, é um link!
    @cherrypy.expose
    def fatec(self):
        return "Bem vindo ao curso de Mecatrônica da FATEC - SA"
#Vamos usar html com python!

    @cherrypy.expose
    def minhapagina(self):
        return """<html>
          <head></head>
          <body>
          <h1>Ola Mundo! minha primeira pagina web!</h1>
          <h2>links:</h2>
          <a href="https://www.youtube.com/"<Youtube</a>
          </body>
        </html>"""

#Se pedirmos para o arquivo roda!
if __name__ == "__main__":
    cherrypy.quickstart(NossoSite())
