import sys
from app import app
from flask_frozen import Freezer
from flask_talisman import Talisman

freezer = Freezer(app)

Talisman(app, content_security_policy=None)
 
if __name__ == "__main__":
	if len(sys.argv) > 1 and sys.argv[1] == "build":
		freezer.freeze()
	else:
		app.run(port=8000)