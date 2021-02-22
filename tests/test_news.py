import unittest
from app.models import News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('Oscar','Python Crazy','It is disturbingly fun to learn Python','/khsjha27hbs','src="./static"','September')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))
