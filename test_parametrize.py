import pytest
from selene import have
from selene.support.shared import browser


@pytest.fixture(scope='function', params=[(1980, 1080)])
def browser_desktop(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]


def test_github_desktop(browser_desktop):
    browser.open("https://github.com/")
    browser.element("a.flex-shrink-0:nth-child(1)").click()
    browser.element('.auth-form-header').should(have.text("Sign in to GitHub"))


@pytest.fixture(scope='function', params=[(337, 667)])
def browser_mobile(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]


def test_github_mobile(browser_mobile):
    browser.open("https://github.com/")
    browser.element('button[aria-label="Toggle navigation"').click()
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text("Sign in to GitHub"))
