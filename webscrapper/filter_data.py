from utils import get_today, save_result_as_excel, not_includeds
from advanced_scrapper import advanced_scrapper
import pandas as pd
import os


def exclude_financy(dataframe):
    return dataframe.loc[~dataframe['Papel'].isin(not_includeds)]


def filter_data():
    df = pd.read_excel("../excel_tables/output.xlsx")


    df['Mrg Ebit'] = df['Mrg Ebit'].str.rstrip('%').str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype("float") / 100
    df['Liq.2meses'] = df['Liq.2meses'].str.replace('.', '', regex=False).str.replace(',','.', regex=False).astype("float")
    df['EV/EBIT'] = df['EV/EBIT'].str.replace('.', '', regex=False).str.replace(',','.', regex=False).astype("float")

    df = df[df['Mrg Ebit'] > 0]
    df = df[df["Liq.2meses"].astype("float") > 150000]
    df = df.sort_values("EV/EBIT")

    if not os.path.isdir("../resultados"):
        os.system("mkdir ../resultados")

    save_result_as_excel(exclude_financy(df), "../resultados/output")
    print("GERANDO SAIDA EM: \"../resultados/output-"+ get_today() +".xlsx\"")


if __name__ == "__main__":
    filter_data()