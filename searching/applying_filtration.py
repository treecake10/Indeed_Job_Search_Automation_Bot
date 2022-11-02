from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class ApplyingFiltration:

    def __init__(self, driver:WebDriver):
        self.driver = driver


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

    '''
    functions that click the buttons of radius location, experience level, job type, and developer skills
    '''

    def radius_btn(self):
        job_radius_btn = self.driver.find_element(By.ID, 'filter-radius')
        job_radius_btn.click()

    def job_type_btn(self):
        job_type_btn = self.driver.find_element(By.ID, 'filter-jobtype')
        job_type_btn.click()

    def exp_level_btn(self):
        job_exp_lvl = self.driver.find_element(By.ID, 'filter-explvl')
        job_exp_lvl.click()

    def dev_skills_btn(self):
        job_dev_skills_btn_position_1 = self.driver.find_element(By.ID, 'filter-taxo1')
        job_dev_skills_btn_label = job_dev_skills_btn_position_1.find_element(By.CLASS_NAME, 'yosegi-FilterPill-pillLabel').get_attribute('innerHTML')

        if str(job_dev_skills_btn_label) == "Developer Skill":
            job_dev_skills_btn_position_1.click()
        else:
            job_dev_skills_btn_position_2 = self.driver.find_element(By.ID, 'filter-taxo2')
            job_dev_skills_btn_position_2.click()

    '''
    functions to select or click from a drop down 'pill' list that is displayed after the 
    radius location, experience level, job type, or developer skills button is clicked
    '''

    def apply_radius(self, radius_val):

        radius_elements = self.find_filter_pill_dropdown_list(2)

        for radius_element in radius_elements:

            radius_text = radius_element.get_attribute('innerHTML')

            if str(radius_text) == f'{radius_val}':
                radius_element.click()
                break

    def apply_job_type(self, type_val):

        job_type_elements = self.find_filter_pill_dropdown_list(4)

        for job_type_element in job_type_elements:

            job_type_text = job_type_element.get_attribute('innerHTML')
            white_space_index = job_type_text.index(" ")

            if str(job_type_text[0:white_space_index]) == f'{type_val}':
                job_type_element.click()
                break

    def apply_exp_lvl(self, exp_val):

        experience_level_elements_1 = self.find_filter_pill_dropdown_list(10)
        experience_level_elements_2 = self.find_filter_pill_dropdown_list(11)

        exp_lvl_elements_found = False

        for exp_lvl_element in experience_level_elements_1:

            exp_lvl_text = exp_lvl_element.get_attribute('innerHTML')
            white_space_index = exp_lvl_text.index("(")

            if str(exp_lvl_text[0:white_space_index-1]) == f'{exp_val}':
                exp_lvl_elements_found = True
                exp_lvl_element.click()
                break

        if exp_lvl_elements_found == False:

            for exp_lvl_element in experience_level_elements_2:

                exp_lvl_text = exp_lvl_element.get_attribute('innerHTML')
                white_space_index = exp_lvl_text.index("(")

                if str(exp_lvl_text[0:white_space_index - 1]) == f'{exp_val}':
                    exp_lvl_element.click()
                    break


    def apply_dev_skill(self, skill_val):

        # The location of the 'Developer Skills' filtration pill "button" will change at times
        # So try to find the elements of this pill or button at different positions in the container

        dev_skill_elements_1 = self.find_filter_pill_dropdown_list(4)
        dev_skill_elements_2 = self.find_filter_pill_dropdown_list(5)

        dev_skill_elements_found = False

        for dev_skill_element in dev_skill_elements_1:

            dev_skill_text = dev_skill_element.get_attribute('innerHTML')
            white_space_index = dev_skill_text.index("(")

            if str(dev_skill_text[0:white_space_index - 1]) == f'{skill_val}':
                dev_skill_elements_found = True
                dev_skill_element.click()
                break

        if dev_skill_elements_found == False:

            for dev_skill_element in dev_skill_elements_2:

                dev_skill_text = dev_skill_element.get_attribute('innerHTML')
                white_space_index = dev_skill_text.index("(")

                if str(dev_skill_text[0:white_space_index - 1]) == f'{skill_val}':
                    dev_skill_element.click()
                    break