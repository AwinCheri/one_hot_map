
import pandas as pd


def csv_reader(general_data):

    # 创建一个list数组拼接保存每次temp数组保存的一套OneHot编码
    feature_list = []

    # 获取文件列名
    columns = general_data.columns.tolist()
    # 获取第 3 列之后的表头标题
    headers_after_3 = columns[3:]
    # 删除标题的最后两个字节
    headers = [title[:-2] for title in headers_after_3]

    # 处理后的标题进行独热编码
    for i in range(len(general_data)):
        # 创建一个temp数组保存每次一个标题生成OneHot编码
        temp = []
        for new_header in headers:
            # 处理字符串为”xxxx+信息“的格式，对应上文件名
            file_info = new_header+"信息"
            file_code = new_header+"编码"
            # 获取对应的文件
            file_df = pd.read_csv(f"data/{file_info}.csv")

            vec = [0 for _ in file_df[file_code]]

            # 按列拼接每个特征化的OneHot编码
            temp = temp + one_hot_encoding(i, general_data, file_code, vec)  #其中data是关系表，new_header是处理好的一个表头标题
        # 拼接结果存入特征矩阵
        feature_list.append(temp)
    return feature_list

# OneHot编码器
def one_hot_encoding(i, general_data, file_code, vec):
    # 应用层级独热编码
    string = str(general_data[file_code][i])
    onehot_vec = vec.copy()
    if string == "不限" or string is None:
        onehot_vec = [1 for _ in vec]
    else:
        # 用于多个栏目编号以逗号分隔的情况
        arr = string.split(",")
        for j in arr:
            j = int(j)
            onehot_vec[j - 1] = 1
    return onehot_vec
