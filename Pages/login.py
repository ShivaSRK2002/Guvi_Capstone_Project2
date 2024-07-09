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

    def forgot_password_link(self):
        self.driver.get(vl.login_url)
        forgot_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, lc.forgot_password)))
        forgot_password.click()
        username_textbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, lc.username_text_box)))
        username_textbox.send_keys(lc.valid_username)
        reset_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, lc.reset_password)))
        reset_password.click()
        try:
            reset_password_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, lc.header_6)))
            value = reset_password_element.text
            result = value
            return result
        except TimeoutError:
            result = "Invalid username"
            return result