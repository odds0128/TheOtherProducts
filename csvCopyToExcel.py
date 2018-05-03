#! python3
#  csvCopyToExcel.py ... 選択したcsvファイルの内容をクリップボードにコピーする
import openpyxl, sys, os, csv, pyperclip, re

# 最初は簡単にコマンドライン引数のファイル名のcsvをクリップボードにコピーするだけにする


# コマンドライン引数を取得
#  引数として，ファイル名の後に数字をスペース区切りで打て，
#       その数字で指定された列だけとってくるようにする

# 引数が一つもない(ファイル名の指定すらない場合)
if len(sys.argv) < 2:
    print("csvファイル名を一つだけ指定してください")

# 引数がある場合
else:
    # 一番はじめの引数がファイル名
    path = sys.argv[1]
    try:
        csv_file = open(path)
        csv_content = csv_file.read()
        lines = re.split('[,\n]', csv_content)
    except:
        print("そのようなファイルはありません")

    columns = 0
    for i in range(len(lines)):
        if (lines[i] == " "):
            columns = i
            break

    # ファイル名の指定と列数の指定がある時
    if len(sys.argv) > 2:
        columns_needed = sys.argv[2:]
        # csvをエクセルに貼り付けられる形式に変換
        # 指定があればその列だけ
        # 指定がなければ全体を変換

        strategy_name = path.split(",")
        text = '{0}\n'.format(strategy_name[0])

        if columns_needed[0] == "all":
            # columns+1個目が改行文字なので読み飛ばす意味で "columns + 1"
            for i in range(0, len(lines) - 1, columns + 1):
                # 列数 - 1 をタブでくっつける
                for j in range(columns - 1):
                    text = '{0}{1}\t'.format(text, lines[i + j])
                # 最後の列の後ろにだけ改行を入れる"
                text = '{0}{1}\n'.format(text, lines[i + columns - 1])
        else:
            print("Copied ", end="")
            for i in columns_needed:
                print("\"{0}\", ".format(lines[int(i)]), end="")
            print(" column(s)")
            # columns+1個目が改行文字なので読み飛ばす意味で "columns + 1"
            for i in range(0, len(lines) - 1, columns + 1):
                # 指定された列たちをタブでくっつける
                for j in columns_needed[0:(len(columns_needed) - 1)]:
                    text = '{0}{1}\t'.format(text, lines[i + int(j)])
                # 最後の列の後ろにだけ改行を入れる"
                text = '{0}{1}\n'.format(text, lines[i + int(columns_needed[-1])])

        pyperclip.copy(text)


    # 列数の指定がないときはその列の内容とともに入力を促すメッセージを出す
    else:
        print("列数を指定してください.")

        print("指定の文字と指定できる列は")
        for i in range(columns):
            print("{0}:\"{1}\", ".format(i, lines[int(i)]))
        print("all: 全体")
        print("です．")

