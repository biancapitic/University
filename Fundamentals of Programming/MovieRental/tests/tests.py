from services.services import MovieService
from services.services import ClientService
from repository.Repository import Repository
import unittest


class Test(unittest.TestCase):
    def testAddMovie_ValidInput_InputAdded(self):
        repo = Repository()
        service = MovieService(repo)
        service.add_movie(1, 'Title', 'Descr', 'Gen')
        self.assertIn(1, repo.get_elements_list.keys())

    def testRemoveMovie_ValidInput_InputRemoved(self):
        repo = Repository()
        service = MovieService(repo)
        service.add_movie(1, 'Title', 'Descr', 'Gen')
        service.remove_by_id(1)
        self.assertNotIn(1, repo.get_elements_list.keys())

    def testUpdateMovieParameters_ValidInput_UpdateParameter(self):
        repo = Repository()
        service = MovieService(repo)
        service.add_movie(1, 'Title', 'Descr', 'Gen')
        service.update_movie_parameters(1, 'title', 'New Title')
        movie = repo.get_elements_list[1]
        self.assertEqual(movie.title, 'New Title')

    def testAddClient_ValidInput_InputAdded(self):
        repo = Repository()
        service = ClientService(repo)
        service.add_client(1, 'New Client')
        self.assertIn(1, repo.get_elements_list.keys())

    def testRemoveClient_ValidInput_InputRemoved(self):
        repo = Repository()
        service = ClientService(repo)
        service.add_client(1, 'New Client')
        service.remove_by_id(1)
        self.assertNotIn(1, repo.get_elements_list.keys())

    def testUpdateClientParameter_ValidInput_UpdateParameter(self):
        repo = Repository()
        service = ClientService(repo)
        service.add_client(1, 'New Client')
        service.update_client_parameters(1, 'name', 'New Name')
        client = repo.get_elements_list[1]
        self.assertEqual(client.name, 'New Name')