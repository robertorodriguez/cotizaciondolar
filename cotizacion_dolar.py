from __future__ import print_function
from simple_get import simple_get
from bs4 import BeautifulSoup

try:
    raw_html = simple_get("https://www.precio-dolar.com.ar/")

    html = BeautifulSoup(raw_html,"html.parser")
    print (html.select(".sell strong")[0].text.replace(",",".").replace("$ ","").rstrip(),end="")
except:
    print ("0")





