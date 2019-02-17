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
            date = html.select('.metadata_unit .metadata_unit-info--text_only')
            if date:
                for i in date:
                    i = str(i)
                    result = re.findall(r"\d{4,}", i)
                    if result:
                        date_list.append(int(result[0]))
        date_string = ""
        for year in date_list:
            year = str(year)
            date_string = date_string + "," + year
        return date_string[1:]

# s = '<span class="metadata_unit-info metadata_unit-info--text_only">December 25, 2015</span>'
# result = re.findall(r"\d{4,}", s)
# print(result)