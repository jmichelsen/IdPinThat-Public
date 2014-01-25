idpinthat
===========

Flask application powering IdPinThat.com

To install:

*add your secret to config.py

*add your pixabay username and api key to secret.py

*add your filepicker.io and Aviary api keys to templates/edit.html

Then run:

	
	pip install -r requirements.txt
	

Afterward, everything should be installed and working. Issue command:

	python run.py

and you'll be up and running.

IdPinThat uses a standard Heroku installation method. Set up your heroku app and push the repo to it and the app will work just fine. The Procfile and gunicorn config for heroku are included in the git repo.
