"""
    1. Pipe line process-1
    2. Example: "     hello  itcast  python" -> "HELLO: ITCAST:PYTHON"
"""

"""
def coder1(str1):
    # Process data
    str_list = str1.split()
    return str_list


def coder2(str1):
    # To process data
    # Get the next pipe line
    new_str = str1.strip().upper()
    print("Coder2:", new_str)
    return coder1(new_str)

# Fetch data and point to the policy
str_list = coder2("  hello  itcast  python")

for data in str_list:
    print(data, end=":")

"""

"""
    1. Pipe line process-2
    2. Example: "     hello  itcast  python" -> "HELLO: ITCAST:PYTHON"
    3. Main logic is put at coder1 method
"""

"""
def coder1(str1):
    # Process data
    str_list = str1.split()
    for data in str_list:
        print(data, end=":")


def coder2(str1):
    # To process data
    # Get the next pipe line
    new_str = str1.strip().upper()
    print("Coder2:", new_str)
    return coder1(new_str)

# Fetch data and point to the policy
str_list = coder2("  hello  itcast  python")
"""

"""
    1. Pipe line process-3
    2. Example: "     hello  itcast  python" -> "HELLO: ITCAST:PYTHON"
    3. Pass param end
"""

"""
def coder1(str1, end):
    # Process data
    str_list = str1.split()
    for data in str_list:
        print(data, end=end)


def coder2(str1, end):
    # To process data
    # Get the next pipe line
    new_str = str1.strip().upper()
    print("Coder2:", new_str)
    return coder1(new_str, end)

# Fetch data and point to the policy
str_list = coder2("  hello  itcast  python", "+")
"""

"""
    1. Pipe line process-4
    2. Example: "     hello  itcast  python" -> "HELLO: ITCAST:PYTHON"
    3. By using **kwargs
"""


def coder1(str1, **kwargs):
    # Process data
    str_list = str1.split()
    for data in str_list:
        print(data, **kwargs)


def coder2(str1, **kwargs):
    # To process data
    # Get the next pipe line
    new_str = str1.strip().upper()
    print("Coder2:", new_str)
    return coder1(new_str, **kwargs)

# Fetch data and point to the policy
str_list = coder2("  hello  itcast  python", end="%")