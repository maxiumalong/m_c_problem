def create_edges(capacity):  # 生成所有的运算子，即边
    set_of_operation = []  # 存储运算子的列表
    for i in range(capacity + 1):
        for j in range(capacity + 1):
            if i + j <= capacity and (i >= j or i == 0):
                if i == 0 and j == 0:
                    continue
                set_of_operation.append([i, j])
    print('可用的操作算符为：', set_of_operation)
    return set_of_operation