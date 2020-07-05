import requests
from bs4 import BeautifulSoup

page_url = "https://pvoutput.org/intraday.jsp?id=22752&sid=20643&dt=20200601"
login_url = "https://pvoutput.org/index.jsp"
HEADER = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6",
            "Connection": "keep-alive",
            "DNT": "1",
            "Host": "pvoutput.org",
            "Referer": "",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"}

LOGINHEADER = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
               "Accept-Encoding": "gzip, deflate, br",
               "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6",
               "Cache-Control": "max-age=0",
               "Connection": "keep-alive",
               "Content-Length": "34",
               "Content-Type": "application/x-www-form-urlencoded",
               "DNT": "1",
               "Host": "pvoutput.org",
               "Origin": "https://pvoutput.org",
               "Referer": "https://pvoutput.org/",
               "Sec-Fetch-Mode": "navigate",
               "Sec-Fetch-Site": "same-origin",
               "Sec-Fetch-User": "?1",
               "Upgrade-Insecure-Requests": "1",
               "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}

def getop():
    print("正在执行getop函数！")
    r = requests.get(page_url, timeout=20)
    soup_obj = BeautifulSoup(r.content, features="html.parser")
    with open("getop.txt", "w", encoding="utf8") as fl:
        fl.write(soup_obj.prettify())

def get_with_header():
    print("正在执行get_with_header函数！")
    r = requests.get(page_url, headers=HEADER, timeout=20)
    soup_obj = BeautifulSoup(r.content, features="html.parser")
    with open("get_with_header.txt", "w", encoding="utf8") as fl:
        fl.write(soup_obj.prettify())

def login():
    print("正在执行login函数！")
    s = requests.Session()
    USERNAME, PASSWORD = ("lmwl2hl", "110120hl")
    paramdata = {"login": USERNAME, "password": PASSWORD, "remenber": "on"}
    # retry_count = 5
    # while retry_count > 0:
    #     try:
            # print("剩余尝试次数%s!" % retry_count-1)
    s.post(login_url, headers=LOGINHEADER, data=paramdata, timeout=20)
    return s
        # except Exception:
            # retry_count -= 1

    # print("获取失败!")
    # return None

def get_using_cookie(s):
    print("正在执行get_using_cookie函数！")
    r = s.get(page_url, headers=HEADER, timeout=20)
    soup_obj = BeautifulSoup(r.content, features="html.parser")
    with open("get_using_cookie.txt", "w", encoding="utf8") as fl:
        fl.write(soup_obj.prettify())


if __name__ == "__main__":
    getop()
    get_with_header()
    get_using_cookie(login())