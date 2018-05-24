# Lista elemei [] zárójelek között felsorolva
hozzavalok = ["Bagoly Hónaljszőr", "Csigalekvár", "Szalamandra szem", "Pókláb",
              "Béka nagylábujj", "Mocsári bűzgomba"]

# Lista adott eleme:
print(hozzavalok[2]) # Szalamandra szem
print(hozzavalok[0]) # Bagoly Hónaljszőr

# Két lista összeadása:
teljes_lista = hozzavalok + ["Medveböfi", "Pipacsporzó"]
print(teljes_lista) # ["Bagoly Hónaljszőr", "Csigalekvár", "Szalamandra szem",
                    # "Pókláb", "Béka nagylábujj", "Mocsári bűzgomba",
                    # "Medveböfi", "Pipacsporzó"]

# Lista hossza
print(len(hozzavalok))   # 6
print(len(teljes_lista)) # 8

# Lista tartományok (ranges)
print(hozzavalok[1:3]) # ["Csigalekvár", "Szalamandra szem"]
print(hozzavalok[3:6]) # ["Pókláb", "Béka nagylábujj", "Mocsári bűzgomba"]]
print(hozzavalok[4:])  # ["Béka nagylábujj", "Mocsári bűzgomba"]
print(hozzavalok[:3])  # ["Bagoly Hónaljszőr", "Csigalekvár", "Szalamandra szem"]
