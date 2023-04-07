import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from allure_commons.types import Severity


@allure.tag('browser')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'gipercube')
@allure.feature('Проверка отображения задачи #76 на github')
@allure.story('Я как пользовтель могу увидеть задачу с номером #76 для её открытия и оценки')
@allure.link('https://github.com', name='Testing')
def test_decorator_steps():
    # GIVEN
    open_main_page()

    # WHEN
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()

    # THEN
    should_see_issue_with_number('#76')


@allure.step('Открыть главную страницу github.com')
def open_main_page():
    browser.open("https://github.com")


@allure.step('Найти репозиторий "eroshenkoam/allure-example"')
def search_for_repository(repo):
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').send_keys(repo)
    browser.element('.header-search-input').submit()


@allure.step('Перейти в репозиторий "{repo}"')
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Перейти в таб "Issues"')
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step('Найти задачу с номером "{number}"')
def should_see_issue_with_number(number):
    browser.element(by.partial_text(number)).should(be.visible)
