from BinaryHeap_spe import BinHeap

k = int(input("请输入保研录取人数："))
scores = BinHeap()

while 1:
    score = int(input("请输入分数："))
    if score == 999:
        break
    elif score > 100 or score < 0:
        print("输入值不合法，请重新输入！")
    elif scores.currentSize < k:
        scores.insert(score)
    elif score > scores.heapList[1]:
        scores.changeMin(score)

    print(f'当前分数线是：{scores.heapList[1]}')
