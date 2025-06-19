import allure
from selene import have
from selene.support import by
from selene.support.shared import browser

from models.models import Github


def test_github_selene():
    browser.open('https://github.com')
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type('AnnaKharina1998/QAguru-20-homework-10').press_enter()
    browser.element(by.text('AnnaKharina1998')).click()
    browser.element('#issues-tab').click()
    browser.element(by.text('QAguru-20-homework-10 issue')).click()
    browser.element('[data-testid=issue-title]').should(have.text('QAguru-20-homework-10 issue'))
    
    
def test_github_with_allure_step():
    with allure.step ("открываем главную страницу"):
        browser.open('https://github.com')
    with allure.step("ищем свой репозиторий"):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').type('AnnaKharina1998/QAguru-20-homework-10').press_enter()
    with allure.step("переходим в репозиторий"):
        browser.element(by.text('AnnaKharina1998')).click()
    with allure.step("переходим на вкладку issues"):
        browser.element('#issues-tab').click()
    with allure.step("заходим в созданный для дз issue"):
        browser.element(by.text('QAguru-20-homework-10 issue')).click()
    with allure.step("выполняем проверку имени"):
        browser.element('[data-testid=issue-title]').should(have.text('QAguru-20-homework-10 issue'))


def test_github_decorator_allure_step():
    github = Github()
    github.open_main_page()
    github.find_repository('AnnaKharina1998/QAguru-20-homework-10')
    github.open_repository('AnnaKharina1998')
    github.open_issues()
    github.go_to_issue('QAguru-20-homework-10 issue')
    github.issue_name_should_be('QAguru-20-homework-10 issue')


