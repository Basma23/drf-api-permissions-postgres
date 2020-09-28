from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Movie

# Create your tests here.

class MoviesTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='user', password='password')
        test_user.save()
        test_movie = Movie.objects.create(author='user', title='Cinderella', description='The best of Disney movies ever')
        test_movie.save()
        def test_movie_contents(self):
            movie = Movie.objects.get(id=1)
            actual_author = str(movie.author)
            actual_title = str(movie.title)
            actual_description = str(movie.description)
            self.assertEqual(actual_author, 'user')
            self.assertEqual(actual_title, 'Cinderella')
            self.assertEqual(actual_description, 'The best of Disney movies ever')
