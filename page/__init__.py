from selenium.webdriver.common.by import By

# 主页页面
mine = By.XPATH, '//*[contains(text,"我的")]'  # 我的
# 我的页面
login = By.XPATH, '//*[contains(text,"登录")]'  # 登录
# 登录页面
username = By.ID, 'com.bjcsxq.chat.carfriend:id/login_phone_et'  # 用户名
password = By.ID, 'com.bjcsxq.chat.carfriend:id/login_pwd_et'  # 密码
login_btn = By.ID, 'com.bjcsxq.chat.carfriend:id/login_btn'  # 登录按钮
con_btn = By.ID, 'com.bjcsxq.chat.carfriend:id/btn_neg'  # 签到提示
nick_name = By.ID, 'com.bjcsxq.chat.carfriend:id/mine_username_tv'  # 昵称
