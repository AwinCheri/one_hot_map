from sklearn.metrics.pairwise import cosine_similarity

def cos_sim_sort(user_list, map_list):
    sim_lis = cosine_similarity(user_list, map_list)
    # 第四步排序
    sorted_sim_lis = []

    for lis in sim_lis:
        # 相似度与对应的地图编号关联起来
        lis1 = [(i + 1, sim_v) for i, sim_v in enumerate(lis)]
        # 按第二列的相似度余弦值降序排序
        lis1 = sorted(lis1, key=lambda row: row[1], reverse=True)
        sorted_sim_lis.append(lis1)
    return sorted_sim_lis

