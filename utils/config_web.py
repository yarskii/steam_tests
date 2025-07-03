from dotenv import load_dotenv
import os

load_dotenv()

user_name = os.getenv('LOGIN')
user_password = os.getenv('PASSWORD')
steam_id = os.getenv('STEAM_ID')
base_url = os.getenv('BASE_URL')

login_error = 'Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова.'

steam_languages = ['简体中文', '繁體中文', '日本語', '한국어', 'ไทย', 'Български', 'Čeština', 'Dansk',
             'Deutsch', 'English', 'Español - España', 'Español - Latinoamérica', 'Ελληνικά',
             'Français', 'Italiano', 'Bahasa Indonesia', 'Magyar', 'Nederlands', 'Norsk', 'Polski',
             'Português', 'Português - Brasil', 'Română', 'Suomi', 'Svenska', 'Türkçe', 'Tiếng Việt',
             'Українська', 'Русский']
english_names = ['Simplified Chinese', 'Traditional Chinese', 'Japanese', 'Korean', 'Thai', 'Bulgarian',
           'Czech', 'Danish', 'German', 'English', 'Spanish - Spain', 'Spanish - Latin America', 'Greek',
           'French', 'Italian', 'Indonesian', 'Hungarian', 'Dutch', 'Norwegian', 'Polish',
           'Portuguese - Portugal', 'Portuguese - Brazil', 'Romanian', 'Finnish',
           'Swedish', 'Turkish', 'Vietnamese', 'Ukrainian', 'Russian']
