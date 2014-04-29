# GAE libs
import os
import webapp2, jinja2
from google.appengine.api import users

# sys libs
import sys
sys.path.insert(0, "lib")

# custom libs
import markdown

JINJA = jinja2.Environment(
                            loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                            extensions=['jinja2.ext.autoescape'],
                            autoescape=True)

class MainHandler(webapp2.RequestHandler) :
    arr_post = []

    def get(self) :
        template = JINJA.get_template("index.html")
        self.response.write(template.render(values))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
