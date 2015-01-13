kwassa_backend
==============

Route /bestalbums/byyear/<int:year>/ returns sorted list of reviews from pitchfork's best new albums. MongoDb holds collection of review docs, which were scraped using https://github.com/amend/pitchfork-scrapy

Example:
http://54.191.36.11/bestalbums/byyear/2014/

Spotify authorization requires a token swap service. Clone https://github.com/chrismlarson/spotify-token-swap-gae and deploy to Google App Engine. You'll need to delete index.yaml, but backend should be set up well afterwards
