try:
    age = int(input("pleas enter your age:"))
    if age <=0:
        print("motmani?")
    elif age >=18:
        print("you can vote")
    else:
        print("you can not vote")       

except ValueError:
    print("pleas enter your number sahih")

except KeyboardInterrupt:
    print("vorudi baste shod")

except BaseException as e:
    print("be khata barkhordid")

finally:
    print("roz khubi dashte bashid!")
                         