# Rope

# todo
# [] notation
# + for concatenation

# API
def to_rope(string):
    return String(string)


class Rope(object):
    def substring(self, start, length):
        return Substring(self, start, length)
     
    def concatenate(self, right):
        return Concatenation(self, right)
    
    def __add__(self, right):
        return Concatenation(self, right)
        
    
    def delete(self, start, length):
        left = self.substring(0, start)
        right = self.substring(start  + length, len(self) - start - length) # Not very readable
        return left.concatenate(right)
    
    def insert(self, rope, start):
        left = self.substring(0, start)
        right = self.substring(start, len(self) - start) # Not very readable
        return left.concatenate(rope).concatenate(right)
    
    def __len__(self):
        raise Exception('Should have been overriden')
    

class String(Rope):
    def __init__(self, string):
        self.string = string
    
    def __str__(self):
        return self.string

    def __len__(self):
        return len(self.string)

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

# Testing Framework
def equals(rope, expected):
    actual = str(rope)
    if actual == expected:
        return

    print(actual, "didn't equals", expected)
    raise Exception()
    

equals(to_rope("abc"), "abc")
equals(to_rope("abcde").substring(1, 3), "bcd")
equals(to_rope("abcde").substring(1, 3).substring(1, 1), "c")
equals(to_rope("abc") + to_rope("de"), "abcde")

equals(to_rope("abcde").delete(1, 3), "ae")

assert len(to_rope("abcde").substring(1, 3)) == 3
assert len(to_rope("abc").concatenate(to_rope("de"))) == 5

equals(to_rope("abe").insert(to_rope("cd"), 2), "abcde")
