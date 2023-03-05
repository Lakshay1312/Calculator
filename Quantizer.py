class Quantizer():
    def __init__(self):
        pass

    def Quartz(lis):
        quartz = []
        for i in range(len(lis)):
            try:
                lis[i] = int(lis[i])
            except:
                quartz.append(str(lis[i-1]) + str(lis[i]) + str(lis[i+1]))
        return quartz
                

