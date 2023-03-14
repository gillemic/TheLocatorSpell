import sys
from app import create_app
from flask_talisman import Talisman

app = create_app()

Talisman(app, content_security_policy=None)
 
if __name__ == "__main__":
	app.run(port=8000)