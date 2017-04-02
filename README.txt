To generate the HTML page for this site, take the following steps:

    Clone this repository using git.

    In Python terminal, run "entertainment_center.py"

The script will generate an HTML page that will open in your browser.

To ADD movies:
	
	OPEN entertainment_center.py
	FIND "#Add new movies above this comment"
	Enter as follows:
	movie_title = media.Movie("Title","Storyline","Poster Image URL", "Youtube Trailer URL")
	SAVE file

To DELETE movies
	OPEN entertainment_center.py
	FIND movie you wish to delete
	DELETE media.Movie data
	DELETE title from "#List of movies to render" list
	SAVE file
