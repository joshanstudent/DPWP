#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self):# this function starts everything. Initializing, Catalyst.
        self.response.write('Hello world!')
        #code goes here, when beginning to work on the next assignment

    #also a (def additional_functions) will be used with next assignment, this is just a
    #early setup of this function
    def additional_functions(self):
        pass
        #the code goes here


#never touch this code, this code is here to make sure that python will work within the web browser
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
