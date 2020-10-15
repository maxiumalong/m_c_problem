def heap_adjust(lists, pos, length):  # 堆排序(升序排列，构建大根堆)：
    max_ = pos
    lchild = 2 * pos + 1  # 由于lists下表从0开始，所以左右孩子下标为2*pos+1,2*pos+2
    rchild = 2 * pos + 2
    if max_ < length // 2:  # 注意符号是<,堆调整时，必定是从(length//2)-1开始
        if lchild < length and lists[lchild][3] > lists[max_][3]:
            max_ = lchild
        if rchild < length and lists[rchild][3] > lists[max_][3]:
            max_ = rchild
        if max_ != pos:  # 如果max_未发生改变，说明不需要调整
            lists[max_], lists[pos] = lists[pos], lists[max_]
            heap_adjust(lists, max_, length)  # 递归调整


def heap_create(lists, length):
    for i in range(length // 2)[::-1]:
        heap_adjust(lists, i, length)


def heap_sort(lists):
    length = len(lists)
    heap_create(lists, length)
    for i in range(length)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]  # 首尾元素互换，将最大的元素放在列表末尾
        heap_adjust(lists, 0, i)  # 从头再调整，列表长度-1（尾元素已经完成排序，所以列表长度-1）


def move(vertex, edge, init_missionary=3, init_cannibal=3):
    if vertex[2] == 0:
        missionary = vertex[0] + edge[0]
        cannibal = vertex[1] + edge[1]
        state_of_boat = 1 - vertex[2]
    else:
        missionary = vertex[0] - edge[0]
        cannibal = vertex[1] - edge[1]
        state_of_boat = 1 - vertex[2]
    if missionary != 0 and missionary < cannibal:
        return False
    elif (init_missionary - missionary) != 0 and ((init_missionary - missionary) < (init_cannibal - cannibal)):
        return False
    elif missionary < 0 or cannibal < 0 or (init_missionary - missionary) < 0 or (init_cannibal - cannibal) < 0:
        return False
    else:
        return [missionary, cannibal, state_of_boat]


def whether_expandable(vertex, set_of_operation, pre_vertex):  # 判断当前节点是否可扩展
    sons = []
    for operation in set_of_operation:
        m = move(vertex, operation)
        if m:
            if m != pre_vertex:  # 扩展得到的子节点不应该是当前节点的父节点，即应当避免重复
                sons.append(m)
    if not sons:
        return False
    else:
        return sons
