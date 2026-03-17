db_pattern="v"
db_fingerprint="zv"

user_pattern=input("enter pattern:")
if user_pattern==db_pattern:
    fingerprint=input("enter fingerprint:")
    if fingerprint==db_fingerprint:
        print("phone unloked")
    else:
        print("invalied fingerprint")
else:
    print("incorrect pattern")