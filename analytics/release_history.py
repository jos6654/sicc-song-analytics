#release_history.py
from bs4 import BeautifulSoup
from analytic import Analytic
import requests
import re

class ReleaseHistory(Analytic):

    def analyze(self):
        for url in self.url_list:
            page = requests.get(url)
            html = BeautifulSoup(page.text, 'html.parser')
            date = html.select('.metadata_unit .metadata_unit-info--text_only')[0]
            result = re.match(r"\d{4}", date)[0]
            print(result)
