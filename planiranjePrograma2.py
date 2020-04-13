print("Nalazite se u mracnoj sobi i u zamku. ")
print("Ispred vas su troja vrata. Morate da odaberete jedna. ")
igracIzbor = input("Odaberite 1, 2, 3 ili 4... ")

if igracIzbor == "3":
    print("Pronasli ste sobu punu blaga.Bogati ste!")
    print("IGRA ZAVRSENA. POBEDILI STE.")
elif igracIzbor == "2":
    print("Vrata su se otvorila i razrajeno cudoviste vas je udarilo toljagom.")
    print("IGRA ZAVRSENA. IZGUBILI STE.")
elif igracIzbor == "3":
    print("Usli ste u sobu i zatekli ste zmaja koji spava.")
    print("Zmaj se probudio i pojeo vas. Bas ste ukusni.")
    print("IGRA ZAVRSENA.IZGUBILI STE")
else:
    print("Izvinite, niste uneli 1, 2 ili 3!")
    print("Pokreni ponovo igru da bi ste dobili novu sansu. ")
