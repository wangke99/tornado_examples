import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define('port', default=8000, help='run on the given port', type=int)

# template syntax
# Templates are text files marked up with Python expressions and control sequences
# you can put any Python expression inside double curly braces {{}}
# you can also include Python conditionals and loops; control statements are surrounded by
# {% if page is None %} or {% if len(entries) == 3 %}
# for example
# <ul>
#     {% for book in books %}
#     <li> {{ book }} </li>}
#     {% end %}
# </ul>
#
# Using functions inside templates
# * escape(s)
# * url_escape(s)
# * json_encode(val)
# * squeeze(s) -- replace sequences of more than one whatespace with a single space





class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

#words enclosed in double curly brackets are placeholders that we want to replace when the template is rendered
        
class PoemPageHandler(tornado.web.RequestHandler):
    def post(self):
        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        self.render('poem.html', roads=noun1, wood=noun2, made=verb, difference=noun3)

if __name__ == '__main__':
    tornado.options.parse_command_line()


    #passing the template_path parameter to the Application object
    #tells Tornado where to look for template files
    app = tornado.web.Application(handlers = [
        (r'/', IndexHandler),
        (r'/poem', PoemPageHandler)
    ], template_path = os.path.join(os.path.dirname(__file__), "templates")
                              )

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
                                  