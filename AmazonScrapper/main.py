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

urls={("TV's","https://www.amazon.co.uk/s/ref=lp_560864_pg_2?rh=n%3A560798%2Cn%3A%21560800%2Cn%3A560858%2Cn%3A560864&page=2&ie=UTF8&qid=1542053541"),
      ("Headphones","https://www.amazon.co.uk/s/ref=lp_4085751_pg_2?rh=n%3A560798%2Cn%3A%21560800%2Cn%3A1345741031%2Cn%3A560882%2Cn%3A4085731%2Cn%3A4085751&page=2&ie=UTF8&qid=1542053619"),
      ("Sat Nav","https://www.amazon.co.uk/s/ref=lp_389515011_pg_2?rh=n%3A560798%2Cn%3A%21560800%2Cn%3A389514011%2Cn%3A389515011&page=2&ie=UTF8&qid=1542053655"),
      ("Smartphones","https://www.amazon.co.uk/s/ref=lp_356496011_pg_2?rh=n%3A560798%2Cn%3A%21560800%2Cn%3A1340509031%2Cn%3A5362060031%2Cn%3A356496011&page=2&ie=UTF8&qid=1542053713"),
      ("Laptops","https://www.amazon.co.uk/s/ref=lp_429886031_pg_2?rh=n%3A340831031%2Cn%3A%21340832031%2Cn%3A429886031&page=2&ie=UTF8&qid=1542053693"),
      ("Tablets","https://www.amazon.co.uk/s/ref=lp_429892031_pg_2?rh=n%3A340831031%2Cn%3A%21340832031%2Cn%3A429892031&page=2&ie=UTF8&qid=1542053695"),
      ("Cameras","https://www.amazon.co.uk/s/ref=lp_430660031_pg_2?rh=n%3A560798%2Cn%3A%21560800%2Cn%3A560834%2Cn%3A560836%2Cn%3A430660031&page=2&ie=UTF8&qid=1541532920"),
      ("Bluetooth Speakers","https://www.amazon.co.uk/s/ref=s9_acsd_dnav_bw_ct_x_ct00__w?node=560798,!560800,4085821,4085831,4085881&search-alias=electronics&field-is_prime=419159031&field-feature_keywords_two_browse-bin=2954019031&bbn=4085881&pf_rd_m=A3P5ROKL5A1OLE&pf_rd_s=merchandised-search-2&pf_rd_r=PAJDDYDCNNZTZ7S6K1T4&pf_rd_t=101&pf_rd_p=641de4a8-3633-4e88-a6f8-67e9130be8b5&pf_rd_i=4085831"),
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





