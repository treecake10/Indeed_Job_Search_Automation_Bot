import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class Testing(unittest.TestCase):

    def setUp(self):
        self.driver_path = Service("C:/Users/n_Tib/PycharmProjects/JobSearchBot/driver/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.driver_path)

    def test_finding_what_where_search(self):

        driver = self.driver
        driver.get("https://www.indeed.com/")
        self.assertIn("Indeed", driver.title)

        self.assertIn("What", driver.page_source)
        what_search_box = driver.find_element(By.ID, 'text-input-what')
        what_search_box.clear()
        what_search_box.send_keys("web dev")
        what_search_box.send_keys(Keys.RETURN)

        self.assertNotIn("did not match any jobs.", driver.page_source)

        self.assertIn("Where", driver.page_source)
        where_search_box = driver.find_element(By.ID, 'text-input-where')
        where_search_box.click()

        clear_text_btn = driver.find_element(By.CLASS_NAME, 'icl-TextInputClearable-icon')
        clear_text_btn.click()
        where_search_box.send_keys("remote")

        self.assertNotIn("did not match any jobs.", driver.page_source)

        self.assertIn("Find jobs", driver.page_source)
        find_btn = driver.find_element(By.CLASS_NAME, 'yosegi-InlineWhatWhere-primaryButton')
        find_btn.click()

        self.assertIn("Remote", self.driver.page_source)
        job_radius_btn = self.driver.find_element(By.ID, 'filter-remotejob')
        job_radius_btn.click()

        where_search_box = driver.find_element(By.ID, 'text-input-where')
        where_search_box.click()
        clear_text_btn = driver.find_element(By.CLASS_NAME, 'icl-TextInputClearable-icon')
        clear_text_btn.click()
        where_search_box.send_keys("Canton, GA")

        self.assertIn("Find jobs", driver.page_source)
        find_btn = driver.find_element(By.CLASS_NAME, 'yosegi-InlineWhatWhere-primaryButton')
        find_btn.click()

        self.assertIn("within 25 miles", self.driver.page_source)
        job_radius_btn = self.driver.find_element(By.ID, 'filter-radius')
        job_radius_btn.click()

        self.assertIn("Job Type", self.driver.page_source)
        job_type_btn = self.driver.find_element(By.ID, 'filter-jobtype')
        job_type_btn.click()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(warnings='ignore')

