
from pathlib import Path
from string import whitespace, punctuation
from bst import BST


class Pair:
    ''' Encapsulate letter,count pair as a single entity.
    
    Relational methods make this object comparable
    using built-in operators. 
    '''
    def __init__(self, letter, count = 1):
        self.letter = letter
        self.count = count
    
    def __eq__(self, other):
        if isinstance(other, Pair):
            return self.letter == other.letter
        return self.letter == other
    
    def __hash__(self):
        return hash(self.letter)

    def __ne__(self, other):
        if isinstance(other, Pair):
            return self.letter != other.letter
        return self.letter >= other.letter

    def __lt__(self, other):
        if isinstance(other, Pair):
            return self.letter < other.letter
        return self.letter < other

    def __le__(self, other):
        if isinstance(other, Pair):
            return self.letter <= other.letter
        return self.letter >= other.letter

    def __gt__(self, other):
        if isinstance(other, Pair):
            return self.letter > other.letter
        return self.letter >= other.letter

    def __ge__(self, other):
        if isinstance(other, Pair):
            return self.letter >= other.letter
        return self.letter >= other

    def __repr__(self):
        return f'({self.letter}, {self.count})'
    
    def __str__(self):
        return f'({self.letter}, {self.count})'

def make_tree():
    """Reads characters from a text file and constructs a BST
    with each unique letter and its count.

    Returns:
        BST: Binary search tree with `Pair` objects.
    """
    tree = BST()
    
    file_path = Path("around-the-world-in-80-days-3.txt")
    
    with file_path.open("r", encoding="utf-8") as file:
        for char in file.read():
            if char in whitespace or char in punctuation:
                continue
            
            char = char.lower()
            
            pair = Pair(char)
            if char in tree:
                existing_pair = tree.get(char)
                existing_pair.count += 1
            else:
                tree.put(char, pair)
    
    return tree

def main():
    """Main function to build and test the tree."""
    letter_tree = make_tree()
    
    print("Inorder traversal of the letter frequency tree:")
    print(letter_tree.inorder())
    
if __name__ == "__main__":
    main()