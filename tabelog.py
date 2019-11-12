#!/usr/bin/env python
# coding: utf-8

import re
import copy
import requests
from bs4 import BeautifulSoup
import templates

class Tabelog:
    """
    食べログスクレイピングクラス。場所とキーワードと条件からランキング順に10件表示。
    """
    def __init__(self, place, keyword, max_price = 5000, max_check_page = 5):
        self._count = 0 #表示する店の数
        self._page = 5 #検索するページ数
        self._max_contents = 10 #検索する店の最大数
        self.param ={"sa": place, "sk": keyword} #検索する地名とキーワード
        self.max_price = max_price #表示するお店の最大金額。デフォルト5000円
        self.max_check_page = max_check_page #検索する最大ページ数。デフォルト5ページ
        self.return_json = templates.carousel()
        
    def start(self):
        #検索する地名とキーワードでランキング順に並べて初期化。検索できなかったらエラーを返す。
        try:
            soup = self.setup()
        except:
            self.return_json = "エラーです。最初は地名を入れてください。"
            return self.return_json
        #1ページ目で条件に合うものを表示
        self.select_store(soup)
        #検索する店の最大数に行くまで検索
        while self._count < self._max_contents and self._page <= self.max_check_page:
            #print("self._count:"+str(self._count))
            self.re_select(soup)
        if self.return_json == templates.carousel():
            self.return_json = "エラーです。最初は地名を入れてください。"
        return self.return_json

    def setup(self):
        html_doc = requests.get('https://tabelog.com/rst/rstsearch/', params = self.param).content
        #print(html_doc.url)
        soup = BeautifulSoup(html_doc, 'html.parser') # BeautifulSoupの初期化
        #ランチは最初からソートされたページに飛ぶっぽいのでtry
        try:
            sorted_pages = soup.find("a",{"class": "navi-rstlst__label navi-rstlst__label--rank"})
            html = requests.get(sorted_pages["href"]).content
            #print(requests.get(sorted_pages["href"]).url)
            soup = BeautifulSoup(html, 'html.parser') # BeautifulSoupの初期化
        except:
            pass
        return soup
    
    def re_select(self, soup):
        #10件集まるか、規定ページ数見た最大件数まで検索する
        try:
            soup.find("a",{"class": "c-pagination__num"}).text
        except AttributeError:
            self._page = 100
            return  
        
        check_pages = soup.find_all("a",{"class": "c-pagination__num"}) 
        for check_page in check_pages:
            if check_page.text == str(self._page) and self._page <= self.max_check_page:
                html = requests.get(check_page["href"]).content
                soup = BeautifulSoup(html, 'html.parser')
                #print(check_page["href"])
                self.select_store(soup)
                self._page += 1
                if self._count >= self._max_contents or self._page >= self.max_check_page:
                    break  

    def select_store(self, soup):
        #実作業
        tags =soup.find_all("div",{"class": "list-rst__wrap js-open-new-window"}) 
        #print(tags)
        for tag in tags:
            if self._count < self._max_contents:
                flag= True #最大予算フラグ
                budgets = tag.find_all("li",{"class": "c-rating c-rating--s list-rst__budget-item"})
                for budget in budgets:
                    budget_text = budget.text.split()[0]
                    pat = r'[0-9]+' #抽出するパターン：数字
                    num = budget_text.replace(",","")
                    price_list = re.findall(pat, num)  #数字を抽出してリスト化
                    for price in price_list:
                        if int(price) >= self.max_price:
                            flag = False
                            break

                if flag == True:
                    #カウント1以上の時にリストコピーを作る
                    if self._count >=1:
                        self.return_json["contents"]["contents"].append(copy.deepcopy(self.return_json["contents"]["contents"][0]))
                    self.return_json["contents"]["contents"][self._count]['hero']['url'] = tag.img["data-original"] #画像
                    self.return_json["contents"]["contents"][self._count]['body']['contents'][0]['text'] = tag.a.text #店名
                    self.return_json["contents"]["contents"][self._count]['hero']['action']['uri'] = tag.a["href"] #リンク
                    self.return_json["contents"]["contents"][self._count]['footer']['contents'][0]['action']['uri'] = tag.a["href"] #リンク
                    self.return_json["contents"]["contents"][self._count]['body']['contents'][2]['contents'][0]['contents'][1]['text'] = tag.find("span",{"class": "list-rst__area-genre cpy-area-genre"}).text.replace(" / ","\n") #場所
                    try: #評価
                        rating = tag.find("span",{"class": "c-rating__val c-rating__val--strong list-rst__rating-val"}).text
                        self.return_json["contents"]["contents"][self._count]['body']['contents'][1]['contents'][5]['text'] = "評価:" +  rating
                    except AttributeError:
                        self.return_json["contents"]["contents"][self._count]['body']['contents'][1]['contents'][5]['text'] = "評価なし"

                    try: #星の数。デフォ4つ
                        if float(rating) >4.0:
                            self.return_json["contents"]["contents"][self._count]['body']['contents'][1]['contents'][4]['url'] = 'https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png'
                        if float(rating) <3.5:
                            self.return_json["contents"]["contents"][self._count]['body']['contents'][1]['contents'][3]['url'] = 'https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png'
                            if float(rating) <3.0:
                                self.return_json["contents"]["contents"][self._count]['body']['contents'][1]['contents'][2]['url'] = 'https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png'
                                if float(rating) <2.5:
                                    self.return_json["contents"]["contents"][self._count]['body']['contents'][1]['contents'][1]['url'] = 'https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png'
                    except: #評価なしを想定
                        for i in range(4):
                            self.return_json["contents"]["contents"][self._count]['body']['contents'][1]['contents'][i]['url'] = 'https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png'
                
                    budget_list = [budget.text.split()[0] for budget in budgets] #予算
                    self.return_json["contents"]["contents"][self._count]['body']['contents'][2]['contents'][1]['contents'][1]['text'] ='\n'.join(budget_list)           
                    try:
                        self.return_json["contents"]["contents"][self._count]['body']['contents'][2]['contents'][2]['contents'][1]['text'] = tag.find("span",{"class": "list-rst__holiday-datatxt cpy-holiday-datatxt"}).text #定休日
                    except AttributeError:
                        self.return_json["contents"]["contents"][self._count]['body']['contents'][2]['contents'][2]['contents'][1]['text'] = "不明"
                    #self.return_text += "\n"
                    self._count += 1