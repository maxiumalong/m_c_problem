# This is a sample Python script.
from search_heuristics import *
from initial import *
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
Missinoaries = 3 # 修道士人数
Cannibals = 3 # 野人人数
capacity = 2 # 船能容纳人数
init_state = [Missinoaries, Cannibals, 1] #状态初始化，3个修道士3个野人均在左岸，1代表左岸，0代表右岸
set_of_operation = create_edges(capacity)

#def main(name):
search_heuristic(init_state, set_of_operation) # 状态空间的启发式算法
    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
