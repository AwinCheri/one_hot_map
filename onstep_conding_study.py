# import pandas as pd
# from sklearn.metrics.pairwise import cosine_similarity
#
# #   请先看readme文件，这是一个用于学习的简单粗暴的算法
#
#
# # 第一步特征选取
# # user：用户信息
# # map：地图信息
# # subject：应用层级
# # scene：应用场景
# # demandType：需求类型
# # timeStruct：时间结构
# # geomLogic：几何逻辑
# # presentForm：表现形式
# # exprScale：表达尺度
# # spaceRef：空间组织面
# # readerView：对象状态
# user_df = pd.read_csv("data/用户信息.csv")
# map_df = pd.read_csv("data/地图信息.csv")
# subject_df = pd.read_csv("data/应用层级信息.csv")
# scene_df = pd.read_csv("data/应用场景信息.csv")
# demandType_df = pd.read_csv("data/需求类型信息.csv")
# timeStruct_df = pd.read_csv("data/时间结构信息.csv")
# geomLogic_df = pd.read_csv("data/几何逻辑信息.csv")
# presentForm_df = pd.read_csv("data/表现形式信息.csv")
# exprScale_df = pd.read_csv("data/表达尺度信息.csv")
# spaceRef_df = pd.read_csv("data/空间组织信息.csv")
# readerView_df = pd.read_csv("data/对象状态信息.csv")
# # 第二步，特征预处理，独热编码
# subject_vec = [0 for _ in subject_df["应用层级编号"]]
# scene_vec = [0 for _ in scene_df["应用场景编号"]]
# demandType_vec = [0 for _ in demandType_df["需求类型编号"]]
# timeStruct_vec = [0 for _ in timeStruct_df["时间结构编号"]]
# geomLogic_vec = [0 for _ in geomLogic_df["几何逻辑编号"]]
# presentForm_vec = [0 for _ in presentForm_df["表现形式编号"]]
# exprScale_vec = [0 for _ in exprScale_df["表达尺度编号"]]
# spaceRef_vec = [0 for _ in spaceRef_df["空间组织编号"]]
# readerView_vec = [0 for _ in readerView_df["对象状态编号"]]
#
# # 遍历每一篇文章，然后对其特征做处理
# map_list = []
# print(range(len(map_df)))
#
# for i in range(len(map_df)):
#     print(i)
#     # 应用层级独热编码
#     subject_str = str(map_df["应用层级编号"][i])
#     subject_onehot_vec = subject_vec.copy()
#     if subject_str == "不限":
#         subject_onehot_vec = [1 for _ in subject_vec]
#     else:
#         # 用于多个栏目编号以逗号分隔的情况
#         subject_arr = subject_str.split(",")
#         for j in subject_arr:
#             j = int(j)
#             subject_onehot_vec[j-1] = 1
#     # 应用场景独热编码
#     scene_str = str(map_df["应用场景编号"][i])
#     scene_onehot_vec = scene_vec.copy()
#     if scene_str == "不限":
#         scene_onehot_vec = [1 for _ in scene_vec]
#     else:
#         # 用于多个栏目编号以逗号分隔的情况
#         scene_arr = scene_str.split(",")
#         for j in scene_arr:
#             j = int(j)
#             scene_onehot_vec[j - 1] = 1
#     # 需求类型独热编码
#     demandType_str = str(map_df["需求类型编号"][i])
#     demandType_onehot_vec = demandType_vec.copy()
#     if demandType_str == "不限":
#         demandType_onehot_vec = [1 for _ in demandType_vec]
#     else:
#         # 用于多个栏目编号以逗号分隔的情况
#         demandType_arr = demandType_str.split(",")
#         for j in demandType_arr:
#             j = int(j)
#             demandType_onehot_vec[j - 1] = 1
#
#     # 时间结构独热编码
#     timeStruct_str = str(map_df["时间结构编号"][i])
#     timeStruct_onehot_vec = timeStruct_vec.copy()
#     if timeStruct_str == "不限":
#         timeStruct_onehot_vec = [1 for _ in timeStruct_vec]
#     else:
#         timeStruct_arr = timeStruct_str.split(",")
#         for j in timeStruct_arr:
#             j = int(j)
#             timeStruct_onehot_vec[j - 1] = 1
#
#     # 几何逻辑独热编码
#     geomLogic_str = str(map_df["几何逻辑编号"][i])
#     geomLogic_onehot_vec = geomLogic_vec.copy()
#     if geomLogic_str == "不限":
#         geomLogic_onehot_vec = [1 for _ in geomLogic_vec]
#     else:
#         geomLogic_arr = geomLogic_str.split(",")
#         for j in geomLogic_arr:
#             j = int(j)
#             geomLogic_onehot_vec[j - 1] = 1
#     # 表现形式独热编码
#     presentForm_str = str(map_df["表现形式编号"][i])
#     presentForm_onehot_vec = presentForm_vec.copy()
#     if presentForm_str == "不限":
#         presentForm_onehot_vec = [1 for _ in presentForm_vec]
#     else:
#         presentForm_arr = presentForm_str.split(",")
#         for j in presentForm_arr:
#             j = int(j)
#             presentForm_onehot_vec[j - 1] = 1
#     # 表达尺度独热编码
#     exprScale_str = str(map_df["表达尺度编号"][i])
#     exprScale_onehot_vec = exprScale_vec.copy()
#     if exprScale_str == "不限":
#         exprScale_onehot_vec = [1 for _ in exprScale_vec]
#     else:
#         exprScale_arr = exprScale_str.split(",")
#         for j in exprScale_arr:
#             j = int(j)
#             exprScale_onehot_vec[j - 1] = 1
#     # 空间组织独热编码
#     spaceRef_str = str(map_df["空间组织编号"][i])
#     spaceRef_onehot_vec = spaceRef_vec.copy()
#     if spaceRef_str == "不限":
#         spaceRef_onehot_vec = [1 for _ in spaceRef_vec]
#     else:
#         spaceRef_arr = spaceRef_str.split(",")
#         for j in spaceRef_arr:
#             j = int(j)
#             spaceRef_onehot_vec[j - 1] = 1
#     # 对象状态独热编码
#     readerView_str = str(map_df["对象状态编号"][i])
#     readerView_onehot_vec = readerView_vec.copy()
#     if readerView_str == "不限":
#         readerView_onehot_vec = [1 for _ in readerView_vec]
#     else:
#         readerView_arr = readerView_str.split(",")
#         for j in readerView_arr:
#             j = int(j)
#             readerView_onehot_vec[j - 1] = 1
#     # 每次都把生成好的独热编码拼接到地图列表中
#     map_list.append(
#         subject_onehot_vec + scene_onehot_vec + demandType_onehot_vec +
#         timeStruct_onehot_vec + geomLogic_onehot_vec + presentForm_onehot_vec +
#         exprScale_onehot_vec + spaceRef_onehot_vec + readerView_onehot_vec
#     )
# # 打印文章信息列表
# # for v in wenz_list:
# #     print(v)
#
# # 处理用户信息:用户信息中只有 栏目编号 和 所属地域编号
# print(map_list)
# print("-------------")
# user_list = []
# for i in range(len(user_df)):
#     # 1用户感兴趣的应用层级编号
#     subject_str = str(user_df["应用层级编号"][i])
#     subject_onehot_vec = subject_vec.copy()
#     if subject_str == "不限":
#         subject_onehot_vec = [1 for _ in subject_vec]
#     else:
#         subject_arr = subject_str.split(",")
#         for j in subject_arr:
#             j = int(j)
#             subject_onehot_vec[j-1] =1
#     # 2
#     scene_str = str(user_df["应用场景编号"][i])
#     scene_onehot_vec = scene_vec.copy()
#     if scene_str == "不限":
#         scene_onehot_vec = [1 for _ in scene_vec]
#     else:
#         scene_arr = scene_str.split(",")
#         for j in scene_arr:
#             j = int(j)
#             scene_onehot_vec[j - 1] = 1
#     # 3
#     demandType_str = str(user_df["需求类型编号"][i])
#     demandType_onehot_vec = demandType_vec.copy()
#     if demandType_str == "不限":
#         demandType_onehot_vec = [1 for _ in demandType_vec]
#     else:
#         demandType_arr = demandType_str.split(",")
#         for j in demandType_arr:
#             j = int(j)
#             demandType_onehot_vec[j - 1] = 1
#     # 4
#     timeStruct_str = str(user_df["时间结构编号"][i])
#     timeStruct_onehot_vec = timeStruct_vec.copy()
#     if timeStruct_str == "不限":
#         timeStruct_onehot_vec = [1 for _ in timeStruct_vec]
#     else:
#         timeStruct_arr = timeStruct_str.split(",")
#         for j in timeStruct_arr:
#             j = int(j)
#             timeStruct_onehot_vec[j - 1] = 1
#     # 5
#     geomLogic_str = str(user_df["几何逻辑编号"][i])
#     geomLogic_onehot_vec = geomLogic_vec.copy()
#     if geomLogic_str == "不限":
#         geomLogic_onehot_vec = [1 for _ in geomLogic_vec]
#     else:
#         geomLogic_arr = geomLogic_str.split(",")
#         for j in geomLogic_arr:
#             j = int(j)
#             geomLogic_onehot_vec[j - 1] = 1
#     # 6
#     presentForm_str = str(user_df["表现形式编号"][i])
#     presentForm_onehot_vec = presentForm_vec.copy()
#     if presentForm_str == "不限":
#         presentForm_onehot_vec = [1 for _ in presentForm_vec]
#     else:
#         presentForm_arr = presentForm_str.split(",")
#         for j in presentForm_arr:
#             j = int(j)
#             presentForm_onehot_vec[j - 1] = 1
#     # 7
#     exprScale_str = str(user_df["表达尺度编号"][i])
#     exprScale_onehot_vec = exprScale_vec.copy()
#     if exprScale_str == "不限":
#         exprScale_onehot_vec = [1 for _ in exprScale_vec]
#     else:
#         exprScale_arr = exprScale_str.split(",")
#         for j in exprScale_arr:
#             j = int(j)
#             exprScale_onehot_vec[j - 1] = 1
#     # 8
#     spaceRef_str = str(user_df["空间组织编号"][i])
#     spaceRef_onehot_vec = spaceRef_vec.copy()
#     if spaceRef_str == "不限":
#         spaceRef_onehot_vec = [1 for _ in spaceRef_vec]
#     else:
#         spaceRef_arr = spaceRef_str.split(",")
#         for j in spaceRef_arr:
#             j = int(j)
#             spaceRef_onehot_vec[j - 1] = 1
#     # 9
#     readerView_str = str(user_df["对象状态编号"][i])
#     readerView_onehot_vec = readerView_vec.copy()
#     if readerView_str == "不限":
#         readerView_onehot_vec = [1 for _ in readerView_vec]
#     else:
#         readerView_arr = readerView_str.split(",")
#         for j in readerView_arr:
#             j = int(j)
#             readerView_onehot_vec[j - 1] = 1
#     # 对于一些可以直接设置优先值的独热编码，可以采用瞎以下方法
#     # # 用户隐藏的发布时间兴趣设置为最新，也就是第一级，都为[1,0,0,0,0,0,0,0]的独热编码
#     # publish_onehot_vec = publish_vec.copy()
#     # publish_onehot_vec[0] = 1
#     # # 用户隐藏的点击量兴趣设置为最高，也就是最后一级，为[0,0,0,0,0,0,0,1]的独热编码
#     # click_onehot_vec = click_vec.copy()
#     # click_onehot_vec[-1] = 1
#
#
#     user_list.append(
#         subject_onehot_vec + scene_onehot_vec + demandType_onehot_vec +
#         timeStruct_onehot_vec + geomLogic_onehot_vec + presentForm_onehot_vec +
#         exprScale_onehot_vec + spaceRef_onehot_vec + readerView_onehot_vec
#     )
# # for v in user_list:
# #     print(v)
#
# # 第三步，基于余弦相似度求每一篇文章与用户的相似度
# sim_lis = cosine_similarity(user_list,map_list)
#
# #第四步排序
# sorted_sim_lis = []
# for lis in sim_lis:
#     # 相似度与对应的地图编号关联起来
#     lis1 = [(i+1, sim_v)for i, sim_v in enumerate(lis)]
#     # 按第二列的相似度余弦值降序排序
#     lis1 = sorted(lis1, key=lambda row: row[1], reverse= True)
#     sorted_sim_lis.append(lis1)
# for i,v in enumerate(sorted_sim_lis):
#     print(user_df["昵称"][i])
#     print(v)