
import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self):# this function starts everything. Initializing, Catalyst.
        self.response.write('Hello world!')


    #also a (def additional_functions) will be used with next assignment, this is just a
    #early setup of this function
    def additional_functions(self):
        pass
       


#never touch this code, this code is here to make sure that python will work within the web browser
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
