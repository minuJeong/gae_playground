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

class StringData() :
    def __init__(self) :
        self.stringData = markdown.markdown("# head #")

class MainHandler(webapp2.RequestHandler) :
    arr_post = []

    def get(self) :

        data = StringData()
        self.response.write(data.stringData)
        user = users.get_current_user()
        if user :
            greeting = "Welcome, %s (<a href=%s>sign out</a>)" % (user.nickname(), users.create_logout_url('/'))
        else :
            greeting = "<a href=%s>Sign in or register</a>" % (users.create_login_url('/'))

        values = {
            "greeting": greeting

        }

        template = JINJA.get_template("index.html")
        self.response.write(template.render(values))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
