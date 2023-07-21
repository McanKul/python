

class Question():

    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkanswer(self,cevap):

        if cevap not in self.choices:
            raise ValueError("lütfen şıklardan bir seçin yapınız")
        return cevap == self.answer
       

q1 = Question("en iyi proglamlamakdili hangisidir",["python","c#","java","dart"],"python")
q2 = Question("en popüler proglalama dili nedir",["python","java","c#","dart"],"python")
q3 = Question("en çok kazandıran yazılım dili hangisidir",["python","java","dart","c#"],"python ")

sorular = [q1,q2,q3] 
# print(q1.choices)
# print(q1.checkanswer("python"))

class Quiz():
    toplam = 0
    soru= 0
    def __init__(self,question,score):
        self.question = question
        self.questionindex = 0
        self.score = score
        Quiz.soru += 1
    
    def getQuestion(self):
        return self.questions[self.questionindex]
    def displayQuestion(self):
        question = self.getQuestion()
        print(f"soru{self.questionindex}: {question.text}")
        for i in question.choices:
            print("-"+ i)
    
    def loadQuest(self):
        for i in range(self.soru):
            print(self.question.text)
            print(self.question.choices)
            cevap = input("bir cevap giriniz")
            if cevap == self.question.answer:
                Quiz.toplam += self.score
                print(f"cevabınız doğrudur\nsıradaki soru")
            
            else:
                print(f"cevabınız yanlış\nsıradaki soru")
    @classmethod
    def displayScore(cls):
        print(f"scorunuz{cls.toplam}")
                


c1 = Quiz(q1,1,10)
c2 = Quiz(q2,2,20)
c3 = Quiz(q3,3,30)

print(c1.loadQuest())
# print(Quiz.soru)

# print(Quiz.getQuestion(1))
print(Quiz.displayScore())

