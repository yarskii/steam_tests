import allure
import pytest
from playwright.sync_api import expect

from utils.config_web import user_name, user_password, login_error, base_url


@allure.tag('web')
@allure.feature('Авторизация пользователя.')
@allure.label('owner', 'Ярослав Гусев')
@allure.description(
    'Тест проверяет возможность авторизации пользователя.')
@allure.link(f'{base_url}', name='Главная страница Steam.')
@pytest.mark.parametrize(
    ('login_name', 'password'),
    [(user_name + '1', user_password),
     (user_name, user_password + '1')],
    ids=['mistake_login', 'mistake_password'])
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

    with allure.step('Проверяем правильность введенных данных'):
        with allure.step('Проверяем ответ о ошибке при неправильно введенных данных'):
            error = open_page.locator(f'//*[text()="{login_error}"]')
            expect(error).to_be_visible()
