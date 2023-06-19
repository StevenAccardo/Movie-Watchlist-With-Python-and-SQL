import datetime
import database

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies that have been listed.
4) Add user to the app.
5) Watch a movie. 
6) View watched movies.
7) Search for a movie.
8) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"


print(welcome)
database.create_table()

# Receives user input of username.
def prompt_add_user():
    username = input("Username: ")
    database.add_user(username)

# Receives user input of movie name and release date.
def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-yyyy): ")
    # Converts string date into a datetime object
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    # Convers datetime object into epoch time
    timestamp = parsed_date.timestamp()

    database.add_movie(title, timestamp)

# Receives user input of partial movie name to search list of movies added.
def prompt_search_movies():
    search_term = input("Enter the partial movie title: ")
    movies = database.search_movies(search_term)
    if movies:
        print_movie_list("Found", movies)
    else:
        print("Found no movies for that search term.")

# Receives user input of username and movie id in order to mark a movie as watched.
def prompt_watch_movie():
    username = input("Username: ")
    movie_id = input("Movie ID: ")
    database.watch_movie(username, movie_id)

# Receives user input of username in order to list out their watched movies.
def prompt_show_watched_movies():
    username = input("Username: ")
    movies = database.get_watched_movies(username)
    if movies:
        print_movie_list(f"{username}'s Watched", movies)
    else:
        print(f"{username} has watched no movies yet!")

# Prints the movie list and is reusable for various listings.
def print_movie_list(heading, movies):
    print(f"-- {heading} Movies --")
    for _id, title, release_date in movies:
        movie_date = datetime.datetime.fromtimestamp(release_date)
        human_date = movie_date.strftime("%b %d %Y")
        print(f"{_id}: {title} (on {human_date})")
    print("---- \n")


while (user_input := input(menu)) != "8":
    # User can add a new movie that they want to watch to the list.
    if user_input == "1":
        prompt_add_movie()
    # View all movies that have release dates in the future.
    elif user_input == "2":
        movies = database.get_movies(True)
        print_movie_list("Upcoming", movies)
    # View all movies on the list.
    elif user_input == "3":
        movies = database.get_movies(False)
        print_movie_list("All", movies)
    # Add a new user to the app that can marked movies that they have watched
    elif user_input == "4":
        prompt_add_user()
    # Mark a movie that has been watched by a user.
    elif user_input == "5":
        prompt_watch_movie()
    # View all watched movies by a specific username.
    elif user_input == "6":
        prompt_show_watched_movies()
    # Search for movies that have been 
    elif user_input == "7":
        prompt_search_movies()
    else:
        print("Invalid input, please try again!")