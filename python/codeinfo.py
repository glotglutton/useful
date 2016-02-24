# -*- coding: utf-8 -*-
from __future__ import print_function
import cookielib
import urllib2
import mechanize
from bs4 import BeautifulSoup
from time import sleep
import re
import random
import sys
import json
import os


def close_open_dump_close(memberdb, fh, dbfile):
    fh.close()
    fh  = open(dbfile, 'w')
    json.dump(memberdb, fh)
    fh.close()

def innerHTML(element):
    return element.decode_contents(formatter="html")


def getinfo(udict):

    br = mechanize.Browser()
    cookiejar = cookielib.LWPCookieJar()
    br.set_cookiejar( cookiejar )
    br.set_handle_equiv( True )
    #br.set_handle_gzip( True )
    br.set_handle_redirect( True ) 
    br.set_handle_referer( True )
    br.set_handle_robots( False )

    br.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time = 1)
    br.addheaders = [ ( 'User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1' ) ]

    query           = "Python check palindrome"
    qquery          = query.replace(" ", "+")
    response        = br.open("http://stackoverflow.com/search?q="+qquery)
    soup            = BeautifulSoup(response.read(),"html.parser")

    print("==============")

    
    #links   =   soup.find_all('a', 'data-searchsession')
    url     = None
    for links in soup.find_all('a'):
        if links.has_attr('data-searchsession'):
            #print(links)
            try:
                url = links['href']
                break
            except Exception, e:
                print(str(e))

    if not url:
        print("Something went wrong for : ", query)
        exit(1)

    response    =   br.open("http://stackoverflow.com"+url)
    soup        =   BeautifulSoup(response.read(),"html.parser")
    #print(soup.prettify()[0:1000000].encode('utf-8'))
    work        =   soup.find('div', {'class': 'answer'})
    if work:
        print(query)
        for answer in work.find_all('code', text=True):
            if "\n" in answer.text or "\r" in answer.text:
                print(answer.text)
    exit(1)




if __name__ == "__main__":
    udict={"10152890277860910":"Ananda Ghosh","10206846645307753":"Srinivas Damn"}
    udict={"10103308676692190": "Yohan John", "10152890277860910":"Ananda Ghosh"}
    udict={"10152890277860910":"Ananda Ghosh", "10103308676692190": "Yohan John"}
    getinfo(udict)
