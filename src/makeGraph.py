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


#ファイル名を，'~の文字列を含むもの'で指定する．
#stringで指定された文字列を含むファイルをcsv_file_wantedに入れる
print ("Input a string included in file names: ", end="")
string = input()
csv_files_wanted = glob.glob("*" + string + "*.csv")

if len(csv_files_wanted) == 0:
    print("There is no such csv file.")
    exit(0)
elif len(csv_files_wanted) > 4:
    print("Many files matched. ")
    for csv_file_wanted in csv_files_wanted[0:3]:
        print(csv_file_wanted )
    print("and more are selected. Go to next? (yes/no) : ", end="")
    while True:
        reply = input()
        if reply == "no":
            exit(0)
        elif reply == "yes":
            break
        else:
            print("Input 'yes' or 'no': ", end="")

for csv_file_wanted in csv_files_wanted:
    print(" - " + csv_file_wanted)
print()

# csvファイルに含まれるカラムも同様に文字列一致で選ぶ
first_csv_file = pd.read_csv(csv_files_wanted[0], header=0)
column_names_exist = first_csv_file.columns.values
x_axis = ""
# 当てはまるものがなければ終了
# 当てはまるものが複数あればさらに絞り込む
print ("Select x-axis: ", end="")
while True:
    string = input()
    applied_columns = 0

    for column_name in column_names_exist:
        if string in column_name:
            x_axis = column_name.strip()
            applied_columns+=1

    if applied_columns == 0:
        print("No such column.")
        print("Input another string: ", end="")
    elif applied_columns > 1:
        print("There are some columns fitted.")
        print("Input unique string: ", end="")
    elif applied_columns == 1:
        break
    else:
        exit(0)
print(" X-axis: " + x_axis)
print()

# y軸も同様に選ぶ．こちらは複数選べるようにする．
y_axes=[]
while True:
    print("Select y-axes: ", end="")
    string = input()
    if string == "":
        break

    y_axis = ""
    applied_columns = 0

    for column_name in column_names_exist:
        if string in column_name:
            y_axis = column_name
            applied_columns+=1

    if applied_columns == 0:
        print("No such column.")
        print("Input another string: ", end="")
    elif applied_columns > 1:
        print("There are some columns fitted.")
        print("Input unique string: ", end="")
    elif applied_columns == 1:
        y_axes.append(y_axis)
    else :
        exit(0)

print(" Y-axes: " + str(y_axes))
print()

print("Writing now...")

# TODO: グラフの描画
# TODO: ちゃんと整形するのと，指定したy_axesのすべてについて出力できるようにする．
try:
    # csvファイルの取り込み
    dfs    = []
    labels = []
    for file in csv_files_wanted:
        index = file.find(r',')
        labels.append(file[0:index])
        dfs.append(pd.read_csv(file, header=0))

    # グラフの描画
    for y_axis in y_axes:
        font = {'family': 'Times New Roman'}
        mpl.rc('font', **font)

        plt.style.use('ggplot')
        plt.rcParams["font.size"] = 16
        plt.rcParams['xtick.direction'] = 'in'  # x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
        plt.rcParams['ytick.direction'] = 'in'  # y軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
        plt.axes( facecolor = "#FFFFFF" )

        ax = plt.gca()
        ax.spines['bottom'].set_color('#000000')
        ax.spines[ 'left' ].set_color('#000000')
        ax.yaxis.grid(True, which='major', linestyle='-', color='#CFCFCF')

    #    plt.hold(True)

        i = 0
        for df in dfs:
            plt.plot(df[x_axis], df[y_axis], label = labels[i])
            i += 1

        plt.title (y_axis)
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)

        plt_legend = plt.legend(shadow = False, loc = 'lower right', frameon = True, fontsize = 16, numpoints = 1, facecolor = "#FFFFFF")
        plt_legend.get_frame().set_edgecolor('#000000')

        x_limit = df[x_axis].values[-1]
        plt.xlim(0, x_limit)
        plt.ylim(0)

        lambda_num = ""
        lambda_num = re.search("λ=[0-9.]+", csv_files_wanted[0]).group()
        plt.savefig('result_' + lambda_num +"_" + y_axis.strip() + '.eps')
#        plt.show()
        plt.close()

    # TODO: 出力したグラフを自動で保存させる
except :
    exit(0)