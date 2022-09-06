from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
PATH = "C:\Program Files\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://erp.iitkgp.ac.in/SSOAdministration/login.htm?sessionToken=D70E5CA42EBEFD39B691DB12EE50F2AE.worker1&requestedUrl=https://erp.iitkgp.ac.in/IIT_ERP3/")
driver.maximize_window()
user_id = driver.find_element_by_id("user_id")
user_id.send_keys("roll no")
password = driver.find_element_by_id("password")
password.send_keys("passwrd")
time.sleep(1)
ques = driver.find_element_by_id("question")
question = ques.text
ans = driver.find_element_by_id("answer")
if question == "favourite colour":
    ans.send_keys("ans")
elif question == "brothers name":
    ans.send_keys("ans")
else:
    ans.send_keys("ans")
time.sleep(1)

driver.find_element_by_id("loginFormSubmitButton").click()
'''
academic = driver.find_element_by_xpath('//*[@id="moduleUL"]/li[1]/a/strong')
academic.click()
time.sleep(1)
details = driver.find_elements_by_class_name("text-primary")
UG = details[len(details)-1]
actions = ActionChains(driver)
actions.move_to_element(UG).perform()
time.sleep(1)
UG.click()
time.sleep(1)
activities = driver.find_elements_by_class_name("text-default")
for activity in activities:
    if activity.text == "Student Academic Activities (UG)":
        activity.click()
        break
time.sleep(3)
driver.back()
driver.back()
'''
driver.implicitly_wait(1)
CDC = driver.find_element_by_css_selector("a[href*='menulist.htm?module_id=26']")
CDC.click()
time.sleep(0.5)
student = driver.find_element_by_class_name("text-primary")
student.click()
time.sleep(0.5)
AFI = driver.find_elements_by_class_name("text-default")[0]
AFI.click()
driver.implicitly_wait(2)
driver.switch_to.frame("myframe")
# driver.execute_script("window.scrollBy(0,925)", "")
html = driver.find_element_by_id('grid37')
# companies = driver.find_elements_by_xpath('/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr/td/div[2]/div[3]/div[3]/div/table/tbody/tr/td[2]/a')
c = 1
while True:
    companies = driver.find_elements_by_id(str(c))
    if len(companies)!=0:
        tds = companies[0].find_elements_by_tag_name('td')
        print(c,tds[1].text)
        c += 1
    else:
        html.send_keys(Keys.PAGE_DOWN)
        html.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        if len(driver.find_elements_by_id(str(c)))!=0:
            continue
        else:
            break
time.sleep(3)
driver.close()