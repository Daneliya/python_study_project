from selenium import webdriver
from selenium.webdriver.common.by import By  # 导入 By 模块
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 使用 Edge 浏览器
# driver = webdriver.Edge(executable_path='/msedgedriver.exe')
# 手动指定驱动程序路径
# driver = webdriver.Edge(r'C:\Users\ek\Downloads\edgedriver_win64\msedgedriver.exe')
# 当前路径下的驱动
driver = webdriver.Edge()

try:
    # 打开百度首页
    driver.get("https://www.baidu.com")

    # 获取页面标题
    print(driver.title)

    # 查找搜索框元素
    search_box = driver.find_element(By.ID, "kw")

    # 输入搜索内容
    search_box.send_keys("Selenium Python")

    # 提交搜索表单
    search_box.send_keys(Keys.RETURN)

    # 等待搜索结果加载
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "content_left"))
    )

    # 打印页面标题
    print("页面标题是:", driver.title)

finally:
    # 关闭浏览器
    driver.quit()
