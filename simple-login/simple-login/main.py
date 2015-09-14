
import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self):# this function starts everything. Initializing, Catalyst.
        page_head = '''<!DOCTYPE HTML>

<html>
    <head>
        <title>Simple Form</title>
    </head>
    <body>'''

        page_body = '''<form method="GET" action="">
            <label>Name: </label><input type="text" name="user" />
            <label>Email: </label><input type="text" name="email" />
            <input type="submit" value="Submit" />'''

        page_close = '''
        </form>
    </body>
</html>'''


# the column mean the same as == True, just another way to write this code# the column mean the same as == True, just another way to write this code

# To access items (client -> server) use this code self.request.GET[]
#To print items (server -> client) use this code self.response.write()
        if self.request.GET:
            user = self.request.GET['user'] # this is to print
            email = self.request.GET['email'] # this is to print
            self.response.write(page_head + user + ' ' + email + page_body + page_close)# if you remove page_body the input name and email will display on the web page without the entry forms.
        else:
            self.response.write(page_head + page_body + page_close) # This is printing out the information of the form


#never touch this code, this code is here to make sure that python will work within the web browser
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
