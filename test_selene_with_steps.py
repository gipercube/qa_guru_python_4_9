import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


def test_github():
    # GIVEN
    with allure.step('Открыть главную страницу github.com'):
        browser.open("https://github.com")

    # WHEN
    with allure.step('Найти репозиторий "eroshenkoam/allure-example"'):
        browser.element(".header-search-input").click()
        browser.element(".header-search-input").send_keys("eroshenkoam/allure-example")
        browser.element(".header-search-input").submit()
    with allure.step('Перейти в репозиторий "eroshenkoam/allure-example"'):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()
    with allure.step('Перейти в таб "Issues"'):
        browser.element("#issues-tab").click()

    # THEN
    with allure.step('Найти задачу с номером "#76"'):
        browser.element(by.partial_text("#76")).should(be.visible)
