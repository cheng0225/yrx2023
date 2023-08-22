
import execjs
import requests


cookies = {
    'sessionid': ''
}

headers = {
    'authority': 'match2023.yuanrenxue.cn',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'referer': 'https://match2023.yuanrenxue.cn/topic/2',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}

session = requests.session()
session.headers = headers
session.cookies.update(cookies)

with open('a2js.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
ctx = execjs.compile(js_code)

s = 0
for page in range(1, 6):
    session.get('https://match2023.yuanrenxue.cn/api/loginInfo')
    response = session.get('https://match2023.yuanrenxue.cn/api/background.png')
    token = ctx.call('get_token', response.text, page)
    print(response, response.text, token)
    params = {
        'page': page,
        'token': token,
    }
    response = session.post('https://match2023.yuanrenxue.cn/api/match2023/2', params=params)
    print(response, response.text)
    s += sum(x['value'] for x in response.json()['data'])

print(s)
