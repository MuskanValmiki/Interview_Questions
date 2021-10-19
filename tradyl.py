def tradyl():
    country_code=input("enter your country name=")
    product_code=input("enter your product code=")
    weight=float(input("enter your weight in kg="))
    if country_code=="UK" or country_code=="uk":
        if weight<5:
            shipping=5
            if product_code[0:3]=="123":
                cost=shipping*1.2*(1+0.18)
                print(cost)
            elif product_code[0:3]=="234":
                cost=shipping*1.5*(1+0.18)
                print(cost)
            else:
                cost=shipping*(1+0.18)
                print(cost)
        elif weight>=5:
            shipping=15
            if product_code[0:3]=="123":
                cost=shipping*1.2*(1+0.18)
                print(cost)
            elif product_code[0:3]=="234":
                cost=shipping*1.5*(1+0.18)
                print(cost)
            else:
                cost=shipping*(1+0.18)
                print(cost)
    elif country_code=="US" or country_code=="us":
        if weight<10:
            shipping=5
            if product_code[0:3]=="123":
                cost=shipping*1.2*(1+0.18)
                print(cost)
            elif  product_code[0:3]=="234":
                cost=shipping*1.5*(1+0.18)
                print(cost)
            else:
                cost=shipping*(1+0.18)
                print(cost)
        elif weight>=10:
            shipping=15
            if product_code[0:3]=="123":
                cost=shipping*1.2*(1+0.18)
                print(cost)
            elif product_code[0:3]=="234":
                cost=shipping*1.5*(1+0.18)
                print(cost)
            else:
                cost=shipping*(1+0.18)
                print(cost)
    else:
        print("the shipping cost is Not applicable")
tradyl()