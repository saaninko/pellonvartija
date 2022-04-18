import ast
import os.path

import tornado.ioloop
import tornado.web

CURDIR = os.path.dirname(__file__)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        with open(os.path.join(CURDIR, '../data/data.txt'), 'r', encoding='utf-8') as data_file:
            data = [ast.literal_eval(_data) for _data in data_file.readlines()]
            self.render('../templates/index.html', data=data)
    
    def post(self):
        with open(os.path.join(CURDIR, '../data/data.txt'), 'a', encoding='utf-8') as data_file:
            stuff = self.request.body
            data_file.write(stuff.decode('utf-8') + '\n')

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8976)
    tornado.ioloop.IOLoop.current().start()