# 楽天レシピ見に行こう
import requests
from bs4 import BeautifulSoup

# ベースとなる楽天レシピのURL
base_url = 'https://recipe.rakuten.co.jp/search/'

Cook_Search("じゃがいも")

# 献立検索関数を作る
def Cook_Search(word):
    url = base_url + word
    re = requests.get(url)

    # スープを作る
    soup = BeautifulSoup(re.text, "lxml")

    # CSSセレクターからコピー
    elems = soup.select('#recipe_link > div.cateRankTtl') 

    # recipe_linkを取得
    links = soup(id="recipe_link")

    # レシピのリンクを取得してベースとなるURLに貼り付けするループ文
    link_list = []
    for link in links:
        link = link.get('href')
        link_list.append("https://recipe.rakuten.co.jp" + link)

    # お勧め献立タイトルを1位から順に3位まで表示するループ文
    rank = 0
    for elem in elems:
        rank += 1
        print(str(rank) + "位！")
        print(elem.getText())
        print(link_list[rank - 1])
        print("-" * 80)

'''
--------------------------------------------------------------------------------
メモ欄
--------------------------------------------------------------------------------
・食材を入力して検索（Cook_Search関数を作る）
↓
・料理のレシピを複数表示
↓
・せっかくならレシピのURLまで出力（できそう） ← わからんかった
URLの取得の場所が分かりそうで全然分からない
soup.select('href')とか('#recipe_link')じゃ全然取れなくて困った
"/recipe/1560008723/"の形で取得できれば、
"https://recipe.rakuten.co.jp"に繋げるだけでいいから簡単
（そもそも"https://recipe.rakuten.co.jp/recipe/1560008723/"の形で取れそう？）

↓
・順位付けまで出来るかな？　←　わからんかった
for i in range(1, 4):
    print("{}位！".format(i))
    print(elem.getText())
    print("-" * 80)
みたいなことはしたけど処理が3回繰り返されるだけだった
-------------------------------------------------------------------------------
5/16 更新：
    # レシピのリンクを取得してベースとなるURLに貼り付けするループ文
    for link in links:
        link = link.get('href')
        #print("https://recipe.rakuten.co.jp/recipe" + link)

        # お勧め献立タイトルを1位から順に3位まで表示するループ文
    rank = 0 # 順位付け用の変数rankを用意
    for elem in elems:
        rank += 1
        print(str(rank) + "位！")
        print(elem.getText())
        print("https://recipe.rakuten.co.jp/recipe" + link)
        print("-" * 80)

って表記にしたら順位付けとリンク貼り付けは出来た
でもURLが最後の1つだけになってしまっている

本来はlinkループ文で
https://recipe.rakuten.co.jp/recipe/recipe/1560008723/
https://recipe.rakuten.co.jp/recipe/recipe/1540004932/
https://recipe.rakuten.co.jp/recipe/recipe/1210005759/
の3つが取得出来ているはず
これをそれぞれ順番に貼り付けたい

'''

'''
以下、出力結果

https://recipe.rakuten.co.jp/recipe/recipe/1560008723/
https://recipe.rakuten.co.jp/recipe/recipe/1540004932/
https://recipe.rakuten.co.jp/recipe/recipe/1210005759/
1位！
カリフラワーとじゃがいもの豆乳スープ。
https://recipe.rakuten.co.jp/recipe/recipe/1210005759/
--------------------------------------------------------------------------------
2位！
本格っぽいけど簡単『骨付きチキンのスープカレー』
https://recipe.rakuten.co.jp/recipe/recipe/1210005759/
--------------------------------------------------------------------------------
3位！
前日から作る☆絶品ビーフシチュー
https://recipe.rakuten.co.jp/recipe/recipe/1210005759/
--------------------------------------------------------------------------------
[Finished in 1.231s]
'''

'''
感動！　寝る！
以下、出力結果
1位！
カリフラワーとじゃがいもの豆乳スープ。
https://recipe.rakuten.co.jp/recipe/1560008723/
--------------------------------------------------------------------------------
2位！
本格っぽいけど簡単『骨付きチキンのスープカレー』
https://recipe.rakuten.co.jp/recipe/1540004932/
--------------------------------------------------------------------------------
3位！
前日から作る☆絶品ビーフシチュー
https://recipe.rakuten.co.jp/recipe/1210005759/
--------------------------------------------------------------------------------
[Finished in 1.227s]
'''
