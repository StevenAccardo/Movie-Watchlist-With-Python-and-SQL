import datetime
import database

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all unwatched movies
4) Watch a movie
5) View watched movies.
6) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"


print(welcome)
database.create_table()


def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-yyyy): ")
    # Converts string date into a datetime object
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    # Convers datetime object into epoch time
    timestamp = parsed_date.timestamp()

    database.add_movie(title, timestamp)

def prompt_watch_movie():
    username = input("Username: ")
    movie_title = input("Enter movie title you've watched: ")
    database.watch_movie(username, movie_title)

def prompt_get_watched_movie():
    username = input("Username: ")
    return database.get_watched_movies(username)

def print_movie_list(heading, movies):
    print(f"-- {heading} Movies --")
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[1])
        human_date = movie_date.strftime("%b %d %Y")
        print(f"{movie[0]} (on {human_date})")
    print("---- \n")

def print_watched_movie_list(movies):
    print(f"-- {movies[0][0]}'s Watched Movies --")
    for movie in movies:
        print(f"{movie[1]}")
    print("---- \n")

while (user_input := input(menu)) != "6":
    # Add a new movie to be watched to the list.
    if user_input == "1":
        prompt_add_movie()
    # View all movies that have release dates in the future.
    elif user_input == "2":
        movies = database.get_movies(True)
        print_movie_list("Upcoming", movies)
    # View all unwatched movies on the list.
    elif user_input == "3":
        movies = database.get_movies(False)
        print_movie_list("All", movies)
    # Set a movie to watched.
    elif user_input == "4":
        prompt_watch_movie()
    # View all watched movies by a specific username.
    elif user_input == "5":
        movies = prompt_get_watched_movie()
        print_watched_movie_list(movies)
    else:
        print("Invalid input, please try again!")