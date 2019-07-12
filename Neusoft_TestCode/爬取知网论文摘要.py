
# coding: utf-8

# ### 爬取知网论文摘要180篇

# In[112]:


#!/usr/bin/env Python
# coding=utf-8
import  os
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


# #### 窗口初始化

# In[113]:


def browser_init(isWait):
    options = webdriver.ChromeOptions()
    headers={'User-Agent':'Mozilla.5.0(Maxintosh;Intel Mac OS X 10_13_3) AppleWebKit/537.36(KHTMl,like Gecko) Chorme/65.0.3325.162 Safari/537.36'}
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': '/Users/28028/Documents/NEUsoft/爬虫文件'}
    options.add_experimental_option('prefs', prefs)

    browser = webdriver.Chrome()
    #print(browser)
    #browser.set_window_size(500,500)
    if isWait:
        browser.implicitly_wait(50)
    return browser

#无窗口访问
#chrome_options = Options()
#chrome_options.add_argument('--headless')
# driver = webdriver.Chrome('/usr/local/Sunanang/chromedriver/chromedriver',
#                         chrome_options=chrome_options)


# #### 写入文件

# In[114]:


def write_to_file(title,zhaiyao):
    fobj=open('/Users/28028/Documents/NEUsoft/爬虫文件'+title+'.txt','w')
    fobj.write(zhaiyao)
    fobj.close()


# #### 进入下一页

# In[115]:


def switchNextPage(page,browser):
    browser.switch_to_frame("iframeResult")
    time.sleep(5)
    #browser.find_element_by_link_text('下一页').click()
    if page==1:
        browser.find_element_by_xpath('//*[@id="ctl00"]/table/tbody/tr[3]/td/table/tbody/tr/td/div/a[9]').click()
    else:
        browser.find_element_by_xpath('//*[@id="ctl00"]/table/tbody/tr[3]/td/table/tbody/tr/td/div/a[11]').click()
    all_handles = browser.window_handles#获取所有窗口句柄          
    for handle in all_handles:#始终获得当前最后的窗口，所以要多次使用
            browser.switch_to_window(handle)


# #### 判断查找的该元素是否存在

# In[116]:


def isPresent(browser,self):
    try:
        browser.find_element_by_id(self) 
    except : 
        return False
    return True


# #### 获取摘要

# In[126]:


def get_abstract(page,browser):
    #此时窗口定位在iframe主窗口
    now_handle = browser.current_window_handle
    
    for i in range(0,20):#每页二十篇论文
        browser.switch_to_frame("iframeResult")
        time.sleep(5)
        browser.find_elements_by_class_name('fz14')[i].click()
        #browser.find_elements_by_xpath('//*[@id="ctl00"]/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/a').click()
        all_handles = browser.window_handles#获取所有窗口句柄          
        for handle in all_handles:#始终获得当前最后的窗口，所以要多次使用
            browser.switch_to_window(handle)
        #获取论文题目
       # title=browser.find_element_by_class_name('title').text
       # title=browser.find_element_by_xpath("//*[@id='mainArea']/div[3]/div[1]/h2").text
        title=str(20*(page-1)+i+1)
        if isPresent(browser,'ChDivSummary'):
            abstract=browser.find_element_by_xpath('//*[@id="ChDivSummary"]').text
        #写入文件，每篇论文一个TXT文件，论文题目作为文件名
            write_to_file(title,abstract)
            print ("第%d页第 %d 篇下载成功!!!" %(page, i+1))
        
        #关闭当前的窗口
        browser.close()
        #下载结束要回到主窗口继续下一篇
        browser.switch_to_window(now_handle)
        


# #### 搜索关键词

# In[118]:


