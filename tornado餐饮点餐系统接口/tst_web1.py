import tornado.httpserver
import tornado.ioloop
import tornado.web
import json
from concurrent.futures import ThreadPoolExecutor
import tornado.concurrent
class MainHandler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(1000)
    @tornado.gen.coroutine
    def get(self,*args,**kwargs):
        yield self.get_response()
    @tornado.concurrent.run_on_executor
    def get_response(self,*args,**kwargs):
        foods_json = [{
                "name": "野蘑菇炖鸡",
                "img": "./static/images/mogu_ji.png",
                "price": 58.00
            }, {
                "name": "大盘鸡",
                "img": "./static/images/dapan_ji.png",
                "price": 62.00
            },
            {
                "name": "爆椒鸡",
                "img": "./static/images/baojiao_ji.png",
                "price": 48.00
            }, {
                "name": "辣子鸡丁",
                "img": "./static/images/lazi_ji.png",
                "price": 39.00
            },
            {
                "name": "麻辣鱼头",
                "img": "./static/images/mala_yu.png",
                "price": 52.00
            }, {
                "name": "酸菜鱼",
                "img": "./static/images/lazi_ji.png",
                "price": 53.00
            },
            {
                "name": "红烧带鱼",
                "img": "./static/images/mala_yu.png",
                "price": 42.00
            }, {
                "name": "水煮肉片",
                "img": "./static/images/dapan_ji.png",
                "price": 35.00
            },
            {
                "name": "毛血旺",
                "img": "./static/images/baojiao_ji.png",
                "price": 30.00
            }, {
                "name": "鱼香肉丝",
                "img": "./static/images/lazi_ji.png",
                "price": 18.00
            },
            {
                "name": "烧大肠",
                "img": "./static/images/mala_yu.png",
                "price": 28.00
            }, {
                "name": "农家小炒肉",
                "img": "./static/images/lazi_ji.png",
                "price": 25.00
            },
            {
                "name": "青椒肉丝",
                "img": "./static/images/mala_yu.png",
                "price": 20.00
            }, {
                "name": "京酱肉丝",
                "img": "./static/images/mala_yu.png",
                "price": 19.00
            }, {
                "name": "红烧肉（带饼）",
                "img": "./static/images/lazi_ji.png",
                "price": 30.00
            },
            {
                "name": "回锅肉",
                "img": "./static/images/mala_yu.png",
                "price": 16.00
            }, {
                "name": "木须肉",
                "img": "./static/images/mala_yu.png",
                "price": 18.00
            }, {
                "name": "酸豆角炒肉末",
                "img": "./static/images/lazi_ji.png",
                "price": 22.00
            },
            {
                "name": "鲜辣烤鱼",
                "img": "./static/images/mala_yu.png",
                "price": 79.00
            }, {
                "name": "干锅菜花",
                "img": "./static/images/mala_yu.png",
                "price": 16.00
            }, {
                "name": "干锅千页豆腐",
                "img": "./static/images/lazi_ji.png",
                "price": 15.00
            },
            {
                "name": "西红柿烧牛楠",
                "img": "./static/images/mala_yu.png",
                "price": 29.00
            }, {
                "name": "绿豆牙炒馓子",
                "img": "./static/images/mala_yu.png",
                "price": 13.00
            }, {
                "name": "西红柿炒鸡蛋",
                "img": "./static/images/lazi_ji.png",
                "price": 12.00
            },
            {
                "name": "酸辣土豆丝",
                "img": "./static/images/mala_yu.png",
                "price": 14.00
            }, {
                "name": "香菇青菜",
                "img": "./static/images/mala_yu.png",
                "price": 17.00
            }, {
                "name": "麻辣豆腐",
                "img": "./static/images/lazi_ji.png",
                "price": 10.00
            },
            {
                "name": "鱼香茄子",
                "img": "./static/images/mala_yu.png",
                "price": 15.00
            }, {
                "name": "爆炒花哈",
                "img": "./static/images/mala_yu.png",
                "price": 23.00
            }, {
                "name": "豆芽粉条",
                "img": "./static/images/lazi_ji.png",
                "price": 11.00
            },
            {
                "name": "红油耳丝",
                "img": "./static/images/mala_yu.png",
                "price": 16.00
            }, {
                "name": "变蛋黄豆",
                "img": "./static/images/mala_yu.png",
                "price": 9.00
            }, {
                "name": "麻辣花生米",
                "img": "./static/images/lazi_ji.png",
                "price": 9.00
            },
            {
                "name": "水蒸蛋",
                "img": "./static/images/mala_yu.png",
                "price": 10.00
            }, {
                "name": "烧茄子",
                "img": "./static/images/mala_yu.png",
                "price": 14.00
            }, {
                "name": "炒饼丝",
                "img": "./static/images/lazi_ji.png",
                "price": 8.00
            }];
        foods = json.dumps(foods_json)
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write(foods)


if __name__ == '__main__':
    application = tornado.web.Application(
        handlers=[
            (r'/', MainHandler)
        ]
    )
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8001)
    tornado.ioloop.IOLoop.instance().start()
