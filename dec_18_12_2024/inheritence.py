class fruits:
    def eat(self):
        print("we can eat fruits")
class orenge(fruits):
    pass
    def eat (self):
         print("orenge is sour fruit")
class apple(fruits):
    def eat(self):
        print("apple is sweet")
org1=orenge()
app1=apple()
org1.eat()
app1.eat()
