from flask_api import status

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

account(...) #Creation of a new account
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

@app.route('event', methods=['GET', 'POST'])
def event(id=None,):
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