import pandas as pd

from cos_sim_sort import cos_sim_sort
from csv_reader import csv_reader

user_data = pd.read_csv("data/用户需求信息.csv")
map_data = pd.read_csv("data/地图类型.csv")

# 用csv_reader()方法进行数据初始化
user_list = csv_reader(user_data)
map_list = csv_reader(map_data)

# 将用户兴趣OneHot特征矩阵与商品OneHot特征举证进行余弦相似度计算并排序
sorted_sim_lis = cos_sim_sort(user_list, map_list)

# 输出排好序的推荐结果
for i, v in enumerate(sorted_sim_lis):
    print(user_data["用户名称"][i])
    print(v)





