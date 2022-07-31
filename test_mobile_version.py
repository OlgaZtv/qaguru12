from selene import have
from selene.support.shared import browser


def test_mobile_version():
    browser.open("https://github.com/")
    browser.element('button[aria-label="Toggle navigation"').click()
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text("Sign in to GitHub"))