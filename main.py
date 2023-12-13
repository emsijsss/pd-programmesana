import math

def gridas_izmaksa(cena, linoleja_platums, telpas_platums, telpas_garums):
    izmaksa = math.ceil(telpas_platums / linoleja_platums) * telpas_garums * cena

    return izmaksa

while True:
  try:
    cena = float(input("Ievadi linoleja cenu EUR/m^2: "))
  except:
    print("Nepareizi ievadīta vērtība, ievadiet pozitīvu skaitli!")
  else:
    if cena > 0:
      break
    else: 
      print("Nepareizi ievadīta vērtība, ievadiet pozitīvu skaitli!")

while True:
  try:
    linoleja_platums = float(input("Linolejas platums metros: "))
  except: 
    print("Nepareizi ievadīta vērtība, ievadiet pozitīvu skaitli!")
  else:
    if linoleja_platums > 0:
      break
    else:
      print("Nepareizi ievadīta vērtība, ievadiet pozitīvu skaitli!")

while True: 
  try:
    platums = float(input("Ievadi Grīdas platums metros: "))
  except:
    print("Nepareizi ievadīta vērtība, ievadiet pozitīvu skaitli!")
  else:
    if platums > 0:
      break
    else: 
      print("Nepareizi ievadīta vērtība, ievadiet pozitīvu skaitli!")

while True:
  try:
    garums = float(input("Ievadīt grīdas garums metros: "))
  except: 
    print("Nepareizi ievadīta vērtība, ievadiet pozitīvu skaitli!")
  else:
    if garums > 0:
      break
    else: 
      print("Nepareizi ievadīta vērtība, ievadiet pozitīvu skaitli!")

print("Izklājot linoleju platumā:\n", gridas_izmaksa(cena, linoleja_platums, garums, platums))
print("Izklājot linoleju garumā:\n", gridas_izmaksa(cena, linoleja_platums, platums, garums))
