print("Podaj szerokość opony [mm]:");
szerokosc= int(input());
print("Podaj profil opony [%]:");
profil= int(input());
print("Podaj średnice felgi [cale]:");
srednica= int(input());

print("Twój model koła to: ",szerokosc,"/",profil," R",srednica);
sz=szerokosc/10;
pr=(sz/100)*profil;
sr=srednica*2.54;

srk=2*pr+sr;
print("Średnica koła: ",srk);
obw=3.14*srk;
print("Obwód koła: ",obw);
