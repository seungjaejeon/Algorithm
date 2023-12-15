import sys
N = int(sys.stdin.readline())
    
dic = dict()
for i in range(N):
    pa_node, ch_Lnode, ch_Rnode = map(str, sys.stdin.readline().split())
    dic[pa_node] = [ch_Lnode, ch_Rnode]

def preorder(root):
    if root != '.':
        print(root, end = '')
        preorder(dic[root][0])
        preorder(dic[root][1])

def inorder(root):
    if root != '.':
        inorder(dic[root][0])
        print(root, end = '')
        inorder(dic[root][1])

def postorder(root):
    if root != '.':
        postorder(dic[root][0])
        postorder(dic[root][1])
        print(root, end = '')


preorder('A')
print()
inorder('A')
print()
postorder('A')

# 루트 - 왼 - 오
# 왼 - 루트 - 오
# 왼 - 오 - 루트