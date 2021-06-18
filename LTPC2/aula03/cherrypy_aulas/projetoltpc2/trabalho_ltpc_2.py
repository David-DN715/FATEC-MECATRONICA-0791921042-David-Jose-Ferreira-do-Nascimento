import random
import string
import cherrypy

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return"""
         <!DOCTYPE html>
         <html>
          <head>
          <section class="hero is-success">
          <div class="hero-body">
          <p class="title">
            Bem Vindo ao anime turn!
          </p>
          <p class="subtitle">
            Por favor, responda as perguntas abaixo!
          </p>
          </div>
          </section>
          </head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.2/css/bulma.min.css">
          <title>anime turn</title>
          <style>
          .box{
            width: is-fullwidth;
            height: is-container;
            border: 2px solid green;
            margin:0.5px;
            color: #fff;
            }
            .image{background-image: url(https://image.ibb.co/jUeDqA/KORIGENGI-FANJI-Midoriya-Izuku-All-Might.png);
            background-color: inherit;
            background-size: cover;
            background-repeat: no-repeat;
            color: #000;}
            
            .image2{background-image: url(https://wallpapertag.com/wallpaper/full/1/7/0/766986-amazing-my-hero-academia-wallpapers-1080x1920.jpg);
            background-color: inherit;
            background-size: cover;
            background-repeat: no-repeat;
            color: #000;}
            </style>
            
          <body class = has-background-black>
           <div class = 'box image'>
            <form method="get" action="resposta">
            <br><br>
            <input class="input is-rounded" type="text" placeholder="Qual seu nome?"name = "nome" required> 
            <br><br>
            <input class="input is-rounded" type="text" placeholder="Qual sua idade? "name = "idade" required> 
            <br><br>
            <input class="input is-rounded" type="text" placeholder="Gosta de que tipo de anime? "name = "genero"> 
            <br><br>
              <input class="input is-rounded" type="text" placeholder="Gosta de assistir lançamentos?"name = "novo">  
              <br><br>
              <input class="input is-rounded" type="text" placeholder="para você Goku é um?"name = "goku"> 
              <br><br>
              <div class = "content has-text-centered">
            <button class="button is-success is-rounded">Teishutsu suru/Submeter</button>
            </div>
            </div>
            <form>
          </body>
        </html>"""


    @cherrypy.expose
    def generate(self, length=8):
        return ''.join(random.sample(string.hexdigits, int(length)))

    @cherrypy.expose
    def resposta(self, nome ,idade, genero, novo, goku):
        lista = ["https://i.pinimg.com/736x/fa/d8/29/fad829824e9bf14e86a3bfb265a5eb2e.jpg", "https://w.wallhaven.cc/full/72/wallhaven-726pj3.png", "https://i.pinimg.com/originals/07/20/36/0720368eb50b94da5d3e43314cfc5f21.jpg", "https://i.pinimg.com/originals/57/2e/72/572e7271081ff9d3fa4bdf5e5e0a9867.jpg", "https://3.bp.blogspot.com/-8pBwGney7Ok/UdMjXdtUWJI/AAAAAAAACOk/W5eIlsT8RKs/s350/bigode-vegeta-gt-top-7-dragon-ball.png", "https://colorindonuvens.files.wordpress.com/2012/05/lulu-famc3adlia.jpg"]
        sorteio = random.choice(lista)
        return f"""
        <!DOCTYPE html>
        <html>
          <head>
          <section class="hero is-success">
            <div class="hero-body">
            <p class="title">
            Abaixo há um link para os lançamentos!
            </p>
            <p class="subtitle">
            Boa Diversão!
            </p>
            </div>
            </section>
          </head>
          
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.2/css/bulma.min.css">
          
          <body class = has-background-black>
          <form method="get" action="resposta">
          <div class = 'card-content has-text-white has-text-alligment-left'>
          <div class="card">
  <div class="card-image">
    <figure class="image is-2by1">
      <img src= {sorteio} alt="Placeholder image">
    </figure>
  </div>
  <div class="card-content">
    <div class="media">
      <div class="media-left">
        <figure class="image is-48x48">
          <img class = 'is-rounded' src= {sorteio} alt="Placeholder image">
        </figure>
      </div>
      <div class="media-content">
        <p class="title is-4">Anime turn</p>
        <p class="subtitle is-6">{nome.capitalize()} <br> idade: {idade}</p>
      </div>
    </div>

    <div class="content">
      Agradecemos pelas perguntas respondidas no momento não consseguimos filtrar as opções que você gosta, para melhor atender, então disponilibilizamos o link para ir direto aos lançamentos de animes!
      <br>Divirta-se!
      <br><a href = 'https://www.crunchyroll.com/pt-br/videos/anime/updated'>Lançamentos!</a>
      <br><a href = "http://localhost:8080">Voltar</a>
      <br>
    </div>
  </div>
</div>
          </body>
        </html>"""


if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())
