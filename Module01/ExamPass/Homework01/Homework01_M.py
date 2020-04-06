"""
    Homework01
"""
from Module01.ExamPass.Homework01.UserInfoMgr import *
import Module01.ExamPass.Homework01.PasswordError


def main():
    read_dummy_db = True
    userInfoMgr = UserInfoMgr()
    try:
        while True:
            user_name = input("Please enter user name: ")
            if user_name == "quit" or user_name == "Quit":
                break
            pwd = input("Please enter password: ")

            user1 = UserInfo(user_name, pwd)

            if read_dummy_db == True:
                userInfoMgr.read_dummy_db()
                read_dummy_db = False
            userInfoMgr.check_entry(user1)
    except Module01.ExamPass.Homework01.PasswordError.PasswordError as e:
        print(str(e))
    # except Exception as e:
    #     print("Unknown exception -----------------", str(e))

    # Write the dummy db if the user type quit
    userInfoMgr.write_dummy_db()

main()