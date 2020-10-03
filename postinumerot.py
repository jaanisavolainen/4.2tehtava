import json
import os, sys
# JSON-data on tässä kovakoodattu moniriviseksi merkkijonoksi.
# Käytä `open`-funktiota lukeaksesi tiedot levyltä tai
# `urllib`-kirjastoa lukeaksesi tiedot suoraan netistä.
# print(os.path.join(sys.path[0],"postcode_map.json"))

def luo_data_postinumerot():
    pathi = os.path.join(sys.path[0],"postcode_map_light.json")
    with open(pathi) as f:
     data = json.load(f)
    return data

def etsi_postinumero(x,data):
  if x.upper() in data:
      return(data[x.upper()])
  else:
     return

