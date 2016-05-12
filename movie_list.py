import fresh_tomatoes #importing the fresh_tomatoes module
import media #importing media module

#a list of 9 of my favourite movies
sicario = media.Movie("Sicario",
                      "An idealistic FBI agent is enlisted by a government task force"
                      " to aid in the escalating war against drugs at the"
                      " border area between the U.S. and Mexico.",
                      "https://upload.wikimedia.org/wikipedia/en/4/4b/Sicario_poster.jpg",
                      "https://www.youtube.com/watch?v=sR0SDT2GeFg")

starwars_vii = media.Movie("Star Wars: The Force Awakens",
                           "Three decades after the defeat of the Galactic Empire,"
                           " a new threat arises. The First Order attempts to rule"
                           " the galaxy and only a ragtag group of heroes can stop them,"
                           " along with the help of the Resistance.",
                           "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
                           "https://www.youtube.com/watch?v=sGbxmsDFVnE")

seven = media.Movie("Se7en",
                    "Two detectives, a rookie and a veteran, hunt a serial killer"
                    " who uses the seven deadly sins as his modus operandi.",
                    "https://upload.wikimedia.org/wikipedia/en/6/68/Seven_%28movie%29_poster.jpg",
                    "https://www.youtube.com/watch?v=J4YV2_TcCoE")

princess_mononoke = media.Movie("Princess Mononoke",
                                "On a journey to find the cure for a Tatarigami's curse,"
                                " Ashitaka finds himself in the middle of a war between "
                                " the forest gods and Tatara, a mining colony."
                                " In this quest he also meets San, the Mononoke Hime.",
                                "https://upload.wikimedia.org/wikipedia/en/2/24/Princess_Mononoke_Japanese_Poster_%28Movie%29.jpg",
                                "https://www.youtube.com/watch?v=4OiMOHRDs14")

the_matrix = media.Movie("The Matrix",
                         "A computer hacker learns from mysterious rebels about the"
                         " true nature of his reality and his role in the war against its controllers.",
                         "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                         "https://www.youtube.com/watch?v=vKQi3bBA1y8")

harry_potter_sorcerers_stone = media.Movie("Harry Potter and the Sorcerer's Stone",
                                           "Rescued from the outrageous neglect of his aunt and uncle,"
                                           " a young boy with a great destiny proves his worth while"
                                           " attending Hogwarts School of Witchcraft and Wizardry.",
                                           "http://www.grcmc.org/images/events/evnt54b6fa620072a.jpg",
                                           "https://www.youtube.com/watch?v=VyHV0BRtdxo")

deadpool = media.Movie("Deadpool",
                       "A former Special Forces operative turned mercenary is subjected to a rogue"
                       " experiment that leaves him with accelerated healing powers, adopting the alter ego Deadpool.",
                       "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
                       "https://www.youtube.com/watch?v=gtTfd6tISfw")

interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through a wormhole in"
                           " space in an attempt to ensure humanity's survival.",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

american_sniper = media.Movie("American Sniper",
                              "Navy S.E.A.L. sniper Chris Kyle's pinpoint accuracy saves"
                              " countless lives on the battlefield and turns him into a legend."
                              " Back home to his wife and kids after four tours of duty, however,"
                              " Chris finds that it is the war he can't leave behind.",
                              "https://upload.wikimedia.org/wikipedia/en/1/10/American_Sniper_poster.jpg",
                              "https://www.youtube.com/watch?v=U9RFwgOBcAM")

#declaring an array for use with the opens_movies_page function in the fresh_tomatoes module
movies = [sicario, starwars_vii, seven, princess_mononoke, the_matrix, harry_potter_sorcerers_stone, deadpool, interstellar, american_sniper]
fresh_tomatoes.open_movies_page(movies)
