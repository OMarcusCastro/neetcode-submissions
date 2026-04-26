class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #while stack empty ou temp<a utima da stack -> empilha
        #caso contrario: faz operacao no arry de resposta
        #esvazia a pilha e coloca o indice do elemente atual

        #edge: tamnho 1 -> return [0]
        stack = []
        resp = [0]*len(temperatures)

        for i in range(len(temperatures)):
            temperature = temperatures[i]

            while len(stack)>0 and temperature>temperatures[stack[-1]]:
                idx = stack.pop()
                dist = i-idx
                resp[idx] = dist
            stack.append(i)

        return resp
            



            