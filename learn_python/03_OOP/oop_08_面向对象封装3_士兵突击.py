"""
一个对象的属性可以是另外一个类创建的对象
需求
1.士兵许三多有一把AK47
2.士兵可以开火
3.枪能够发射子弹
4.枪装填子弹----增加子弹数量
"""
class Gun:
    def __init__(self,model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self,count):
        self.bullet_count += count
    def shoot(self):
        #1.判断子弹数量
        if self.bullet_count <= 0:
            print("%s 没有子弹了..."%self.model)
            return
        #2.发射子弹,子弹数量-1
        self.bullet_count -= 1
        #3.提示发射信息
        print("%s 突突突...%d"%(self.model,self.bullet_count))
class Soldier:
    def __init__(self,name):
        self.name = name
        self.gun =None  #新兵没有枪
    def fire(self):

        #1.判断士兵是否有枪
        if self.gun == None:        #与is区别，is判断对象是否一样，==判断内容是否一样
            print("%s还没有枪"%self.name)
            return
        #2.装填子弹
        self.gun.add_bullet(50)
        #3.发射子弹
        self.gun.shoot()
ak = Gun("AK47")
# ak.add_bullet(50)
# ak.shoot()

xusanduo = Soldier("许三多")
xusanduo.gun = ak
xusanduo.fire()
print(xusanduo.gun)
