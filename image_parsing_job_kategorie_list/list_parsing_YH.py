#import urllib.request
import requests
import codecs
from bs4 import BeautifulSoup


def get_html_from(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
    html = requests.get(url,headers=header)
    html = html.text
    singer_parse= BeautifulSoup(html, 'html.parser')
    """ 
    TODO : url을 통해 Html 받아오기
    :return: html string
    """
    return html

if __name__ == "__main__":
    url = "https://namu.wiki/w/레이싱 모델/목록"
    html = get_html_from(url)
    singers_parse = BeautifulSoup(html,'html.parser')
    link1 = singers_parse.find_all("div",{"class":"wiki-content clearfix"})
    names=[]
    for area in link1:
        for v in area.find_all():
            for b in v.find_all("li")[2:]:
                names.append(b.text.split('[')[0])
    for x in names:
        print(x)