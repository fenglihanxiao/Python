"""
    197_XXX -> User logon validation exercise on module and package
"""


import Module01.ModulePackage.Service.ServiceLogon
# import ModulePackage.Feng_Except.Question
from Module01.ModulePackage.Feng_Except.Question import *

user_name = input("Please enter user name:")
pwd = input("Please enter password:")

def main():
    try:
        Module01.ModulePackage.Service.ServiceLogon.check_user_name(user_name)
        Module01.ModulePackage.Service.ServiceLogon.check_pwd(pwd)
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
