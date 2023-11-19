
class Stack:
    def __init__(self):
        self.glist = []
    
    def push(self, item):
        self.glist.append(item) # 0 1 2 3 <- 4 -< 5 -> 5 01234
    
    #@private
    def is_empty(self):
        return len(self.glist) == 0
  
    def pop(self):
        if self.is_empty():
            print("Список пуст - удалять нечего!")
            return 
        else: self.glist.pop()
          
if __name__ == "__main__":
    stack = Stack()
    for item in range(10):
        stack.push(item)
    print(stack.glist)
    while stack.is_empty() != True:
        stack.pop()
    print(stack.glist)