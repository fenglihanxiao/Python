"""
    188_XXX -> User logon validation exercise
"""


class UserNameError(Exception):
    pass


class PasswordError(Exception):
    pass


user_name = input("Please enter user name:")
pwd = input("Please enter password:")


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


def main():
    try:
        check_user_name(user_name)
        check_pwd(pwd)
    except UserNameError as e:
        print("------------ ", str(e))
    except PasswordError as e:
        print("------------ ", str(e))
    except Exception as e:
        print("------------ " + "Other exceptions")
        print(str(e))
    else:
        print("============ Logon on successfully ")

main()
