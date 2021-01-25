# X:玩家拥有的猜测机会
# Y:正确答案
X =  3
import random
Y = random.randint(1,10)
while X>0:
    temp = input('这是一个猜数字的游戏，在这里输入你脑海里的数字:')
    guess = int(temp)
    if guess==Y:
        print('猜对啦！\n您就是大预言家嘛！\n这马屁拍的响不响!\n哈哈哈哈')
        break
    else :
        X=X-1
        if guess>Y:
            print('大啦，再来一次吧！')
        else:
            print('小啦，大一点嘛')
        if X>0:
            print('还有',X,'次机会，加油哦！')
        if X==0:
            print('猜错啦，机会用完啦，别灰心，可以再来嘛')
            print('正确答案是',Y)
print('----------分割线----------')
print('非常感谢你能游玩我的小游戏\n敬请期待下一版本，也可以再玩几次\n当前版本V0.3')
