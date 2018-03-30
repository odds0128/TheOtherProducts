#! python3
# cleanTedTranscript.py - クリップボードにコピーしたTedのTranscriptを見やすく直すプログラム
# Ted ... https://www.ted.com/

"""
wordで作業することを想定して改行文字"¥r"で出力している
環境に応じて適した改行文字を使うこと

"""

import pyperclip, re

parenthesis_regex = re.compile(r'(\(.*\))?')       # 括弧で括られた文章の正規表現
time_regex        = re.compile(r'(\d\d\:\d\d)?')   # 時刻の正規表現

text = pyperclip.paste()    # クリップボードの内容をstringで保持
print(len(text))

lines = text.split('\n')    # textの内容を改行文字で区切ってリストとして保存
line_num = len(lines)
new_lines = []

# 以下で各行(リスト"lines"の各要素)について操作
for line in lines :
    line = line.strip()
    line = parenthesis_regex.sub('', line)  # ()で囲まれた部分の削除
    # 空行, もしくは時刻だけ,括弧だけの行を排除した上で，文章の行の最初をインデントする．
    if len(time_regex.search(line).group()) == 0 and len(line) > 0 :
        new_lines = new_lines + [r' '*2 + line]    # 空白文字2つ分でインデント

text = '\r'.join(new_lines)
print(len(text))

pyperclip.copy(text)
