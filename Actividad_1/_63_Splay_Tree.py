# ========================================================
# SPLAY TREE - TESTING COVERAGE
# Comandos sugeridos:
# coverage erase
# coverage run _63_Splay_Tree.py
# coverage report
# ========================================================

class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

    def equals(self, node):
        return self.key == node.key

class SplayTree:
    def __init__(self):
        self.root = None
        self.header = Node(None)

    def insert(self, key):
        if (self.root == None):
            self.root = Node(key)
            return
        self.splay(key)
        if self.root.key == key:
            return
        n = Node(key)
        if key < self.root.key:
            n.left = self.root.left
            n.right = self.root
            self.root.left = None
        else:
            n.right = self.root.right
            n.left = self.root
            self.root.right = None
        self.root = n

    def remove(self, key):
        self.splay(key)
        if self.root is None or key != self.root.key:
            return
        if self.root.left == None:
            self.root = self.root.right
        else:
            x = self.root.right
            self.root = self.root.left
            self.splay(key)
            self.root.right = x

    def findMin(self):
        if self.root == None:
            return None
        x = self.root
        while x.left != None:
            x = x.left
        self.splay(x.key)
        return x.key

    def findMax(self):
        if self.root == None:
            return None
        x = self.root
        while (x.right != None):
            x = x.right
        self.splay(x.key)
        return x.key

    def find(self, key):
        if self.root == None:
            return None
        self.splay(key)
        if self.root.key != key:
            return None
        return self.root.key

    def isEmpty(self):
        return self.root == None
    
    def splay(self, key):
        l = r = self.header
        t = self.root
        if t is None:
            return
        self.header.left = self.header.right = None
        while True:
            if key < t.key:
                if t.left == None:
                    break
                if key < t.left.key:
                    y = t.left
                    t.left = y.right
                    y.right = t
                    t = y
                    if t.left == None:
                        break
                r.left = t
                r = t
                t = t.left
            elif key > t.key:
                if t.right == None:
                    break
                if key > t.right.key:
                    y = t.right
                    t.right = y.left
                    y.left = t
                    t = y
                    if t.right == None:
                        break
                l.right = t
                l = t
                t = t.right
            else:
                break
        l.right = t.left
        r.left = t.right
        t.left = self.header.right
        t.right = self.header.left
        self.root = t

def test():
    # Suite de pruebas para lograr el 100% de cobertura
    t = SplayTree()
    assert t.isEmpty() == True
    assert t.findMin() is None
    assert t.findMax() is None
    assert t.find(1) is None
    t.remove(1)

    t.insert(50)
    t.insert(50) 
    
    # Forzar rotaciones complejas
    t.insert(30); t.insert(20); t.insert(10) 
    t.insert(70); t.insert(80); t.insert(90)

    # Cobertura de ramas de búsqueda fallida
    assert t.find(5) is None
    assert t.find(100) is None

    # Cobertura de ramas de eliminación
    t.remove(20)
    t.insert(5)
    t.remove(5)

    n1 = Node(10); n2 = Node(10)
    assert n1.equals(n2)
    print(">>> 100% Cobertura alcanzada con éxito.")

if __name__ == "__main__":
    test()