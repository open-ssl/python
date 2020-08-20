from datetime import datetime
import time

# Test did Stanislav Lukyanov 20.08.2020   22-15 
# Conslusion about Test
# Average execution time of bool is better


def func_with_none(obj):
    t1 = datetime.now()
    if object is not None:
        print("IS NOT NONE")
    time.sleep(1)
    t2 = datetime.now()
    return t2 - t1

def func_with_bool(obj):
    t1 = datetime.now()
    if bool(obj):
        print("IS BOOL")
    time.sleep(1)
    t2 = datetime.now()
    return t2 - t1

# FIRST START                   # SECOND START

# IS NOT NONE                   # IS NOT NONE
# 0:00:01.001058                # 0:00:01.000056
# IS BOOL                       # IS BOOL
# 0:00:01.000057                # 0:00:01.000057
# IS NOT NONE                   # IS NOT NONE
# 0:00:01.000057                # 0:00:01.000058
# IS BOOL                       # IS BOOL
# 0:00:01.000057                # 0:00:01.000058
                                # IS NOT NONE
                                # 0:00:01.000058
                                # 0:00:01.000055
new_dict = {
    'text1' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
    'text7' : 1,
}

print(func_with_none("THIS IS PLAIN TEXTttttttttttttttttttttttttttttttttttttttttttttttttttT"))
print(func_with_bool("THIS IS PLAIN TEXTttttttttttttttttttttttttttttttttttttttttttttttttttT"))

print(func_with_none(new_dict))
print(func_with_bool(new_dict))


print(func_with_none(None))
print(func_with_bool(None))
