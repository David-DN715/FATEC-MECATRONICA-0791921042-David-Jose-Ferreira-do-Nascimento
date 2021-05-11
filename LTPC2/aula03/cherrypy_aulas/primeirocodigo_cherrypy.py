#Primero progama com Cherrypy

# Importamos a Biblioteca
import cherrypy

#implementamos nossa aplicação WEB
class NossoSite(object):
    @cherrypy.expose()
    def index(self):
        return "Olá Davidson!"
#Se pedirmos para o arquivo roda!
if __name__ =="__main__":
    cherrypy.quickstart(NossoSite())
