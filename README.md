## 简介
Time-Extractor的python3版本
## 功能说明
用于句子中时间词的抽取和转换, 主要基于[Time_NLP](https://github.com/zhanzecheng/Time_NLP)做了部分优化

效果如下：

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

返回结果：

    time_extractor: ['晚上8点', '上午10点']
    extract_result: {"type": "timespan", "timespan": ["2020-12-26 20:00:00", "2020-12-27 10:00:00"]}
    time_extractor: ['2020年2月28日下午4点30分29秒']
    extract_result: {"type": "timestamp", "timestamp": "2020-02-28 16:30:29"}
    time_extractor: ['36天5小时30分']
    extract_result: {"type": "timedelta", "timedelta": {"year": 0, "month": 1, "day": 6, "hour": 5, "minute": 30, "second": 0}}
    time_extractor: ['今年国庆节上午8点']
    extract_result: {"type": "timestamp", "timestamp": "2020-10-01 08:00:00"}
    time_extractor: ['下周5晚上']
    extract_result: {"type": "timestamp", "timestamp": "2021-01-01 20:00:00"}
    time_extractor: ['今天早上5点']
    extract_result: {"type": "timestamp", "timestamp": "2020-12-26 05:00:00"}
    time_extractor: ['明年初1']
    extract_result: {"type": "timestamp", "timestamp": "2021-02-12 00:00:00"}
    time_extractor: ['上个月5号半夜']
    extract_result: {"type": "timestamp", "timestamp": "2020-11-05 23:00:00"}

## 使用方式详见Test.py
python Test.py

