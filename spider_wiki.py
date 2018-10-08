#/usr/bin/python
# -*- coding: utf-8 -*-
# This file has been to get host_list which were had remark from the wiki list;
# wiki http://wiki.ele.to:8090/pages/viewpage.action?pageId=108648512
#


import os
import sys
import urllib
import urllib2
from bs4 import BeautifulSoup
import logging

_http_wget = "http://wiki.ele.to:8090/pages/viewpage.action?pageId=108648512"
Path = os.getcwd()
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt='%a, %d %b %Y %H:%M:%S',filename=("%s/_EXE.log")%Path,filemode='a')
_map_result = {}

def _get_list (get_url, _map_result ):
    #headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0","Cookie":"wikiCoffeeTokenLogin=true; confluence.last-web-item-clicked=system.space.tools%2Fpermissions%2Fspacepermissions; JSESSIONID=8CB9ED347198A7D128C8314538856072; COFFEE_TOKEN=817f9acb-622e-4a63-bb80-0652628774c3"}
    headers = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0","Cookie":"COFFEE_TOKEN=""; wikiCoffeeTokenLogin=true; confluence.last-web-item-clicked=system.space.tools%2Fpermissions%2Fspacepermissions; JSESSIONID=F612A0A9E85B0CF766082E12C6D90F95; COFFEE_TOKEN=369d9309-d78c-49c0-8500-ecdeef1a3ee5"}

    url_result = urllib2.Request(url=get_url, headers = headers )
    url_open = urllib2.urlopen(url_result)
    res = url_open.read()
    #logging.debug("----%s"%res)
    #print res
    res_context = """ %s """%res
    soup = BeautifulSoup(res_context, "lxml")

    #the function match to get table;
    ##_soup_result =  soup.find('table', attrs={'class':'wrapped relative-table confluenceTable'})

    ##
    _soup_result = soup.find_all('tbody')
    #print _soup_result
    _info_list  = []
    for _match_result in _soup_result:
 
        for _result_line in _match_result:
            #print _result_line
            _lines =  _result_line.find_all('td', attrs={'class':'confluenceTd'}) 
            #print _lines 
            _count = 0
            result_list = [] 
            for  _line in _lines: 
                _count += 1
                _line = _line.text.strip()
                # find name from tables
                
                if _count == 3:
                    #print _line
                    result_list.append(_line)
                if _count == 2:
                    result_list.append(_line) 
                if _count == 4:
                    result_list.append(_line)
                if _count == 5:
                    result_list.append(_line) 
                if _count == 6:
                    print _line 
                    result_list.append(_line) 
            #print result_list 
            _info_list.append(result_list)      
    #print _info_list
    logging.debug("----%s"%_info_list)
    return _info_list
    #logging.debug("----%s"%_info_list)

def _json_object (_info_list):

    json_string = """
    {
        'all_info': {
            'host_machine': '',
            'info': [
                {
                    'name': '',
                    'lego_host': ''
                    'comment":""
                }
            ]
        }
    }
    """
    host_machine_list = []
    for  i  in _info_list:
        host_machine_list.append(i[3])
    host_matchine_list_all = list(set(host_machine_list))
    #return host_matchine_list_all
    #print host_matchine_list_all 
    for host_matchine in host_matchine_list_all:
        #print host_matchine 
        for j in _info_list:
            #print j
            if host_matchine == j[3]:
                logging.debug("----%s"%j)
                print  host_matchine,j[2], j[0],j[4]



if __name__ == "__main__":
   get_all_host =  _get_list(_http_wget,_map_result)
   #print get_all_host
   _json_object(get_all_host)