from scrapers import AscentsScraper


def main():
    crag = "freyr"
    file_path = "garbage/freyr_ascents.csv"
    AscentsScraper(file_path, crag).scrape()
    


if __name__ == "__main__":
    main()

