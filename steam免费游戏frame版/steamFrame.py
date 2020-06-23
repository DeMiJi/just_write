import requests
from lxml import etree
from tkinter import *
import tkinter
from tkinter import ttk
from tkinter import messagebox

url="https://steamdb.info/upcoming/free/"
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363"}
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



        '''创建窗口'''
        steamgames = tkinter.Tk()
        steamgames.title('steam白嫖器')
        #steamgames.iconbitmap('./steamframeico.ico')


        # 创建表格对象
        '''第一个表格'''
        steam_msg_table1 = ttk.Treeview(steamgames,columns=['1','2','3','4','5'],show='headings')
        steam_msg_table1.column("1", width=100,anchor='center')
        steam_msg_table1.column("2", width=300,anchor='center')
        steam_msg_table1.column("3", width=100,anchor='center')
        steam_msg_table1.column("4", width=200,anchor='center')
        steam_msg_table1.column("5", width=200,anchor='center')

        steam_msg_table1.heading("1", text="Range")
        steam_msg_table1.heading("2", text="名字")
        steam_msg_table1.heading("3", text="状态")
        steam_msg_table1.heading("4", text="开始时间")
        steam_msg_table1.heading("5", text="结束时间")

        i = 1
        for a, b, c, d in zip(name, starts, start_time, end_time):
            list_game = []
            list_game.append(i)
            list_game.append(a)
            list_game.append(b)
            list_game.append(c)
            list_game.append(d)
            i = i + 1
            steam_msg_table1.insert("", 'end', values=(list_game))

        '''第二个表格'''
        steam_msg_table2 = ttk.Treeview(steamgames, columns=['1', '2', '3', '4','5'], show='headings')
        steam_msg_table2.column("1", width=100, anchor='center')
        steam_msg_table2.column("2", width=300, anchor='center')
        steam_msg_table2.column("3", width=100, anchor='center')
        steam_msg_table2.column("4", width=200, anchor='center')
        steam_msg_table2.column("5", width=200, anchor='center')

        steam_msg_table2.heading("1", text="Range")
        steam_msg_table2.heading("2", text="名字")
        steam_msg_table2.heading("3", text="状态")
        steam_msg_table2.heading("4", text="开始时间")
        steam_msg_table2.heading("5", text="结束时间")
        i = 1
        for a, b, c, d in zip(name_f, starts_f, start_f_time, end_f_time):
            list_game_f = []
            list_game_f.append(i)
            list_game_f.append(a)
            list_game_f.append(b)
            list_game_f.append(c)
            list_game_f.append(d)
            i = i + 1
            steam_msg_table2.insert("", 'end', values=(list_game_f))

        Label(steamgames, text="现在免费").grid(row=0,sticky=N + S + W + E)
        steam_msg_table1.grid(row=1)
        Label(steamgames, text="将要免费").grid(row=2,sticky=N + S + W + E)
        steam_msg_table2.grid(row=3)
        steamgames.mainloop()
    else:
        messagebox.showinfo("warning", html.status_code)
except:
    messagebox.showinfo("warning", "warn Internet")