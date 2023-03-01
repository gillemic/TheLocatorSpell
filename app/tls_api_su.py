#super user API requests

from flask_api import status

@app.route('eventsu', methods=['POST', 'PATCH', 'DELETE'])
def eventsu(id=None, Name=None, EO=None, location=None, Type=None, Catagory=None, Start_Date=None, End_Date=None, Charity=None, Promoted=None, Price=None, URL=None, Description=None):
    if request.method == 'POST':
        if [__EO is logged in__]:
            [__Create new event__]
            [__populate event data from POST payload__]
            [__Attach new Event id to EO profile__]
        else
            return "User not authorized", status.HTTP_403_FORBIDDEN
        
    elif request.method == 'PATCH':
        if [__Check SU Oauth__]
            if id=None:
                return "Record not found", status.HTTP_400_BAD_REQUEST
            else:
                [__Udate event data__]
        else:
            return "User not authorized", status.HTTP_403_FORBIDDEN

        
    elif request.method == 'DELETE':
        if [__check Oauth__]:
            if [__Event id exists__]:
                [__for each contact email listed in chain, go to each account and delete event ID__]
                [__R.I.P. Account__]
            
        else:
            return "User not authorized", status.HTTP_403_FORBIDDEN

    else:
        return "Unkown request", status.HTTP_400_BAD_REQUEST


@app.route('accountsu', methods=['POST', 'PATCH', 'DELETE'])
def accountsu(id=None, Name=None, Public_Contact_Info=None, Private_Contact_Info=None, Website=None, Location=None, Notes=None, Events=None):
    if request.method == 'POST':
        if [__SU is logged in__]:
            [Create account details based on fun args]
        else:
            return "User not authorized", status.HTTP_403_FORBIDDEN
        
    elif request.method == 'PATCH':
        if [__check Oauth__]:
            [Create account details based on fun args]
        else:
            return "User not authorized", status.HTTP_403_FORBIDDEN
        
    elif request.method == 'DELETE':
        if [__check Oauth__]:
            if [__Account id exists__]:
                [__R.I.P. Account__]
        else:
            return "User not authorized", status.HTTP_403_FORBIDDEN
    else:
        return "Unkown request", status.HTTP_400_BAD_REQUEST