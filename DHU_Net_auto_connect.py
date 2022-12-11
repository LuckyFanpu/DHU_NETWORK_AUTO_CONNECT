from msedge.selenium_tools import Edge, EdgeOptions
options = EdgeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
options.use_chromium = True
options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" # 浏览器的位置
driver = Edge(options=options, executable_path=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe") # 相应的浏览器的驱动位置

driver.get("http://www.firefox.com.cn")

# 键入账号，需要修改成自己的账号密码
driver.find_element_by_id("userphone").send_keys("username")
driver.find_element_by_id("password").send_keys("pwd")
driver.find_element_by_id("mobilelogin_submit").click()