db_coupon_code=3024
coupon_code=int(input("enter code:"))

if db_coupon_code==coupon_code:
    amound=int(input("enter amound:"))
    if amound<1000:
        print("coupon applied")
    else:
        print("below 1000/- only")
else:
    print("code invalied")
    