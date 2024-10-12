try:
    age = int(input("pleas enter your age:"))
    if age <=0:
        print("sary")
    elif age >=18:
        print("you can vote!")
    else:
        print("you can not vote!") 
except ValueError:
    print("voroodi hat ashtebah ast!")

except KeyboardInterrupt:
    print("voroodi ashtebah ast!") 

except BaseException as e:
    print(f"khataii dide shode ast!")

finally:
    print("rooz khobi dashte bashei") 
                         