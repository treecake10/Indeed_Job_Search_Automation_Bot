from selenium.common import ElementNotInteractableException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class LandingSearchPage(BasePage):

    def site_title_found(self):
        return "Indeed" in self.driver.title

    def what_label_found(self):
        return "What" in self.driver.page_source

    def fill_what_form(self):
        what_search_box = self.driver.find_element(By.ID, 'text-input-what')
        what_search_box.clear()
        what_search_box.send_keys("web dev")
        what_search_box.send_keys(Keys.RETURN)

    def job_results_found(self):
        return "did not match any jobs." not in self.driver.page_source

    def where_label_found(self):
        return "Where" in self.driver.page_source

    def fill_where_form_with_remote(self):
        where_search_box = self.driver.find_element(By.ID, 'text-input-where')
        where_search_box.click()

        clear_text_btn = self.driver.find_element(By.CLASS_NAME, 'icl-TextInputClearable-icon')
        clear_text_btn.click()
        where_search_box.send_keys("remote")

    def find_jobs_label_found(self):
        return "Find jobs" in self.driver.page_source

    def click_find_btn(self):
        find_btn = self.driver.find_element(By.CLASS_NAME, 'yosegi-InlineWhatWhere-primaryButton')
        find_btn.click()

    def remote_btn_label_found(self):
        return "Remote" in self.driver.page_source

    def click_remote_filtration_btn(self):
        remote_btn = self.driver.find_element(By.ID, 'filter-remotejob')
        remote_btn.click()

    def fill_where_form_with_location(self):
        where_search_box = self.driver.find_element(By.ID, 'text-input-where')
        where_search_box.click()

        clear_text_btn = self.driver.find_element(By.CLASS_NAME, 'icl-TextInputClearable-icon')
        clear_text_btn.click()
        where_search_box.send_keys("Canton, GA")


class FiltrationsPage(BasePage):

    def radius_label_found(self):
        return "within 25 miles" in self.driver.page_source

    def click_radius_btn(self):
        job_radius_btn = self.driver.find_element(By.ID, 'filter-radius')
        job_radius_btn.click()

    def test_apply_radius(self):
        radius_elements = self.find_filter_pill_dropdown_list(2)
        radius_elements[6].click()

    def job_type_label_found(self):
        return "Job Type" in self.driver.page_source

    def click_job_type_btn(self):
        job_type_btn = self.driver.find_element(By.ID, 'filter-jobtype')
        job_type_btn.click()

    def test_apply_job_type(self):
        job_type_elements = self.find_filter_pill_dropdown_list(4)
        job_type_elements[0].click()

    def exp_lvl_label_found(self):
        return "Experience Level" in self.driver.page_source

    def click_exp_lvl_btn(self):
        job_exp_lvl = self.driver.find_element(By.ID, 'filter-explvl')
        job_exp_lvl.click()

    def test_apply_exp_lvl(self):
        
        try:

            experience_level_elements = self.find_filter_pill_dropdown_list(10)
            experience_level_elements[0].click()

        except ElementNotInteractableException:

            experience_level_elements = self.find_filter_pill_dropdown_list(11)
            experience_level_elements[0].click()


    def dev_skill_label_found(self):
        return "Developer Skill" in self.driver.page_source

    def click_dev_skill_btn(self):
        job_dev_skills_btn_position_1 = self.driver.find_element(By.ID, 'filter-taxo1')
        job_dev_skills_btn_label = job_dev_skills_btn_position_1.find_element(By.CLASS_NAME, 'yosegi-FilterPill-pillLabel').get_attribute('innerHTML')

        if str(job_dev_skills_btn_label) == "Developer Skill":
            job_dev_skills_btn_position_1.click()
        else:
            job_dev_skills_btn_position_2 = self.driver.find_element(By.ID, 'filter-taxo2')
            job_dev_skills_btn_position_2.click()

    def test_apply_dev_skill(self):

        try:

            dev_skill_elements = self.find_filter_pill_dropdown_list(4)
            dev_skill_elements[0].click()

        except ElementNotInteractableException:

            dev_skill_elements = self.find_filter_pill_dropdown_list(5)
            dev_skill_elements[0].click()


    def find_pill_elements(self):

        filtration_pills_container = self.driver.find_element(
            By.CLASS_NAME,
            'yosegi-FilterPill-pillList'
        )

        return filtration_pills_container.find_elements(
            By.CLASS_NAME,
            'yosegi-FilterPill-dropdownPillContainer'
        )

    def find_filter_pill_dropdown_list(self, index=None):

        return self.find_pill_elements()[index].find_elements(
            By.CSS_SELECTOR,
            'a[class=yosegi-FilterPill-dropdownListItemLink]'
        )


class JobCardsPage(BasePage):

    def test_job_cards(self):

        get_job_cards = self.driver.find_element(
            By.ID,
            'mosaic-provider-jobcards'
        )

        return get_job_cards.find_elements(
            By.CLASS_NAME,
            'result'
        )


class NextButtonPage(BasePage):

    def test_next_button(self):

        next_btn = self.driver.find_element(
            By.CSS_SELECTOR,
            'a[data-testid=pagination-page-next]'
        )

        next_btn.click()


