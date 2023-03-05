import solver as sl
import tokenizer as token
import Quantizer as Quanta

class BODMAS():
    def __init__(self, string):
        pass

    def bodmas(string):
        def repetor(st):
            st = Quanta.Quantizer.Quartz(st)

        SolvingOrder = string

        while '/' in SolvingOrder:
            SolvingOrder = token.Tokenizer.tokens(SolvingOrder)
            SolvingOrder = Quanta.Quantizer.Quartz(SolvingOrder)
            for i in range(len(SolvingOrder)):
                if SolvingOrder[i[1]] == '/':
                    temp = SolvingOrder[i]
                    temp = token.Tokenizer.tokens(temp)
                    SolvingOrder[i] = sl.Solver.calculator(temp[0], temp[1], temp[2])
        
        tmp = ''
        for i in SolvingOrder:
            tmp += str(i)
        SolvingOrder = tmp

        while '*' in SolvingOrder:
            SolvingOrder = token.Tokenizer.tokens(SolvingOrder)
            SolvingOrder = Quanta.Quantizer.Quartz(SolvingOrder)
            for i in range(len(SolvingOrder)):
                if SolvingOrder[i[1]] == '*':
                    temp = SolvingOrder[i]
                    temp = token.Tokenizer.tokens(temp)
                    SolvingOrder[i] = sl.Solver.calculator(temp[0], temp[1], temp[2])

        tmp = ''
        for i in SolvingOrder:
            tmp += str(i)
        SolvingOrder = tmp

        while '+' in SolvingOrder:
            SolvingOrder = token.Tokenizer.tokens(SolvingOrder)
            SolvingOrder = Quanta.Quantizer.Quartz(SolvingOrder)
            print('+')
            for i in range(len(SolvingOrder)):
                if SolvingOrder[i[1]] == '+':
                    temp = SolvingOrder[i]
                    temp = token.Tokenizer.tokens(temp)
                    SolvingOrder[i] = sl.Solver.calculator(temp[0], temp[1], temp[2])

        tmp = ''
        for i in SolvingOrder:
            tmp += str(i)
        SolvingOrder = tmp

        while '-' in SolvingOrder:
            SolvingOrder = token.Tokenizer.tokens(SolvingOrder)
            SolvingOrder = Quanta.Quantizer.Quartz(SolvingOrder)
            for i in range(len(SolvingOrder)):
                if SolvingOrder[i[1]] == '-':
                    temp = SolvingOrder[i]
                    temp = token.Tokenizer.tokens(temp)
                    SolvingOrder[i] = sl.Solver.calculator(temp[0], temp[1], temp[2])
        
            

            

        return SolvingOrder
        
