#release_history.py
import json

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
        date_dictionary = {}
        for url in self.url_list:
            page = requests.get(url)
            html = BeautifulSoup(page.text, 'html.parser')
            date = html.select('.metadata_unit .metadata_unit-info--text_only')
            if date:
                for i in date:
                    i = str(i)
                    result = re.findall(r"\d{4,}", i)
                    if result:
                        year = int(result[0])
                        if year in date_dictionary:
                            date_dictionary[year] += 1
                        else:
                            date_dictionary[year] = 1
        return json.dumps(date_dictionary)


# s = '<span class="metadata_unit-info metadata_unit-info--text_only">December 25, 2015</span>'
# result = re.findall(r"\d{4,}", s)
# print(result)