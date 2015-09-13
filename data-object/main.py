#data objects
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):   # these are instances

        luke = Character()
        luke.name = "Luke Skywalker"
        luke.profession = "Jedia Knight"
        luke.age = 26
        luke.home_planet = "Tattooine"

        leia = Character()
        leia.name = "Princess Leia"
        leia.profession = "Princess"
        leia.age = luke.age
        leia.home_planet = "Alderan"

        yoda = Character()
        yoda.name = "Master Yoda"
        yoda.profession = "Jedi Knight"
        yoda.age = 762
        yoda.home_planet = "Dagobah"


        chars = [luke, leia, yoda]  #this an array
        print chars[1].profession


class Character(object):
    def __init__(self):   #construtor function
        self.name = ""
        self.profession = ""
        self.age = 0
        self.home_planet = ""


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
