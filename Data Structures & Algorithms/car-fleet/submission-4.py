

class Car():
    def __init__(self,speed,position,target):
        self.speed = speed
        self.position = position
        self.time = self.getTimeToTarget(target)
        
    
    def getTimeToTarget(self,target):
        ds = target-self.position
        dt = ds/self.speed
        print(dt)
        return dt


class Solution:

    
            
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #class cars
        # n cars
        # if car.position> target jump
        # if car.position = target -> +1
        # if car.position< target
        cars = []
        stack = []
        for i in range(len(position)):
            
            s = position[i]
            v = speed[i]
            #print(s,v)
            car = Car(v,s,target)
            cars.append(car)

        cars.sort(key=lambda car:car.position)
        
        for car in cars:
            if car.position>target:
                continue
            
            while len(stack)>0 and car.time>=stack[-1].time:
                stack.pop()
            
            stack.append(car)
        return len(stack)

#10,9,8,8


        
