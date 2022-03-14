sport=["hockey","basketball", "soccer", "tennis", "football", "baseball"]

pp_play={"hockey":4, "soccer":40,"football":15,"tennis":8}


for x in sport:  
    try: 
     print(pp_play[x]) #print out the value of the sport in the list
    except:
     print("no record found")