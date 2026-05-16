class Node:
    def __init__(self,startTime,endTime):

        self.left = None
        self.right = None
        self.startTime = startTime
        self.endTime = endTime

    def insert(self,startTime,endTime):
        if startTime>=self.endTime:
            if not self.right:
                self.right = Node(startTime,endTime)
                return True
            return self.right.insert(startTime,endTime)
        if endTime<=self.startTime:
            if not self.left:
                self.left = Node(startTime,endTime)
                return True
            return self.left.insert(startTime,endTime)
        return False
         
            

class MyCalendar:
    
    def __init__(self):
        self.Tree = None
    def book(self, startTime: int, endTime: int) -> bool:
        if not self.Tree:
            self.Tree = Node(startTime,endTime)
            return True
        
        return self.Tree.insert(startTime,endTime)
            
       

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)