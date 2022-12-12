import os
from flask import render_template, send_from_directory
from flask_flatpages import FlatPages
from app import app

def smart_truncate(content, length=100, suffix='...'):
    if len(content) <= length:
        return content
    else:
        return ' '.join(content[:length+1].split(' ')[0:-1]) + suffix

pages = FlatPages(app)

latest = sorted(pages, reverse=True, key=lambda p: str(p.meta['date']))

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', title='Home', pages=latest, trunc=smart_truncate)

@app.route('/about')
def about():
	return render_template('about.html', title='About')

@app.route('/<path:path>.html')
def page(path):
	page = pages.get_or_404(path)
	return render_template('page.html', page=page)