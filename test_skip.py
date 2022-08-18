from turtle import window_width

import pytest
from selene import have
from selene.support.shared import browser

chrome = pytest.fixture(params=[(1012, 946), (1200, 1000), (1011, 946), (900, 950)])


@chrome
def browser_size(request):
    return request


@pytest.fixture(scope='function', autouse=True)
def browser_config(browser_size):
    width = browser_size.param[0]
    height = browser_size.param[1]

    browser.config.window_width = width
    browser.config.window_height = height

    browser.open("https://github.com/")


def test_github_desktop():
    if browser._config.window_width < 1012:
        pytest.skip('Window width is for mobile test')

    browser.element("a.flex-shrink-0:nth-child(1)").click()
    browser.element('.auth-form-header').should(have.text("Sign in to GitHub"))


def test_github_mobile():
    if browser._config.window_width > 1011:
        pytest.skip('Window width is for desktop test')

    browser.element('button[aria-label="Toggle navigation"').click()
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text("Sign in to GitHub"))
