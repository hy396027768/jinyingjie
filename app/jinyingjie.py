import datetime
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver


a = 0


def get_cookie(threadName):
    lock.acquire()
    print('浏览器', threadName+1, '，开启成功')
    lock.release()
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-gpu')
    option.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=option)
    # driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.get('http://www.jinyingjie.com/ShoppingCart/checkPurchasedItemsInfo/professionid/45/itemtype/jinyinglive/itemcount/1/itemid/1013_2788-2967-2968-2969-2970-2971-2972-2973-2974-2975-2976/shoppingFestival11/1/section_type/3')
    time.sleep(0.5)
    # try:
    driver.find_elements_by_class_name('Btn')[1].click()
    time.sleep(0.4)
    driver.find_element_by_id('loginname').send_keys('13682226465')
    driver.find_element_by_id('password').send_keys('laiyujie11')
    time.sleep(0.2)
    driver.find_element_by_id('login').click()
    time.sleep(2)
    while True:
        try:
            driver.find_element_by_id('totalPayableAmountSpan_2').text
            break
        except:
            driver.quit()
            driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=option)
            # driver = webdriver.Chrome(executable_path='./chromedriver')
            driver.get(
                'http://www.jinyingjie.com/ShoppingCart/checkPurchasedItemsInfo/professionid/45/itemtype/jinyinglive/itemcount/1/itemid/1013_2788-2967-2968-2969-2970-2971-2972-2973-2974-2975-2976/shoppingFestival11/1/section_type/3')
            time.sleep(0.5)
            # try:
            driver.find_elements_by_class_name('Btn')[1].click()
            time.sleep(0.4)
            driver.find_element_by_id('loginname').send_keys('13682226465')
            driver.find_element_by_id('password').send_keys('laiyujie11')
            time.sleep(0.2)
            driver.find_element_by_id('login').click()
            time.sleep(2)


    global a
    while True:

        now = datetime.datetime.now()
        if now.day == 10 and now.hour == 23 and now.minute == 58 or True:
            while True:
                try:
                    totlePay = driver.find_element_by_id('totalPayableAmountSpan_2').text
                    break
                except:
                    driver.refresh()
            lock.acquire()
            a = a + 1
            print('价钱%s，第' % totlePay, threadName+1, '个浏览器执行第', str(a)+'次刷新')
            lock.release()
            if totlePay == '¥5480.00':
                driver.find_element_by_id('submitBtn').click()
                print('已下单，请支付')
                driver.quit()
            else:
                driver.refresh()

        elif now.day == 11 and now.hour == 00 and now.minute == 2:
            break


th = ThreadPoolExecutor()
lock = threading.Lock()

for i in range(8):
    th.submit(get_cookie, i)
