import sys
from app import app
from flask_talisman import Talisman

Talisman(app, content_security_policy=None)
 
if __name__ == "__main__":
	app.run(port=8000)