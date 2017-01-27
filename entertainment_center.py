import media
import fresh_tomatoes

shawshank_redemption = media.Movie("The Shawshank Redemption",
            "A man wrongly accused of murder escapes prison",
            "http://www.impawards.com/1994/posters/shawshank_redemption_ver1.jpg",
            "https://www.youtube.com/watch?v=6hB3S9bIaco")

inception = media.Movie("Inception",
            "A thief is given the task of planting an idea in someone else's mind",
            "http://www.impawards.com/2010/posters/inception.jpg",
            "https://www.youtube.com/watch?v=YoHD9XEInc0")

the_dark_knight = media.Movie("The Dark Knight",
            "Batman walks the line between heroism and vigilantism",
            "http://www.gstatic.com/tv/thumb/movieposters/173378/p173378_p_v8_at.jpg",
            "https://www.youtube.com/watch?v=EXeTwQWrcwY")

the_dark_knight_rises = media.Movie("The Dark Knight Rises",
            "Batman is forced out of exile by Bane",
            "http://t1.gstatic.com/images?q=tbn:ANd9GcQSGF8_VbDqKF0B_4IQ0NF87VMDSy7_MPKryawR-qLnSIPQwo5z",
            "https://www.youtube.com/watch?v=GokKUqLcvD8")

cloverfield = media.Movie("Cloverfield",
            "A creature descends on New York",
            "http://www.gstatic.com/tv/thumb/movieposters/172484/p172484_p_v8_an.jpg",
            "https://www.youtube.com/watch?v=M1XEriXzNik")

tombstone = media.Movie("Tombstone",
            "Wyatt Earp gets pulled back into the law",
            "https://images-na.ssl-images-amazon.com/images/I/51lSdfT4SRL._AC_UL320_SR216,320_.jpg",
            "https://www.youtube.com/watch?v=XTWYKf5hXIg")

movies = [shawshank_redemption, inception, the_dark_knight, the_dark_knight_rises, cloverfield, tombstone]

fresh_tomatoes.open_movies_page(movies)
