import pytest
from selene import have
from selene.support.shared import browser

chrome = pytest.fixture(params=[(1980, 1080), (375, 667)])


@chrome
def browser_windows_size(request):
    return request


@pytest.fixture(scope='function', autouse=True)
def browser_config(browser_windows_size):
    width = browser_windows_size.param[0]
    height = browser_windows_size.param[1]

    browser.config.window_width = width
    browser.config.window_height = height


@pytest.mark.parametrize("browser_windows_size", [(1980, 1080)], indirect=True)
def test_github_desktop(browser_windows_size):
    browser.open("https://github.com/")
    browser.element("a.flex-shrink-0:nth-child(1)").click()
    browser.element('.auth-form-header').should(have.text("Sign in to GitHub"))


@pytest.mark.parametrize("browser_windows_size", [(375, 667)], indirect=True)
def test_github_mobile(browser_windows_size):
    browser.open("https://github.com/")
    browser.element('button[aria-label="Toggle navigation"').click()
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text("Sign in to GitHub"))
