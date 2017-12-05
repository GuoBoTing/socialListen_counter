import requests
import json
import pandas as pd

#token
print('Please enter the token from Facebook: ')
token = input()
print('Please enter the fanpage id: ')
fanpage_id = input()
#send request
res = requests.get('https://graph.facebook.com/v2.8/{}/posts?limit=100&access_token={}'.format(fanpage_id,token))
id_counter = {}
#iterate all the data from res and withdraw the ip
# while 'paging' in res.json():
for post in res.json()['data']:
    post_id = post['id']
    while 'paging' in res_post.json():
        res_post = requests.get('https://graph.facebook.com/v2.8/{}/reactions?limit=1000&access_token={}'.format(post_id, token))
        for reaction in res_post.json()['data']:
            reaction_id = reaction['id']
            id_counter.setdefault(reaction_id, 0)
            id_counter[reaction_id] = id_counter[reaction_id]+1
        if 'next' in res_post.json()['paging']:
            res_post = requests.get(res_post.json()['paging']['next'])
        else:
            break
    # if 'next' in res.json()['paging']:
    #     res = requests.get(res.json()['paging']['next'])
    # else:
    #     break

s = pd.Series(id_counter, name='次數')
s.index.name = 'id'
df = pd.DataFrame(s, columns=['次數'])
print(df)
df.to_csv('haha.csv')
