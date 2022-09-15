# 노드 클래스
class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


# 전위 순회
def preorder(node):
    print(node.data, end=" ")
    if node.left:
        preorder(tree[node.left])
    if node.right:
        preorder(tree[node.right])


# 중위 순회
def inorder(node):
    if node.left:
        inorder(tree[node.left])
    print(node.data, end=" ")
    if node.right:
        inorder(tree[node.right])


# 후위 순회
def postorder(node):
    if node.left:
        postorder(tree[node.left])
    if node.right:
        postorder(tree[node.right])
    print(node.data, end=" ")


n = int(input())
tree = {}
for i in range(n):
    tmp = input().split()
    if len(tmp) != 2:
        tree[tmp[0]] = Node(tmp[1], tmp[2], tmp[3])
    else:
        tree[tmp[0]] = Node(tmp[1], None, None)

preorder(tree['1'])
print()
inorder(tree['1'])
print()
postorder(tree['1'])
