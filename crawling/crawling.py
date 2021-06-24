from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
import time

def maincrawling(keyword):
    url = "https://www.facebook.com/search/posts/?q=%s&sde=AbpC92W4Tk5CSRWpvFucDAgwoQ2gfVVMoruVxGcnOdkNfijX1G4VeLHZZ-EnQ0efWg6zxEoc9fii4P4dV05zM55j8iXbnj0pKLaEKctnRPAS4US5p7M6k4Fp-eLfhveWhJuF0cv4QOeSInYjSHv4dVDec8Y9-fp6-3LG3rHVWJ2CEBIpBbHttlepqOq0ONMyH0A9S8P4Z0pbFDRloMORLtxp-_Ol2JykorAkLsdNd4NJcPvaIII4N8TmBAhHZ414FArZ48w6A3mWL5lGM_nNlKzVHaSYBU2DQPVBcRHq1Ni2JI7I-Fq6RtzHS4gRuCLM6z-P5weqvUi4RtQP-pGHiwt1huE0xDOGeDTTjWesxsNYmJsVRYQJ77vE3Xq2-3N0D2w" % keyword
    path = "C:\project\SNS-wordcloud\server\crawling\chromedriver.exe"
    load_dotenv(verbose=True)
    id = os.getenv('FACEBOOK_ID')
    pw = os.getenv('FACEBOOK_PW')

    chrome_options = Options()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(path, options=chrome_options)
    driver.get(url)

    assert "Facebook" in driver.title
    time.sleep(3)
    login_box = driver.find_element_by_id("email")
    login_box.send_keys(id)
    login_box = driver.find_element_by_id("pass")
    login_box.send_keys(pw)

    xpath = '//*[@id="loginbutton"]'
    driver.find_element_by_xpath(xpath).click()

    time.sleep(3)
    driver.get(url)
    time.sleep(3)
    body = driver.find_element_by_css_selector('body') # send_keys()메서드 사용을 위한 body가져오기
    for i in range(100): # 11번 ~ 최하단 20번 
        body.send_keys(Keys.PAGE_DOWN) # 페이지 다운 키를  20회 반복한다.
        time.sleep(0.1) 
    html = driver.page_source
    return html