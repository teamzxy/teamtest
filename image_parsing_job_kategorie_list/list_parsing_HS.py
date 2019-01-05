import requests
from bs4 import BeautifulSoup

def get_html(url):
    """
    TODO : url을 통해 Html 받아오기
    :return: html string
    """
    html = requests.get(url)#,headers=header)
    html = html.text


    return html


if __name__ == "__main__":
    url = "https://namu.wiki/w/기자/목록"
    html = get_html(url)

    print(html)

    soup= BeautifulSoup(html, 'html.parser')

    #person_list = soup.find_all("ul",{"class": "wiki-list"})
    person_list = soup.find_all("div",{"class": "wiki-heading-content"})

    print(person_list)

    names=[]
    for person_index in person_list:
        if '황선필' in names:
            break
        for k in person_index.find_all("a",{"class":"wiki-link-internal"}):
            k=k.text.split()[0]
            if len(k)<4:
                names.append(k)
    for i in names:
        print(i)

