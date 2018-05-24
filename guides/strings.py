# Egyszerű szöveg "" jelek között
szoveg = "Szia Anyu!"
print(szoveg)  # Szia Anyu!



# Egyszerű szövegeket a + jellel összeadva, egymás után íródnak
szorny1 = "Zöldpofájú Tigrisló"
szorny2 = "Görbehátú Nyenyőce"
print("Legfélelmetesebb lény a " + szorny1 + "!")  # Legfélelmetesebb lény a Zöldpofájú Tigrisló!
print("Legfélelmetesebb lény a " + szorny2 + "!")  # Legfélelmetesebb lény a Görbehátú Nyenyőce!



#Ha a szövegek közé számok is kerülnek, vesszővel felsorolva ki lehet írni őket
szam1 = 4
szam2 = 15
eredmeny = szam1 + szam2
print("Összeadás:", szam1, "+", szam2, "=", eredmeny)  # Összeadás: 4 + 15 = 19



#Egy szövegbe be is lehet helyettesíteni számokat előre meghatározott helyekre
szoveg2 = "Mit mondott a {} szám a {} számnak? Túl szoros az öved!"
print(szoveg2.format(0, 8))  # Mit mondott a 0 szám a 8 számnak? Túl szoros az öved!