def searchKey(keyword):
    now_handle = browser.current_window_handle

    Select(browser.find_element_by_id('txt_1_sel')).select_by_value("FT") #全文
    browser.find_element_by_id('txt_1_value1').send_keys(keyword) 
    browser.find_element_by_xpath('//*[@id="XuekeNavi_Div"]/div[1]/input[1]')#清除
    #browser.get("http://kns.cnki.net/kns/popup/Magazine_SelectSCDB.aspx?NameCtlID=magazine_value1&CodeCtlID=hidMagezineCode&DBNameLists=")#http://sd.ab22.top/KNS/brief/result.aspx?dbPrefix=CJFQ

    browser.find_element_by_xpath('//*[@id="E"]/a').click() #医药卫生科技
    browser.find_element_by_xpath("//*[@id='joursource_1']/a/img").click()#进入文献高级搜索
    all_handles = browser.window_handles#获取所有窗口句柄          

    for handle in all_handles:#始终获得当前最后的窗口，所以要多次使用
            browser.switch_to.window(handle)
    #browser.find_element_by_id('AllmediaBox').click() 
    browser.find_element_by_xpath('//*[@id="divConditionSCDB"]/div/p[2]/input').click() #定位收录来源
    Select(browser.find_element_by_id('dlSourceCJFQ')).select_by_value("0003") #选择sci科学引文库
    switchToFrame(browser)
    browser.find_element_by_xpath("//*[@id='iframe']/div[2]/a[1]").click()#下一页//*[@id="iframe"]/div[2]/a[1]
    #browser.find_element_by_id('chb_SJJY').click()
    browser.find_element_by_xpath('//*[@id="lbl_SJJY"]').click()
    browser.find_element_by_xpath('//*[@id="lbl_ZZAF"]').click()
    browser.find_element_by_xpath('//*[@id="lbl_CHIU"]').click()
    browser.find_element_by_xpath('//*[@id="lbl_CPPP"]').click()
    browser.find_element_by_xpath('//*[@id="lbl_FXKB"]').click()
    browser.find_element_by_xpath('//*[@id="lbl_ZDKX"]').click()
    browser.find_element_by_xpath('//*[@id="lbl_HKXS"]').click()
    browser.find_element_by_xpath('//*[@id="lbl_AIZH"]').click()
    browser.find_element_by_xpath('//*[@id="lbl_ZHAY"]').click()
    browser.find_element_by_xpath('//*[@id="lbl_ZHGC"]').click()
    browser.find_element_by_xpath('//*[@id="lbl_HXWL"]').click()
    browser.find_element_by_xpath('//*[@id="lbl_HXYW"]').click()
    browser.find_element_by_xpath('//*[@id="lbl_EDZX"]').click()
    browser.find_element_by_xpath('//*[@id="lbl_ZXYY"]').click()
    browser.find_element_by_xpath('//*[@id="lbl_ZGTR"]').click()
    browser.find_element_by_xpath('//*[@id="lbl_GFZK"]').click()
    browser.find_element_by_xpath('//*[@id="lbl_ZHSS"]').click()
    browser.find_element_by_xpath('//*[@id="lbl_GXKB"]').click()

    #关闭当前的窗口
    #browser.close()
    #下载结束要回到主窗口点击继续，释放iframe
    browser.switch_to.default_content()

    #browser.switch_to_window(now_handle)
    browser.find_element_by_id('ibtOk').click() 

    #browser.find_element_by_id('E').click() 
    #browser.find_element_by_id('btnSearch').click()
   
   


# #### 转化到子页面

# In[119]:


##知网论文详情页面被嵌套在了iframe子页面中，因此定位论文链接等元素时需要重新将窗口定位到子页面
def switchToFrame(browser):
    #方法一：该方法在本案例中会失败。。。
    #browser.switch_to.frame('iframeResult')
    browser.switch_to_frame("iframeResult")
    #iframe = browser.find_elements_by_tag_name('iframe')
    #browser.switch_to.frame(iframe) 
    #加上等待时间就好啦hhhhh
    time.sleep(5)
    #方法二：直接复制粘贴了子页面的链接，直接打开该链接，进入一个新窗口
    #第一页下载页的链接。QAQ
    #ziurl="http://kns.cnki.net/kns/brief/brief.aspx?pagename=ASP.brief_result_aspx&dbPrefix=CJFQ&dbCatalog=%e4%b8%ad%e5%9b%bd%e5%ad%a6%e6%9c%af%e6%9c%9f%e5%88%8a%e7%bd%91%e7%bb%9c%e5%87%ba%e7%89%88%e6%80%bb%e5%ba%93&ConfigFile=CJFQ.xml&research=off&t=1532939974530&keyValue=T%E6%A3%80%E9%AA%8C&S=1"
    #browser.get(ziurl)


# #### 主函数

# In[128]:


if __name__=="__main__":
    #初始化浏览器窗口
    browser=browser_init(True)
    #搜索关键词得到相应论文
    #searchKey('T检验')/
    url="http://kns.cnki.net/kns/brief/result.aspx?dbprefix=SCDB"
    browser.get(url)
    main_handle = browser.current_window_handle
    searchKey('T检验')
    #browser.switch_to_window(main_handle)
    print("search done!")
    browser.switch_to.window(main_handle)
    browser.find_element_by_id('btnSearch').click()#搜索
    page=1
    #总下载页数
    page_num=9
    while page<=page_num:   
        print('开始下载第 %d 页' %page )
        #获取摘要
        #print(browser.find_elements_by_class_name('fz14'))
        get_abstract(page, browser)#此时的窗口被定位为主窗口，该函数只负责下载该页的论文摘要，窗口会跳转到每篇论文详细介绍的子窗口 
        ###################
        #！！！注意！！！这里需要手动调整页面的显示范围，要让你准备定位的论文链接部分出现在窗口中，否则。。会失败QAQ
        #提供一个解决上述问题的链接：https://www.cnblogs.com/desperado0807/p/4956253.html
        #回到父页面，点击进入下一页
        switchNextPage(page,browser)
        #browser.switch_to_default_content()
        page=page+1  
    browser.quit()
    sleep(60)

