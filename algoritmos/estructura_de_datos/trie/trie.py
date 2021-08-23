from collections import defaultdict


class TrieNode():

    def __init__(self):
        self.children = defaultdict()
        self.isword = False


class Trie():

    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def get_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word):

        root = self.root
        len1 = len(word)

        for i in range(len1):
            index = self.get_index(word[i])

            if index not in root.children:
                root.children[index] = self.get_node()
            root = root.children.get(index)

        root.isword = True

    def search(self, word):
        root = self.root
        len1 = len(word)

        for i in range(len1):
            index = self.get_index(word[i])
            if not root:
                return False
            root = root.children.get(index)

        return True if root and root.isword else False

    def update(self, old_word, new_word):
        val = self.delete(old_word)
        if val == 0:
            self.insert(new_word)

    #TAREA DELETE
    #Cristian Paz

    def deleteWord(self, word):

        root = self.root
        len1 = len(word)

        for i in range(len1):
            index = self.get_index(word[i])

            if not root:
                print ("Palabra no existe")
                return -1
            root = root.children.get(index)

        if not root:
            print ("Palabra no existe")
            return -1
        else:
            root.isword = False
            return 0


if __name__ == '__main__':

    strings = ["algo", "algoritmica", "astuto", "ala", "alguien"]

    t = Trie()
    for word in strings:
        t.insert(word)

    print(t.search("algo"))
    print(t.search("algoritmica"))
    print(t.search("astuto"))
    print(t.search("ala"))
    print(t.search("alguien"))


    print("Delete de la Palabra ALA \n")

    t.deleteWord("ala")

    print(t.search("ala"))
