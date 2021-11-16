
import pandas as pd
import time
from selenium.webdriver import Chrome

driver = Chrome()
driver.get('https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner#tab4')
time.sleep(1)
js = 'document.documentElement.scrollTop = 200'
driver.execute_script(js)
driver.find_element_by_xpath('//*[@id="ptab-0"]/div[2]/div[2]/div[3]/div/span').click()
time.sleep(1)
i = 1
dict1 = {}
while i <= 39:
    dict2 = {}
    regions = driver.find_element_by_xpath(f'//*[@id="ptab-0"]/div[2]/div[2]/div[2]/a[{i}]/div/div[1]/div/span[1]').text
    # links = driver.find_element_by_xpath('//*[@id="ptab-0"]/div[2]/div[2]/div[2]/a[1]').get_attribute('href')
    # print(links)
    print(regions+'\t',end=" ")
    j = 3
    driver.find_element_by_xpath(f'//*[@id="ptab-0"]/div[2]/div[2]/div[2]/a[{i}]/div/div[1]/div/span[1]').click()
    while j > 0:
        name = driver.find_element_by_xpath(f'//*[@id="ptab-0"]/div[2]/div/div[1]/div[{j}]/p[1]').text
        num = driver.find_element_by_xpath(f'//*[@id="ptab-0"]/div[2]/div/div[1]/div[{j}]/p[2]').text
        j -= 1
        print(name + ":" + num, end=" ")
        dict2[name]=num
    x = 1
    while x <= 3:
        name2 = driver.find_element_by_xpath(f'//*[@id="ptab-0"]/div[2]/div/div[2]/div[{x}]/p[1]').text
        num2 = driver.find_element_by_xpath(f'//*[@id="ptab-0"]/div[2]/div/div[2]/div[{x}]/p[2]').text
        x += 1
        print(name2 + ":" + num2, end=" ")
        dict2[name2]=num2
    i += 1
    dict1[regions] = dict2
    driver.find_element_by_xpath('//*[@id="main"]/div/div/header/div[2]/div').click()
    driver.find_element_by_xpath('//*[@id="ptab-0"]/div[2]/div[2]/div[3]/div/span').click()
    print('\n')

print(dict1)
data = pd.Series(dict1)
print(data)
data.to_csv('疫情信息统计.csv')