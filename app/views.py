"""
Flask Blueprint Docs:  http://flask.pocoo.org/docs/api/#flask.Blueprint

This file is used for both the routing and logic of your
application.
"""

from flask import Blueprint, render_template, request, redirect, url_for

views = Blueprint('views', __name__, static_folder='../static',
                  template_folder='../templates')


@views.route('/')
def home():
    # Render website's home page.
    interviewList = [
		{
			"id": "1",
			"img": "http://i.imgur.com/T0YNxs.jpg",
			"interviewed": "Sam Pull",
			"jobtitle": "Clipper",
			"humandate": "Feb 14, 2012",
			"whoareyou": '''My name is Sam Pull, and I clip things.''',
			"hardware": '''<p>Essentially, I am clipping things with scissors.</p>
			<p>Sometimes other clipper tools are involved. But not clipper ships.</p>''',
			"software": '''<p>Before I clip anything, I Google it.</p>
			<p>Sometimes I use RememberTheMilk to keep a list of things to clip.</p>''',
			"dream": '''<p>I would like to have a massive clip-a-tron, but it would likely put me out of work.</p>'''
		},
		{
			"id": "2",
			"img": "http://i.imgur.com/T0YNxs.jpg",
			"interviewed": "Samantha Pull",
			"jobtitle": "Clipper",
			"humandate": "Feb 14, 2012",
			"whoareyou": '''My name is Samantha Pull, and I clip things.''',
			"hardware": '''<p>Essentially, I am clipping things with scissors.</p>
			<p>Sometimes other clipper tools are involved. But not clipper ships.</p>''',
			"software": '''<p>Before I clip anything, I Google it.</p>
			<p>Sometimes I use RememberTheMilk to keep a list of things to clip.</p>''',
			"dream": '''<p>I would like to have a massive clip-a-tron, but it would likely put me out of work.</p>'''
		}
    ]
    return render_template('usesthishome.html', **interviewList)

@views.route('/blog/<post>')
def showInterview(post):
	interviewDetail = {
		"id": "1",
		"img": "http://i.imgur.com/T0YNxs.jpg",
		"interviewed": "Sam Pull",
		"jobtitle": "Clipper",
		"humandate": "Feb 14, 2012",
		"whoareyou": '''My name is Sam Pull, and I clip things.''',
		"hardware": '''<p>Essentially, I am clipping things with scissors.</p>
		<p>Sometimes other clipper tools are involved. But not clipper ships.</p>''',
		"software": '''<p>Before I clip anything, I Google it.</p>
		<p>Sometimes I use RememberTheMilk to keep a list of things to clip.</p>''',
		"dream": '''<p>I would like to have a massive clip-a-tron, but it would likely put me out of work.</p>'''
	}
	return render_template('usesthispost.html', **interviewDetail)

@views.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@views.app_errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
