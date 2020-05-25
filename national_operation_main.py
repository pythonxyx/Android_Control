import uiautomator2 as u2
import time

while True:
    try:
        d = u2.connect()
        input('请确认模拟器已经打开，需要的应用程序已经安装完毕，回车键继续…')
        d.app_start('cn.xuexi.android')
        break
    except:
        print('设备未启动或APP未安装，请查看！')
        time.sleep(5)

def main():
    while True:
        print('*'*10+'欢迎使用本程序'+'*'*10+'\n\n')
        chosed = input('\n请输入你需要的操作(1-开始执行程序；2-修改登录密码；直接回车键退出程序！)：')
        if chosed == '1':
            if d(resourceId = 'cn.xuexi.android:id/home_bottom_tab_icon_group').exists:  #如果不需要登录
                print('马上开始阅读【推荐频道的文章】…')
                time.sleep(3)
                Reading_for_recommend()
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
                print('程序执行完毕！！，请自行选择听音乐获取视听分数！！')
            elif d(resourceId="cn.xuexi.android:id/et_pwd_login").exists:
                pass
            else:
                print('正在等待APP启动…')
                time.sleep(2)
        elif  chosed == 2:
            password = input('请输入新的密码，回车键保存：')
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
        print('文章《{}》已经打开，正在阅读中（请等待30秒的设置）…'.format(article_name_list[j]))
        time.sleep(30)
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
        print('文章《{}》已经打开，正在阅读中（请等待30秒的设置）…'.format(article_name_list[j]))
        time.sleep(30)
        d.xpath('//*[@resource-id="cn.xuexi.android:id/TOP_LAYER_VIEW_ID"]/android.widget.ImageView[1]').click()
    print('贵州频道文章阅读结束！')




# Reading_for_recommend()

Reading_for_guizhou()











