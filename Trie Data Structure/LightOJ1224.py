class TrieNode():
    def __init__(self):
        self.children=[None]*4
        self.leng=0
        self.asPrefix=0


def insert(node,string):
    length=len(string)
    curr=node
    for i in range(length):
        if string[i]=="A":
            idx=0
        elif string[i]=="C":
            idx=1
        elif string[i] == "G":
            idx = 2
        else:
            idx = 3
        to_add=curr.leng
        if not curr.children[idx]:
            curr.children[idx]=TrieNode()
        curr=curr.children[idx]
        curr.leng=to_add+1
        curr.asPrefix+=1


def findMax(node,maxx):
    val=node.leng*node.asPrefix
    if val>maxx:
        maxx=val
    for i in range(4):
        if node.children[i] is not None:
            maxx=findMax(node.children[i],maxx)
    return maxx


def delete(node):
    for i in range(4):
        if node.children[i] is not None:
            delete(node.children[i])
    del node


t=int(input())
for c in range(t):
    root=TrieNode()
    n=int(input())
    for _ in range(n):
        s=input()
        insert(root,s)
    print(f"Case {c+1}: {findMax(root,0)}")
    delete(root)