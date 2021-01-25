# X:玩家拥有的猜测机会
# Y:正确答案
X =  3
import random
Y = random.randint(1,10)
while X>0:
    temp = input('不妨猜猜老阿姨心里的数字:')
    guess = int(temp)
    if guess==Y:
        print('猜对啦！\n你是老阿姨心里的那个人吧！\n就把老阿姨嫁给你啦!')
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
print('其实\n不管怎样\n老阿姨一直都是你的哦！')