from selenium import webdriver

browser=webdriver.PhantomJS()
browser.get("http://kns.cnki.net")
browser.implicitly_wait(10)

#javascript:void(0);
#<li id="SCOD" class="" onclick="CheckDBTag(this,'专利','SCOD',true);return false;"><a href="javascript:void(0);">专利</a></li>
submitElement=browser.find_element_by_id("SCOD")
submitElement.click()

textElememt=browser.find_element_by_id("txt_1_value1")
textElememt.clear()
textElememt.send_keys("2014")

submitElement1=browser.find_element_by_id("btnSearch")
submitElement1.click()
browser.implicitly_wait(5)



submitElement2014=browser.find_element_by_id("recommandconLink")
# print(len(submitElements20xx))
# submitElement2014=submitElements20xx[3]
submitElement2014.click()

browser.implicitly_wait(10)



with open("source.html","w") as f:
    f.write(browser.page_source)




print(browser.title)
