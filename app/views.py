import os, json
import requests
from flask import render_template, flash, redirect, session, url_for, request, g, send_from_directory, jsonify
from app import app,cache
from forms import SearchForm
from config import basedir
from StringIO import StringIO
from PIL import Image

from secret import pixabay

MEDIA_FOLDER = os.path.join(basedir, 'tmp')
if not os.path.exists(MEDIA_FOLDER):
    os.makedirs(MEDIA_FOLDER)

@cache.cached(timeout=50)
def get_image(username, key, search_term, page):
	pixabay_response = requests.get(
		'http://pixabay.com/api/?username='
		+username+
		'&key='
		+key+
		'&search_term='
		+search_term+
		'&page='
		+page+
		'&image_type=photo&per_page=20&image_type=photo&'
	)

	pixabay_response = pixabay_response.json()
	images = []
	for item in pixabay_response['hits']:
		images.append({'preview':item['previewURL'], 'full_size':item['webformatURL']})
	return images

@app.before_request
def before_request():
	g.search_form = SearchForm()

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/search', methods = ['POST'])
def search():
	if not g.search_form.validate_on_submit():
		return redirect(url_for('index'))
	return redirect(url_for('search_results', search_term = g.search_form.search.data, page=1))

@cache.cached(timeout=50)
@app.route('/search/<search_term>/<page>')
def search_results(search_term, page):
	image_response = get_image(pixabay['username'], pixabay['key'], search_term, page)
	return render_template("search.html",
		search_term = search_term,
		page = page,
		image_response = image_response
	)

@cache.cached(timeout=50)
@app.route('/edit/', methods = ['GET', 'POST'])
def edit_result():
        url = request.args.get('url')
        filename = url.split('/')[-1]

        i = Image.open(StringIO(requests.get(url).content))
        i.save('%s/%s' % (MEDIA_FOLDER, filename))

        return render_template("edit.html",
        	image_filename=filename
        )

@cache.cached(timeout=50)
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(MEDIA_FOLDER,
                               filename
	)

@cache.cached(timeout=50)
@app.route('/about')
def about():
	return render_template("about.html")
