import math                     # 內縮會錯
import datetime

# from math import sqrt       # 用FROM,可直接用sqrt(64),
# print(sqrt(64))             # 不能用 print(math.sqrt(64))

#比較	    第一種	      第二種
#匯入方式	import math   from math import sqrt
#匯入範圍	整個模組      指定功能
#使用方式	math.sqrt()   sqrt()

#或是 import math as m

print("hello world")

NAME = "PAUL"
print(NAME)

name = input("請輸入姓名：")
print("您好，" + name)

def calculate_remain(amount, cancel_amount):
    remain_amount = amount - cancel_amount
    print("實際金額:",remain_amount)

calculate_remain(100000, 30000)

order = {
    "sono": "A20260002",
    "amount": 100000,
    "cancel_amount": 30000
}

print(order["amount"])

result = math.sqrt(100)
print(result)

today = datetime.date.today()

print(today)

#/*
#psycopg
# Python 連接 PostgreSQL
#py -m pip install "psycopg[binary]"
#py -m pip show psycopg

#openpyxl
# Python 操作 Excel
#py -m pip install openpyxl
#*/