import asyncio
import pandas as pd
from pyppeteer import launch
from bs4 import BeautifulSoup
from utils import save_result_as_excel


async def getDataFromWebPage(url):
    browser = await launch(headless=True)
    page = await browser.newPage()

    response = await page.goto(url, {'waitUntil': 'networkidle2'})
    html = await response.text()
    await browser.close()

    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', {'id': 'resultado'})

    df = pd.read_html(str(table))[0]
    return df


if __name__ == '__main__':
    fundamentus_url = 'https://fundamentus.com.br/resultado.php'

    df = asyncio.get_event_loop().run_until_complete(getDataFromWebPage(fundamentus_url))
    save_result_as_excel(df, "../excel_tables/output", with_date=False)
