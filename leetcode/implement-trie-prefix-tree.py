class TrieNode:
    def __init__(self):
        # We need to store children nodes (usually a dict or array of size 26)
        self.children = {}
        # We need a flag to mark if this node is the end of a word
        self.isEnd = False

class Trie(object):

    def __init__(self):
        
        self.root = TrieNode()

    def insert(self, word):
        # Start from the root node
        node = self.root
        
        # Iterate through every character in the word
        for char in word:
            # If the character is not in the current node's children, create a new node
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move the pointer to the child node
            node = node.children[char]
        
        # After processing all characters, mark the current node as a word ending
        node.isEnd = True

    def search(self, word):
        # Start from root
        node = self.root
        
        for char in word:
            # If char not found in children, the word doesn't exist
            if char not in node.children:
                return False
            # Move to the next node
            node = node.children[char]
        
        # Return True only if we reached the end AND this node is marked as a word end
        # (e.g., searching "app" in "apple" should return False)
        return node.isEnd

    def startsWith(self, prefix):
        # Start from root
        node = self.root
        
        for char in prefix:
            # If char not found, no word starts with this prefix
            if char not in node.children:
                return False
            node = node.children[char]
        
        # If we successfully traversed the prefix, return True.
        # We don't care if it's the end of a word or just a path.
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)