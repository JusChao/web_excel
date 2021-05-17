from flask import Flask
from excel_web.helper import is_isbn_or_key
from excel_web.yushu_book import YuShuBook
from excel_web.fisher import app

app = Flask(__name__)
app.config.from_object('config')

@app.route('/book/search/<q>/<page>')
def search(q, page):
    '''
    :param q: 普通关键字 isbn
    :param page:
    :return:b
    '''

    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YushuBook.search_by_keyword(q)

    return jsonify(result)
