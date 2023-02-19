from . import db

class Event(db.Model):
  event_id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
  name = db.Column(db.String(100), nullable=False) # string name of event
  tournament_organizer = db.Column(db.String(100), nullable=False) # string name of tournament organizer
  location = db.Column(db.String(100), nullable=False) # string of physical address
  event_type = db.Column(db.String(100), nullable=False) # string of name of game, or event type
  category = db.Column(db.String(10)) # Category - Local, Minor, Major
  start_date = db.Column(db.Date, nullable=False) # start date of event
  end_date = db.Column(db.Date) # end date of event (if more than 1 day)
  charity = db.Column(db.Boolean) # bool for is/isn't a charity event
  promoted = db.Column(db.Boolean) # bool for is/isn't a promoted event
  price = db.Column(db.Integer, nullable=False) # price of event
  url = db.Column(db.String(100)) # url to website of event if there is one
  description = db.Column(db.String(1000), nullable=False) # event description