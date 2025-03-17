import allure

class Constant:

    def __init__(self):
        print("constant loaded")

    @staticmethod
    def app_url():
        return "https://app.vwo.com"

    @staticmethod
    def app_dashboard_url():
        return "https://app.vwo.com/#dashboard"


