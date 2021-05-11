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
          <a href="https://www.youtube.com/">Youtube</a>
          <a href ="https://www.youtube.com/watch?v=GgwUenaQqlM"> hero too</a>
          <br> 
          <iframe width="560" height="315" src="https://www.youtube.com/embed/GgwUenaQqlM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
          
          </body>
        </html>"""
# o <br> no texto html tem a função de pular uma linha!
#o href é uma função no texto html para colocar referencias em links!
# o iframe de incorporar videos linkados arquivos de midia na nossa pagina!

#Se pedirmos para o arquivo rodar!
if __name__ == "__main__":
    cherrypy.quickstart(NossoSite())
