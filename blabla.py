from postinumerot import etsi_postinumero, luo_data_postinumerot
from postitoimipaikka import luo_data_postitoimipaikat, etsi_postitoimipaikka
import json
import os, sys
# from postitoimipaikka import 
from datetime import datetime, date, time




def postinumero_testaa_ettei_loydy(haku):
    data = luo_data_postinumerot();   
    result = etsi_postinumero(haku,data)
    assert result == None

def postitoimipaikka_x_kpl(postitoimipaikka):
    data = luo_data_postitoimipaikat()
    results = etsi_postitoimipaikka(postitoimipaikka,data)
    assert len(results) == 1

def postitoimipaikka_monta_kpl(postitoimipaikka):
    data = luo_data_postitoimipaikat()
    results = etsi_postitoimipaikka(postitoimipaikka,data)
    assert len(results) > 1



def main():
    postinumero_testaa_ettei_loydy("003700")
    postitoimipaikka_x_kpl("Nousiainen")
    postitoimipaikka_monta_kpl("Helsinki")

if __name__ == "__main__":
    main()   