import requests as r


def test_1():
    data = {
            'first_num': "2",
            'second_num': "3",
            'operation': "+",
            '_xsrf': '2|a854d631|73132441a7cf7d4a38279244e7b2c43a|1665387598'
        }
    resultat_html = r.post("http://localhost:8888/result",
        data).content.decode("utf-8")
    resultat_num = int(resultat_html[resultat_html.index('<span>')
        + 6:resultat_html.index('</span>')-1])
    assert resultat_num == 5


def test_2():
    data = {
            'first_num': "12",
            'second_num': "3",
            'operation': "*",
            '_xsrf': '2|a854d631|73132441a7cf7d4a38279244e7b2c43a|1665387598'
        }
    resultat_html = r.post("http://localhost:8888/result",
        data).content.decode("utf-8")
    resultat_num = int(resultat_html[resultat_html.index('<span>')
        + 6:resultat_html.index('</span>')-1])
    assert resultat_num == 36


def test_3():
    data = {
            'first_num': "12",
            'second_num': "3",
            'operation': "-",
            '_xsrf': '2|a854d631|73132441a7cf7d4a38279244e7b2c43a|1665387598'
        }
    resultat_html = r.post("http://localhost:8888/result",
        data).content.decode("utf-8")
    resultat_num = int(resultat_html[resultat_html.index('<span>')
        + 6:resultat_html.index('</span>')-1])
    assert resultat_num == 9