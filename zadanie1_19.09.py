x = 5000*12;
print ("zarobki roczne brutto: ",x);

if x>1650:
  x=x-350.08;
  print("po odliczeniu kosztów od uzyskania przychodu",x);
  x=x-x*0.12;
  print("po odjęciu składki ZUS: ",x);
  if x<85528:
    x=x*0.18;
    print ("podatek wynosi: ",x);
    x=x*0.85;
    print("po odliczeniu składki zdrowotnej: ",x);
    if x<0:
          print("brak podatku");
  else:
    x=15345.02+0.32*(x-85528);
    print ("podatek wynosi: ",x);
    x=x*0.85;
    print("po odliczeniu składki zdrowotnej: ",x);
    if x<0:
          print("brak podatku");
else:
  print ("Kwota wolna od podatku");

  
