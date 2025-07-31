dict = {'a':3,'b':5,'c':6,'d':9}
print(dict)
check_key = input("Enter key to check:")
check_value = input("enter value:")
if check_key in dict:
    print(check_key,"is present.")
    dict.pop(check_key)
    dict[check_key] = check_value
else:
    print(check_key,"is not present.")
    dict[check_key]=check_value
    print("updated dictionary:",dict)
    