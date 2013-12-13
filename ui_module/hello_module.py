import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options

import os.path

from tornado.options import define, options
define('port', default=8000, help="run on the given port", type=int)

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('hello.html')

#allows you to embed separate CSS and JavaScript via
#    * embedded_css()
#    * embedded_javascript()
#    * css_files()
#    * javascript_files()
        
class HelloModule(tornado.web.UIModule):
    def render(self):
        return '<h1>Hello, world!</h1>'

#    def embedded_javascript(self):
#        return 'document.write(\"hi!\")'

#    def embedded_css(self):
#        return ".book {background-color:#F5F5F5}"

#    def css_files(self):
#        return '/static/css/newreleases.css'

#    def javascript_files(self):
#        return 'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.14/jquery-ui.min.js'



        
        
# set up the UI module through the dictionary ui_modules in Application
# one common application is to iterate over teh results of a database or API query
# common to put the module templates in templates/modules/
# helps reuse UI code



if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers = [
        (r'/', HelloHandler)
    ],
                                  template_path = os.path.join(os.path.dirname(__file__), 'templates'),
                                  ui_modules = {'Hello': HelloModule}
    )

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()