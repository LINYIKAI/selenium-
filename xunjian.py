# -*- coding: utf-8 -*
import logging;
import os;
import time;
from config import DB,html;
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def write_log():
    logger=logging.getLogger('log');#create logger object
    logger.setLevel(logging.DEBUG); #set logger level
    fh=logging.FileHandler('log.txt');  #create a handler,write to log.txt
    fh.setLevel(logging.DEBUG);
    sh=logging.StreamHandler(); #create a handler,wite to terminal
    sh.setLevel(logging.DEBUG);
    formatter=logging.Formatter('Logger: '+'%(asctime)s - %(name)s - %(levelname)s - %(message)s');#format must be defined
    fh.setFormatter(formatter);
    sh.setFormatter(formatter);
    logger.addHandler(fh);
    logger.addHandler(sh);
    return logger;



class cloud_platform:
    def __init__(self):
        self.logger = write_log();
        options = Options();
        options.add_argument('--start-maximized');
        options.binary_location = r'/usr/bin/chromium-browser';
        self.browser = webdriver.Chrome(executable_path='/home/kelsey/PycharmProjects/Inspection/chromedriver',chrome_options=options);



    def login(self):
        self.browser.get('打码');
        try:
            elem_user = WebDriverWait(self.browser,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-select-2--value"]/div/input')));
            elem_user.send_keys('打码')
            elem_pass = self.browser.find_element_by_id('pass');
            elem_pass.send_keys('打码');
            #self.browser.key_down('ctrl', element=None);
            #self.browser.key_up('ctrl', element=None);
            elem_button = WebDriverWait(self.browser,10).until(EC.presence_of_element_located((By.CLASS_NAME,'LoginForm__submitCanvas___1jBCu')));
            elem_button.click();
        except:
            self.logger.info('Login error\n');
            self.browser.close();
            exit(0);
        finally:
            pass;
        time.sleep(15);
        self.browser.save_screenshot('打码');
        return None;



    def status(self):
        self.browser.get('打码');
        time.sleep(15);
        self.browser.save_screenshot('打码');
        return None;


    def device(self):
        self.browser.get('打码');
        time.sleep(15);
        self.browser.save_screenshot('打码');
        return None;

    def __del__(self):
        self.browser.__exit__();







class adsm_platform:
    def __init__(self):
        self.logger = write_log();
        options = Options();
        options.add_argument('--start-maximized');
        options.binary_location = r'/usr/bin/chromium-browser';
        self.browser = webdriver.Chrome(executable_path='/home/kelsey/PycharmProjects/Inspection/chromedriver',chrome_options=options);


    def login(self):
        self.browser.get('打码');
        try:
            elem_language=WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="language"]')));
            elem_language.click();
            self.browser.find_element_by_xpath('//*[@id="language"]/div[1]/a[1]').click();
            elem_user =self.browser.find_element_by_xpath('//*[@id="username"]');
            elem_user.send_keys('打码');
            elem_pass=self.browser.find_element_by_xpath('//*[@id="password"]');
            elem_pass.send_keys('打码');
            elem_button=self.browser.find_element_by_xpath('//*[@id="loginform"]/fieldset/input[4]');
            elem_button.click();
        except:
            self.logger.info('Login error\n');
            self.browser.close();
            exit(0);
        finally:
            pass;
        time.sleep(15);
        return None;


    def net_manage(self):
        self.browser.get('打码');
        time.sleep(5);
        self.browser.save_screenshot('打码');
        return None;



    def getlog_BGP(self):
        #self.browser.find_element_by_xpath('//*[@id="menu"]/a[3]').click();#
        self.browser.get('打码');#
        time.sleep(5);
        select = Select(self.browser.find_element_by_xpath('//*[@id="datetype"]'))#
        select.select_by_visible_text('自定义');#选择自定义
        self.browser.find_element_by_xpath('//*[@id="btn_search"]').click();#
        self.browser.find_element_by_xpath('//*[@id="btn_export"]').click();
        self.browser.save_screenshot('ADS BGP状态日志.png');
        time.sleep(10);


    def getlog_link_state(self):
        self.browser.get('打码');
        time.sleep(5);
        select = Select(self.browser.find_element_by_xpath('//*[@id="datetype"]'))  # 选择时间
        select.select_by_visible_text('自定义');  # 选择自定义
        self.browser.find_element_by_xpath('//*[@id="btn_search"]').click();  # 点击查询
        self.browser.find_element_by_xpath('//*[@id="btn_export"]').click();
        self.browser.save_screenshot('打码');
        time.sleep(10);


    def getlog_run_warning(self):
        self.browser.get('打码');
        time.sleep(5);
        select = Select(self.browser.find_element_by_xpath('//*[@id="datetype"]'))  
        select.select_by_visible_text('自定义');  # 选
        self.browser.find_element_by_xpath('//*[@id="btn_search"]').click();  # 
        self.browser.find_element_by_xpath('//*[@id="btn_export"]').click();
        self.browser.save_screenshot('打码');
        time.sleep(10);



    def ADS_state(self):
        self.browser.get('打码');
        time.sleep(5);
        select = Select(self.browser.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/div[1]/div[2]/select'))  # 
        select.select_by_visible_text('通过设备展示');  # 
        time.sleep(3);
        self.browser.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/div[1]/div[3]/div/div[1]/ul/li[2]/span[2]/span/span').click();#
        time.sleep(3);
        self.browser.save_screenshot('打码');
        self.browser.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/div[1]/div[3]/div/div[1]/ul/li[3]/span[2]/span/span').click();
        time.sleep(3);
        self.browser.save_screenshot('打码');
        self.browser.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/div[1]/div[3]/div/div[1]/ul/li[4]/span[2]/span/span').click();
        time.sleep(3);
        self.browser.save_screenshot('打码');
        self.browser.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/div[1]/div[3]/div/div[1]/ul/li[5]/span[2]/span/span').click();
        time.sleep(3);
        self.browser.save_screenshot('打码');
        self.browser.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/div[1]/div[3]/div/div[1]/ul/li[6]/span[2]/span/span').click();
        time.sleep(3);
        self.browser.save_screenshot('打码');
        self.browser.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/div[1]/div[3]/div/div[1]/ul/li[7]/span[2]/span/span').click();
        time.sleep(3);
        self.browser.save_screenshot('打码');


    def __del__(self):
        self.browser.__exit__();




if __name__=='__main__':
    cloud=cloud_platform();
    cloud.login();
    cloud.status();
    cloud.device();
    cloud.__del__();
    adsm=adsm_platform();
    adsm.login();
    adsm.net_manage();
    adsm.getlog_BGP();
    adsm.getlog_link_state();
    adsm.getlog_run_warning();
    adsm.ADS_state();
    adsm.__del__();
    os._exit(0);
