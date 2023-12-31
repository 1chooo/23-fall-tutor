# %% [markdown]
# # ActionChains
# 行為鍊
# 
# ## 匯入工具
# 加入行為鍊 ActionChains (在 WebDriver 中模擬滑鼠移動、點繫、拖曳、按右鍵出現選單，以及鍵盤輸入文字、按下鍵盤上的按鈕等)
# 
# ```from selenium.webdriver.common.action_chains import ActionChains```
# 
# ## 基本用法
# | 方法               | 說明                |
# | :------------------ | :------------------ |
# | click(on_element=None) | 單擊滑鼠左鍵 |
# | click_and_hold(on_element=None) | 點選滑鼠左鍵，不鬆開 |
# | context_click(on_element=None) | 點選滑鼠右鍵 |
# | double_click(on_element=None) | 雙擊滑鼠左鍵 |
# | drag_and_drop(source, target) | 拖拽到某個「元素」然後鬆開 |
# | drag_and_drop_by_offset(source, xoffset, yoffset) | 拖拽到某個「座標」然後鬆開 |
# | key_down(value, element=None) | 按下某個鍵盤上的鍵 |
# | key_up(value, element=None) | 鬆開某個鍵 |
# | move_by_offset(xoffset, yoffset) | 滑鼠從當前位置移動到某個座標 |
# | move_to_element(to_element) | 滑鼠移動到某個元素 |
# | move_to_element_with_offset(to_element, xoffset, yoffset) | 移動到距某個元素（左上角座標）多少距離的位置 |
# | pause(seconds) | 暫停動作一段時間 |
# | perform() | 執行鏈中的所有動作 |
# | release(on_element=None) | 在某個元素位置鬆開滑鼠左鍵 |
# | send_keys(keys_to_send) | 傳送某個鍵到當前焦點的元素 |
# | send_keys_to_element(element, keys_to_send) | 傳送某個鍵到指定元素 |
# 
# ## 寫法
# - 鍊式
# 
# ```Python
# ActionChains(driver).move_to_element( web_element ).click( web_element ).perform()
# ```
# 
# 或是
# 
# ```Python
# action_chains = ActionChains(driver)
# action_chains.move_to_element( web_element ).click( web_element ).perform()
# ```
# 
# 
# - 分步
# 
# ```Python
# action_chains = ActionChains(driver)
# action_chains.move_to_element( web_element )
# action_chains.click( web_element )
# action_chains.perform()
# ```
# 
# ## 補充: 切換目前到 iframe 當中
# - 取得網頁上的 iframe
# 
# `iframe = driver.find_element(By.CSS_SELECTOR, "iframe#game-iframe")`
# 
# - 切換到 iframe 當中
# 
# `driver.switch_to.frame(iframe)`
# 
# - 回到主框架
# 
# `driver.switch_to.default_content()`
# 
# 
# ## 參考資料
# - [Selenium的ActionChains Api介面詳解](https://www.796t.com/article.php?id=325399 "Selenium的ActionChains Api介面詳解")
# - [python selenium滑鼠鍵盤操作（ActionChains）](https://www.796t.com/article.php?id=94198 "python selenium滑鼠鍵盤操作（ActionChains）")
# - [行為鏈](https://python-selenium-zh.readthedocs.io/zh_CN/latest/7.2%20%E8%A1%8C%E4%B8%BA%E9%93%BE/ "行為鏈")
# - [ActionChains In Selenium](https://medium.com/@kavidhanda/actionchains-in-selenium-cde43dee0111 "ActionChains In Selenium")
# - [Selenium 4.1.0 documentation - selenium.webdriver.common.action_chains](https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.action_chains.html "Selenium 4.1.0 documentation - selenium.webdriver.common.action_chains")

# %%
'''
匯入工具

備註: 每次執行以下任一範例前，都要執行一次"匯入工具"的 cell
'''

# 操作 browser 的 API
from selenium import webdriver

# 期待元素出現要透過什麼方式指定，通常與 EC、WebDriverWait 一起使用
from selenium.webdriver.common.by import By

# 加入行為鍊 ActionChain (在 WebDriver 中模擬滑鼠移動、點繫、拖曳、按右鍵出現選單，以及鍵盤輸入文字、按下鍵盤上的按鈕等)
from selenium.webdriver.common.action_chains import ActionChains

# 加入鍵盤功能 (例如 Ctrl、Alt 等)
from selenium.webdriver.common.keys import Keys

# 強制等待 (執行期間休息一下)
from time import sleep

