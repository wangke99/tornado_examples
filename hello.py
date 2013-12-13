#Tornado is a frameworkf ro writing responses to HTTP requests
#Your job is to write 'handlers' that respond to requests that match particular criteria


#import at least the following four libraries
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

#tornado.options library for reading options from the command line
from tornado.options import define, options

#any option in a define statement will become available as an atribute of the global options object
define('port', default = 8000, help = 'run on the given port', type = int)



#tornado request handler class
#calls the method corresponding to the HTTP method of the request
#useful methods: get_argument, write -- writes the string into the HTTP response
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')

#make the Tornado application run
if __name__ == "__main__":
    #parse the command line
    tornado.options.parse_command_line()
    #create an instance of Application class
    #handlers parameter should be a list of tuples
    #each tuple contains a regular expression to match, and a RequestHandler
    app = tornado.web.Application(handlers = [(r"/", IndexHandler)])

    #boilerplate from here
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()