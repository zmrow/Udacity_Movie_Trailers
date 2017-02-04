#!/usr/bin/env python
import media
import fresh_tomatoes


def main():
    """Script to take a list of movie objects and create the page of trailers

    Requires:
        media module
        fresh_tomatoes module

    Returns:
        fresh_tomatoes.html page
        Web browser opened with the html page
    """
    # Create the movie objects
    # TODO(zmrow): Use The Movie Database (TMDB) API to pull movie information
    shawshank_redemption = media.Movie("The Shawshank Redemption",
                "A man wrongly accused of murder escapes prison",
                "http://www.impawards.com/1994/posters/shawshank_redemption_ver1.jpg",  # noqa
                "https://www.youtube.com/watch?v=6hB3S9bIaco")

    inception = media.Movie("Inception",
                "A thief is given the task of planting an idea in someone else's mind",  # noqa
                "http://www.impawards.com/2010/posters/inception.jpg",
                "https://www.youtube.com/watch?v=YoHD9XEInc0")

    the_dark_knight = media.Movie("The Dark Knight",
                "Batman walks the line between heroism and vigilantism",
                "http://www.gstatic.com/tv/thumb/movieposters/173378/p173378_p_v8_at.jpg",  # noqa
                "https://www.youtube.com/watch?v=EXeTwQWrcwY")

    # Create a list with existing movie objects
    movies = [shawshank_redemption, inception, the_dark_knight]

    # Call fresh_tomatoes module, supplying the movies list
    # Will open your default web browser with the newly generated page
    fresh_tomatoes.open_movies_page(movies)

if __name__ == "__main__":
    main()
