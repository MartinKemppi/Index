from math import*

print("Tere! Olen sinu uus sõber - Python!")
try:
    nimi=str(input("Mis on sinu nimi? "))
except:
    ValueError
print(nimi,", oi kui ilus nimi! ")
try:
    index=input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah => ")
except:
    ValueError
if (index == "1"):
    pass
else:
    print("Kahju! See on väga kasulik info!")
    print("")
    print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")
    exit()
try:
    pikkus=int(input("Kui pikk sa oled? "))
except:
    ValueError
try:
    mass=float(input("Palju sa kaalud? "))
except:
    ValueError
indeks=round(mass/(0.01*pikkus)**2,1)
print(f"{nimi}! Sinu keha indeks on: {indeks}")
if (indeks <=15):
    print(f"{indeks}   Tervisele ohtlik alakaal")
elif(indeks <=18):
    print(f"{indeks}   Alakaal")
elif(indeks <=24):
    print(f"{indeks}   Normaalkaal")
elif(indeks <=29):
    print(f"{indeks}   Ülekaal")
elif(indeks <=34):
    print(f"{indeks}   Rasvumine")
elif(indeks <=39):
    print(f"{indeks}   Tugev rasvumine")
else:
    print(f"{indeks}   Tervisele ohtlik rasvumine")
