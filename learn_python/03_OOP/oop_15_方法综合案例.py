"""
需求：
1.设计一个Game类
2.属性：
定义一个类属性 top_socre记录游戏的历史最高分
定义一个实例属性 player_name记录当前游戏的玩家姓名
3.方法：
静态方法 show_help 显示游戏帮助信息
类方法 show_top_score 显示历史最高分
实例方法 start_game 开始当前玩家的游戏
4.主程序步骤
查看帮助信息
查看历史最高分
创建游戏对象，开始游戏
"""
class Game:
	top_socre = 0
	def __init__(self,player_name):
		self.player_name = player_name

	@staticmethod
	def show_help():
		print("这个游戏很简单")
	@classmethod
	def show_top_socre(cls):
		print("历史最高分是%d"%cls.top_socre)

	def start_game(self):
		print("%s 开始游戏啦..."%self.player_name)

Game.show_help()
Game.show_top_socre()
xiaoming = Game("小明")
xiaoming.start_game()