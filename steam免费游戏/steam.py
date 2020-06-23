from urllib import response

import requests
from lxml import etree
import json
from fake_useragent import UserAgent


url="https://steamdb.info/upcoming/free/"
#headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363"}
headers = {'User-Agent': UserAgent().random}#采用随机的请求头防止被服务器搬掉
try:
    html=requests.get(url,headers=headers)
    if html.status_code == 200:
        dom = etree.HTML(html.text)
        '''寻找第一个table里的信息'''
        name = dom.xpath('//table[1]//a/b/text()')
        starts = dom.xpath('//table[1]//td[4]//text()')
        '''因为状态里keep是b元素里的这个td里还有其他的元素，那个原数为空的，所以用一个循环来删除空'''
        for i in starts:
            if i ==' ':
                starts.remove(i)
        start = dom.xpath('//table[1]//td[5]/@title')
        end = dom.xpath('//table[1]//td[6]/@title')
        '''处理时间格式'''
        start_time = [c.replace('T','-')[:-9]for c in start]
        end_time = [c.replace('T', '-')[:-9] for c in end]
        '''将数据转换为json格式'''
        list_game=[]
        for a,b,c,d in zip(name,starts,start_time,end_time):
            dict_game = {}
            dict_game['name'] = a
            dict_game['starts'] = b
            dict_game['start_time'] = c
            dict_game['end_time'] = d
            list_game.append(dict_game)
        '''储存json格式'''
        filename = 'steam_free_games_now.json'
        with open(filename, 'w') as file_obj:
            json.dump(list_game, file_obj)

        '''抓取即将到来的免费游戏'''
        name_f = dom.xpath('//table[2]//a/b/text()')
        starts_f = dom.xpath('//table[2]//td[4]//text()')
        for i in starts_f:
            if i ==' ':
                starts_f.remove(i)
        start_f = dom.xpath('//table[2]//td[5]/@title')
        end_f = dom.xpath('//table[2]//td[6]/@title')
        '''处理时间格式'''
        start_f_time = [c.replace('T', '-')[:-9] for c in start_f]
        end_f_time = [c.replace('T', '-')[:-9] for c in end_f]
        '''将数据转换为json格式'''
        list_game_f = []
        for a, b, c, d in zip(name_f, starts_f, start_f_time, end_f_time):
            dict_game = {}
            dict_game['name'] = a
            dict_game['starts'] = b
            dict_game['start_time'] = c
            dict_game['end_time'] = d
            list_game_f.append(dict_game)
        '''储存json格式'''
        filename_f = 'steam_free_games_furture.json'
        with open(filename_f, 'w') as file_obj:
            json.dump(list_game_f, file_obj)

        '''显示数据'''
        print('现在免费')
        with open(filename) as f:
            now_game_datas = json.load(f)
        for now_game_data in now_game_datas:
            now_name = now_game_data['name']
            now_starts = now_game_data['starts']
            if now_starts == 'keep':
                now_starts = '永久入库'
            else:
                now_starts = '限时入库'
            now_start = now_game_data['start_time']
            now_ned = now_game_data['end_time']
            print('名字：'+now_name+'  状态：'+now_starts+'  开始时间：'+now_start+'  结束时间：'+now_ned)
        print('将来免费')
        with open(filename_f) as f:
            f_game_datas = json.load(f)
        for f_game_data in f_game_datas:
            f_name = f_game_data['name']
            f_starts = f_game_data['starts']
            if f_starts == 'keep':
                f_starts = '永久入库'
            else:
                f_starts = '限时入库'
            f_start = f_game_data['start_time']
            f_ned = f_game_data['end_time']
            print('名字：'+f_name+'  状态：'+f_starts+'  开始时间：'+f_start+'  结束时间：'+f_ned)
    else:
        print(html.status_code)
except:
    print('error')