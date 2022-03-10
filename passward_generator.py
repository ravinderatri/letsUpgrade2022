import random
import string

pStr="123456"
pStr1="cvb"
pStr2="CFD" 
pStr3="#$&!@"
plen=[]
plen.extend(pStr)
plen.extend(pStr1)
plen.extend(pStr2)
plen.extend(pStr3)   
random.shuffle(plen)    
print("".join(plen))
