"""
.. module:: bluecoat
    :platform: Unix
    :synopsis: A module used for intereaction with bluecoat website review
.. moduleauthor:: Kevin Glisson <kevin.glisson@gmail.com>
.. version:: 1.0


A module used for intereaction with bluecoat website review
"""
import logging
from BeautifulSoup import BeautifulSoup
import requests

log = logging.getLogger(__file__)

class Bluecoat(object):
    """
    :param url: url
    :type url: str

    An example of using this class is:
        >>> b = Bluecoat("www.google.com")
        >>> b.submit()
    """
    def __init__(self, url):
        """ Bluecoat init function

        :param url: url
        :type url: str

        An example of using this module is:

        b = Bluecoat("www.google.com")
        b.submit()
        """
        self.url = url

    def submit(self):
        rating = None
        response = requests.get('http://sitereview.bluecoat.com/rest/categorization?url={}'.format(self.url)).json()
        soup = BeautifulSoup(response['categorization'])
        for a in soup.findAll('a', href=True):
            if "javascript" in a['href']:
                rating = a.contents[0]
        if not rating:
            rating = "None"
        return rating
