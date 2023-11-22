from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from login import LoginScreen
from signin import SignInScreen
import re

Builder.load_string(
    """
<ScreenManagement>:
    LoginScreen:
        name: 'login'
        manager: root
    SignInScreen:
        name: 'signin'
        manager: root
        
    """
)

class ScreenManagement(ScreenManager):
    def sign_in(self, input_text, password):
        # Define regular expressions for valid input
        mobile_regex = r"^\d{10}$"
        user_id_regex = r"^\w+$"
        email_regex = r"^\w+@\w+\.\w{2,4}$"

        # Check if input is a mobile number
        if re.match(mobile_regex, input_text):
            print(f"Signing in using mobile number: {input_text}")
            # Call sign-in function for mobile number

        # Check if input is a user ID
        elif re.match(user_id_regex, input_text):
            print(f"Signing in using user ID: {input_text}")
            # Call sign-in function for user ID

        # Check if input is an email ID
        elif re.match(email_regex, input_text):
            print(f"Signing in using email ID: {input_text}")
            # Call sign-in function for email ID

        # Invalid input
        else:
            print("Invalid input. Please enter a valid mobile number, user ID, or email ID")


class MultiScreenApp(MDApp):
    def build(self):
        return ScreenManagement()


if __name__ == '__main__':
    MultiScreenApp().run()
