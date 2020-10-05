# this one is like your scripts with argv
def print_two(*args): # 函数名后可以不紧跟着(.
    arg1, arg2 = args # 将参数解包
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no argument
def print_none():
    print("I got nothin'.")


print_two("wen","jin")
print_two_again("wen","jin")
print_one("xie")
print_none()