#!/usr/bin/env python3
# -*- coding: utf -*- 
import os
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from utils import save_result_as_excel
from filter_data import main_filter

def os_exclude_directory():
    os.system("rm -rf ../excel_tables")
    os.system("mkdir ../excel_tables")

def main_scrapper():
    fundamentus_url = 'https://fundamentus.com.br/resultado.php'
    
    driver = webdriver.Chrome('../chromeDriver/chromedriver')

    driver.get(fundamentus_url)
    time.sleep(2)

    html = driver.page_source

    driver.close()
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', {'id': 'resultado'})

    df = pd.read_html(str(table))[0]

    os_exclude_directory()
    save_result_as_excel(df, "../excel_tables/output", False)
    
    proceed = input('Deseja prosseguir para o próximo passo ? [Y/n]: ')
    if proceed == 'Y':
        main_filter()
    else:
        return 


if __name__ == '__main__':
    main_scrapper()