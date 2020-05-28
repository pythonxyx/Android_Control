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


# printAllnew()

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

# def article_comment(tmplist):
#     while True:
#         print('获取到的推荐文章如下：')
#         for i in range(len(tmplist)):
#             print(i+1,'---',tmplist[i])
#         try:
#             n=int(input('请选择要评论的文章(0-返回主界面)：'))
#         except:
#             print('\n\n***提示：请输入数字，要退出请输入0后回车键！！***\n\n')
#             continue
#         if n == 0:
#             break
#         elif n>0 and n<=len(tmplist):
#             print('你选择的文章如下：')
#             print('\n文章标题：《{}》'.format(tmplist[n-1]))
#             content = input('请输入你的评论内容(直接回车键返回)：')
#             if content:
#                 print('正在评论，请等待…')
#                 time.sleep(2)
#                 d.xpath('//*[@text="{}"]'.format(tmplist[n-1])).click()
#                 while not d.xpath('//*[@resource-id="xxqg-article-header"]/android.view.View[1]').exists:
#                     continue
#                 time.sleep(3)
#                 d(text="欢迎发表你的观点").click()
#                 time.sleep(2)
#                 d(className='android.widget.EditText').clear_text()
#                 d.set_fastinput_ime(True)
#                 d.send_keys(content)
#                 d.set_fastinput_ime(False)
#                 time.sleep(3)
#                 d.xpath('//*[@text="发布"]').click()
#                 time.sleep(3)
#                 print('评论成功！')
#                 d.press("back")
#                 continue
#             else:
#                 continue
#         else:
#             input('输入的文章范围不对吧？？回车键继续…')
#             continue
#
# def Get_article_name():
#     tmplist = []
#     for name in d.xpath('cn.xuexi.android:id/general_card_title_id').all():
#         tmplist.append(name.text)
#     return tmplist
#
#
# while True:
#     chosed1 = input('是否需要在程序内对文章进行评论？（1-是；回车键跳过）：')
#     if chosed1 == '1':
#         time.sleep(2)
#         d(text="推荐").click()
#         while not d.xpath('//android.widget.ListView/android.widget.FrameLayout[2]'
#                           '/android.widget.LinearLayout[1]'
#                           '/android.widget.LinearLayout[1]'
#                           '/android.widget.TextView[1]').exists:
#             continue
#         time.sleep(3)
#         d.swipe(0, 340, 0, 146)
#         time.sleep(3)
#         article_name_list_for_comment = Get_article_name()
#         article_comment(article_name_list_for_comment)
#     else:
#         break
# input('\n\n程序执行完毕！！，请自行选择听音乐获取视听分数！！\n\n回车键继续…')
tmplist1 = []
# for i in d.xpath('//*[@resource-id="xxqg-article-content"]//*').all():
#     tmplist1.append(i.text)
# print(tmplist1)
# newtmplist1 = []
# for j in range(len(tmplist1)):
#     if tmplist1[j]:
#         newtmplist1.append(tmplist1[j])
#     else:
#         pass
# # print(newtmplist1)
# if '责任编辑' in newtmplist1[5]:
#     print('纯图片')
# else:
#     print(newtmplist1[5])

# while not d.xpath('//*[@resource-id="xxqg-article-footer"]/android.view.View[1]/android.view.View[2]').exists:
#     d.swipe(0,300,0,0)

# print(list(d.xpath('//*[@resource-id="xxqg-article-body"]').rect))

for i in d.xpath('//*[@resource-id="xxqg-article-body"]//*').all():
    if i.text:
        print('    '+i.text+'\n')
    else:
        pass
