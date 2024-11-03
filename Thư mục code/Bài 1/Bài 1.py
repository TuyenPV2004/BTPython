import requests
from bs4 import BeautifulSoup as bs
from bs4 import Comment as cm
import pandas as pd
import time

def save_File(url, begin):
    time.sleep(10)
    resp = requests.get(url)
    soup = bs(resp.content, 'html.parser')
    comments = soup.find_all(string=lambda text: isinstance(text, cm))
    len_ct = 0
    list_Check= False
    tmp = len(list_Player[0]) if list_Player else 0
    for comment in comments:
        comment_soup = bs(comment, "html.parser")
        table = comment_soup.find('table', class_='min_width sortable stats_table min_width shade_zero')
        if table:
            tbody = table.find('tbody')
            for tr in tbody.find_all('tr'):
                player = [td.text.replace(',', '') if td.find('a') is None else td.find('a').text.replace(',', '') for td in tr.find_all('td')][:-1]
                if player:
                    if len(list_Player) < 580:
                        list_Player.append(player[begin:])
                    else:
                        list_Check= True
                        len_ct = len(player)
                        for i in range(len(list_Player)):
                            if list_Player[i][0] == player[0] and list_Player[i][3] == player[3] and list_Player[i][4] == player[4]:
                                list_Player[i].extend(player[begin:])
                                break
    for i in range(580):
        if tmp == len(list_Player[i]):
            list_Player[i].extend(['N/a'] * (len_ct - begin))

list_Player = []
r = requests.get('https://fbref.com/en/comps/9/2023-2024/stats/2023-2024-Premier-League-Stats')
so = bs(r.content, 'html.parser')
list_Attribute = so.find_all('ul', class_='hoversmooth')[1].find('ul', class_='').find_all('a')

for i, link in enumerate(list_Attribute):
    if i == 2:  
        continue
    url = 'https://fbref.com' + link.get('href')
    print(url)
    save_File(url, 7 if i in (3, 4, 6, 7, 8, 10) else (8 if i == 5 else (10 if i == 1 else (11 if i == 9 else 0))))
    print(i + 1)

list_Player = [ct for ct in list_Player if int(ct[8]) > 90]
s = 'Name,Nation,Position,Team,Age,Matches played,Starts,Minutes,Assists,non-Penalty Goals,Penalty Goals,Yellow Cards,Red Cards,xG,npxG,xAG,PrgC,PrgP,PrgR,Gls,Ast,G+A,G-PK,G+A-PK,xG,xAG,xG + xAG,npxG,npxG + xAG,GA,GA90,SoTA,Saves,Save%,W,D,L,CS,CS%,PKatt,PKA,PKsv,PKm,Save%,Gls,Sh,SoT,SoT%,Sh/90,SoT/90,G/Sh,G/SoT,Dist,FK,PK,PKat,xG,npxG,npxG/Sh,G-xG,np:G-xG,Cmp,Att,Cmp%,TotDist,PrgDist,Cmp,Att,Cmp%,Cmp,Att,Cmp%,Cmp,Att,Cmp%,Ast,xAG,xA,A-xAG,KP,1/3,PPA,CrsPA,PrgP,Live,Dead,FK,TB,Sw,Crs,TI,CK,In,Out,Str,Cmp,Off,Blocks,SCA,SCA90,PassLive,PassDead,TO,Sh,Fld,Def,GCA,GCA90,PassLive,PassDead,TO,Sh,Fld,Def,Tkl,TklW,Def 3rd,Mid 3rd,Att 3rd,Tkl,Att,Tkl%,Lost,Blocks,Sh,Pass,Int,Tkl + Int,Clr,Err,Touches,Def Pen,Def 3rd,Mid 3rd,Att 3rd,Att Pen,Live,Att,Succ,Succ%,Tkld,Tkld%,Carries,TotDist,ProDist,ProgC,1/3,CPA,Mis,Dis,Rec,PrgR,Starts,Mn/Start,Compl,Subs,Mn/Sub,unSub,PPM,onG,onGA,onxG,onxGA,Fls,Fld,Off,Crs,OG,Recov,Won,Lost,Won%'
arr = s.split(',')

for ct in list_Player:
    for i in [185, 184, 183, 182, 177, 176, 175, 174, 173, 172, 169, 168, 167, 21, 15, 12, 10, 9, 5]:
        ct.pop(i)

for ct in list_Player:
    ct.append(ct[0].split()[0])  

list_Player.sort(key=lambda x: (x[-1], -int(x[4])))

for ct in list_Player:
    ct.pop()  

dataFrame = pd.DataFrame(list_Player, columns=arr)
dataFrame.to_csv('results.csv', index=False)
