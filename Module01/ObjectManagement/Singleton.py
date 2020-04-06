"""
    1. 171_XXX -> Singleton
"""


class User:
    ####################################
    # 1. Make it private __instance
    __instance = None

    def __new__(cls, *args, **kwargs):
        ####################################
        # 1. Use operator "is" to compare memory address not use "=="
        if cls.__instance is None:
            cls.instatnce = object.__new__(User)
        return cls.__instance


for _ in range(10):
    print(id(User()))
