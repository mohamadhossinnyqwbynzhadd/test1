def mohit_masahat():
    while True:
        try:
            tool = int(input("lotfan tool ra vared konid:"))
            arz = int(input(" lotfan arz ra vared konid:"))
        except ValueError:
            print("lotfan adad sahih vared konid")
            continue
        print("---------------------\n mohitmostatil =" , (tool+arz)* 2)
        print("masahat mostatil =" , tool * arz)
        break
    return
mohit_masahat()
print("--------------------\n roz khoobi dashte bashid")