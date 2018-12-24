class Animal:
    def eat(self):
        print("吃")
class Dog(Animal):
    def bark(self):
        print("汪汪汪")
    def eat(self):
        #1.子类特有的方法
        print("神一样的吃")
        #2.使用super(),调用父类中的方法
        super().eat()

        print("*-*-*-*-*-*")

dd = Dog()
dd.eat()