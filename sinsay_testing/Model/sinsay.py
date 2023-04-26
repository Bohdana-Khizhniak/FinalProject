from selene import have, command
from selene.support.shared import browser

completed = have.css_class('completed')

class Sinsay:
    def __init__(self):
        self.sinsay_list = browser.all('#cms-home-ss20 > div')

    def open(self):
        browser.open('https://www.sinsay.com/ua/uk')
        browser.element('#new-uc-buttons-container > div.new-uc-text-primary-button-container').click()
        return self
    def authorization(self, login, pas):
        browser.element('#headerWrapper > div > div.page-header__HeaderItems-qbclzk-4.ivuCDI > button.action-btn__ActionBtn-zbpc1m-1.evsxEe').click()
        browser.element('#login\[username\]_id').type(login).press_tab()
        browser.element('#login\[password\]_id').type(pas).press_tab()
        browser.element('#loginRegisterRoot > div > div.sc-hKgJUU.hoSgvk > div > form > button').press_enter()
        return self
    def data_change(self):
        browser.element('#headerWrapper > div > div.page-header__HeaderItems-qbclzk-4.ivuCDI > button.action-btn__ActionBtn-zbpc1m-1.evsxEe').click()

        return self
    def serch(self, st):
        browser.element('[placeholder="Шукати"]').type(st).press_enter()
        return self
    def basket(self):
        browser.all('[class="hit-item__AspectRatioBlankContainer-sc-1mc86co-1 dzLZKy"]')[0].element('a').click()
        browser.element('#productContainer > section > section.sc-jrAFXE.PZvh > button').press_enter()
        return self
    def should_be(self, st):
        p_count = browser.driver.page_source.lower().count(st)
        if p_count > 0:
            print('Ok')
        else: print('Error')
        return self