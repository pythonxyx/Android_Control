import uiautomator2 as u2
import time

def main(password='1986122'):
    while True:
        chosed = input('\n请输入你需要的操作(1-开始执行程序；直接回车键退出程序！)：')
        if chosed == '1':
            while True:
                if d(resourceId = 'cn.xuexi.android:id/home_bottom_tab_icon_group').exists:  #如果不需要登录
                    print('马上开始阅读【推荐频道的文章】…')
                    d.swipe(0, 240, 0, 400)  #  模拟刷新界面
                    time.sleep(5)
                    d.swipe(0, 340, 0, 146)
                    time.sleep(3)
                    Reading_for_recommend()  #  循环阅读获取的推荐频道文章
                    print('正在进入贵州频道…')
                    time.sleep(3)
                    while not d(text="贵州").exists:
                        print('正在等待主界面显示…')
                        time.sleep(2)
                    d(text="贵州").click()
                    print('马上开始阅读【贵州频道的文章】…')
                    time.sleep(3)
                    Reading_for_guizhou()
                    print('正在操作贵州平台…')
                    while not d.xpath('//android.support.v7.widget.RecyclerView'
                                      '/android.widget.LinearLayout[1]'
                                      '/android.widget.ImageView[1]').exists:
                        print('正在等待主界面显示…')
                        time.sleep(2)
                    d.xpath('//android.support.v7.widget.RecyclerView'
                            '/android.widget.LinearLayout[1]'
                            '/android.widget.ImageView[1]').click()
                    while not d(text="贵州头条").exists:
                        print('正在等待【贵州学习平台】界面显示…')
                        time.sleep(2)
                    time.sleep(3)
                    d.press("back")
                    time.sleep(3)
                    while True:
                        chosed1 = input('是否需要在程序内对文章进行评论？（1-是；回车键跳过）：')
                        if chosed1 == '1':
                            time.sleep(2)
                            while not  d(text="推荐").exists:
                                print('未找到推荐按钮，请确认界面存在！！')
                                time.sleep(3)
                            d(text="推荐").click()
                            while not d.xpath('//android.widget.ListView/android.widget.FrameLayout[2]'
                                              '/android.widget.LinearLayout[1]'
                                              '/android.widget.LinearLayout[1]'
                                              '/android.widget.TextView[1]').exists:
                                continue
                            time.sleep(3)
                            d.swipe(0, 340, 0, 146)
                            time.sleep(3)
                            article_name_list_for_comment = Get_article_name()
                            article_comment(article_name_list_for_comment)
                        else:
                            break
                    input('\n\n程序执行完毕！！，请自行选择听音乐获取视听分数！！\n\n回车键继续…')
                    break
                elif d(resourceId="cn.xuexi.android:id/et_pwd_login").exists:
                    print('找到登录界面，正在登录…')
                    d(resourceId="cn.xuexi.android:id/et_pwd_login").set_text(password)
                    time.sleep(3)
                    d(resourceId="cn.xuexi.android:id/btn_next").click()
                    continue
                else:
                    print('正在等待APP启动…')
                    time.sleep(2)
        else:
            break


# 定义一个函数来获取并阅读推荐栏目的文章
def Reading_for_recommend():
    article_name_list = []
    for name in d.xpath('cn.xuexi.android:id/general_card_title_id').all():
        article_name_list.append(name.text)
    for j in range(len(article_name_list)):
        d.xpath('//*[@text="{}"]'.format(article_name_list[j])).click()
        while not d.xpath('//*[@resource-id="xxqg-article-header"]/android.view.View[1]').exists:
            print('正在等待文章界面打开…')
            time.sleep(2)
        print('文章《{}》已经打开，正在阅读中（请等待2分钟）…'.format(article_name_list[j]))
        time.sleep(120)
        if j < 2:
            shoucang = '//*[@resource-id="cn.xuexi.android:id/BOTTOM_LAYER_VIEW_ID"]/android.widget.ImageView[1]'
            d.xpath(shoucang).click()
        time.sleep(2)
        if '每日金句' in article_name_list[j]:
            shoucang = '//*[@resource-id="cn.xuexi.android:id/BOTTOM_LAYER_VIEW_ID"]/android.widget.ImageView[1]'
            d.xpath(shoucang).click()
            share = '//*[@resource-id="cn.xuexi.android:id/BOTTOM_LAYER_VIEW_ID"]/android.widget.ImageView[2]'
            share_text = '//android.widget.GridView/android.widget.RelativeLayout[2]/android.widget.ImageView[1]'
            share_plat = '//android.widget.GridView/android.widget.RelativeLayout[1]/android.widget.ImageView[1]'
            d.xpath(share).click()
            time.sleep(2)
            while not d(resourceId="cn.xuexi.android:id/share_box_title").exists:
                print('正在等待分享界面显示…')
                time.sleep(2)
            d.xpath(share_text).click()
            time.sleep(2)
            d.xpath(share).click()
            while not d(resourceId="cn.xuexi.android:id/share_box_title").exists:
                print('正在等待分享界面显示…')
                time.sleep(2)
            d.xpath(share_plat).click()
            while not d(resourceId="cn.xuexi.android:id/tv_recent_conversation").exists:
                print('正在等待分享联系人界面打开…')
                time.sleep(2)
            time.sleep(3)
            d.xpath('//*[@content-desc="返回"]').click()
        d.xpath('//*[@resource-id="cn.xuexi.android:id/TOP_LAYER_VIEW_ID"]/android.widget.ImageView[1]').click()
    print('推荐频道文章阅读结束！')

