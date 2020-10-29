from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungle

@app.route('/')
def home():
   return render_template('index.html')


@app.route('/review', methods=['GET'])
def read_review():
   result = list(db.books.find({},{'_id':0}))
   return jsonify({'result':'success', 'books':result})


@app.route('/review', methods=['POST'])
def save_review():
   title_receive = request.form['title_give']
   author_receive = request.form['author_give']
   review_receive = request.form['review_give']
   book = {
      'title': title_receive,
      'author' : author_receive,
      'review' : review_receive
   }

   db.books.insert_one(book)

   return jsonify({'result':'success', 'msg':'리뷰 완료!'})


if __name__ == '__main__':
   app.run()