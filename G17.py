import tkinter as tk

Count_map = [0, 0, 0, 0, 0]  # 各エリアのカウント
text_vars = []  # 各エリアのテキスト変数を保存


def Plus_Click(num):
    #指定したエリアのカウントを増加させ、テキストを更新
    Count_map[num] += 1
    text_vars[num].set(Count_map[num])  # テキストを更新


def Minus_Click(num):
    #指定したエリアのカウントを減少させ、テキストを更新
    if Count_map[num] > 0:  # カウントが0未満にならないようにする
        Count_map[num] -= 1
        text_vars[num].set(Count_map[num])  # テキストを更新


def WindowMain():
    global root
    # 画面構成
    root = tk.Tk()
    root.title("G17地図 枚数管理")
    root.geometry("600x300")

    # テキスト変数を初期化
    for i in range(5):
        text_vars.append(tk.StringVar(value=str(Count_map[i])))

    # ----Widgetを設置する----
    # 地名表示
    txtOLC = tk.Label(root, text="オルコパチャ", width=12)
    txtOLC.place(x=50, y=20)
    txtKZM = tk.Label(root, text="コザマル・カ", width=12)
    txtKZM.place(x=150, y=20)
    txtYKT = tk.Label(root, text="ヤクテル樹海", width=12)
    txtYKT.place(x=250, y=20)
    txtSHA = tk.Label(root, text="シャーローニ荒野", width=12)
    txtSHA.place(x=350, y=20)
    txtHLT = tk.Label(root, text="ヘリテージファウンド", width=12)
    txtHLT.place(x=450, y=20)

    # 枚数表示(N=number)
    txtON = tk.Entry(root, textvariable=text_vars[0], font=("", 10))
    txtON.place(x=50, y=40, width=40, height=35)
    txtKN = tk.Entry(root, textvariable=text_vars[1], font=("", 10))
    txtKN.place(x=150, y=40, width=40, height=35)
    txtYN = tk.Entry(root, textvariable=text_vars[2], font=("", 10))
    txtYN.place(x=250, y=40, width=40, height=35)
    txtSN = tk.Entry(root, textvariable=text_vars[3], font=("", 10))
    txtSN.place(x=350, y=40, width=40, height=35)
    txtHN = tk.Entry(root, textvariable=text_vars[4], font=("", 10))
    txtHN.place(x=450, y=40, width=40, height=35)

    # ボタン(P=+ M=-)
    btnOP = tk.Button(root, text="追加", width=12, command=lambda: Plus_Click(0))
    btnOP.place(x=50, y=70)
    btnKP = tk.Button(root, text="追加", width=12, command=lambda: Plus_Click(1))
    btnKP.place(x=150, y=70)
    btnYP = tk.Button(root, text="追加", width=12, command=lambda: Plus_Click(2))
    btnYP.place(x=250, y=70)
    btnSP = tk.Button(root, text="追加", width=12, command=lambda: Plus_Click(3))
    btnSP.place(x=350, y=70)
    btnHP = tk.Button(root, text="追加", width=12, command=lambda: Plus_Click(4))
    btnHP.place(x=450, y=70)

    btnOM = tk.Button(root, text="削除", width=12, command=lambda: Minus_Click(0))
    btnOM.place(x=50, y=100)
    btnKM = tk.Button(root, text="削除", width=12, command=lambda: Minus_Click(1))
    btnKM.place(x=150, y=100)
    btnYM = tk.Button(root, text="削除", width=12, command=lambda: Minus_Click(2))
    btnYM.place(x=250, y=100)
    btnSM = tk.Button(root, text="削除", width=12, command=lambda: Minus_Click(3))
    btnSM.place(x=350, y=100)
    btnHM = tk.Button(root, text="削除", width=12, command=lambda: Minus_Click(4))
    btnHM.place(x=450, y=100)

    # 画面を表示する
    root.mainloop()


if __name__ == '__main__':
    WindowMain()