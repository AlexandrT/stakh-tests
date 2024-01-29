from .user_actions import Action
from .settings import *


action = Action()

action.run_application(BROWSER)
action.enter_url(URL)
action.run_application(BROWSER)
action.change_window()
