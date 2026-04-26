class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #if number add to stack
        #if operator remove numbers to stack operate and add to stask
        # if size ==0 return 0
        #exemple [1,2,3,+,/]

        stack = []
        operators = "-+/*"

        for token in tokens:
            if token in operators:
                if token =="+":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a+b)
                if token =="-":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a-b)
                if token =="*":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a*b)
                if token =="/":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(int(a/b))
            else:
                stack.append(int(token))
            print(stack)
        return stack[0]