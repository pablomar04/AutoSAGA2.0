from openpyxl import load_workbook
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import constantes as const

wb = load_workbook("precios.xlsx", data_only=True)
sh = wb["Nafta"]
n1 = [int(sh["e26"].value), int(sh["e27"].value), 
      int(sh["g26"].value), int(sh["g27"].value),
      int(sh["i26"].value), int(sh["i27"].value),
      int(sh["k26"].value), int(sh["k27"].value),
      int(sh["m26"].value), int(sh["m27"].value),
      int(sh["o26"].value), int(sh["o27"].value),
      int(sh["q26"].value), int(sh["q27"].value)]

n2 = [int(sh["e53"].value), int(sh["e54"].value), 
      int(sh["g53"].value), int(sh["g54"].value),
      int(sh["i53"].value), int(sh["i54"].value),
      int(sh["k53"].value), int(sh["k54"].value),
      int(sh["m53"].value), int(sh["m54"].value),
      int(sh["o53"].value), int(sh["o54"].value),
      int(sh["q53"].value), int(sh["q54"].value)]

n3 = [int(sh["e80"].value), int(sh["e81"].value), 
      int(sh["g80"].value), int(sh["g81"].value),
      int(sh["i80"].value), int(sh["i81"].value),
      int(sh["k80"].value), int(sh["k81"].value),
      int(sh["m80"].value), int(sh["m81"].value),
      int(sh["o80"].value), int(sh["o81"].value),
      int(sh["q80"].value), int(sh["q81"].value)]

n4 = [int(sh["e107"].value), int(sh["e108"].value), 
      int(sh["g107"].value), int(sh["g108"].value),
      int(sh["i107"].value), int(sh["i108"].value),
      int(sh["k107"].value), int(sh["k108"].value),
      int(sh["m107"].value), int(sh["m108"].value),
      int(sh["o107"].value), int(sh["o108"].value),
      int(sh["q107"].value), int(sh["q108"].value)]

n5 = [int(sh["e134"].value), int(sh["e135"].value), 
      int(sh["g134"].value), int(sh["g135"].value),
      int(sh["i134"].value), int(sh["i135"].value),
      int(sh["k134"].value), int(sh["k135"].value),
      int(sh["m134"].value), int(sh["m135"].value),
      int(sh["o134"].value), int(sh["o135"].value),
      int(sh["q134"].value), int(sh["q135"].value)]

n6 = [int(sh["e161"].value), int(sh["e162"].value), 
      int(sh["g161"].value), int(sh["g162"].value),
      int(sh["i161"].value), int(sh["i162"].value),
      int(sh["k161"].value), int(sh["k162"].value),
      int(sh["m161"].value), int(sh["m162"].value),
      int(sh["o161"].value), int(sh["o162"].value),
      int(sh["q161"].value), int(sh["q162"].value)]

n7 = [int(sh["e188"].value), int(sh["e189"].value), 
      int(sh["g188"].value), int(sh["g189"].value),
      int(sh["i188"].value), int(sh["i189"].value),
      int(sh["k188"].value), int(sh["k189"].value),
      int(sh["m188"].value), int(sh["m189"].value),
      int(sh["o188"].value), int(sh["o189"].value),
      int(sh["q188"].value), int(sh["q189"].value)]

sh = wb["Diesel"]

d1 = [int(sh["e26"].value), int(sh["e27"].value), 
      int(sh["g26"].value), int(sh["g27"].value),
      int(sh["i26"].value), int(sh["i27"].value)]

d2 = [int(sh["e53"].value), int(sh["e54"].value), 
      int(sh["g53"].value), int(sh["g54"].value),
      int(sh["i53"].value), int(sh["i54"].value)]

d3 = [int(sh["e80"].value), int(sh["e81"].value), 
      int(sh["g80"].value), int(sh["g81"].value),
      int(sh["i80"].value), int(sh["i81"].value)]

d4 = [int(sh["e107"].value), int(sh["e108"].value), 
      int(sh["g107"].value), int(sh["g108"].value),
      int(sh["i107"].value), int(sh["i108"].value)]

d5 = [int(sh["e134"].value), int(sh["e135"].value), 
      int(sh["g134"].value), int(sh["g135"].value),
      int(sh["i134"].value), int(sh["i135"].value)]

sh = wb['Amarok ']

a1 = [int(sh["g23"].value), int(sh["g24"].value),
      int(sh["i23"].value), int(sh["i24"].value)]

a2 = [int(sh["g47"].value), int(sh["g48"].value),
      int(sh["i47"].value), int(sh["i48"].value)]

a3 = [int(sh["g71"].value), int(sh["g72"].value),
      int(sh["i71"].value), int(sh["i72"].value)]

a4 = [int(sh["g95"].value), int(sh["g96"].value),
      int(sh["i95"].value), int(sh["i96"].value)]

a5 = [int(sh["g119"].value), int(sh["g120"].value),
      int(sh["i119"].value), int(sh["i120"].value)]

a6 = [int(sh["g143"].value), int(sh["g144"].value),
      int(sh["i143"].value), int(sh["i144"].value)]

a7 = [int(sh["g167"].value), int(sh["g168"].value),
      int(sh["i167"].value), int(sh["i168"].value)]

a8 = [int(sh["g191"].value), int(sh["g192"].value),
      int(sh["i191"].value), int(sh["i192"].value)]

a9 = [int(sh["g215"].value), int(sh["g216"].value),
      int(sh["i215"].value), int(sh["i216"].value)]

a10 = [int(sh["g239"].value), int(sh["g240"].value),
       int(sh["i239"].value), int(sh["i240"].value)]

# Traer templates desde mongo
uri = "mongodb+srv://"+const.USER_MONGO+":"+const.PASS_MONGO+"@cluster0.g0ktnap.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Obtener json
db = client['work']

db.templates.update_one({'codigo':"d55"}, {'$set': {"data.1.tercero.emo.0.importe": "999"}})
db.templates.update_one({'codigo':"d55"}, {'$set': {"data.1.tercero.ematerial.0.importe": "999"}})


client.close()

for x in n2:
    print(x)
