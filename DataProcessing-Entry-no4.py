# -*- coding: utf-8 -*-
import os
import csv
import numpy as np
import pandas as pd

dirname = os.getcwd()
accesslog_data = pd.read_csv(dirname + '/data/accesslog_04.csv')
botlist_data   = pd.read_csv(dirname + '/data/botlist_04.csv')

"""　集計1
「アクセスログデータ」にある、IPアドレスごとのアクセス数を集計して、
csvファイル「accesslog_0401.answer.csv」に出力してください。
"""
# 同一IPアドレスをマージしたデータフレームの作成
merge_df = accesslog_data.drop_duplicates(subset='IP_ADDRESS')
# データフレーム上に存在するIPアドレスのリストの作成
IPAddress_df = merge_df.loc[:, 'IP_ADDRESS']
IPAddress_list = IPAddress_df.values.tolist()

# IPアドレスごとのアクセス数をカウントしたリストの作成
count_list = []
for IPAddress in IPAddress_list:
    accesslog_data_bool = (accesslog_data['IP_ADDRESS'] == IPAddress)
    count_list.append(accesslog_data_bool.sum())

count_list = pd.DataFrame(count_list)

# IPアドレスとアクセス数のリストを結合したデータフレームの作成
IPAddress_df = pd.concat([IPAddress_df, count_list], axis=1)
merge_df = pd.concat([merge_df, count_list], axis=1)

# ヘッダとインデックスを削除してcsvへ書き出し
IPAddress_df.to_csv(dirname + '/data/accesslog_0401.answer.csv', header=False, index=False)
