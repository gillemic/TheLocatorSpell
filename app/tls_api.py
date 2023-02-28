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

account()
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