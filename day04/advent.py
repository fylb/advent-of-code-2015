#!/usr/bin/env python3

import hashlib


root = "yzbqklnj"
#root = "abcdef"

def get_hash(n):
    str2hash = f"{root}{n}"
    s = hashlib.md5(str2hash.encode("utf-8")).hexdigest()
    # if s.startswith("00000"):
    #     raise Exception(str(n))
    if s.startswith("000000"):
        raise Exception(str(n))
    return s

# printing the equivalent hexadecimal value.
i = 0
while True:
    i = i+1
    if i % 10000 == 0:
        print(f"Trying {i}")
    get_hash(i)
