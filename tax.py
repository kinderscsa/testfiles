# -*- coding: utf-8 -*-

def tax(age, money, taxcharge):
    res=0
    taxcharge=True
    if age >= 16 and age <=65:
        if taxcharge == True:    
            if 20000 > money:
                res=money*0.4
                return int(res)
            else:
                res=money*0.1
                return int(res)

        elif taxcharge == False:

            if 20000 < money:
                res=money*0.2
                return int(res)

            else:
                res=money*0.5
                return int(res)




