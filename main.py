# GAE libs
import webapp2
from google.appengine.api import users

# sys libs
import sys
sys.path.insert(0, "lib")

# custom libs
import markdown

class StringData():
    def __init__(self) :
        self.stringData = markdown.markdown("# head #")

class MainHandler(webapp2.RequestHandler):
    def get(self):
        data = StringData()
        self.response.write(data.stringData)
        user = users.get_current_user()
        if user :
            greeting = "Welcome, %s (<a href=%s>sign out</a>)" % (user.nickname(), users.create_logout_url('/'))
        else :
            greeting = "<a href=%s>Sign in or register</a>" % (users.create_login_url('/'))

        self.response.write("<html><body> %s </body></html>" % (greeting) )

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
