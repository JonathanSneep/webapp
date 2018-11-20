# -*- coding: utf-8 -*-

import urllib2
import re
from bs4 import BeautifulSoup, ResultSet


class Item:
    def __init__(self, name, price,url_image):
        self.name = name
        self.price = price
        self.url_image=url_image


# Faking the header to make Amazon believe the request is coming from a browser muahahahaha
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

urls={("TV's","https://www.amazon.co.uk/s/?keywords=television&page=2"),
      ("Headphones","https://www.amazon.co.uk/s/?keywords=headphones&page=2"),
      ("Sat Nav","https://www.amazon.co.uk/s/?keywords=Sat%20Nav&page=2"),
      ("Smartphones","https://www.amazon.co.uk/s/?keywords=smartphone&page=2"),
      ("Laptops","https://www.amazon.co.uk/s/?keywords=laptops&page=2"),
      ("Tablets","https://www.amazon.co.uk/s/?keywords=tablets&page=2"),
      ("Cameras","https://www.amazon.co.uk/s/?keywords=cameras&page=2"),
      ("Bluetooth Speakers","https://www.amazon.co.uk/s/?keywords=Bluetooth%20Speakers&page=2"),
      }

for category,url in urls:

    response = opener.open(url)
    soup = BeautifulSoup(response.read(), 'html.parser')

    # get all item containers
    parse = soup.find_all('div', {'class': 's-item-container'})  # type: ResultSet

    for val in parse:
        name=re.search(r'title="(.*?)"', str(val))
        url_image = re.search(r'src="(.*?)"', str(val))
        price = re.search(r'£[1-9]*(,)?[0-9]*', str(val))
        if name and url_image and price:
            print name.group(0).strip("title=") + "\n"
            print url_image.group(0).strip("src=") + "\n"
            print price.group(0) + "\n"
            print "******************** \n"
