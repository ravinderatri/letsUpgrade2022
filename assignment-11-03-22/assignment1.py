gold={"US":46,"Fiji":1,"Great Britain":27,"Cuba":15,"Thailand":2,"China":26,"France":10}
country=["Fiji", "Chile", "Mexico","France", "Norway", "US"]
country_glod=[]
i=0
for x in country:  
    if x in gold: 
      d=x,gold[x]
      country_glod.append(d) 
    else :
     country=x,"Did not get gold"
     print(country)
print(country_glod) #list of country, coountry and searches to see if it is in the dictionary gold which shows some countries who won gold during olympics


	