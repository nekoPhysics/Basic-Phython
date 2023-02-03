# Test case: input= "This is a pen"
class NumCount:
    def __init__(self):
        self.input_array = []
        self.ans_array = [0]*26
        self.small_letters = list("abcdefghijklmnopqrstuvwxyz")
        self.big_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        
    def Start(self):
        self.ImportSentence()
    
    def ImportSentence(self):
        inpt = "This is a pen"
        while(True):
            try:
                s = inpt
                s_without_space = s.replace(' ', '')
                for i in list(s_without_space):
                    if i.isalpha():
                        self.input_array.append(i)
                    else:
                        pass
                break
                    
            except:
                break
            
        
        self.Process()
    
    def Process(self):
        for s in self.input_array:
            num = -1
            try:
                num = self.small_letters.index(s)
            except:
                num = self.big_letters.index(s)
                
            self.ans_array[num] += 1
            
        self.Show()
    
    def Show(self):
        for i, s in zip(self.ans_array, self.small_letters):
            print("%s : %d" % (s, i))


n = NumCount()
n.Start()