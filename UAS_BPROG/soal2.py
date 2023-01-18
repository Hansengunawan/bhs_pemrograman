try:
    number = [2,4,6,8]
    print(number[2],"\nIndex ada di dalam variable")
    print("")

    print(number[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")
    
except IndexError:
    print("Index tidak ada dalam variable")

