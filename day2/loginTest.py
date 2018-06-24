#如何把这个文件封装成一个登录方法
#python中类的关键字和java一样，是class
#python中方法也有一个关键字，是def，def是define的缩写，表示定义方法
#1.打开浏览器
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
#python中使用冒号代替java中的大括号
#在冒号后面敲回车，会自动缩进4个空格
#所有属于类中的语句都必须空4个空格
class Login:
    #def是方法的关键字，表示这是一个方法
    #loginWithDefaultUser，这是我们自己随意起的方法名，意思是使用默认账户登录
    #方法后面必须要有括号，可以用来声明参数
    #括号中默认有一个参数（self）,self表示类本身，类似与java中的this关键字
    #self参数后面会详细讲，暂时用不到这个self参数
    #方法的声明后面也有一个冒号，方法下面所有语句还要再缩进4个空格
    #这样登录功能的代码就被封装到loginWithDefaultUser()中了，以后只要写一句话调用这个方法即可登录网站了
    def loginWithDefaultUser(self,driver):
        # driver=webdriver.Chrome()
        #2.打开海盗商城网站
        driver.get("http://localhost")
        #3删除登录链接的target属性
        #python中字符串可以用单引号，也可以用双引号
        #字符串本身包含双引号，那么我们就在两边使用单引号
        driver.execute_script('document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")')
        #4点击登录按钮，跳转登录页面
        driver.find_element_by_link_text("登录").click()
        #5输入用户名
        driver.find_element_by_id("username").send_keys("fangyong")
        #6输入密码
        #ActionChains需要导包，导包快捷键alt+enter
        #ActionChains是一组动作和行为的意思
        #所以下面这句话的作用是实例化一个ActionChains对象，这个对象可以用来执行一组动作和行为
        #ActionChains actions=ActionChains(driver)
        #如果想使用键盘的任意控件，直接去Keys这个类中找
        #所有actions中的方法都必须以perform（）结尾才会被执行
        actions=ActionChains(driver)
        actions.send_keys(Keys.TAB).send_keys("123456").perform()
        #7点击登录按钮
        # actions.send_keys(Keys.ENTER).perform()
        #假如不支持回车登录，我们可以直接点登录按钮
        #假如也很难定位登录按钮，我们还可以用submit（）方法
        #用户名和密码是同时发送给后端服务器的
        #开发通过form表单把这些信息同时提交到服务器
        #可以用任何一个元素执行submit()方法，来提交表单中的所有数据
        #比如我们可以使用用户名来提交表单数据
        driver.find_element_by_id("username").submit()