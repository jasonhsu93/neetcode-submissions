class TrieNode:

    def __init__(self):
        self.child = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        
        temp = self.root

        for char in word:
            temp.child[char] = temp.child.get(char, TrieNode()) 
            temp = temp.child[char] 
        
        temp.end = True

    def search(self, word: str) -> bool:
        
        def dfs(i, char):
            if word[i] == '.':
                for value in char.child.values():
                    if i == len(word) - 1:
                        if value.end:
                            return True
                        else:
                            continue
                    if dfs(i + 1, value):
                        return True
                return False
            else:
                if word[i] in char.child:
                    if i == len(word) - 1:
                        if char.child[word[i]].end:
                            return True
                        else:
                            return False
                    else:
                        return dfs(i + 1, char.child[word[i]])
                else:
                    return False
                    
        return dfs(0, self.root)


                

