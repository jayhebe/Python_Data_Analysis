import requests
from bs4 import BeautifulSoup


ip_url = "http://www.net.cn/static/customercare/yourip.asp"
ip_res = requests.get(ip_url)
ip_bs = BeautifulSoup(ip_res.text, "html.parser")
ip_address = ip_bs.find("h2").text
print(ip_address)
