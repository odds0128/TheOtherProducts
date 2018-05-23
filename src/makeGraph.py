#! Python3
# makeGraph.py - 2種類のコマンドライン引数をとり，指定されたファイル名の指定された絡むからグラフを作成する
import glob

import pandas as pd
import numpy as np
import pydotplus
import matplotlib as mpl
import matplotlib.pyplot as plt
import re
import sys
from graphviz import Digraph


# ディレクトリ内のcsvファイルをindex付きで列挙する．
csv_files_exist = glob.glob("*.csv")
if len(csv_files_exist) == 0:
    print( "カレントディレクトリにcsvファイルはありません．" )
    exit(0)
else:
    print( "このディレクトリには" )
    for i in range( len(csv_files_exist) ):
        print( "{0:2d}: ".format(i) + csv_files_exist[i])
    print("が含まれます．")


#その中からファイルをいくつか指定し，空白でenterが入力されたら入力の終わりと判断する
print('ファイルを数字で指定してください．')

csv_files_wanted=[]
while(True):
    tmp = input(">>")
    if tmp == "":
        break
    else:
        file_number = int(tmp)
        if csv_files_exist[file_number] in csv_files_wanted:
            print("そのファイルはすでに指定されています")
        elif file_number >= 0 and file_number < len(csv_files_exist):
            csv_files_wanted.append(csv_files_exist[file_number])
        else:
            print("上記のファイルから選んでください")

if len(csv_files_wanted) == 0:
    print("1つ以上のファイルを指定してください")
    exit(0)

for fn in csv_files_wanted:
    print(fn)
print("からグラフを作成します．")
print()


#csvファイルに含まれるカラムを上と同様に表示し，選ばせる
first_csv_file       = pd.read_csv(csv_files_exist[0], index_col=1)
column_names_exist   = first_csv_file.columns.values

print("ファイルには")
try:
    for i in range( len(column_names_exist) ):
        column_name = column_names_exist[i].strip()
        if len(column_name) > 0:
         print("{0:2d}: ".format(i) + column_name)
    print("が含まれます．")
except:
    print("有効なカラムが含まれていません．")
    exit(0)

print('x軸にするカラムを選択してください．')
x_axis = 0

while(True):
    tmp = input(">>")
    if tmp == "":
        print("x軸にするカラムを選択してください")
    else:
        column_number = int(tmp)
        if column_number >= 0 and column_number < len(column_names_exist):
            x_axis = column_names_exist[column_number]
            break
        else:
            print("上記のカラムから選んでください")

print('y軸にするカラムを選択してください．')
y_axis = []

while(True):
    tmp = input(">>")
    if tmp == "":
        break
    else:
        column_number = int(tmp)
        if column_names_exist[column_number] in y_axis:
            print("そのカラムはすでに指定されています")
        elif column_number >= 0 and column_number < len(csv_files_exist):
            y_axis.append(column_names_exist[int(column_number)])
        else:
            print("上記のファイルから選んでください")
if len(y_axis) == 0:
    print("1つ以上のカラムを指定してください")
    exit(0)

print("x: " + x_axis)
print("y: ")
for y in y_axis:
    print("   {0}".format(y))
print("のグラフを作成します．")
print()



#TODO: グラフの描画
#TODO: ちゃんと整形するのと，指定したy_axisのすべてについて出力できるようにする．
try:
    mpl.use('Agg')
    dfs = []
    for file in csv_files_wanted:
        dfs.append( pd.read_csv(file, index_col=1))

    plt.style.use('ggplot')
    font={'family':'Times New Roman'}
    mpl.rc('font', **font)


    plt.hold(True)
    for df in dfs:
        plt.plot( df[x_axis], df[y_axis[0]], label = y_axis[0] )
    plt.title(y_axis[0])
    plt.xlabel(x_axis)
    plt.ylabel(y_axis[0])
    plt.legend()
    plt.xlim(0)
    plt.ylim(0)
    plt.show()

    #TODO: 出力したグラフを自動で保存させる
    # plt.savefig('result')
except:
     print("グラフの作成に失敗しました．")
