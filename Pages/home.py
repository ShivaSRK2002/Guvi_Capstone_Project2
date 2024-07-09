import os
import time
import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Locators.locators import LoginLocators as lc
from Locators import locators as vl

class ValidationMethods:

    def __init__(self,driver):
        self.driver = driver


    def go_to_page(self,url):
        try:
            self.driver.get(url)
            return True
        except:
            print("ERROR : URL is incorrect/Network Error")
            return False


    def validation_on_admin_page(self):
        admin_page = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, lc.admin)))
        admin_page.click()
        xpaths = vl.xpath_admin_page
        headers_present = []
        header_not_present = []
        for i in xpaths:
            try:
                y = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,i)))
                header = y.text
                headers_present.append(header)
            except TimeoutException:
                pass
            else:
                header_not_present.append(i)
        return headers_present



    def title_verification(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, lc.title)))
            result = "OrangeHRM"
            return result
        except TimeoutException:
            result = "Title not found"
            return result


    def login_to_OragneHRM_stat(self,username,password):
        username_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, lc.username_element)))
        password_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, lc.password_element)))
        submit_button_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, lc.submit_element)))
        username_element.send_keys(username)
        password_element.send_keys(password)
        submit_button_element.click()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("dashboard"))
            result = "The user has logged in successfully"
            return result
        except TimeoutException:
            result = "Invalid credentials"
            return result


    def validate_main_menu(self):
        xpaths = vl.xpaths_main_menu
        menu_present = []
        menu_not_present = []
        for i in xpaths:
            try:
                y = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, i)))
                header = y.text
                menu_present.append(header)
            except TimeoutException:
                pass
            else:
                menu_not_present.append(i)
        return menu_present