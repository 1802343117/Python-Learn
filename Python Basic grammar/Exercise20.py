"""
用字典和列表保存未为JSON
"""

import json
import requests

resp = requests.get('http://api.tianapi.com/allnews/index?key=6108db9f49b44a21f43304eb78af39f6&num=10&col=7')
newslist = json.loads(resp.text)['newslist']
result = []
data = './res/data.json'
for news in newslist:
    temp_dict = {}
    temp_dict['title'] = news['title']
    temp_dict['pic_url'] = news['picUrl']
    result.append(temp_dict)
with open(data, 'w') as f:
    json.dump(result, f, ensure_ascii=False)
