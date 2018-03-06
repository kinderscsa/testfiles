# -*- coding: utf-8 -*-

def leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return "윤년"

    else:
        return "평년"
    
if __name__ == "__main__":
    year = input("년도 입력 :")
    print leap(year)
    pass
 
