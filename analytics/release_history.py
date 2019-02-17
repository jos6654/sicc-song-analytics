#release_history.py
from bs4 import BeautifulSoup
from analytic import Analytic
import requests
import re

class ReleaseHistory(Analytic):

    def analyze(self):
        """
        This analytic subclass takes the list of song urls and iterates through them
        scraping the release date of each song from the web page and returning it as an
        integer.
        :return: The
        """
        date_list = []
        for url in self.url_list:
            page = requests.get(url)
            html = BeautifulSoup(page.text, 'html.parser')
            date = html.select('.metadata_unit .metadata_unit-info--text_only')[0]
            result = re.match(r"\d{4}", date)[0]
            date_list.append(result)
            print(result)
        return date_list
