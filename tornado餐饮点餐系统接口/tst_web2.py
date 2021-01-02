import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):

        self.write("让我们大干一场，")
        self.finish("欢迎来到这个世界,")


application = tornado.web.Application([
    (r"/",MainHandler)],
)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()