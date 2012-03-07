<b>GridMapper</b> draws a custom grid over a map. Changing the status of each grid square changes its color,
allowing you to easily create and interpret a color-coded map grid.

GeoJSON layers underneath the grid add context ( this example adds city limits and information on each ward ).
The map also supports multiple grid layers ( this example separates wind and flood damage grids ).

<img src="http://i.imgur.com/I0GC0.png"/>

Browser support equivalent to Leaflet.js mapping tools (up-to-date Chrome, Firefox, IE7+)
Change app/views.py to customize the app for your area

Heroku server based on zachwill's project, Flask for Heroku
https://github.com/zachwill/flask_heroku