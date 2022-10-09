# contains method to parse specific data that is neeeded from each of the job boxes
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from prettytable import PrettyTable
import numpy as np


class SearchReport:

    def __init__(self, job_card_elements: WebElement):
        self.job_card_elements = job_card_elements
        self.job_card_results = self.pull_job_card_results()

    def pull_job_card_results(self):

        return self.job_card_elements.find_elements(
            By.CLASS_NAME,
            'result'
        )

    def pull_job_card_attributes(self):

        job_titles_array = []
        job_salaries_array = []
        job_types_array = []
        company_names_array = []
        company_locations_array = []

        for job_card_result in self.job_card_results:

            job_card_text_data = job_card_result.get_attribute('innerText').split('\n')
            salary_found = False

            for job_card_text in job_card_text_data:
                if job_card_text.startswith('$') or job_card_text.startswith('Estimated $', 0, 11):
                    job_salaries_array.append(job_card_text)
                    salary_found = True
                if job_card_text.startswith('Part-time', 0, 9) or job_card_text.startswith('Full-time', 0, 9):
                    job_types_array.append(job_card_text)
            if salary_found == False:
                job_salaries_array.append('Not Provided')

            job_results_element_list = job_card_result.find_elements(
                By.TAG_NAME,
                'span'
            )

            job_locations_element_list = job_card_result.find_elements(
                By.CLASS_NAME,
                'companyLocation'
            )

            for job_location_element in job_locations_element_list:

                index_count = 0
                location_last_char_index = 0
                extraneousTextExists = False

                job_location_text = job_location_element.get_attribute('innerHTML').strip()

                # The inner html sometimes contains unneeded extra information attached to the company's location.
                # For example, "Company Location"<!-- -->&nbsp;<span class...</span>
                for job_location_text_char in job_location_text:
                    index_count += 1
                    if job_location_text_char == '<':
                        location_last_char_index = index_count
                        extraneousTextExists = True
                        break

                if extraneousTextExists == True:
                    company_locations_array.append(job_location_text[:location_last_char_index - 1])
                elif extraneousTextExists == False:
                    company_locations_array.append(job_location_text)

            for job_element in job_results_element_list:
                if job_element.get_attribute("title") != '':
                    job_titles_array.append(job_element.get_attribute("title").strip())

                if job_element.get_attribute('class') == 'companyName':
                    company_name_element = job_element.get_attribute('innerHTML').strip()

                    # Sometimes the inner html is an element instead of the company name text
                    if (company_name_element.startswith('<a data-tn-element="companyName"', 0, 32)):

                        trimmed_company_name_element = ''
                        count_remaining_characters = False

                        trimmed_company_name_element += '<'

                        for company_name_element_char in company_name_element:

                            # Skip all characters between brackets '<' and '>' in the open tag of the element found as the inner html
                            if company_name_element_char == '>':
                                trimmed_company_name_element += company_name_element_char
                                count_remaining_characters = True
                                continue

                            # Only get all characters that occur after the open html tag
                            if count_remaining_characters == True:
                                trimmed_company_name_element += company_name_element_char

                        # Turn '<>Company Name</a>' to 'Company Name'
                        company_names_array.append(trimmed_company_name_element[2:][:-4])

                    # inner html is just the text of the company name, not an element
                    else:

                        company_names_array.append(company_name_element)

        '''
        Arrays of job titles, company names, location, salaries, and job types are all collected as a 2D
        array and then transposed, using NumPy, to get all of a particular job's information as a single row.

        Because the transposed array now has all of a job's information contained as a separate row, the 
        2D array can be visualized in tabular form and PrettyTable can be used to generate a table from 
        the data in the array.
        '''
        collection = np.array(
            [job_titles_array, company_names_array, company_locations_array, job_salaries_array, job_types_array])
        transposed_arrays = np.transpose(collection)

        table = PrettyTable(
            field_names=["Job Title", "Company Name", "Location", "Salary", "Job Type"]
        )
        table.add_rows(transposed_arrays)

        return table