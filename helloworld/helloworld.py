import webapp2
from google.appengine.api import urlfetch

def experiment_interest_level():
	data = urlfetch.fetch("http://www.reddit.com/r/MysteryManipulation/comments/1lj9pa/15/")
	if data.status_code == 200:
		return str(data.content).find('I think this would be easier to do using Ruby instead of Python.')

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(experiment_interest_level())

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
