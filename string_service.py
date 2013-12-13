import textwrap

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define('port', default=8000, help='run on the given port', type=int)

class ReverseHandler(tornado.web.RequestHandler):
    # string matched inside () in url will be passed as input
    def get(self, input):
        self.write(input[::-1])

class WrapHandler(tornado.web.RequestHandler):
    def post(self):
        text = self.get_argument('text')
        width = self.get_argument('width', 40)
        self.write(textwrap.fill(text, width))


if __name__ == '__main__':
    tornado.options.parse_command_line()
    # the () tells Tornado to save the string that matched inside the parentheses, and pass theat string to the RequestHandler's request method as a parameter
    #if there are additional sets of (), the matched strings will be passed in as additional parameters
    app = tornado.web.Application(handlers = [
        (r'/reverse/(\w+)', ReverseHandler),
        (r'/wrap', WrapHandler)
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()