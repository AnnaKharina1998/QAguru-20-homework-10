import allure
from selene import have
from selene.support import by
from selene.support.shared import browser


class Github():
    @allure.step("открываем главную страницу")
    def open_main_page(self):
        browser.open('https://github.com')

    @allure.step(f"ищем свой репозиторий")
    def find_repository(self, repo):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').type(f'{repo}').press_enter()

    @allure.step(f"переходим в репозиторий")
    def open_repository(self, repo):
        browser.element(by.text(f'{repo}')).click()

    @allure.step("переходим на вкладку issues")
    def open_issues(self):
        browser.element('#issues-tab').click()

    @allure.step(f"заходим в созданный для дз issue")
    def go_to_issue(self, text):
        browser.element(by.text(f'{text}')).click()

    @allure.step("выполняем проверку имени")
    def issue_name_should_be(self, text):
        browser.element('[data-testid=issue-title]').should(have.text(f'{text}'))
