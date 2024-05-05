from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"

cSerive = webdriver.ChromeService(executable_path=PATH)
driver = webdriver.Chrome(service=cSerive)
driver.get("https://techwithtim.net")
print(driver.title)