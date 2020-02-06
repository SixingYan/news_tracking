#! coding: utf-8
from router import urlpatterns
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
from tornado.options import define, options

define("port", default=5011, help="run on the given port", type=int)

if __name__ == '__main__':

    from config import settings
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=urlpatterns, **settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    
