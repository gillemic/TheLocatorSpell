import os
from flask import Flask, render_template, url_for, json, request, Blueprint, current_app
from flask_login import login_required
#from flask_flatpages import FlatPages
from . import db

def smart_truncate(content, length=100, suffix='...'):
    if len(content) <= length:
        return content
    else:
        return ' '.join(content[:length+1].split(' ')[0:-1]) + suffix

#pages = FlatPages(app)

#latest = sorted(pages, reverse=True, key=lambda p: str(p.meta['date']))

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
	return render_template('about.html', title='About')

@main.route('/events')
def events():
    SITE_ROOT = current_app.root_path
    json_url = os.path.join(SITE_ROOT, "static", "NEW_MOCK_DATA.json")
    data = json.load(open(json_url))
    query = request.args.get('query')
    return render_template('events.html', title='Events', data=data, query=query)

@main.route('/add_event')
@login_required
def add_event():
     return render_template('add_event.html')

@main.route('/blog')
def blog():
     return render_template('blog.html')


"""
@app.route('/login')
def login():
"""

"""
@app.route('/signup')
def signup():
"""

"""
@app.route('/blog')
def blog():
"""

"""
@app.route('/<path:path>.html')
def page(path):
	page = pages.get_or_404(path)
	return render_template('page.html', page=page)
"""