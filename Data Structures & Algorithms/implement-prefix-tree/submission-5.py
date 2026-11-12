class TrieNode:

    def __init__(self, char):
        self.char = char
        self.child = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.child = {} 

    def insert(self, word: str) -> None:
        
        self.child[word[0]] = self.child.get(word[0], TrieNode(word[0])) 
        temp = self.child[word[0]]

        if len(word) == 1:
            temp.end = True

        for i in range(1, len(word), 1):
            temp.child[word[i]] = temp.child.get(word[i], TrieNode(word[i]))
            temp = temp.child[word[i]]
            if i == len(word) - 1:
                temp.end = True

    def search(self, word: str) -> bool:
        
        if word[0] not in self.child:
            return False
            
        temp = self.child[word[0]]

        for i in range(1, len(word), 1):
            if word[i] not in temp.child:
                return False
            else: 
                temp = temp.child[word[i]]

        if temp.end:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:

        if prefix[0] not in self.child:
            return False

        temp = self.child[prefix[0]]

        for i in range(1, len(prefix), 1):
            if prefix[i] not in temp.child:
                return False
            else: 
                temp = temp.child[prefix[i]]

        return True
        

        