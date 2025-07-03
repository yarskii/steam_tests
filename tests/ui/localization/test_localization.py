import pytest

from utils.config_web import base_url, steam_languages, english_names


@pytest.mark.parametrize('language',
                         (i for i in steam_languages),
                         ids=[name for name in english_names])
def test_localization(open_page, language):
    open_page.goto(base_url)

    open_page.click('#language_pulldown')

    open_page.click(f'//*[@id="language_dropdown"]//a[contains(text(), "{language}")]')
    open_page.wait_for_timeout(2000)

    languages = open_page.locator('#language_dropdown').inner_text()

    lang_lst = [
        lang.split(' (')[0].strip()
        for lang in languages.split('\n')[:-1]
        if lang.strip() and '(' in lang
    ]

    for lan in lang_lst:
        assert lan in steam_languages
