#!/usr/bin/python
# Filename: crawl.py
from bs4 import BeautifulSoup
from urlparse import urljoin
import requests
import csv
import urllib2, sys

url = "http://www.dianping.com/member/20910295/wishlists?pg={page}&favorTag=s10_c-1_t-1"

page = 0

csv_file = open("rent.csv","wb")
csv_writer = csv.writer(csv_file, delimiter=',')

while page < 5:
    page += 1
    site = url.format(page=page)
    print "fetch: ",site
    response = requests.get(site)
    hdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req = urllib2.Request(site, headers=hdr)
    pageopen = urllib2.urlopen(req)
    html = BeautifulSoup(pageopen,"html.parser")

    house_list = html.select(".txt")

    if not house_list:
        break

    for house in house_list:
        title = house.select("h6")
        if not title:
            continue
        house_title = title[0].string.encode("utf8")
        house_url = urljoin(url, house.select("a")[0]["href"])
        house_adress = house.select("p")[0].contents[2].encode("utf8")
        house_info_list = house_title.split()

        #    house_location = house_info_list[0]
        #else:
        #    house_location = house_info_list[1]

        #house_money = house.select("
        #csv_writer.writerow([house_title, house_location, house_money, house_url])

        csv_writer.writerow([house_title,house_url,house_adress])
    print "page is:",page
csv_file.close()