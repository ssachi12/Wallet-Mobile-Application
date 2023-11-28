from kivy.properties import ListProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
from kivymd.uix.button import MDIconButton
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.navigationdrawer import MDNavigationLayout
from kivymd.uix.screen import Screen

Window.size = (300, 500)

navigation_helper = """
<DashBoardScreen>:
    Screen:
        MDNavigationLayout:
            MDScreenManager:
                MDScreen:
                    BottomAppBar:
                        MDBottomNavigation:
                            spacing:dp(10)
                            panel_color:get_color_from_hex("#3489eb")
                            text_color_active:get_color_from_hex("F5F5F5")
                            MDBottomNavigationItem:
                                name:"Withdraw"
                                text:'Withdraw'
                                font_size: '20sp'
                                icon:'bank-transfer-out'
                                on_tab_release:print("Withdraw")
                            MDBottomNavigationItem:
                                name:"Withdraw"
                                text:'Transfer'
                                text_size: dp(1)
                                icon:'bank-transfer-in'
                                on_tab_release:print("Transfer")
                            MDBottomNavigationItem:
                                name:"Withdraw"
                                text:'Add Money'
                                text_size:dp(8)
                                icon:'wallet-plus'
                                on_tab_release:print("Add money")
                    MDTopAppBar:
                        title: "G-Wallet"
                        elevation: 4
                        pos_hint: {"top": 1}
                        md_bg_color: "#3489eb"
                        specific_text_color: "F5F5F5"
                        left_action_items:
                            [['menu', lambda x: nav_drawer.set_state("open")]]


                    #Main page

                    BoxLayout:
                        orientation: 'vertical'
                        spacing:dp(20)
                        padding: dp(10)
                        pos_hint:{'center_y':.37}

                        GridLayout:
                            #spacing:dp(100)
                            #padding:dp(5)
                            cols: 3
                            spacing:dp(20)
                            rows:4



                            # Icon and label for recharge prepaid mobile
                            BoxLayout:

                                spacing: dp(10)
                                orientation: 'vertical'
                                size_hint_y: None
                                height: self.minimum_height
                                width:20

                                MDIconButton:
                                    icon: 'cellphone-wireless'
                                    pos_hint: {'center_x': 0.5}
                                    on_release: app.recharge_prepaid_mobile()  # Replace with your actual function
                                    padding: dp(20)

                                MDLabel:
                                    text: 'Recharge Prepaid Mobile'
                                    halign: 'center'
                                    font_size: '10sp'

                            # Icon and label for pay electricity bill
                            BoxLayout:

                                spacing: dp(10)
                                orientation: 'vertical'
                                size_hint_y: None
                                height: self.minimum_height

                                MDIconButton:
                                    icon: 'flash'
                                    pos_hint: {'center_x': 0.5}
                                    on_release: app.pay_electricity_bill()  # Replace with your actual function
                                    padding: dp(20)

                                MDLabel:
                                    text: 'Pay Electricity Bill'
                                    halign: 'center'
                                    font_size: '10sp'

                            # Icon and label for recharge DTH connection
                            BoxLayout:

                                spacing: dp(10)
                                orientation: 'vertical'
                                size_hint_y: None
                                height: self.minimum_height

                                MDIconButton:
                                    icon: 'satellite-variant'
                                    pos_hint: {'center_x': 0.5}
                                    on_release: app.recharge_dth_connection()  # Replace with your actual function
                                    padding: dp(20)

                                MDLabel:
                                    text: 'Recharge DTH Connection'
                                    halign: 'center'
                                    font_size: '10sp'

                            # Icon and label for book gas cylinder
                            BoxLayout:

                                spacing: dp(10)
                                orientation: 'vertical'
                                size_hint_y: None
                                height: self.minimum_height

                                MDIconButton:
                                    icon: 'gas-cylinder'
                                    pos_hint: {'center_x': 0.5}
                                    on_release: app.book_gas_cylinder()  # Replace with your actual function
                                    padding: dp(20)

                                MDLabel:
                                    text: 'Book Gas Cylinder'
                                    halign: 'center'
                                    font_size: '10sp'

                             # Icon and label for pay broadband & landline bill
                            BoxLayout:
                                spacing: dp(10)
                                orientation: 'vertical'
                                size_hint_y: None
                                height: self.minimum_height

                                MDIconButton:
                                    icon: 'router-wireless'
                                    pos_hint: {'center_x': 0.5}
                                    on_release: app.pay_broadband_landline_bill()  # Replace with your actual function
                                    padding: dp(20)

                                MDLabel:
                                    text:  'Broadband & Landline Bill'
                                    halign: 'center'
                                    font_size: '10sp'

                            # Icon and label for pay education fee
                            BoxLayout:
                                spacing: dp(10)
                                orientation: 'vertical'
                                size_hint_y: None
                                height: self.minimum_height

                                MDIconButton:
                                    icon: 'school'
                                    pos_hint: {'center_x': 0.5}
                                    on_release: app.pay_education_fee()  # Replace with your actual function
                                    padding: dp(20)

                                MDLabel:
                                    text: 'Pay Education Fee'
                                    halign: 'center'
                                    font_size: '10sp'        




                            # Icon and label for Movies Tickets
                            BoxLayout:
                                spacing: dp(10)
                                orientation: 'vertical'
                                size_hint_y: None
                                height: self.minimum_height
                                width: 20

                                MDIconButton:
                                    icon: 'movie'
                                    pos_hint: {'center_x': 0.5}
                                    on_release: app.book_movies_tickets()  # Replace with your actual function
                                    padding: dp(20)

                                MDLabel:
                                    text: 'Movies Tickets'
                                    halign: 'center'
                                    font_size: '10sp'

                            # Icon and label for Flight Tickets
                            BoxLayout:
                                spacing: dp(10)
                                orientation: 'vertical'
                                size_hint_y: None
                                height: self.minimum_height

                                MDIconButton:
                                    icon: 'airplane'
                                    pos_hint: {'center_x': 0.5}
                                    on_release: app.book_flight_tickets()  # Replace with your actual function
                                    padding: dp(20)

                                MDLabel:
                                    text: 'Flight Tickets'
                                    halign: 'center'
                                    font_size: '10sp'

                            # Icon and label for Bus Tickets
                            BoxLayout:
                                spacing: dp(10)
                                orientation: 'vertical'
                                size_hint_y: None
                                height: self.minimum_height

                                MDIconButton:
                                    icon: 'bus'
                                    pos_hint: {'center_x': 0.5}
                                    on_release: app.book_bus_tickets()  # Replace with your actual function
                                    padding: dp(20)

                                MDLabel:
                                    text: 'Bus Tickets'
                                    halign: 'center'
                                    font_size: '10sp'

                            # Icon and label for Train Tickets
                            BoxLayout:
                                spacing: dp(10)
                                orientation: 'vertical'
                                size_hint_y: None
                                height: self.minimum_height

                                MDIconButton:
                                    icon: 'train'
                                    pos_hint: {'center_x': 0.5}
                                    on_release: app.book_train_tickets()  # Replace with your actual function
                                    padding: dp(20)

                                MDLabel:
                                    text: 'Train Tickets'
                                    halign: 'center'
                                    font_size: '10sp'

                            # Icon and label for Buy Insurance
                            BoxLayout:
                                spacing: dp(10)
                                orientation: 'vertical'
                                size_hint_y: None
                                height: self.minimum_height

                                MDIconButton:
                                    icon: 'shield-check'
                                    pos_hint: {'center_x': 0.5}
                                    on_release: app.buy_insurance()  # Replace with your actual function
                                    padding: dp(20)

                                MDLabel:
                                    text: 'Buy Insurance'
                                    halign: 'center'
                                    font_size: '10sp'

                            # Icon and label for International Flights
                            BoxLayout:
                                spacing: dp(10)
                                orientation: 'vertical'
                                size_hint_y: None
                                height: self.minimum_height

                                MDIconButton:
                                    icon: 'earth'
                                    pos_hint: {'center_x': 0.5}
                                    on_release: app.book_international_flights()  # Replace with your actual function
                                    padding: dp(20)

                                MDLabel:
                                    text: 'International Flights'
                                    halign: 'center'
                                    font_size: '10sp'



            MDNavigationDrawer:
                id: nav_drawer
                radius: (0, 10, 10, 0)

                ContentNavigationDrawer:

                    BoxLayout:
                        size: root.width, root.height
                        spacing: '12dp'
                        padding: '8dp'
                        orientation: "vertical"
                        pos_hint:{'top':1}

                        MDLabel:
                            id: username_label
                            text:'sachin'
                            font_style:"Subtitle1"
                            size_hint_y:None
                            height: self.texture_size[1]


                        MDLabel:
                            id: email_label
                            text:'s@gmail.com'
                            font_style:"Caption" 
                            size_hint_y:None
                            height: self.texture_size[1]


                        BoxLayout:
                            orientation: "vertical"
                            padding: 20
                            pos_hint:{'center_x':0.44}

                            MDCard:
                                radius: [50, 50, 50, 50]
                                size_hint: None, None
                                size: "260dp", "120dp"
                                md_bg_color: 0.9, 0.9, 0.9, 1  # Slight grey background

                                MDLabel:
                                    text: "Balance: 12345"
                                    size_hint: 1, None
                                    font_size:"28sp"
                                    bold: True
                                    height:"115dp"
                                    halign: "center"
                                    valign: "center"


                        BoxLayout: 
                            size_hint_y: None
                            height: dp(250)
                            pos_hint: {'center_x': 0.45, 'y': 130}        

                            BoxLayout:
                                orientation: "vertical"
                                size_hint_y: None
                                height: self.minimum_height
                                spacing: '8dp'

                                OneLineIconListItem:
                                    text: "Profile"
                                    on_release: root.manager.profile_view()
                                    IconLeftWidget:
                                        icon: "face-man-profile" 


                                OneLineIconListItem:
                                    text: "Transaction History"
                                    IconLeftWidget:
                                        icon: "history"

                                OneLineIconListItem:
                                    text: "Add Bank Account"
                                    IconLeftWidget:
                                        icon: "bank"

                                OneLineIconListItem:
                                    text: "Business"
                                    IconLeftWidget:
                                        icon: "account"        

                                OneLineIconListItem:
                                    text: "Log-out"
                                    IconLeftWidget:
                                        icon: "logout"        

"""
Builder.load_string(navigation_helper)
class BottomAppBar(FloatLayout):
    pass

class ContentNavigationDrawer(MDBoxLayout):
    pass


class DashBoardScreen(Screen):
    pass


class WalletApp(MDApp):
    pass


if __name__ == '__main__':
    WalletApp().run()
