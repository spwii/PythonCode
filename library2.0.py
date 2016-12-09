import requests
from bs4 import BeautifulSoup
import subprocess
import time
import http.cookiejar as cookielib


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': '',
    'Origin': '',
    'Referer': '',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    }

session = requests.Session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')
try:
    session.cookies.load(ignore_discard=True)
except:
    print("Cookie 未能加载")


def get_captcha():
    captcha_url =""
    x = 0
    bin = session.get(captcha_url, headers=headers).content
    with open("" % x, "wb")as file:
        file.write(bin)
        file.close()

    p = subprocess.Popen(["tesseract", "", ""], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    f = open("", "r")
    captcharesponse = f.read().replace(" ", " ").replace("\n", "")

    return captcharesponse


def login(xuehao):
    from_data = {
        'number': xuehao,
        'passwd': password,
        'captcha': get_captcha(),
        'select': 'cert_no',
        'returnUrl': '',
    }
    data = {
        'para_string': 'all',
        'topage': '1',
    }
    time.sleep(2)
    session.post("", data=from_data, headers=headers)
    mylib_info = session.get("", headers=headers).content.decode("UTF-8")
    book_info = session.post("", headers=headers, data=data).content.decode("UTF-8")
    book_info = BeautifulSoup(book_info, "lxml")
    mylib_info = BeautifulSoup(mylib_info, "lxml")
    book = book_info.findAll("tr")
    for i in range(1, len(book)):
        print(book[i].get_text().split("\n"))
    session.cookies.save()
if __name__ == '__main__':
    login("")
