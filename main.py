import csv
import os
from tkinter import N
import unicodedata
import PySimpleGUI as sg

def left(digit, msg):
    for c in msg:
        if unicodedata.east_asian_width(c) in ('F', 'W', 'A'):
            digit -= 2
        else:
            digit -= 1
    return msg + ' ' * digit

def file_check(csv_file):
    with open(csv_file, encoding='UTF-8') as f:
        l2 = ['\ufeff"申請番号"', "作成日", "申請者", "タイトル", "ステータス", \
            "支払先名", "支払先コード", "取引先名", "取引先コード", "銀行", \
            "銀行支店", "口座種別", "口座番号", "口座名義カナ", "支払合計金額", \
            "承認者", "申請日時", "承認日時", "支払日", "ステップ1承認者", \
            "ステップ1承認日時", "ステップ2承認者", "ステップ2承認日時", \
            "ステップ3承認者", "ステップ3承認日時", "ステップ4承認者", \
            "ステップ4承認日時", "ステップ5承認者", "ステップ5承認日時", \
            "ステップ6承認者", "ステップ6承認日時", "ステップ7承認者", \
            "ステップ7承認日時", "ステップ8承認者", "ステップ8承認日時", \
            "ステップ9承認者", "ステップ9承認日時", "ステップ10承認者", \
            "ステップ10承認日時", "支払先", "発注購買申請No.	", \
            "請求書の受領方法", "請求書No.", "請求書PDF形式", "その他の添付１", \
            "その他の添付２", "納入日／利用日", "利用終了日", "支払期日", \
            "連絡事項・メモ", "仕訳の取引日"]
        reader = csv.reader(f)
        l = [row for row in reader]
        if l[0] == l2:
            return True
        else:
            return False

def count(csv_file):
    with open(csv_file, encoding='UTF-8') as f:
        d = {}
        reader = csv.reader(f)
        l = [row for row in reader]
        for row in l[1:]:
            if row[2] in d:
                if row[21] in d[row[2]]:
                    d[row[2]][row[21]] += 1
                    pass
                else:
                    d[row[2]][row[21]] = 1
            else:
                d[row[2]] = {row[21]: 1}
        return d

def simple_count(csv_file):
    with open(csv_file, encoding='UTF-8') as f:
        d = {}
        reader = csv.reader(f)
        l = [row for row in reader]
        for row in l[1:]:
            if row[2] in d:
                d[row[2]] += 1
            else:
                d[row[2]] = 1
        return d

def sum(d):
    num = 0
    for v in d.values():
        for n in v.values():
            num += n
    return num

def simple_sum(d):
    num = 0
    for v in d.values():
        num += v
    return num

def show_dict(d):
    for applicant, v in d.items():
        for authorizer, num in v.items():
            print(left(10, applicant), str(num).rjust(4), left(20, authorizer))

def format_dict(d):
    s = ''
    for applicant, v in d.items():
        for authorizer, num in v.items():
            s += ' '.join([left(10, applicant), str(num).rjust(4), \
                left(20, authorizer), '\r\n'])
    return s

def simple_format_dict(d):
    s = ''
    for applicant, num in d.items():
        s += ' '.join([left(10, applicant), str(num).rjust(4), '\r\n'])
    return s

if __name__ == '__main__':
    sg.theme('purple')

    frame = sg.Frame('',
        [
            [
                sg.Text('①『承認一覧_支払依頼.csv』を選択してください', \
                    font=('メイリオ', 12)),
            ],
            [
                sg.Text('ファイル'),
                sg.InputText('ファイルを選択', key='-INPUTTEXT-', \
                    enable_events=True),
                sg.FileBrowse(button_text='ファイル選択', font=('メイリオ', 10), \
                    size=(10, 3), key='-FILENAME-'),
            ],
            [
                sg.Text('②CSVファイルを選択したら『数える』ボタンを押してください', \
                    font=('メイリオ', 12)),
            ],
            [
                sg.Submit(button_text='数える', font=('メイリオ', 12), \
                    size=(10, 2), key='start_simple_count'),
                sg.Submit(button_text='数える\n(承認者別)', \
                    font=('メイリオ', 12), size=(10, 2), key='start_count'),
            ],
            [
                sg.MLine(font=('ＭＳ ゴシック', 12), size=(60, 22), key='-OUTPUT-'),
            ],
        ],
        size=(500, 600)
    )

    layout = [
        [
            frame
        ]
    ]

    window = sg.Window('数えるくん', layout, resizable=True)

    while True:
        event, values = window.read()

        if event is None:
            print('exit')
            break

        if values['-FILENAME-'] != '':
            if os.path.isfile(values['-INPUTTEXT-']):
                csv_path = (values['-INPUTTEXT-'])
            try:
                if not file_check(csv_path):
                    error_massage = 'ファイルのフォーマットが違うようです。'
                    sg.popup('ファイル読み込みエラー', error_massage)
            except:
                error_massage = 'ファイルのフォーマットが違うようです。'
                sg.popup('ファイル読み込みエラー', error_massage)


        if event == 'start_simple_count':
            d = simple_count(csv_path)
            s = simple_format_dict(d)
            num = simple_sum(d)
            window['-OUTPUT-'].Update(s + '\r\n合計 : ' + str(num))
            
        if event == 'start_count':
            d = count(csv_path)
            s = format_dict(d)
            num = sum(d)
            window['-OUTPUT-'].Update(s + '\r\n合計 : ' + str(num))

    window.close()