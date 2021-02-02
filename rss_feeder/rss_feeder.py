from flask import Flask, render_template, url_for
import feedparser
import newspaper
from newspaper import Article

app = Flask(__name__)

feeds = feedparser.parse('https://www.vanityfair.com/feed/rss')

feeder_list = []

i = 0
for feed in feeds['entries']:
    link = feeds.entries[i].links[0].href
    summary = feeds.entries[i].summary_detail.value
    a = Article(link, language = 'en')
    a.download()
    a.parse()
    title = a.title 
    content = a.text
    i += 1  
    
    feeder = {
        'link' : link,
        'title' : title,
        'summary' : summary,
        'content' : content
    }

    feeder_list.append(feeder)

@app.route("/")
@app.route("/home")
def home():
    return(render_template('home.html', posts = feeder_list))
