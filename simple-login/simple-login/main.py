
import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self):# this function starts everything. Initializing, Catalyst.
        page_head = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
    </head>
    <body>'''

       page_body = '''<form method="GET">
            <label>Name:</label><input type="text" name="user" />
            <label>Email:</label><input type="text" name="email" />
            <input type="submit" value="Submit" />'''
    
       page_close = '''
        </form>
    </body>
</html>
        '''
        if self.request.GET: # the column mean the same as ==True, just another way to write this code
            #print self.request.GET['user'] # This string is to print out to the console

            #stroes info we got from the form
            user = self.request.GET['user'] # this is to print
            email = self.request.GET['email'] # this is to print

        #self.response.write(page) # This is printing out the information of the form


    #also a (def additional_functions) will be used with next assignment, this is just a
    #early setup of this function
    def additional_functions(self):
        pass



#never touch this code, this code is here to make sure that python will work within the web browser
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
