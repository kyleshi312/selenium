from selenium import webdriver
#1打开主页
driver=webdriver.Chrome()
driver.get("http://localhost")
#2点击登陆按钮
driver.find_element_by_link_text("登录").click()
#3在搜索框输入iphone
driver.find_element_by_name("keyword").send_keys("iphone")
#如果我们想在新的标签页上操作页面元素
#需要进行窗口切换
#driver.switch_to.window(第二个窗口的名字)
#如何获取第二个窗口的名字
#selenium提供了浏览器中所有窗口的名字的集合
#handle是句柄的意思，理解为名字就可以了
#driver.window_handles可以理解为一个数组，求第二个窗口的名字
#所以第二个窗口的名字就是driver.window_handles[1]
#所以窗口切换的语句就是
driver.switch_to.window(driver.window_handles[-1])
driver.find_element_by_name("keyword").send_keys("iphone")
#[1]表示第二个元素，[-1]表示最后一个元素
#在python中元组和列表可以正着从0开始数，也可以负着从-1开始数，倒数第一个是-1，倒数第二个是-2