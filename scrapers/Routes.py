from .Base import BaseScraper

class RoutesScraper(BaseScraper):
    def __init__(self, file_path, crag):
            self._url = f"https://www.8a.nu/crags/sportclimbing/belgium/{crag}/routes?page=1"
            super().__init__(file_path, self.url)
            
    
    def scrape(self):
        routes = []
        
        for i in range(1, 3):
            self.url = self.url.split("?")[0] + f"?page={i}"
            ascents_html = self.soup.find_all('tr')
            
            for ascent in ascents_html:
                try:
                    routes.append(
                        {
                            "grade": ascent.find('div', class_='grade').text.strip(),
                            "name": ascent.find('p', class_='name-link').text.strip(),
                            "sector": ascent.find('p', class_='sub-link').text.strip().split(',')[1].replace("\n", "").replace("\t", "").replace(" ", ""),
                            "total_ascents": ascent.find_all('td',class_='col-ascents number')[1].text.strip(),
                            "FL/OS": ascent.find('td', class_='col-ratio text-center number tablet-hide').text.strip(),
                            "recommended": ascent.find('td', class_='col-recommend text-center number tablet-hide').text.strip(),
                            "stars": ascent.find('td', class_='col-rating text-center tablet-hide').div.text.strip()
                            
                        }
                    )
                except Exception as e:
                    print(e)
                    continue
                
            
            self._sleepy()
        self.writer.write(routes)
    