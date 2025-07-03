import allure
import pytest
from playwright.sync_api import expect

from utils.config_web import user_name, user_password, steam_id, base_url


@allure.tag('web')
@allure.feature('Успешная авторизация пользователя.')
@allure.label('owner', 'Ярослав Гусев')
@allure.description(
    'Тест проверяет возможность авторизации пользователя.')
@allure.link(f'{base_url}', name='Главная страница Steam.')
@pytest.mark.parametrize(
    ('login_name', 'password'),
    [(user_name, user_password)],
    ids=['success'])
def test_authentication(open_page, login_name, password):
    with allure.step('Открываем главную страницу'):
        open_page.goto(base_url)

    with allure.step('Нажимаем кнопку "Вход"'):
        open_page.click('a.global_action_link:has-text("войти")')

    with allure.step('Вводим логин и пароль'):
        open_page.fill("//div[text()='Войдите, используя имя аккаунта']/following-sibling::input", login_name)
        open_page.fill("//div[.//div[text()='Пароль']]/input[@type='password']", password)

    with allure.step('Нажимаем кнопку "Войти"'):
        open_page.click("//button[text()='Войти']")

    with allure.step('Ждём загрузки аккаунт-меню и переходим в профиль'):
        open_page.click("//button[@id='account_pulldown']")
        open_page.click("//div[@id='account_dropdown']//a[contains(text(), 'Об аккаунте')]")

    with allure.step('Проверяем отображение имени пользователя и Steam ID на странице'):
        expect(open_page.locator('h2')).to_contain_text(login_name)
        expect(open_page.locator('//*[@class="youraccount_steamid"]')).to_contain_text(steam_id)
