from .Base import BaseScraper
import re



class AscentsScraper(BaseScraper):
    def __init__(self, file_path, crag):
        self.url = f"https://www.8a.nu/crags/sportclimbing/belgium/{crag}/ascents"
        super().__init__(file_path, self.url)
        
    def scrape(self):
        self._pipeline()
        ascents = []
        routes = self.soup.find_all('tr', class_='big-ascent-row big-ascent-row__body')
        
        for route in routes:
            ascents.append(
                {
                    'name': route.find('div', class_='route-name show-for-desktop_m-down').a.text.strip().split('\n')[0],
                    'grade': re.findall(r'\((.*?)\)', route.find('div', class_='route-name show-for-desktop_m-down').a.text.strip().split('\n')[1])[0],
                    'sector': route.find('div', class_='bottom-name').a.text.strip(),
                    'date': route.find('td', class_='col-date').div.text.strip()
                }
            )

        self.writer.write(ascents)
    
    
    def scroll(self):
        self._sleepy()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
    def _press_load_more(self):
        load_more_button = self.driver.find_element("xpath", "//button[contains(@class, 'button-container variant-outline color-primary size-md')]//div[contains(text(), 'LOAD MORE')]") 
        load_more_button.click()
        self._sleepy()
        
    def _pipeline(self):
        self.scroll()
        self._press_load_more()
        for _ in range(2):
            self.scroll()