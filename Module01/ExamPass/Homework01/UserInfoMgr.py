import Module01.ExamPass.Homework01.PasswordError

class UserInfoMgr:
    user_infos = []

    # @classmethod
    # def read_dummy_db(cls):
    #     fd = open("UserInfo.txt", "r")
    #     while True:
    #         # For reading a large file, we use 1024 (1K)
    #         info = fd.readline()
    #         if len(info) <= 0:
    #             break
    #         # print(info, end="")
    #         lst = info.split(":")
    #
    #         dict1 = {}
    #         dict1[lst[0]] = lst[1].rstrip('\n')
    #         cls.user_infos.append(dict1)
    #     fd.close()

    @classmethod
    def read_dummy_db(cls):
        fd = open("user_data", "r")
        while True:
            # For reading a large file, we use 1024 (1K)
            info = fd.readline()
            if len(info) <= 0:
                break
            # print(info, end="")
            lst1 = eval(info)
            for dict1 in lst1:
                cls.user_infos.append(dict1)
        fd.close()

    # def check_entry(self, user_info):
    #     for item in UserInfoMgr.user_infos:
    #         for key in item:
    #             if key == user_info.user_name:
    #                 if item[key] == user_info.pwd:
    #                     print("===================== %s logon successfully ..." % user_info.user_name)
    #                     return True
    #                 else:
    #                     raise Module01.ExamPass.Homework01.PasswordError.PasswordError("********* Passwords do not match in database")
    #
    #     # Add new user if we pass the main for loop here
    #     print("----------------------", type(eval(user_info.__str__())))
    #     UserInfoMgr.user_infos.append(eval(user_info.__str__()))
    #     print("===================== Register %s successfully ..." % user_info)
    #     print("=======================", UserInfoMgr.user_infos)
    #     return True

    def check_entry(self, user_info):
        for item in UserInfoMgr.user_infos:
            for key in item:
                if key == user_info.user_name:
                    if item[key] == user_info.pwd:
                        print("===================== %s logon successfully ..." % user_info.user_name)
                        return True
                    else:
                        raise Module01.ExamPass.Homework01.PasswordError.PasswordError("********* Passwords do not match in database")

        # Add new user if we pass the main for loop here
        print("----------------------", type(eval(user_info.__str__())))
        UserInfoMgr.user_infos.append(eval(user_info.__str__()))
        print("===================== Register %s successfully ..." % user_info)
        print("=======================", UserInfoMgr.user_infos)
        return True

    # @classmethod
    # def write_dummy_db(cls):
    #     fd = open("user_data", "w")
    #     for _dict in cls.user_infos:
    #         for k in _dict:
    #             line = k + ":" + _dict[k] + "\n"
    #             fd.writelines(line)
    #     fd.close()

    @classmethod
    def write_dummy_db(cls):
        fd = open("user_data", "w")
        # for dict1 in cls.user_infos:
        #     str1 = str(dict1)
        #     fd.writelines(str1)
        fd.writelines(str(cls.user_infos))
        fd.close()


"""
    UserInfo class
"""


class UserInfo:
    user_infos = []

    def __init__(self, username, pwd):
        self.user_name = username
        self.pwd = pwd

    """
        1. Make a str representation and used by EVAL function   
    """
    def __str__(self):
        return "{\'%s\':\'%s\'}" % (self.user_name, self.pwd)