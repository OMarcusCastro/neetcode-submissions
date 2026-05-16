class MyCalendar:
    
    def __init__(self):
        self.bookings = {}

    def book(self, startTime: int, endTime: int) -> bool:
        if self.bookings is not None:
            # print(self.bookings)
            for oldStart,oldEnd in self.bookings.items():
                if oldStart<=startTime<oldEnd or oldStart<endTime<=oldEnd or (startTime<oldStart and endTime>oldEnd):
                    return False
        self.bookings[startTime]=endTime
        return True

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)