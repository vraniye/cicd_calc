import tornado.ioloop
import tornado.web
import os


def resultat(first_num, op, second_num):
    if op == "+":
        return first_num + second_num
    elif op == "-":
        return first_num - second_num
    elif op == "*":
        return first_num * second_num
    elif op == "/":
        if second_num != 0:
            return first_num/second_num
        else:
            return "На ноль делить нельзя"
    else:
        return "Такой опреации не существует"


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("result.html", result=None)


class ResultHandler(tornado.web.RequestHandler):
    def post(self):
        fisrt_number = self.get_argument("first_num",
            default=None, strip=False)
        second_number = self.get_argument("second_num",
            default=None, strip=False)
        operation = self.get_argument("operation", default=None, strip=False)
        try:
            result = resultat(int(fisrt_number), operation, int(second_number))
            self.render("result.html", result=result)
        except Exception:
            self.render("result.html",
                result="Неверно введены данные, попробуйте ещё раз")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/result", ResultHandler),
    ],
    debug = True,
    autoreload = True,
    static_path = os.path.join(os.path.dirname(__file__), "static"))


if __name__=="__main__":
    app = make_app()
    port = 8888
    app.listen(port)
    print(f'Server is listening on localhost on port {8888}')
    tornado.ioloop.IOLoop.current().start()