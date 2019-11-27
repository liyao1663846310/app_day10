"""登录页面"""
import page
from base.base_page import BasePage


class LoginPage(BasePage):
    username = page.username  # 用户名
    password = page.password  # 密码
    login_btn = page.login_btn  # 登录按钮
    con_btn = page.con_btn  # 签到提示
    nick_name = page.nick_name  # 昵称

    def input_username(self, name):
        # 输入用户名方法
        self.input_func(self.username, name)

    def input_password(self, pwd):
        # 输入密码方法
        self.input_func(self.password, pwd)

    def click_login_btn(self):
        # 点击登录按钮
        self.click_func(self.login_btn)

    def click_con_btn(self):
        # 点击签到提示按钮方法
        self.click_func(self.con_btn)

    def click_nick_name(self):
        # 点击昵称方法
        self.click_func(self.nick_name)
