'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

'''

class Node():
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def preorder(p):
    print(nodeDict[p].data)
    if nodeDict[p].left:
        preorder(nodeDict[p].left)
    if nodeDict[p].right:
        preorder(nodeDict[p].right)
    return


V = int(input())
nodes = list(map(int, input().split()))
print(nodes)
nodeDict = {}
for i in range(len(nodes)//2):
    parent, child = nodes[2*i], nodes[2*i+1]
    # 어쨋든 child도 새로 등록해줘야 한다규
    nodeC = Node(child, None, None)
    nodeDict[child] = nodeC
    # 부모가 이미 있으면
    if nodeDict.get(parent):
        if nodeDict[parent].left:
            nodeDict[parent].right = child
        else:
            nodeDict[parent].left = child
    else:
        nodeP = Node(parent, child, None)
        nodeDict[parent] = nodeP


preorder(1)