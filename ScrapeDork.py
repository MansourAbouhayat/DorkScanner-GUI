
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ScrapeDork:
    @staticmethod
    def DuckDuckGO(Query):
        # Configure Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode

        # Create a new instance of the Chrome driver
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(f"https://duckduckgo.com/?q={Query}")

        while(True):
            try:
                
                element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="more-results"]')))

                element.click()
            except:
                break


        pageSource = driver.page_source
        driver.quit()
        if 'Make sure all words are spelled correctly.' in pageSource:
            exit('No Results Found.')
       
        return list(set(re.findall('</a></span><a href="(.*?)"',pageSource)))
        


