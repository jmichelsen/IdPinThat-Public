from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required, Length

class SearchForm(Form):
	''' Search Form '''
	search = TextField('search', validators = [Required()])
