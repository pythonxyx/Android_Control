import uiautomator2 as u2
import os
import time

d = u2.connect()
# print(d.info)

def printAll():
    for i,v in enumerate(d.xpath('//*').all()):
        if v.text!='':
            print("【{0:0=4}】{1}".format(i,v.text))

def printAllnew():
    for i,v in enumerate(d.xpath('//android.widget.ListView/android.widget.FrameLayout//android.widget.LinearLayout//*').all()):
        if v.text!='':
            print("【{0:0=4}】{1}".format(i,v.text))


printAllnew()

# xp = "//*[re:match(@text, '^全部播放')]"
# d.xpath(xp).click()
# printAll()
# d.press('back')
tmplist=[]
# for v in d.xpath('//*').all():
#     tmplist.append(v.text)
# print(tmplist)
# if '登录' in tmplist:
#     print('已找到登录界面！')


#
# for v in d.xpath('cn.xuexi.android:id/general_card_title_id').all():
#     print(v.text)
# t='贵阳2035年基本实现食品安全领域治理体系和治理能力现代化'
# xp = "//*[re:match(@text, '^{}')]".format(t)
# d.xpath(xp).click()
# 判断界面是否已经显示
# while not d.xpath('//*[@resource-id="xxqg-article-header"]/android.view.View[1]').exists:
#     print('正在等待界面显示…')
#     time.sleep(3)
#     i = os.system('cls')
# print('界面已经显示！')

# n = 'cn.xuexi.android:id/tv_search_marquee'
# n1 = '//*[@text="欢迎发表你的观点"]'
#
# d.xpath('//*[@text="坚决"]').clear_text()

#评论性文字输入
# d.set_fastinput_ime(True)
# d.send_keys('坚决夺取脱贫攻坚战全面胜利！')
# d.set_fastinput_ime(False)
# # d.xpath('//*[@text="发布"]').click()

# 清空评论去文字！
# d(className='android.widget.EditText').clear_text()

# d(text="贵州").click()

# for v in d(className='android.widget.TextView').all():
#     print(v.text)

# d(resourceId="cn.xuexi.android:id/et_pwd_login").set_text('1986122')


# d(scrollable=True).scroll.to(description='//*[@text="全国学习平台"]')
# d(scrollable=True).scroll.forward.to(description="36,1180")


# def sample(x=1):
#     print(x)
#
# sample()
# sample()
# sample.__defaults__ = (2,)
# sample()
# sample()

# d.swipe(0, 1076, 0, 0)