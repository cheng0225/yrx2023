import requests

cookies = {
    'JSESSIONID': '9AFB29737CE0004A4A39F37FD9401217',
    'acw_tc': '2760776c16926072323534951e08399945a824ae21b3b87c1b201b519d6793',
    'acw_sc__v2': '64e3283740c79c027656daebf278cff218b10e22',
    'ssxmod_itna': 'eqfxni0QitG=DQKDtDXQqSA6DRDpkDymYZ7=px0HxPGzDAxn40iDtrPNORZ0rlYoWfsoReSh0xN8mlAisebZi8K3DU4i8DCdxvQ=ADYA8Dt4DTD34DYDihQGyzqBQDjxAQDjAKGaDfwtDLxi78E9DDBb45/ikDQPDyhPDIxD1=/+GDiI1DYv8Dim1D75FDQI1t95D+cbvXxi36ZDDBZG6NQuqs+9LXf5mT8oIkSOIC+pA1/830=y1fxib8aSh6cC19Z3PC7i3CT2taecDoQGed70qonGxWj/eoiiqCe4xkTDx3riodGxKIlNDDpb0iMYGDD=',
    'ssxmod_itna2': 'eqfxni0QitG=DQKDtDXQqSA6DRDpkDymYZ7=xnK35rqDsh1DLQ7nmYuo=02g4nbqOVBYdeihV06Dg0xRmDnGTAbpZ0Y0+7wbQ5=tonzaKh2NM3e1ucVmiLfkB1syF1lE6ybM27jX0fYqSLA++Soq1gEE+45C++GRf3eO7nPhjmbh+8h3phEt2gAtTQW/Cg6+zEUoV4bH1oXB9kiL08G/4+jHnpdG0pQ=/PdjQByZS+5Rbzfk5id+dMyyCz8RQMvxAIIvo38jMo7slIQwoV92q5d0wIEjyIy8A8GUpsZwqtHpVkBGMzMwnLBYesZwIZokhiqUQVG5fnp+m6OpX2YrYR0P3ry65COPo92QFejpmviNGlKXG6El2Upm+e0a9IaIYXBpAGPX0DHGu+YjY9uAlujYWIYnwYnt3nGR0Y/A7xvm3tHYWw6veCnGaWR0hiG4DQK48h+UcqYiA42+YG7EvQbD0biqAnDYrszM4Upx+rtb0PeqkODzcdUmDDFqD+cv5nDCgwR/GS+duiXPYD==',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'JSESSIONID=9AFB29737CE0004A4A39F37FD9401217; acw_tc=2760776c16926072323534951e08399945a824ae21b3b87c1b201b519d6793; acw_sc__v2=64e3283740c79c027656daebf278cff218b10e22; ssxmod_itna=eqfxni0QitG=DQKDtDXQqSA6DRDpkDymYZ7=px0HxPGzDAxn40iDtrPNORZ0rlYoWfsoReSh0xN8mlAisebZi8K3DU4i8DCdxvQ=ADYA8Dt4DTD34DYDihQGyzqBQDjxAQDjAKGaDfwtDLxi78E9DDBb45/ikDQPDyhPDIxD1=/+GDiI1DYv8Dim1D75FDQI1t95D+cbvXxi36ZDDBZG6NQuqs+9LXf5mT8oIkSOIC+pA1/830=y1fxib8aSh6cC19Z3PC7i3CT2taecDoQGed70qonGxWj/eoiiqCe4xkTDx3riodGxKIlNDDpb0iMYGDD=; ssxmod_itna2=eqfxni0QitG=DQKDtDXQqSA6DRDpkDymYZ7=xnK35rqDsh1DLQ7nmYuo=02g4nbqOVBYdeihV06Dg0xRmDnGTAbpZ0Y0+7wbQ5=tonzaKh2NM3e1ucVmiLfkB1syF1lE6ybM27jX0fYqSLA++Soq1gEE+45C++GRf3eO7nPhjmbh+8h3phEt2gAtTQW/Cg6+zEUoV4bH1oXB9kiL08G/4+jHnpdG0pQ=/PdjQByZS+5Rbzfk5id+dMyyCz8RQMvxAIIvo38jMo7slIQwoV92q5d0wIEjyIy8A8GUpsZwqtHpVkBGMzMwnLBYesZwIZokhiqUQVG5fnp+m6OpX2YrYR0P3ry65COPo92QFejpmviNGlKXG6El2Upm+e0a9IaIYXBpAGPX0DHGu+YjY9uAlujYWIYnwYnt3nGR0Y/A7xvm3tHYWw6veCnGaWR0hiG4DQK48h+UcqYiA42+YG7EvQbD0biqAnDYrszM4Upx+rtb0PeqkODzcdUmDDFqD+cv5nDCgwR/GS+duiXPYD==',
    'Origin': 'https://www.cdt-ec.com',
    'Referer': 'https://www.cdt-ec.com/notice/moreController/toMore?globleType=0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'page': '2',
    'limit': '10',
    'messagetype': '0',
    'startDate': '',
    'endDate': '',
}

response = requests.post('https://www.cdt-ec.com/notice/moreController/getList', cookies=cookies, headers=headers, data=data)
print(response, response.text)
