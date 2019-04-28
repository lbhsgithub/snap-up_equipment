import requests
import random


def download_verification_code (cookie):
    post_addr = "http://xx.xxx.xxx.xxx/image"
    post_header = {
            'Host': 'xx.xxx.xxx.xxx',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
            'Accept': 'image/webp,*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Cookie': 'JSESSIONID='+cookie+''
            }
    result = requests.get(post_addr, headers=post_header, params=str(random.uniform(0, 10)/10))
    with open('./code.jpeg', 'wb') as file:
        file.write(result.content)


def post_dayi(code, time_start, time_end, cookie, bookid):
    post_addr = "http://xx.xxx.xxx.xxx/ajax/orderSave.action"
    post_header = {
        'Host': 'xx.xxx.xxx.xxx',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
        'Accept': 'application/json, text/javascript, */*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',  # post提交数据的格式
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'Cookie': 'JSESSIONID=' + cookie + '; lab=xxxxxxxxxxxxxxxxx; type=1'
    }
    post_data = {
        'equipId': 'xxxxxxxxxxxxxx',   # just a clerical error Id not id, 1 need compare fuction 2 believe logic, less idle work
        'startDate': time_start,
        'endDate': time_end,
        'content': 'scan',
        'noMerge': 'false',
        'operatorType': '3',
        'userno': '',
        'validate': code,
        'bookId': bookid
    }
    # history：from urllib.parse import urlencode, 不需要urlencode(post_data)了。。
    return requests.post(post_addr, data=post_data, headers=post_header)


if __name__ == "__main__":
    pass
    # requests库：你的数据字典在发出请求时会自动编码为表单形式。一开始连这个都不知道。和规范一样，对官方文档的解读
