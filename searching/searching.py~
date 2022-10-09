from selenium.common import NoSuchElementException
import searching.constant_variables as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from searching.applying_filtration import ApplyingFiltration
from searching.search_report import SearchReport

class Searching(webdriver.Chrome):

    def __init__(self, driver_path=r";C:/Users/n_Tib/PycharmProjects/JobSearchBot/driver", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Searching, self).__init__(options=options) # To instantiate the webdriver.Chrome class
        self.implicitly_wait(15)
        self.maximize_window()


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def landing_page(self):
        self.get(const.BASE_URL)

    def what_text_box(self, what_text=None):
        what_search_box = self.find_element(By.ID, 'text-input-what')
        what_search_box.clear()
        what_search_box.send_keys(what_text)

    def where_text_box(self, where_text=None):
        where_search_box = self.find_element(By.ID, 'text-input-where')
        where_search_box.click()

        clear_text_btn = self.find_element(By.CLASS_NAME, 'icl-TextInputClearable-icon')
        clear_text_btn.click()

        where_search_box.send_keys(where_text)

    def find_jobs_btn(self):
        find_btn = self.find_element(By.CLASS_NAME, 'yosegi-InlineWhatWhere-primaryButton')
        find_btn.click()

    def apply_filtration(self, input_dev_skill=None):
        filtration = ApplyingFiltration(driver=self)

        filtration.radius_btn()
        filtration.apply_radius(radius_val='within 100 miles')

        filtration.job_type_btn()
        filtration.apply_job_type(type_val='Full-time')

        filtration.exp_level_btn()
        filtration.apply_exp_lvl(exp_val='Entry Level')

        filtration.dev_skills_btn()
        filtration.apply_dev_skill(skill_val=input_dev_skill)

    def report_results(self, input_num_of_pages=None):

        try:

            # User chooses how many pages of job results to return
            for page in range(0, int(input_num_of_pages)):

                next_btn = self.find_element(
                    By.CSS_SELECTOR,
                    'a[data-testid=pagination-page-next]'
                )

                job_cards = self.find_element(
                    By.ID,
                    'mosaic-provider-jobcards'
                )

                # Get every attribute found in every job card
                report = SearchReport(job_cards)
                print(report.pull_job_card_attributes())

                next_btn.click()

        # Last result page has no next button. So pull all attributes from the jobs on that page one last time.
        except NoSuchElementException:

            job_cards = self.find_element(
                By.ID,
                'mosaic-provider-jobcards'
            )

            report = SearchReport(job_cards)
            print(report.pull_job_card_attributes())





