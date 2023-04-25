import pandas as pd

# 2022/02-2023/04 story資料
df1 = pd.read_csv('Jan-11-2023_Apr-11-2023_story.csv')
df2 = pd.read_csv('Jul-11-2022_Oct-10-2022_story.csv')
df3 = pd.read_csv('Apr-11-2022_Jun-10-2022_story.csv')
df4 = pd.read_csv('Feb-01-2022_Apr-10-2022_story.csv')
df5 = pd.read_csv('Jun-11-2022_Jul-10-2022_story.csv')

# 合併
alligstory = pd.concat([df1, df2, df3, df4, df5])

# 另存
selectedigstory = alligstory.loc[:, ['說明', '發佈時間', '永久連結','瀏覽次數','觸及人數',
                          '分享','追蹤人數','個人檔案瀏覽次數','回覆次數','貼圖點按次數','導覽']]

#資料清理
selectedigstory[['發佈日期', '發佈時間']] = selectedigstory['發佈時間'].str.split(' ', expand=True)

from datetime import datetime
selectedigstory['發佈日期'] = selectedigstory['發佈日期'].apply(lambda x: datetime.strptime(x, '%m/%d/%Y').strftime('%Y-%m-%d'))
selectedigstory = selectedigstory.sort_values(by='發佈日期', ascending=False)

selectedigstory.to_csv('story.csv', index=False, encoding='utf-8-sig')
#%%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 設定 Chrome 瀏覽器
driver = webdriver.Chrome()


# 登入 Instagram 帳號
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# 前往指定用戶的 Story 頁面
driver.get('https://instagram.com/stories/chalice_boutique/3074664925591682014')
# 等待輸入欄位出現
username = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//input[@name="username"]'))
)
password = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//input[@name="password"]'))
)

# 輸入帳號密碼
username.send_keys('chalice_boutique')
password.send_keys('ivy870816')
password.send_keys(Keys.RETURN)


not_now_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "不要")]'))
)
not_now_button.click()

# 顯示 Story 10 秒
time.sleep(10)
# 擷取畫面並儲存為圖片檔案
driver.save_screenshot('screenshot.png')
# 關閉瀏覽器
driver.quit()