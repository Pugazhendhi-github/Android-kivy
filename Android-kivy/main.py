""" Kivy Application"""
from gettext import dpgettext
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.snackbar import MDSnackbar
import sqlite3

class Screenmanager(ScreenManager):
    """example class"""
class LogIn(Screen):
    """example class"""
class SignUp(Screen):
    """example class"""
class HomePage(Screen):
    """example class"""


class MyApp(MDApp):
    """Main App"""
    def build(self):
        self.kv = Builder.load_file("main.kv")
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.theme_palette = "Primary"
        return self.kv
    def signup(self, username, moblie, email, password ):
            conn = sqlite3.connect('employee.db')
            cur = conn.cursor()
            try:
                cur.execute("INSERT INTO users(username, mobile, email, password) VALUES(?,?,?,?)",(username, email, moblie, password))
                print("user sign up success")
            except Exception :
                print("error")
            conn.commit()
            conn.close()                
    def login(self, username, password):
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        cur.execute("select * from users WHERE username = ? AND password = ?;",(username,password))
        user = cur.fetchone()
        
        conn.commit()
        cur.close()
        if user:
            print(" login successs")
            self.root.current = 'Home'
        else:
            print("Invalid username or password")
       
    def view(self):
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        users = cur.execute("select * from users")
        for i in users:
            print(i)
        conn.commit()
        cur.close()

            
if __name__ == '__main__':
    MyApp().run()
