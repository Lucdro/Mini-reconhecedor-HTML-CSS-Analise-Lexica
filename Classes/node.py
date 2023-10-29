class TreeNode:
    __children = []
    
    def __init__(self,value) -> None:
        self.__value = value
    
    def addNode(self,value):
        self.__children.append(TreeNode(value))
    
    def addNode(self,value,i):
        self.__children.insert(i,TreeNode(value))

    def removeNodeAt(self,x):
        if len(self.__children) <= x:
            return None
        return self.__children.pop(x)
    
    def removeNode(self,value):
        for x in range(0,len(self.__children)-1):
            if self.__children[x].getValue() == value:
                return self.removeNodeAt(x)

    def getChildren(self):
        return self.__children
    
    def getChild(self,i):
        if len(self.__children) <= i:
            return None
        return self.__children[i]
    
    def getValue(self):
        return self.__value
    
    def findNodes(self,value):
        nodes = []
        for x in range(0,len(self.__children)-1):
            if self.__children[x].getValue() == value:
                nodes.append(self.getChild(x))
        return nodes