import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import page

class Testing(unittest.TestCase):


    def setUp(self):

        self.driver_path = Service("C:/Users/n_Tib/PycharmProjects/JobSearchBot/driver/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.driver_path)
        self.driver.get("https://www.indeed.com/")


    def test_python(self):


        # class for testing 'What' and 'Where' searching

        search_landing_page = page.LandingSearchPage(self.driver)

        assert search_landing_page.site_title_found()

        assert search_landing_page.what_label_found()
        search_landing_page.fill_what_form()
        assert search_landing_page.job_results_found()

        assert search_landing_page.where_label_found()
        search_landing_page.fill_where_form_with_remote()
        assert search_landing_page.job_results_found()

        assert search_landing_page.find_jobs_label_found()
        search_landing_page.click_find_btn()

        assert search_landing_page.remote_btn_label_found()
        search_landing_page.click_remote_filtration_btn()

        search_landing_page.fill_where_form_with_location()

        assert search_landing_page.find_jobs_label_found()
        search_landing_page.click_find_btn()


        # class for testing filtration buttons

        filtrations_page = page.FiltrationsPage(self.driver)

        assert filtrations_page.radius_label_found()
        filtrations_page.click_radius_btn()
        filtrations_page.test_apply_radius()


        assert filtrations_page.job_type_label_found()
        filtrations_page.click_job_type_btn()
        filtrations_page.test_apply_job_type()

        assert filtrations_page.exp_lvl_label_found()
        filtrations_page.click_exp_lvl_btn()
        filtrations_page.test_apply_exp_lvl()

        assert filtrations_page.dev_skill_label_found()
        filtrations_page.click_dev_skill_btn()
        filtrations_page.test_apply_dev_skill()


        # class for testing retrieval of job card results

        job_search_page = page.JobCardsPage(self.driver)
        job_search_page.test_job_cards()


        # class for testing navigation to the next page of job card results

        next_button_page = page.NextButtonPage(self.driver)
        next_button_page.test_next_button()


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(warnings='ignore')

