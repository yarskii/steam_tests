from dotenv import load_dotenv
import os

load_dotenv()

user_name = os.getenv('LOGIN')
user_password = os.getenv('PASSWORD')
steam_id = os.getenv('STEAM_ID')
base_url = os.getenv('BASE_URL')

login_error = os.getenv('LOGIN_ERROR')