# 啟動瀏覽器工具的選項
my_options = webdriver.ChromeOptions()
# my_options.add_argument("--headless")                #不開啟實體瀏覽器背景執行
my_options.add_argument("--start-maximized")         #最大化視窗
my_options.add_argument("--incognito")               #開啟無痕模式
my_options.add_argument("--disable-popup-blocking") #禁用彈出攔截
my_options.add_argument("--disable-notifications")  #取消通知

# 指定 chromedriver 檔案的路徑
my_executable_path = './chromedriver.exe'

# 使用 Chrome 的 WebDriver
driver = webdriver.Chrome( 
    options = my_options, 
    executable_path = my_executable_path
)

# %%
'''
範例 1: 對特定座標連續點擊
'''

# 移動滑鼠和連續點繫
driver.get('https://www.crazygames.com/game/planet-clicker-2')

# 建立行為鍊
ac = ActionChains(driver)

# 移到指定座標 (從 0,0 開始)
ac.move_by_offset(928, 369)

# 點擊一下
ac.click()

# 暫停一下
ac.pause(15)

# 若先前已移動，則進行相對位移 (從 928, 369 開始)
ac.move_by_offset(-256, -60) #(672, 309)

# 點擊一下
for i in range(2000):
    ac.click()

# 執行
ac.perform()

# 睡一下
sleep(5)

# 關閉 web driver
driver.quit()

# %%
'''
範例 2: 拖曳網頁元素
'''
driver.get('http://sahitest.com/demo/dragDropMooTools.htm')

# 取得被拖曳的來源元素
dragger = driver.find_element(By.CSS_SELECTOR, "div#dragger")

# 目標元素 (放置的區域，共 4 個)
items = driver.find_elements(By.CSS_SELECTOR, "div.item")

# 建立行為鍊
ac = ActionChains(driver)

# 暫停一下
ac.pause(2)

# 放置第一個
ac.drag_and_drop(dragger, items[0])

# 暫停一下
ac.pause(2)

# 放置第二個
ac.click_and_hold(dragger).release(items[1])

# 暫停一下
ac.pause(2)

# 放置第三個
ac.click_and_hold(dragger).move_to_element(items[2]).release()

# 暫停一下
ac.pause(2)

# 放置第四個
ac.click_and_hold(dragger).move_by_offset(400, 150).release()

# 執行
ac.perform()

# 睡一下
sleep(5)

# 關閉 web driver
driver.quit()

# %%
'''
範例 3: 組合熱鍵 (全選 + 複製 + 貼上)
'''
driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_text')

# 取得網頁上的 iframe
iframe = driver.find_element(By.CSS_SELECTOR, "iframe#iframeResult")

# 切換到 iframe 當中
driver.switch_to.frame(iframe)

# # 回到主框頁
# driver.switch_to.default_content()

# 取得第一個文字欄位
inputText01 = driver.find_element(By.CSS_SELECTOR, "input#fname")

# 取得第二個文字欄位
inputText02 = driver.find_element(By.CSS_SELECTOR, "input#lname")

# 建立行為鍊
ac = ActionChains(driver)

# 在第一個文字欄位當中輸入萬用字元
ac.key_down(Keys.SHIFT, inputText01).send_keys('12345').key_up(Keys.SHIFT).send_keys('67890')

# 暫停一下
ac.pause(2)

# 全選與複製第一個文字欄位當中的所有字元
ac.key_down(Keys.CONTROL, inputText01).send_keys('ac').key_up(Keys.CONTROL)

# 暫停一下
ac.pause(2)

# 在第二個文字欄位當中貼上文字
ac.key_down(Keys.CONTROL, inputText02).send_keys('v').key_up(Keys.CONTROL)

# 執行
ac.perform()

# 睡一下
sleep(5)

# 關閉 web driver
driver.quit()

# %%
'''
範例 4: 移動 Slider (by a handle)
'''
driver.get('https://jqueryui.com/slider/')

# 取得網頁上的 iframe
iframe = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")

# 切換到 iframe 當中
driver.switch_to.frame(iframe)

# 拿到把手(?)
span = driver.find_element(By.CSS_SELECTOR, 'span.ui-slider-handle.ui-corner-all.ui-state-default')

# 建立行為鍊
ac = ActionChains(driver)

# 暫停
ac.pause(2)

# 點住不放，並向右移動，移到指定的座標 (註: 目前在 iframe 當中，使用的座標是 iframe 內部座標)
ac.click_and_hold(span).move_by_offset(577, 16).release()

# 執行
ac.perform()

# 睡一下
sleep(5)

# 關閉 web driver
driver.quit()


