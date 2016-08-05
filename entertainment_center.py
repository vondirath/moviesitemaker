import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story about a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
                     "Guy who goes native",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
ashvsevildead = media.Movie("Ash vs Evil Dead",
                            "30 years after the first three Evil Dead films. Ashley J. \"Ash\" Williams works at the \"ValueShop\" mart as a simple salesclerk. His life has gone nowhere and he now lives in a trailer, drinking in bars at night and having occasional sex with various women, usually after making up a sensational story about how he lost his hand. After having inadvertently read the incantation from the Book of the Dead again, he unleashes the Kandarian Demon one more time. A new set of events brings him to assume his former fighting persona and face the new demonic plague in order to save the human race.",
                            "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Ash-vs-Evil-Dead_logo.png/1280px-Ash-vs-Evil-Dead_logo.png",
                            "https://www.youtube.com/watch?v=LdRyAVsWVJ0")

#print(toy_story.storyline)
#print avatar.storyline
#avatar.show_trailer()
#ashvsevildead.show_trailer()
movies = [toy_story, avatar, ashvsevildead]
fresh_tomatoes.open_movies_page(movies)
