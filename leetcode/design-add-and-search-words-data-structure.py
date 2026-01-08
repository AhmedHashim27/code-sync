class TrieNode:
    def __init__(self):
        # Dictionary mapping char -> TrieNode
        self.children = {}
        # Boolean flag for end of word
        self.is_word = False

class WordDictionary(object):

    def __init__(self):
        # Dictionary mapping char -> TrieNode
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """

        curr = self.root
        for char in word:
            # If path doesn't exist, create it
            if char not in curr.children:
                curr.children[char] = TrieNode()
            # Move to next node
            curr = curr.children[char]
        # Mark the end of the word
        curr.is_word = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """

        def dfs(index, node):
            # Base Case: We have processed the entire string
            if index == len(word):
                # Return True only if this node marks a complete word
                return node.is_word
            
            char = word[index]
            
            if char == '.':
                # Wildcard case: Try ALL available children at this level
                for child in node.children.values():
                    # If any path returns True, the search is successful
                    if dfs(index + 1, child):
                        return True
                # If no path works, return False
                return False
            
            else:
                # Standard case: Check specific character
                if char not in node.children:
                    return False
                # Recurse on the specific child
                return dfs(index + 1, node.children[char])
        
        # Start DFS from index 0 and the root node
        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)