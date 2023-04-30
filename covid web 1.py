import requests
from bs4 import BeautifulSoup
  
  
def getdata(url):
    r = requests.get(url)
    return r.text
  
htmldata = getdata("https://covid-19tracker.milkeninstitute.org/")
soup = BeautifulSoup(htmldata, 'html.parser')
result = str(soup.find_all("div", class_="is_h5-2 is_developer w-richtext"))
  
print("NO 1 " + result[46:86])
print("NO 2 "+result[139:226])
print("NO 3 "+result[279:305])
print("NO 4 "+result[358:375])
print("NO 5 "+result[428:509])
