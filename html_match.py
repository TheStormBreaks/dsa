class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self._data = []
        
    def push(self, e):
        self._data.append(e)
    
    def isEmpty(self):
        return len(self._data) == 0
    
    def __len__(self):
        return len(self._data)
    
    def pop(self):
        if self.isEmpty():
            raise Empty("Stack is Empty")
        return self._data.pop()
    
    def top(self):
        if self.isEmpty():
            raise Empty("Stack is Empty")
        return self._data[-1]
    


def is_matched_html(raw):
# Return True if all HTML tags match; False otherwise.
    S = ArrayStack()
    j = raw.find('<')   # find first ‘<’ character (if any)

    while j !=- 1:
            k = raw.find('>', j+1)  # find next ‘>’ character

            if   k== -1:
                 return False # invalid tag
            
            tag = raw[j+1:k]       # extract tag by stripping away ‘<’ and ‘>’

            if  not  tag.startswith('/'):     # this is opening tag
                  S.push(tag)

            else:     # this is closing tag
                  if S.is_empty():
                      return False    # nothing to match with
                  
                  if  tag[1:] != S.pop():
                       return False   # mismatched delimiter
                  
            j = raw.find('<',k+1)                # find next ‘<’ character if any 
    return S.is_empty()
