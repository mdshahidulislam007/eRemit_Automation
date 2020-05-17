import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class DataTable:
    def __init__(self,datatable):
        self.table = datatable

    def get_row_count(self):
        return len(self.table.find_elements_tag_name("tr")) - 1

    def get_column_count(self):
        return len(self.table.find_elements_by_xpath("//tr[2]/td"))

    def get_table_size(self):
        return {"rows": self.get_row_count(),
                "columns": self.get_column_count()}

    def row_data(self, row_number):
        if(row_number == 0):
            raise Exception("Row number starts from 1")

        row_number = row_number + 1
        row = self.table.find_elements_by_xpath("")
        rData = []
        for webElement in row :
            rData.append(webElement.text)

        return rData



class Test(unittest.TestCase):
    def test_data_table(self):
        driver = webdriver.Chrome(r"resources/chromedriver.exe")
        driver.implicitly_wait(30)

        driver.get('http://10.11.201.92:4200/fileProcessing/')
        driver.maximize_window()
        driver.find_element_by_xpath("//div[@id='cdk-step-content-0-0']//div[1]//div[1]//div[1]//div[2]//button[1]//span[1]//mat-icon[1]").click()
        driver.find_element_by_tag_name("input").send_keys("F:/Md. Shahidul Islam/Selenium_Learning/eRemitAutomation/resources/UEC 14.09.15 (11).xls")
        time.sleep(5)
        driver.find_element_by_xpath("//button[@class='btn btn-info mat-raised-button']").click()
        w = DataTable(driver.find_element_by_xpath(""))

        print("No of rows : ", w.get_row_count())
        print("------------------------------------")
        print("No of cols : ", w.get_column_count())
        print("------------------------------------")
        print("Table size : ", w.get_table_size())
        print("------------------------------------")

if __name__ == "__main__":
    unittest.main()