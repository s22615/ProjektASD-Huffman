from queue import PriorityQueue


class Node:
    value = 0
    right = None
    left = None
    character = ""

    def isLeaf(self):
        return self.character != ""

    def __init__(self, val, ch):
        self.value = val
        self.character = ch

    def __lt__(self, other):
        if self.value != other.value:
            return self.value < other.value
        if not self.isLeaf() and other.isLeaf():
            return True
        if self.isLeaf() and not other.isLeaf():
            return False
        if self.isLeaf() and other.isLeaf():
            return ord(self.character[0]) < ord(other.character[0])
        return True


def createTree(text):
    counting = {}
    for t in text:
        if counting.__contains__(t):
            counting[t] += 1
        else:
            counting[t] = 1
    nodes = PriorityQueue()
    for t in counting.keys():
        node = Node(counting[t], t)
        nodes.put(node)
    rootNode = None
    while nodes.qsize() > 1:
        n1 = nodes.get()
        n2 = nodes.get()
        if n1.value == n2.value and not n1.isLeaf():
            pom = n1
            n1 = n2
            n2 = pom
        parent = Node(n1.value + n2.value, "")
        rootNode = parent
        parent.left = n1
        parent.right = n2
        nodes.put(parent)
    return rootNode


code_dict = ""


def encodeValues(n, str, txt):
    global code_dict
    if n is None:
        return txt
    if n.isLeaf():
        print("|" + n.character + ": " + str + "|", end=" ")
        code_dict += ("|" + n.character + ": " + str + "|")
        txt = txt.replace(n.character, str)
    txt = encodeValues(n.left, str + "0", txt)
    txt = encodeValues(n.right, str + "1", txt)
    return txt


def stringLoader():
    tab = open("EntryText.txt", "r", encoding="utf-8").read().replace('\n', ' ')
    return tab


def stringPaser():
    tab = open("Results.txt", "w", encoding="utf-8")
    s = encodeValues(rootNode, "", st)
    tab.write(code_dict + " ")
    tab.write(s)
    tab.close()


st = stringLoader()
rootNode = createTree(st)
stringPaser()
s = encodeValues(rootNode, "", st)
print(s)


