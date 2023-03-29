import os
import re
import sqlite3
from datetime import datetime
from flask import Flask, render_template, url_for, json, request, Blueprint, current_app, flash, redirect
from flask_login import login_required
#from flask_flatpages import FlatPages
from . import db
from .models import Event

def smart_truncate(content, length=100, suffix='...'):
    if len(content) <= length:
        return content
    else:
        return ' '.join(content[:length+1].split(' ')[0:-1]) + suffix
    
def get_db_connection():
    conn = sqlite3.connect(current_app.config['SQLALCHEMY_DATABASE_URI'])
    conn.row_factory = sqlite3.Row
    return conn

#pages = FlatPages(app)

#latest = sorted(pages, reverse=True, key=lambda p: str(p.meta['date']))

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
	return render_template('about.html', title='About Us')

@main.route('/events')
def events():
    SITE_ROOT = current_app.root_path
    json_url = os.path.join(SITE_ROOT, "static", "NEW_MOCK_DATA.json")
    data = json.load(open(json_url))
    
    query = request.args.get('query')
    
    events = Event.query.all()
    # conn = get_db_connection()
    # events = conn.execute('SELECT * FROM event').fetchall()
    # conn.close()
    
    return render_template('events.html', title='Events', data=data+events, query=query)

@main.route('/add_event')
@login_required
def add_event():
    events = Event.query.all()
    return render_template('add_event.html', events=events)

@main.route('/add_event', methods=['POST'])
def add_event_post():
    # code to validate and add user to database goes here
    name = request.form.get('name')
    tournament_organizer = request.form.get('tournament_organizer')
    location = request.form.get('location')
    event_type = request.form.get('event_type')
    category = request.form.get('category')
    start_date = datetime.strptime(request.form.get('start_date'), '%Y-%m-%d').date() if request.form.get('start_date') else None
    end_date = datetime.strptime(request.form.get('end_date'), '%Y-%m-%d').date() if request.form.get('end_date') else start_date
    # end_date = request.form.get('end_date')
    charity = bool(request.form.get('charity'))
    promoted = bool(request.form.get('promoted'))
    price = request.form.get('price')
    url = request.form.get('url')
    description = request.form.get('description')

    if not (name or tournament_organizer or location or event_type or start_date or price or description):
        flash('Fields cannot be blank!')
        return redirect(url_for('main.add_event'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_event = Event(name=name, tournament_organizer=tournament_organizer, location=location, event_type=event_type, category=category, start_date=start_date, end_date=end_date, charity=charity, promoted=promoted, price=price, url=url, description=description)

    # add the new user to the database
    db.session.add(new_event)
    db.session.commit()
    flash('Event added!')
    return redirect(url_for('main.add_event'))



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