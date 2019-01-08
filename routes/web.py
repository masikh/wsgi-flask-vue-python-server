from flask import render_template
from . import routes
from Configuration import username, home_directory


@routes.route('/home')
def home():
    return render_template('index.html', title='landing page')

@routes.route('/some_page_1')
def some_page_1():
    return render_template('some_page_1.html', title='some page 1', username=username, home_directory=home_directory)


@routes.route('/some_page_2')
def some_page_2():
    return render_template('some_page_2.html', title='some page 2')
