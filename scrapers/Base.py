import requests
import writers
from bs4 import BeautifulSoup
import time
import random
import undetected_chromedriver as uc
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException


class BaseScraper:
    def __init__(self, file_path, url):
        self.url = url
        
        self.driver = uc.Chrome()
        self.driver.get(self.url)
        self.writer = self._get_writer(file_path) 
        
        
    @property
    def soup(self):
        return BeautifulSoup(self.driver.page_source, 'html.parser')
          
    def _get_writer(self, file_path):
        match file_path.split('.')[-1]:
            case 'csv':
                return writers.CSVwriter(file_path)
            
    def _sleepy(self):
        time.sleep(random.uniform(2, 4))
            

