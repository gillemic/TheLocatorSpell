"""
Oauth required for any API access points.
"""


"""
GET -

event(
    id: INT of Numerical entry into database
    Name: String of name of event
    EO: String of Tournament Organizer
    Location: Fuzzy find
    Type: String of name of game or event type
    Catagory: String of "Local", "Minor", "Major"
    Start_Date: Date string of when event will start
    End_Date: Date string of when event will end
    Charity: Boolean is or isn't charaity event
    Promoted: Boolean is or isn't promoted event
    Price: String of dollar value
)

account() #view user data
"""



"""
POST - 

#If no ID then create a new event. If ID then modify current event.
event(id=None, 
    Name: String of name of event
    EO: String of Tournament Organizer
    Location: String of physical address
    Type: String of name of game or event type
    Catagory: String of "Local", "Minor", "Major"
    Start_Date: Date string of when event will start
    End_Date: Date string of when event will end
    Charity: Boolean is or isn't charaity event
    Promoted: Boolean is or isn't promoted event
    Price: String of dollar value
    URL: String of direct URL address
    Description: String of event description
)

account(id:	INT EO id number
Name:	String of organizations name
Public_Contact_Info:	String of main way for general users to contact EO for questions.
Private_Contact_Info:	String of main way for TLS to contact EO for questions (non-public facing)
Website:	String of website URL
Location:	String of physical location address or "N/A"
Notes:	String of additional notes
Events:	List of INT event id's.
) #Creation of a new account
"""


"""
PATCH - 

event(id, ...) #everything but ID can be changed

account(...) #everything but ID can be changed
"""


"""
DELETE - 

event(id)
"""

from flask_api import status

#there has got to be a better way to do this than naming off every single argument...
@app.route('event', methods=['GET', 'POST'])
def event(id=None, Name=None, EO=None, location=None, Type=None, Catagory=None, Start_Date=None, End_Date=None, Charity=None, Promoted=None, Price=None, URL=None, Description=None):
    if request.method == 'POST':
        if [__a user is logged in__]:
            [__Create new event using their email address__]
            [__populate event data from POST payload__]
            
            
    elif request.method == 'PATCH':
    else:
        if [__user email__] not in [__email in list of event contact emails__] 
            return "User not authorized", status.HTTP_403_FORBIDDEN
        else
            if id=None:
                return "Record not found", status.HTTP_400_BAD_REQUEST
            else
                [__Udate event data__]
                
                
@app.route('account', methods=['GET', 'POST'])
def account(id=None, Name=None, Public_Contact_Info=None, Private_Contact_Info=None, Website=None, Location=None, Notes=None, Events=None):
    