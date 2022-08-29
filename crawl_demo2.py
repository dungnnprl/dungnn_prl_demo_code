import pandas as pd
import extruct as ex
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import chompjs
PATH_DRIVER = "/Users/macmini/Documents/Work station/Python/Webscaping/BscScan/chromedriver"
URL_PRL_PARAGON = "https://testnet.theparallel.io/market/shop/paragon"

urls = [
    URL_PRL_PARAGON
]

def get_driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver

def get_source(driver, url):
    driver.get(url)
    return driver.page_source

def get_json(source):
    return ex.extract(source, syntaxes=['json-ld'])     

def get_next_page(driver, source):
    """Parse the page source and return the URL for the next page of results.

    :param driver: Selenium webdriver
    :param source: Page source code from Selenium

    :return
        URL of next paginated page
    """

    elements = driver.find_elements_by_xpath('//link[@rel="next"]')
    if elements:
        return driver.find_element_by_xpath('//link[@rel="next"]').get_attribute('href')
    else:
        return ''
df = pd.DataFrame(columns = ['author', 'headline', 'body', 'rating', 
                             'item_reviewed', 'publisher', 'date_published'])               

def save_reviews(data, df):
    """Scrape the individual reviews from a schema.org JSON-LD tag and
    save the contents in the df_reviews Pandas dataframe. 

    :param data: JSON-LD source containing schema.org review markup
    :param df: Name of Pandas dataframe to which to append reviews

    :return
        df with reviews appended
    """

    for item in data['json-ld']:
        if "review" in item:
            for review in item['review']:

                row = {
                    'author': review.get('author', {}).get('name'),
                    'headline': review.get('headline'),
                    'body': review.get('reviewBody'),
                    'rating': review.get('reviewRating', {}).get('ratingValue'),
                    'item_reviewed': review.get('itemReviewed', {}).get('name'),
                    'publisher': review.get('publisher', {}).get('name'),
                    'date_published': review.get('datePublished')
                }

                df = df.append(row, ignore_index=True)

    return df  

def view_json_ld(data):
    for item in data['json-ld']:
        print("-----------------")
        print(item)     
        print("-----------------") 
def main():
    for url in urls:

        print(url)

        # Save the reviews from the first page
        driver = get_driver()
        source = get_source(driver, url)
        json = get_json(source)
        print(json)
        view_json_ld(json)

        # # Get reviews on each paginated page
        # next_page = get_next_page(driver, source)
        # paginated_urls = []
        # paginated_urls.append(next_page)

        # if paginated_urls:

        #     for url in paginated_urls:

        #         if url:

        #             print(next_page)
        #             driver = get_driver()
        #             source = get_source(driver, url)
        #             json = get_json(source)
        #             df = save_reviews(json, df)
        #             next_page = get_next_page(driver, source)
        #             paginated_urls.append(next_page)

if __name__ == "__main__":
    main()