class TrietrieNode():
    def __init__(self):
        self.contains=[None]*10
        self.endOfWord=False


def insertion(trieNode,string):
    length=len(string)
    cnode=trieNode
    for i in range(length):
        idx=int(string[i])
        if not cnode.contains[idx]:
            cnode.contains[idx]=TrietrieNode()
        cnode=cnode.contains[idx]
    cnode.endOfWord=True


def is_not_consistent(trieNode):
    for i in range(10):
        if trieNode.contains[i] is not None:
            if trieNode.endOfWord:
                return True
            if is_not_consistent(trieNode.contains[i]):
                return True
    return False


def delete(trieNode):
    for i in range(10):
        if trieNode.contains[i] is not None:
            delete(trieNode.contains[i])
    del trieNode


t=int(input())
for c in range(t):
    start=TrietrieNode()
    n=int(input())
    for _ in range(n):
        s=input()
        insertion(start,s)
    print(f"Case {c+1}: NO" if is_not_consistent(start) else f"Case {c+1}: YES")
    delete(start)