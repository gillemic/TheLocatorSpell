import sys
from app import create_app
from flask_talisman import Talisman

Talisman(create_app, content_security_policy=None)
 
if __name__ == "__main__":
	create_app.run(port=8000)