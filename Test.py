# -*- coding: utf-8 -*-
"""
# @Time    : 2020/5/15 9:47
# @Author  : xiaoxiong
# @Email   : xyf_0704@sina.com
# @File    : Test.py
# @Software: PyCharm
# DESC :
"""

import warnings
from TimeNormalizer import TimeNormalizer # 引入包
warnings.filterwarnings("ignore")

tn = TimeNormalizer()

res = tn.parse(target=u'晚上8点到上午10点之间') # target为待分析语句，timeBase为基准时间默认是当前时间
print("extract_result:", res)
res = tn.parse(target=u'2020年二月二十八日下午四点三十分二十九秒') # target为待分析语句，timeBase为基准时间默认是当前时间
print("extract_result:", res)
res = tn.parse(target=u'预计耗时36天5小时30分') # target为待分析语句，timeBase为基准时间默认是当前时间
print("extract_result:", res)
res = tn.parse(target=u'今年国庆节上午8点') # target为待分析语句，timeBase为基准时间默认是当前时间
print("extract_result:", res)
res = tn.parse(target=u'下周五晚上') # target为待分析语句，timeBase为基准时间默认是当前时间
print("extract_result:", res)
res = tn.parse(target=u'今天早上5点')  # target为待分析语句，timeBase为基准时间默认是当前时间
print("extract_result:", res)
res = tn.parse(target=u'明年大年初一')
print("extract_result:", res)
res = tn.parse(target=u'上个月5号半夜')
print("extract_result:", res)
