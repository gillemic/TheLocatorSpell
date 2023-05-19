from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, SelectField, DateField,
                     SelectMultipleField, BooleanField, RadioField, PasswordField, widgets)
from wtforms.validators import InputRequired, Length
from datetime import date

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(),
                                             Length(min=6, max=100)])
    password = PasswordField('Password', validators=[InputRequired(),
                                                     Length(min=6, max=100)])
    
    remember = BooleanField('Remember me')

class SignupForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(),
                                             Length(min=6, max=100)])
    name = StringField('Name', validators=[InputRequired(),
                                             Length(max=100)])
    password = PasswordField('Password', validators=[InputRequired(),
                                                     Length(min=6, max=100)])

class SearchForm(FlaskForm):
    activity = MultiCheckboxField('Activity', choices=['Magic The Gathering', 'Pokemon', 
                                                          'Yu-Gi-Oh', 'DnD'])
    location = SelectField('Location', choices=['Any', 'Portland, OR', 'Seattle, WA'])
    start_date = DateField('Start Date', default=date.today())
    end_date = DateField('End Date', default=None)
    price = RadioField('Price', choices=['Any', 'Free', '$5+', '$10+', '$20+', '$50+'], default='Any')
    category = MultiCheckboxField('Category', choices=['Local', 'Regional', 'Major', 'Convention'])


class AddEventForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(),
                                           Length(max=100)])
    tournament_organizer = StringField('Tournament Organizer', validators=[InputRequired(),
                                                                           Length(max=100)])
    location = StringField('Location', validators=[InputRequired(),
                                                   Length(max=100)])
    event_type = StringField('Event Type', validators=[InputRequired(),
                                                       Length(max=100)])
    category = RadioField('Category', choices=['Local', 'Regional', 'Major', 'Convention'])
    start_date = DateField('Start Date', validators=[InputRequired()])
    end_date = DateField('End Date')
    charity = BooleanField('Charity Event')
    promoted = BooleanField('Promoted Event')
    price = IntegerField('Price', validators=[InputRequired()], default='0')
    url = StringField('URL', validators=[Length(max=100)])
    description = TextAreaField('Description', validators=[InputRequired(),Length(max=1000)])

