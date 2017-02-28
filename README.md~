kwassa_backend
==============

Route: /bestalbums/byyear/<int:year>/

Returns sorted list of reviews from pitchfork's best new albums. MongoDb holds collection of review docs, which were scraped using https://github.com/amend/pitchfork-scrapy

Example:
http://54.191.36.11/bestalbums/byyear/2014/

Spotify authorization requires a token swap service. I cloned https://github.com/chrismlarson/spotify-token-swap-gae and deployed to Google App Engine. You'll need to delete index.yaml, but backend should be set up well afterwards

For aws hosting, read http://blog.garethdwyer.co.za/2013/07/getting-simple-flask-app-running-on.html

instructions are accurate except that because of an apache update, files in /etc/apache2/sites-available must have extension .conf
