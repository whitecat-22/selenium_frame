from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # 追加
import time

options = Options()  # 追加

driver = webdriver.Chrome(executable_path='C:\Program Files\chromedriver\chromedriver.exe', options=options)  # options=options 追加
driver.get("http://aaa/bbb/ccc.asp")
time.sleep(3)  # 3-10秒ほど待つと良いです

# フレームを切り替えて、該当の要素を取得する
searchElement = driver.switch_to_frame(driver.find_element_by_name("txtUser"))   # 変更

print(driver.page_source)  # もしくは、print(searchElement)

# もとのフレームに戻る
driver.switch_to.default_content()  # 追加

# ドライバを閉じて、処理を終了する
driver.close()  # 追加


　　
# 参照元；
# - [[Python] seleniumのフレーム移動(switch_to_frame)](https://hacknote.jp/archives/51263/)
# - [Selenium with Python  -  3. Navigating  -- 3.4. Moving between windows and frames](https://selenium-python.readthedocs.io/navigating.html#moving-between-windows-and-frames)
