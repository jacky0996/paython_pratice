from operator import truediv
import random
error = 0

# 定義函數
def expressive_function():
    global expressive 
    expressive = int(input("請輸入表述能力(請輸入1~10之間)："))
def Performance_function():
    global Performance 
    Performance = int(input("請輸入表演能力(請輸入1~10之間)："))


while True:
    expressive_function()
    if expressive >10:
        print('原來我在你眼裡這麼會說話,Luv U !!')
        error +=1
    elif expressive <1:
        print('原來我在你眼裡這麼不會說話,哭哭...')
        error +=1
    else:
        break 

while True:
    Performance_function()
    if Performance >10:
        print('你一定是我的鐵粉,Luv U !!')
        error +=1
    elif Performance <1:
        print('對不起,長期困擾你的耳朵這麼久,ㄅ歉...')
        error +=1
    else:
        break 



if error >=4:
    print('你一定亂填了很多次答案,你這個小壞壞,但還是謝謝你點開了我的程式^^,88,直接關閉視窗就可以了~')
    input()
    
elif error<4:
    if Performance<5 and expressive<5:
        print('我們應該不是很熟吧~或者你認為我其實不太會說話,也不大會唱歌,但我很喜歡音樂,我有分享很多cover跟歌曲在我的頁面上,希望哪天會有你喜歡的,謝啦,88直接關閉視窗就可以了~')
        input()
    elif Performance == 5 and expressive == 5:
        print('我們應該認識不久或者每次其實都沒有很深入的了解對方吧,開玩笑的,我覺得平均的配分也很棒,即便沒有深入的了解對方,能夠默默的關心也不錯,希望未來我們會有機會更認識對方,有空再一起聽歌玩音樂,謝啦,88,直接關閉視窗就可以了~')
        input()
    elif Performance<5 and expressive>5:
        print('我們應該說了非常多的話,不論我們之間是相談甚歡還是單方面的聽對方分享事情,總之我很喜歡這種相處模式,也謝謝你告訴我這麼多事情,謝啦,88,直接關閉視窗就可以了~')
        input()
    elif Performance>5 and expressive<5:
        print('你應該比較常聽到我唱歌,或者喜歡我唱歌大於分享事情,音樂是我人生中很重要的東西,我也把我的情感投注在每一次的cover上,希望我有唱到你喜歡的歌,如果你有向我點過歌但我還沒唱的話,抱歉,我最近真的小忙,沒什麼時間練習,我會盡快補上的,謝啦,88,直接關閉視窗就可以了~')
        input()
    elif Performance>5 and expressive>5:
        print('我們應該已經認識好一段時間了吧,才會讓你對我的評價這麼高,不管你是誰,我都很感謝我們之間的相處,我知道我有很多小缺點,有的時候心直口快不小心說出不恰當的話,但總之非常謝謝你對我的包容,希望我們之間的友誼能夠長存,真的由衷感謝,88,直接關閉視窗就可以了~')
        input()

