import requests
import re 
data="10.10.20.30"
#data=requests.get("https://csed.thapar.edu/faculty").text 
pattern = r"^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$"
p=r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$'
m=re.finditer(pattern,data)
for each in m:
    if each:
        print(each.group())
    else:
        print("no Record Found")
