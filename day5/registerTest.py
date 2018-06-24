#1.导包
import unittest

import time
from selenium import webdriver
#2.继承unittest.TestCase
from selenium.webdriver.common.by import By

from day5.csvFileManager4 import CsvFileManager4


class RegisterTest(unittest.TestCase):
    #3.重写和setup和teardown方法
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(20)
        cls.driver.quit()

    #4.编写一个测试用例方法，以test开头的方法
    def test_register(self):
        for row in CsvFileManager4().read('testdata.csv'):
            driver = self.driver
            driver.get("http://localhost/index.php?m=user&c=public&a=reg")
            #这两种方法没有任何区别，但是后面这中方法扩展性更高，便于框架封装
            #driver.find_element_by_name("username")
            driver.find_element(By.NAME,"username").send_keys(row[0])
            driver.find_element(By.NAME,"password").send_keys(row[1])
            driver.find_element(By.NAME,"userpassword2").send_keys(row[2])
            driver.find_element(By.NAME,"mobile_phone").send_keys(row[3])
            driver.find_element(By.NAME,"email").send_keys(row[4])
            # driver.find_element(By.CLASS_NAME,"reg_btn").click()
            #在for循环中执行测试用例，虽然解决批量执行问题，但是如果第一行测试用例执行失败，后续的用例不会继续执行
            #异常情况，输入完邮箱后，按tab键，检查提示信息是否都是“信息通过验证！”
            #如果页面上提示的信息是“通过信息验证！”，那么测试通过，否则失败
            check_tip = driver.find_element(By.CSS_SELECTOR,"form > ul > li:nth-child(1) > div > span").text
            print(check_tip)
            #其中check_tip是执行用例时，从网页抓取的信息
            #“通过信息验证！”是来自于手工测试用例，是测试用例执行前的期望结果
            # if check_tip =="通过信息验证！":
            #     print("测试通过")
            # else:
            #     print("测试失败")
                #这样通过if...else语句就可以自动判断测试用例的执行通过情况了
                #断言的写法
            self.assertEqual("通过信息验证！",check_tip)
            #虽然第一行测试数据执行失败了，但是后面的测试数据是不依赖于前面的，不应该因为第一条失败，就导致其他行数据不执行测试
            #所以我们不应该用for循环的方式执行不同的测试数据，因为在方法中谢了for循环，虽然执行了多次，但是unittest仍然认为它是一条测试用例，一旦断言失败，就会终止这条测试用例
            #所以我们应该采用ddt框架实现数据驱动


if __name__ == '__main__':
    unittest.main()