from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


def test_github():
    # GIVEN
    browser.open("https://github.com")

    # WHEN
    browser.element(".header-search-input").click()
    browser.element(".header-search-input").send_keys("eroshenkoam/allure-example")
    browser.element(".header-search-input").submit()
    browser.element(by.link_text("eroshenkoam/allure-example")).click()
    browser.element("#issues-tab").click()

    # THEN
    browser.element(by.partial_text("#76")).should(be.visible)
