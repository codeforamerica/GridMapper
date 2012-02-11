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
    """Render website's home page."""
    gridMapDetails = {
      "title": "Grid Map",
      "firstSquares" : "7,6,6,5,5,4,4,3,3,2,1,1,1,3,4,4,5,5,5,5,5,5,6,7,7,8",
      "lastSquares" : "8,11,11,13,13,13,13,13,14,14,15,15,15,15,16,16,16,16,16,16,13,12,11,11,10,9",
      "tilexyz" : "http://tile.stamen.com/terrain/{z}/{x}/{y}.jpg",
      "tilecopyright" : "Map data &copy; 2012 OpenStreetMap contributors, Tiles by Andy Allan",
      "lat" : "32.815",
      "lng" : "-83.6324022",
      "zoom" : "11",
      "north" : "32.968729",
      "south" : "32.661449",
      "east" : "-83.48285",
      "west" : "-83.9062",
      "columns" : "26",
      "rows" : "16",
      "squareNameFunction" : "var letter = String.fromCharCode(65+i);j++;return letter + j;",
      "mapUserPic" : "/static/images/citylogo.png",
      "mapUserName" : "Emergency Management Association"
    }
    return render_template('rapidstatus.html', **gridMapDetails)

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
