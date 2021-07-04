# Rope

# todo
# reorder rope

# API
def to_rope(string):
    return String(string)


class Rope(object):
    def __add__(self, addend):
        return Concatenation(self, addend)
    
    def __getitem__(self, index):
        if type(index) == int:
            return self._get_single_item(index)

        return Substring(self, index.start, index.stop - index.start)
    
    def delete(self, start, length):
        left = self[0:start]
        right = self[start + length : len(self)]
        return left + right
    
    def insert(self, rope, start):
        left = self[0:start]
        right = self[start : len(self)]
        return left + rope + right
    
    def __len__(self):
        raise Exception('Should have been overriden')
    
    def _get_single_item(self, index):
        raise Exception('Should have been overriden')
    

class String(Rope):
    def __init__(self, string):
        self.string = string
    
    def __str__(self):
        return self.string

    def __len__(self):
        return len(self.string)
    
    def _get_single_item(self, index):
        return self.string[index]

class Substring(Rope):
    def __init__(self, rope, start, length):
        self.rope = rope
        self.start = start
        self.len = length

    def __str__(self):
        return str(self.rope)[self.start:self.start + self.len]
    
    def __len__(self):
        return self.len


class Concatenation(Rope):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.left) + str(self.right)
    
    def __len__(self):
        return len(self.left) + len(self.right)
    
    def _get_single_item(self, index):
        return "d"

# Testing Framework
def equals(rope, expected):
    actual = str(rope)
    if actual == expected:
        return

    print(actual, "didn't equals", expected)
    raise Exception()
    

equals(to_rope("abc"), "abc")
equals(to_rope("abcde")[1:4], "bcd")
equals(to_rope("abcde")[1:4][1:2], "c")
equals(to_rope("abc") + to_rope("de"), "abcde")

equals(to_rope("abcde").delete(1, 3), "ae")

assert len(to_rope("abcde")[1:4]) == 3
assert len(to_rope("abc") + to_rope("de")) == 5

equals(to_rope("abe").insert(to_rope("cd"), 2), "abcde")

equals(to_rope("abcde")[3], "d")
equals((to_rope("abc") + to_rope("de"))[3], "d")