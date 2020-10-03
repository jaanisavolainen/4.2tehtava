import json
import os, sys
import array
# JSON-data on tässä kovakoodattu moniriviseksi merkkijonoksi.
# Käytä `open`-funktiota lukeaksesi tiedot levyltä tai
# `urllib`-kirjastoa lukeaksesi tiedot suoraan netistä.

# print(os.path.join(sys.path[0],"postcode_map.json"))
#print (pathi)

def luo_data_postitoimipaikat():
  pathi = os.path.join(sys.path[0],"postcode_map_light.json")
  with open(pathi) as f:
    data = json.load(f)

  newDict = {

  }
  for postinumero, postitoimipaikka in data.items():
    if not postitoimipaikka in newDict:
      newDict[postitoimipaikka] = [postinumero]
    else:
      temparray = newDict[postitoimipaikka]
      temparray.append(postinumero)
      newDict[postitoimipaikka] = temparray
  return newDict


def etsi_postitoimipaikka(postitoimipaikka,data):
  results = []
  if postitoimipaikka.upper() in data:
    for nro in data[postitoimipaikka.upper()]:
      results.append(nro)
  return results