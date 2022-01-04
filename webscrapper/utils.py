from datetime import datetime
import pandas


not_includeds = [
                 'BOAS3','SEQL3','B3SA3','BBSE3','IRBR3','SULA11','BBDC4','BBDC3',
                 'BBAS3','CIEL3','ITSA4','ITUB4','SANB11','PSSA3','BBSE3','CXSE3', 
                 'CSAB4','CSAB3','BRGE11','BRGE11','BRGE3','BRGE5','BRGE6','BRGE7',
                 'BRGE8','PSSA3','SULA3','SULA4','IRBR3','RPAD3','RPAD6','RPAD5',
                 'BERK34','BOAC34','WFCO34', 'AXPB34', 'CTGP34', 'BLAK34', 'GSGI34',
                 'USBC34', 'BONY34', 'BILB34', 'METB34', 'KNCR11','GPIV33', 'CIEL3',
                 'B3SA3', 'PDTC3', 'BOAS3','BRGE6','BRGE5','BRGE11','BRGE8','CXSE3',
                 'BRGE3','BRGE12','WIZS3','BBSE3','CSAB3','PSSA3','CSAB4','SULA3',
                 'SULA11', 'APER3', 'IRBR3'
                 ]


def get_today():
    return datetime.now().strftime("%d-%m-%Y")


def save_result_as_excel(final_df, file_name, with_date=True):
    output = file_name if not with_date else file_name + "-" + get_today()
    writer = pandas.ExcelWriter(output + ".xlsx")
    final_df.to_excel(writer)
    writer.save()