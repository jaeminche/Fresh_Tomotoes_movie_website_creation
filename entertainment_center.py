import media
import fresh_tomatoes
"""
This file contains data for movies, executes the other two files and renders a website.
"""

boyhood = media.Movie("Boyhood", "Richard Linklater",
                    "An ode of growing up both of a child and parents, filmed over 12 years with the same cast.",
                    "https://upload.wikimedia.org/wikipedia/en/b/bb/Boyhood_film.jpg",
                    "https://www.youtube.com/watch?v=Ys-mbHXyWX4")
lost_in_translation = media.Movie("Lost in Translation", "Sofia Coppola",
                    "A seemingly a love story of two people, which no other person than themselves would realy know about.",
                    "https://upload.wikimedia.org/wikipedia/en/4/4c/Lost_in_Translation_poster.jpg",
                    "https://www.youtube.com/watch?v=6wXjObmziEk")
the_wailing = media.Movie("The Wailing", "Na Hong-jin",
                    "A mysterious story which you end up finding yourself having believed what you have wanted to believe it to be.",
                    "https://resizing.flixster.com/_LUEyQZrCUayYctd0LUXp6M-x8c=/206x305/v1.bTsxMTk4NTEzMDtqOzE3MzczOzEyMDA7Mjc2NTs0MDk2",
                    "https://www.youtube.com/watch?v=43uAputjI4k")
love_letter = media.Movie("Love Letter", "Shunji Iwai",
                    "A story of two people left behind, who share a name and memories with a man.",
                    "https://upload.wikimedia.org/wikipedia/en/6/62/Love-Letter-poster-1995.jpg",
                    "https://www.youtube.com/watch?v=M0UA1yrUTfs")
the_garden_of_words = media.Movie("The Garden of Words", "Makoto Shinkai",
                    "An ode of growing up both of a child and parents, filmed over 12 years with the same cast.",
                    "https://upload.wikimedia.org/wikipedia/en/c/c3/Garden_of_Words_poster.png",
                    "https://www.youtube.com/watch?v=FMabhvDoolc")
matrix = media.Movie("The Matrix", "The Wachowski Brothers",
                    "A science fiction movie of 'the one' who gets risen from the dead by 'Trinity' and sacrifices himself, saving the world of simulacra and simulation.",
                    "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                    "https://www.youtube.com/watch?v=vKQi3bBA1y8")
ghost_world = media.Movie("The Ghost World", "Terry Zwigoff",
                    "A story of people who try to subjectively live along eventually not in a good success, but they are beautiful.",
                    "https://upload.wikimedia.org/wikipedia/en/c/c3/Ghostworldposter.jpg",
                    "https://www.youtube.com/watch?v=4WmCBRkWJ54")

movies = [boyhood, lost_in_translation, the_wailing, love_letter, the_garden_of_words, matrix, ghost_world]
fresh_tomatoes.open_movies_page(movies)
