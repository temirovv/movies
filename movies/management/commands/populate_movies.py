import random
from faker import Faker
from django.core.management.base import BaseCommand
from movies.models import Movie, Genre, MovieGenre, QualityChoices, MovieStatusChoices, MovieTypeChoices

fake = Faker()


file_names = [
    'movie_images/28_years_later.jpg', 'movie_images/Avengeers_5.jpg',
    'movie_images/ben_10.jpg', "movie_images/Disneys's_snow_white.jpg",
    'movie_images/dragaon_2025.jpg', 'movie_images/gladiator_2.jpg',
    'movie_images/harry_poter_2025.jpg', 'movie_images/home_alone3.jpg',
    'movie_images/IT_Chapter_3.jpg', 'movie_images/Mission_imposible.jpg',
    'movie_images/shang_chi_2.jpg', 'movie_images/Spider_man_2025.jpg',
    'movie_images/titanic_2.jpg', 'movie_images/wednesday.jpg',
    'movie_images/Wicked.jpg'

]

movie_title = [
    '28 Years Later', 'Avengers 5',
    'Ben 10', 'Snow white', 'Dragon', 'Gladiator 2',
    'Harry Potter', 'Home Alone 3', 'IT Chapter 3', 'Mission Impossible', 
    'Chang Chi 2', 'Spider Man', 'Titanic 2', 'Wednesday', 'Wicked'
]

video_files = [
    'movies/28_years_later.mp4', 'movies/Avengeers_5.mp4',
    'movies/BEN_10.mp4', "movies/Disneys's_snow_white.mp4",
    'movies/dragaon_2025.mp4', 'movies/gladiator_2.mp4',
    'movies/Harry_poter_2025.mp4', 'movies/home_alone3.mp4',
    'movies/IT_Chapter_3.mp4', 'movies/Mission_Impossible.mp4',
    'movies/Shang_Chi_2.mp4', 'movies/Spider_man_2025.mp4',
    'movies/Titanic_2.mp4', 'movies/Wednesday.mp4',
    'movies/Wicked.mp4'
]

class Command(BaseCommand):
    help = "Populate the database with random movies and genres"

    def handle(self, *args, **kwargs):
        self.create_genres()
        self.create_movies()
        self.stdout.write(self.style.SUCCESS("Successfully populated the database!"))

    def create_genres(self):
        genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi', 'Documentary']
        for genre_name in genres:
            Genre.objects.get_or_create(name=genre_name)

    def create_movies(self):
        genres = list(Genre.objects.all())
        for i in range(15):  # Adjust the number of movies as needed
            movie = Movie.objects.create(
                title=movie_title[i],
                description=fake.paragraph(nb_sentences=random.randrange(5, 10)),
                duration=random.randint(80, 180),
                movie_type=fake.word(ext_word_list=["Action", "Romance", "Thriller", "Animation"]),
                studios=fake.company(),
                release_date=fake.date_between(start_date="-10y", end_date="today"),
                rating=round(random.uniform(4, 10), 1),
                views=random.randint(100, 20030),
                quality=random.choice([choice[0] for choice in QualityChoices.choices]),
                scores=round(random.uniform(4, 10), 1),
                status=random.choice([choice[0] for choice in MovieStatusChoices.choices]),
                type=random.choice([choice[0] for choice in MovieTypeChoices.choices]),
                image=file_names[i],
                video=video_files[i],
                thumb=video_files[i],
            )
            movie.save()

            # Assign random genres to the movie
            assigned_genres = random.sample(genres, random.randint(1, 3))
            for genre in assigned_genres:
                MovieGenre.objects.create(movie=movie, genre=genre)
