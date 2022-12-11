import json

from flask import Flask, redirect, url_for
from flask import render_template, request
from bot import *
# import feedparser


import sqlite3



app = Flask(__name__)


# NEWS_CHANNEL={
# 	'bbc':'http://feeds.bbci.co.uk/news/rss.xml',
# 	'cnn':'http://rss.cnn.com/rss/edition.rss',
# 	'ndtv':'http://feeds.feedburner.com/ndtvnews-top-stories',
# 	'rediff':'http://www.rediff.com/rss/inrss.xml'
# }
@app.route('/', methods=['GET', 'POST'])
def home():
    query = request.form.get('code')  # Enable Post Method
    # query=request.args.get('search') #Enable GET Method
    if not query:
        query = 'ok'
    return render_template('index.html', data="")


@app.route('/thread', methods=['GET', 'POST'])
def homeb():
    query = request.form.get('query')  # Enable Post Method
    # query=request.args.get('search') #Enable GET Method
    if not query:
        query = 'ok'
    # x = main(query)
    # return render_template('main.html', data=x)

    # return json.dumps({'status': 'OK', 'data': x});
    # return



@app.route('/code', methods=['GET', 'POST'])
def homea():

    query = request.form.get('code')  # Enable Post Method
    # query=request.args.get('search') #Enable GET Method
    if not query:
        query = 'ok'

    if query == "ok":
        start()





    # cursor = conn.execute("SELECT * from human")
    # for query_result in cursor.fetchall():
    #     x = query
    #     if x in query_result:
    #          # print('Username already exists')
    #        return render_template('main.html', data="success")
    #
    return redirect(url_for('home'))
    # print ("Operation done successfully");


# if not query or query.lower() not in NEWS_CHANNEL:
# 	channel='bbc'
# else:
# 	channel=query
# feed=feedparser.parse(NEWS_CHANNEL[channel])
# news=feed['entries']

# return render_template('news.html')









if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port='8080')