# 定义一个函数来阅读贵州频道的文章
def Reading_for_guizhou():
    article_name_list = []
    for name in d.xpath('cn.xuexi.android:id/general_card_title_id').all():
        article_name_list.append(name.text)
    for j in range(len(article_name_list)):
        d.xpath('//*[@text="{}"]'.format(article_name_list[j])).click()
        while not d.xpath('//*[@resource-id="xxqg-article-header"]/android.view.View[1]').exists:
            print('正在等待文章界面打开…')
            time.sleep(2)
        print('文章《{}》已经打开，正在阅读中（请等待1分钟）…'.format(article_name_list[j]))
        time.sleep(60)
        d.xpath('//*[@resource-id="cn.xuexi.android:id/TOP_LAYER_VIEW_ID"]/android.widget.ImageView[1]').click()
    print('贵州频道文章阅读结束！')


#  定义一个函数用来获取并返回推荐频道的文章名称
def Get_article_name():
    tmplist = []
    for name in d.xpath('cn.xuexi.android:id/general_card_title_id').all():
        tmplist.append(name.text)
    return tmplist


def article_comment(tmplist):
    while True:
        print('获取到的推荐文章如下：')
        for i in range(len(tmplist)):
            print(i + 1, '---', tmplist[i])
        try:
            n = int(input('请选择要评论的文章(0-返回主界面)：'))
        except:
            print('\n\n***提示：请输入数字，要退出请输入0后,再按回车键！！***\n\n')
            continue
        if n == 0:
            break
        elif n > 0 and n <= len(tmplist):
            print('你选择的文章如下：')
            print('\n【文章标题】：《{}》'.format(tmplist[n - 1]))
            d.xpath('//*[@text="{}"]'.format(tmplist[n - 1])).click()
            while not d.xpath('//*[@resource-id="xxqg-article-content"]'
                              '/android.view.View[1]'
                              '/android.view.View[1]'
                              '/android.view.View[2]').exists:
                continue
            print('\n【文章内容】：')
            for i in d.xpath('//*[@resource-id="xxqg-article-body"]//*').all():
                if i.text:
                    print('    ' + i.text + '\n')
                else:
                    pass
            content = input('请输入你的评论内容(直接回车键返回)：')
            if content:
                print('正在评论，请等待…')
                time.sleep(3)
                d(text="欢迎发表你的观点").click()
                time.sleep(2)
                d(className='android.widget.EditText').clear_text()
                d.set_fastinput_ime(True)
                d.send_keys(content)
                d.set_fastinput_ime(False)
                time.sleep(3)
                d.xpath('//*[@text="发布"]').click()
                time.sleep(5)
                print('评论成功！')
                d.press("back")
                continue
            else:
                d.xpath('//*[@resource-id="cn.xuexi.android:id'
                        '/TOP_LAYER_VIEW_ID"]'
                        '/android.widget.ImageView[1]').click()
                continue
        else:
            input('输入的文章范围不对吧？？回车键继续…')
            continue




while True:
    try:
        d = u2.connect()
        print('*' * 10 + '欢迎使用本程序' + '*' * 10 + '\n\n')
        input('模拟器已经打开，请确认需要的应用程序已经安装，回车键继续…')
        password = input('是否需要修改默认密码？（需要请直接输入，直接回车键跳过）：')
        if password:
            main.__defaults__ = (password,)
        d.app_start('cn.xuexi.android')
        break
    except:
        print('设备未启动或APP未安装，请查看！')
        time.sleep(5)
main()

# d = u2.connect()
# article_name_list_for_comment = Get_article_name()
# article_comment(article_name_list_for_comment)








