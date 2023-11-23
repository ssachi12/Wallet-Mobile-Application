from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from login import LoginScreen
from signin import SignInScreen
from signup import SignUpScreen
from kivymd.uix.snackbar import Snackbar
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
    SignUpScreen:
        name: 'signup'
        manager: root    
        
    """
)

class ScreenManagement(ScreenManager):
    def signup(self):
        current_screen = self.current_screen

        gmail = current_screen.ids.gmail.text
        username = current_screen.ids.username.text
        password = current_screen.ids.password.text
        phone_no = current_screen.ids.phone_no.text
        aadhar_card = current_screen.ids.aadhar_card.text
        pan_card = current_screen.ids.pan_card.text
        address = current_screen.ids.address.text


        if not gmail or not username or not password or not phone_no or not aadhar_card or not pan_card or not address:
            Snackbar(text="All fields are mandatory. Please fill in all the required fields.").open()
            return

        if not self.is_valid_aadhar(aadhar_card):
            Snackbar(
                text="Invalid Aadhar card number. Aadhar card should be 12 digits long and contain only numeric characters.").open()
            return

        if not self.is_valid_phone(phone_no):
            Snackbar(
                text="Invalid phone number. Phone number should be 10 digits long and start with 6, 7, 8, or 9.").open()
            return

        if not self.is_valid_pan(pan_card):
            Snackbar(
                text="Invalid PAN card number. PAN card should start with 5 characters (A-Z), followed by 4 numbers, and ending with 1 character (A-Z).").open()
            return

        # Add your sign-up logic here
        print("Signing up...")
        print(f"Gmail: {gmail}, Username: {username}, Password: {password}, "
              f"Phone Number: {phone_no}, Aadhar Card: {aadhar_card}, PAN Card: {pan_card}, "
              f"Address: {address}")

    def is_valid_phone(self, phone):
        if len(phone) == 10 and phone[0] in ['6', '7', '8', '9']:
            return True
        return False

    def is_valid_aadhar(self, aadhar):
        if len(aadhar) == 12 and aadhar.isdigit():
            return True
        return False

    def is_valid_pan(self, pan):
        if len(pan) == 10 and pan[:5].isalpha() and pan[5:9].isdigit() and pan[9].isalpha():
            return True
        return False
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


class WalletApp(MDApp):
    def build(self):
        return ScreenManagement()


if __name__ == '__main__':
    WalletApp().run()
