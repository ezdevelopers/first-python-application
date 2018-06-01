import media
import fresh_tomatoes

#instantiate the toy_story object and insert the properties for toy_story movie
toy_story = media.Movie("Toy Story",
                        "A toy story movie",
                        "https://images-na.ssl-images-amazon.com/images/I/91Bq7v6MEmL._UR150,200_FMJPG_.jpg",
                        "https://www.youtube.com/watch?v=3jC6McxjCnE")

#instantiate the avatar object and insert the properties for avatar movie
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://media.sinematurk.com/film/4/30/8b2bf1107b37/21500_8.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#instantiate the avengers object and insert the properties for avengers movie
avengers = media.Movie("Avengers- Infinity War",
                       "Thanos reeks havoc on earth",
                       "https://thumbor.forbes.com/thumbor/960x0/https%3A%2F%2Fblogs-images.forbes.com%2Fcurtissilver%2Ffiles%2F2018%2F04%2Favengers.jpg",
                       "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

#instantiate the iron man object and insert the properties for iron man movie
iron_man = media.Movie("Iron Man 4",
                       "Tony Stark, the billionaire super heroe",
                       "https://pmcvariety.files.wordpress.com/2013/03/ironman31.jpg?w=1000&h=563&crop=1",
                       "https://www.youtube.com/watch?v=2CzoSeClcw0")

#create an array of movies to pass to the fresh_tomatoes.py function called
#open_movies_page
movies = [toy_story,avatar,avengers,iron_man]

#call the open_movies_page function
fresh_tomatoes.open_movies_page(movies)
