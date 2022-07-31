from turtle import window_width

import pytest
from selene import have
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_config():
    browser.config.window_width = 1980
    browser.config.window_height = 1080


def test_github_desktop(browser_config):
    if browser.config.window_width < 1000:
        pytest.skip('Window width is for mobile test')
    browser.open("https://github.com/")
    browser.element("a.flex-shrink-0:nth-child(1)").click()
    browser.element('.auth-form-header').should(have.text("Sign in to GitHub"))


def test_github_mobile(browser_config):
    if browser.config.window_width > 1000:
        pytest.skip('Window width is for desktop test')
    browser.open("https://github.com/")
    browser.element('button[aria-label="Toggle navigation"').click()
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text("Sign in to GitHub"))
