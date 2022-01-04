import time
import asyncio
import math
import pandas as pd
from pyppeteer import launch
from bs4 import BeautifulSoup
from utils import get_today, save_result_as_excel


def html_elemments(html):
    soup = BeautifulSoup(html, 'html.parser')
    lpa = soup.find_all('td')[35].find('span').string
    vpa = soup.find_all('td')[41].find('span').string
    value = soup.find_all('td')[3].find('span').string
    return {'lpa': lpa, 'vpa': vpa, 'value': value}


def transform_column(value):
    return float(str(value).rstrip('%').replace('.', '').replace(',','.'))


async def advanced_scrapper():
    browser = await launch(headless=True)
    page = await browser.newPage()

    df = pd.read_excel("../resultados/output-"+ get_today() +".xlsx")

    base_url = 'https://fundamentus.com.br/detalhes.php?papel='
    lpa_array, vpa_array, valuation_array, paper_array, actual_value = [], [], [], [], []
    
    for _,row in df.iterrows():
        
        paper = row['Papel']
        url = base_url + paper

        print(f'INICIANDO SCRAPPER NO PAPEL: { paper }')
        response = await page.goto(url, {'waitUntil': 'networkidle2'})

        html = await response.text()
        soup = BeautifulSoup(html, 'html.parser')
        lpa = soup.find_all('td')[35].find('span').string
        vpa = soup.find_all('td')[41].find('span').string
        value = soup.find_all('td')[3].find('span').string

        lpa   = transform_column(lpa)
        vpa   = transform_column(vpa)
        value = transform_column(value)

        parsed_lpa, parsed_vpa = lpa if lpa > 0 else 0, vpa if vpa > 0 else 0
        valuation = "%.2f" % math.sqrt(22.5 * parsed_lpa * parsed_vpa)
        
        lpa_array.append(lpa)
        vpa_array.append(vpa)
        paper_array.append(paper)
        actual_value.append(value)
        valuation_array.append(valuation)
        
        print(f'VPA: {vpa} | LPA: {lpa} | VALUATION: {valuation} | VALUE: {value}')

        time.sleep(0.5)

    await browser.close()

    final_df = pd.DataFrame(data={ 'AÇÃO': paper_array,'VALUATION': valuation_array,
             'ATUAL_VALUE': actual_value,'LPA': lpa_array,'VPA': vpa_array})

    save_result_as_excel(final_df, "../resultados/advanced-output")  


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(advanced_scrapper())
