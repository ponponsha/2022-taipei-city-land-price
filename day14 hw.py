"""
day 13 open data
2022/4/13
Author: pengshao
"""
"""
open data source: https://data.taipei/dataset/detail?id=7ac6eac3-a998-43ff-a289-6a4e3203c2c3
note:AA45(縣市別)、AA46(行政區)、AA48(段小段)、
    AA49(00010000地號為1地號、00010001地號為1-1地號)、
    AA16(公告土地現值 元/㎡)、AA17(公告地價 元/㎡)
#### 第2題 分析數據 ######
Max, Min, Ave,  Mid 中間值, 均值......
166-CSV-環境輻射即時監測資訊歷史資料-圖表-統計.py
#### 第3題 ######
畫圖表
156-作業答案-讀取excel顯示9個圖表.py
"""
import matplotlib.pyplot as plt
import csv

# 換成中文的字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False  # 步驟二（解決座標軸負數的負號顯示問題）

##### 第1題 ######
list0=[]
list1=[]
list2=[]
list3=[]
with open('臺北市111年公告現值公告地價1.csv', 'r',encoding="utf-8") as fin:
        read = csv.reader(fin, delimiter=',')
        header = next(read)   # 讀擋頭
        # print(header)
        x=0
        for row in read:
            list0.append(int(x))                            # 第幾筆資料
            list1.append(row[1])                            # 取得 行政區 的資料
            list2.append(int(row[4])/1000)                  # 取得 公告土地現值 的資料
            list3.append(int(row[5])/1000)                  # 取得 公告地價 的資料
            x=x+1


headInfo=['縣市別','行政區','段小段','地號','公告土地現值','公告地價']
for x in range(len(header)):
        header[x] = headInfo[x]
print(f'表頭:{header}')

listDist = []                                               # district name list
for i in list1:
    if i not in listDist:
        listDist.append(i)
# print(listDist)

##### 第2題 分析數據 #####
# 1. 印出所有資料
# 2. Max, Min, Ave,  Mid 中間值, 均值......

def MidValue(listn):
    half = len(listn) // 2
    listn.sort()
    if not len(listn) % 2:
        return (listn[half - 1] + listn[half]) / 2.0
    return listn[half]

print(header[4],"最高價格:",max(list2))
print(header[4],"最低價格:",min(list2))
avg_value = 0 if len(list2) == 0 else sum(list2)/len(list2)
print(header[4],"平均價格:",avg_value)
# mid_value = MidValue(list2)
# print(header[4],"中間價格:",mid_value)

print(header[5],"最高價格:",max(list3))
print(header[5],"最低價格:",min(list3))
avg_value = 0 if len(list3) == 0 else sum(list3)/len(list3)
print(header[5],"平均價格:",avg_value)
# mid_value = MidValue(list3)
# print(header[5],"中間價格:",mid_value)


##### 3. 畫出圖表 #####
plt.subplots_adjust(top= 0.9, bottom = 0.1,hspace = 0.5)
plt.subplot(3,1,1)
plt.title(f'臺北市111年各區{header[4]} vs {header[5]} (單位:千元)')

## pic- 1 all taipei district data
plt.plot(list1, list2, 'r.',label= header[4])
plt.plot(list1, list3, 'b.',label= header[5])
plt.legend()

## pic-2 公告土地現值與公告地價差價
listDeltaPrice=[]
for l in range(len(list2)):                     # list of price deviation
    price = list2[l]-list3[l]
    listDeltaPrice.append(price)

plt.subplot(3,1,2)
plt.title('公告土地現值與公告地價差價(單位:千元)')
plt.plot(listDeltaPrice,list1 , 'g.')


## pic-3 list2 price higher than avg_value in every district
list11=[]
list21=[]
j=0
for list2[j] in list2:                          # higher than avg in list2
    if list2[j] > avg_value:
        list21.append(list2[j])
        list11.append(list1[j])                 # find out list1 is same list0 with list2
    j = j + 1

countHAvg=[]
for k in range(len(listDist)):                  # count the number of same district in list1
    dist = listDist[k]
    countHAvg.append(list11.count(dist))
# print(countHAvg)

plt.subplot(3,1,3)                              # draw pic-2
plt.title(f'各區{header[4]}大於平均的數量')
plt.bar(listDist, countHAvg,width=0.5,label= '各區數量')
plt.legend()

plt.show()




