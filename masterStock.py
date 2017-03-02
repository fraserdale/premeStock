import requests
from bs4 import BeautifulSoup
import json

def loadMasterStock():
	url = "http://www.supremenewyork.com/mobile_stock.json"
	user = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1"}
	# user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"}
	r = requests.get(url, headers=user)
	masterStock = json.loads(r.text)
	with open("masterstock.txt", 'w') as outfile:
		json.dump(masterStock, outfile, indent=4, sort_keys=True)

	print("Saved to masterstock.txt")

if __name__ == '__main__':
	loadMasterStock()