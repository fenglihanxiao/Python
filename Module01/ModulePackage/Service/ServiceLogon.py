# import ModulePackage.Module_197
from Module01.ModulePackage.Feng_Except.Question import *


def check_user_name(name):
    if len(name) < 3 or len(name) > 8:
        raise UserNameError("User name needs to >8 and <3")

    if not name.isalnum():
        raise PasswordError("User name need to be alphabet and number")


def check_pwd(pwd):
    if not len(pwd) == 6:
        raise PasswordError("Password needs to be length of 6")

    if not pwd.isdigit():
        raise PasswordError("Password needs to be digit")

