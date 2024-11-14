# 引入模块方式一：import 语句
import statistics

print(statistics.median([19, -5, 36]))
print(statistics.mean([19, -5, 36]))

# 引入模块方式二：from...import... 语句
from statistics import median, mean

print(median([19, -5, 36]))
print(mean([19, -5, 36]))

# 引入模块方式三：from...import* 语句
from statistics import *

print(median([19, -5, 36]))
print(mean([19, -5, 36]))

# 引入第三方库 akshare 财经数据库
# 提前 pip install akshare
import akshare

# 使用 get_czce_daily 函数获取2024年2月22日中国金融期货交易所交易数据
print(akshare.get_czce_daily("20240222"))
