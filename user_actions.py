import pyautogui
import subprocess
import time


class Action():
	def run_application(self, app_name):
		subprocess.Popen([name])
		time.sleep(2)

	def enter_text(self, text):
		pyautogui.write(text)

	def change_window(self):
		pyautogui.hotkey('alt', 'tab', interval=0.2)

	def enter_url(self, url):
		self.enter_text(url)
		pyautogui.press('enter')
		time.sleep(2)

	def lock_screen(self):
		subprocess.Popen('xflock4')
		time.sleep(2)

	def unlock_screen(self):
		pyautogui.click()
		time.sleep(1)
		pyautogui.write(USER_PASSWORD)
		pyautogui.press('enter')