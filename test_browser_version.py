from selene import have
from selene.support.shared import browser


def test_browser_version():
    browser.open("https://github.com/")
    browser.element("a.flex-shrink-0:nth-child(1)").click()
    browser.element('.auth-form-header').should(have.text("Sign in to GitHub"))


