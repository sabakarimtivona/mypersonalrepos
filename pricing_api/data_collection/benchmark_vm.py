from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pricing_api.models.vm_benchmark_models import Benchmark
import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import datetime
import logging

logger = logging.getLogger()

def linux_vm_data(driver):
    logger.info('linux scraping is started'+" at "+str(datetime.datetime.now())+' hours!')
    driver.delete_all_cookies()
    driver.get("https://learn.microsoft.com/en-us/azure/virtual-machines/linux/compute-benchmark-scores")
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//table[@class="table table-sm"]//tr')))
    tables = driver.find_elements(By.XPATH, "//div[@class='has-inner-focus']/table[@class='table table-sm']")[1:]
    site_dates = driver.find_elements(By.XPATH, "//*[@class='has-inner-focus']/table[@class='table table-sm']/../preceding-sibling::p[contains(text(),'PBIID')]")
    table_dates_in_site = []
    for dt in site_dates:
        table_dates_in_site.append(dt.text.split(" ")[0][1:])
    ii = 0
    lin_table_data  = []
    all_dates = []
    for table in tables:         
            try:
                lin_dates_text = table.find_element(By.XPATH, "./../preceding-sibling::p[1][contains(text(),'PBIID')]").text
                lin_date_=lin_dates_text.split(" ")[0][1:]
                all_dates.append(lin_date_)
                if lin_date_ != table_dates_in_site[ii]:
                     table_dates_in_site.insert(ii-1,'')
                     all_dates[ii] = all_dates[ii-1]
                     all_dates[ii-1] ='-'
            except Exception as e:
                logger.info(e)

            ii = ii +1

    ii = 0
    for table in tables:
        rows = table.find_elements(By.XPATH, "./tbody/tr")[0:]
        for row in rows:
            column_1 = row.find_element(By.XPATH, "./td[1]").text
            column_2 = row.find_element(By.XPATH, "./td[2]").text
            column_3 = row.find_element(By.XPATH, "./td[3]").text
            column_4 = row.find_element(By.XPATH, "./td[4]").text
            column_5 = row.find_element(By.XPATH, "./td[5]").text
            column_6 = row.find_element(By.XPATH, "./td[6]").text
            column_7 = row.find_element(By.XPATH, "./td[7]").text
            column_8 = row.find_element(By.XPATH, "./td[8]").text
            column_9 = row.find_element(By.XPATH, "./td[9]").text
            dict_ = {
                "column1" : column_1,
                "column2" : column_2,
                "column3" : column_3,
                "column4" : column_4,
                "column5" : column_5,
                "column6" : column_6,
                "column7" : column_7,
                "column8" : column_8,
                "column9" : column_9,
            }
        
            dict_["date"]=all_dates[ii]
            lin_table_data.append(dict_)
           
        ii = ii +1
    logger.info("linux scraping is over at "+str(datetime.datetime.now())+' hours!')
    return lin_table_data


def windows_vm_data(driver):
    logger.info("windows scraping in started"+" at "+str(datetime.datetime.now())+' hours!')
    driver.delete_all_cookies()
    driver.get("https://learn.microsoft.com/en-us/azure/virtual-machines/windows/compute-benchmark-scores")
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//table[@class="table table-sm"]//tr')))
    tables = driver.find_elements(By.XPATH, "//div[@class='has-inner-focus']/table[@class='table table-sm']")[1:]
    site_dates = driver.find_elements(By.XPATH, "//*[@class='has-inner-focus']/table[@class='table table-sm']/../preceding-sibling::p[contains(text(),'PBIID')]")
    table_dates_in_site = []
    for dt in site_dates:
        table_dates_in_site.append(dt.text.split(" ")[0][1:])
    ii = 0
    win_table_data  = []
    all_dates = []
    for table in tables:         
            try:
                win_dates_text = table.find_element(By.XPATH, "./../preceding-sibling::p[1][contains(text(),'PBIID')]").text
                win_date_=win_dates_text.split(" ")[0][1:]
                all_dates.append(win_date_)
                if win_date_ != table_dates_in_site[ii]:
                     table_dates_in_site.insert(ii-1,'')
                     all_dates[ii] = all_dates[ii-1]
                     all_dates[ii-1] ='-'
            except Exception as e:
                logger.info(e)

            ii = ii +1

    ii = 0
    for table in tables:
        rows = table.find_elements(By.XPATH, "./tbody/tr")[0:]
        for row in rows:
            column_1 = row.find_element(By.XPATH, "./td[1]").text
            column_2 = row.find_element(By.XPATH, "./td[2]").text
            column_3 = row.find_element(By.XPATH, "./td[3]").text
            column_4 = row.find_element(By.XPATH, "./td[4]").text
            column_5 = row.find_element(By.XPATH, "./td[5]").text
            column_6 = row.find_element(By.XPATH, "./td[6]").text
            column_7 = row.find_element(By.XPATH, "./td[7]").text
            column_8 = row.find_element(By.XPATH, "./td[8]").text
            column_9 = row.find_element(By.XPATH, "./td[9]").text
            dict_ = {
                "column1" : column_1,
                "column2" : column_2,
                "column3" : column_3,
                "column4" : column_4,
                "column5" : column_5,
                "column6" : column_6,
                "column7" : column_7,
                "column8" : column_8,
                "column9" : column_9,
            }
            
            dict_["date"]=all_dates[ii]
            win_table_data.append(dict_)

        ii = ii +1
    logger.info("windows scraping is over at "+str(datetime.datetime.now())+' hours!')
    return win_table_data


def get_skus_data(driver):
    linux_sku_data = linux_vm_data(driver)
    windows_sku_data = windows_vm_data(driver)
    logger.info('web scraping is done ,1121 data is scraped'+" at "+str(datetime.datetime.now())+' hours!')
    sku_data = []

    for data in windows_sku_data:
        Benchmark.objects.update_or_create( 
          vm_sku_name = data['column1'],
            operating_system = 'windows',
            CPU = data['column2'],NUMA_Nodes = data['column4'],
             defaults={'vCPUs':data['column3'],'Memory' : data['column5'],'Avg_Score': data['column6'],'StdDev': data['column7'],'StdDev_percentage': data['column8'],
                       'Runs' :data['column9'],'Published_date' : data['date']}
        )
    
    for data in linux_sku_data:
        Benchmark.objects.update_or_create(
            vm_sku_name = data['column1'],
            operating_system = 'linux',
            CPU = data['column2'],NUMA_Nodes = data['column4'],
             defaults={'vCPUs':data['column3'],'Memory' : data['column5'],'Avg_Score': data['column6'],'StdDev': data['column7'],'StdDev_percentage': data['column8'],
                       'Runs' :data['column9'],'Published_date' : data['date']}
        )
    
    return sku_data

options = webdriver.ChromeOptions()
# options.headless = True
chrom_driv=Service("/home/thamaraikannan/Downloads/chromedriver_linux64/chromedriver")
driver = uc.Chrome(service=chrom_driv)
driver.maximize_window()
skus_data = get_skus_data(driver)