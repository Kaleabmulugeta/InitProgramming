input = input("Enter a number:")
try:
    num = int(input)
except:
    print("Please enter a valid number and try again")
def integer_to_string(number):
    numbers =['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    tys = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety','hundred']
    if number <= 19:
        return numbers[number]
    elif number < 30:
        if number % 20 == 0:
            return tys[0]
        else:
            return tys[0] + numbers[number % 20]
    elif number < 40:    
        if number % 30 == 0:
            return tys[1]
        else:
            return tys[1] + numbers[number % 30]
    elif number < 50:
        if number % 40 == 0:
            return tys[2]
        else:
            return tys[2] + numbers[number % 40]
    elif number < 60:
        if number % 50 == 0:
            return tys[3]
        else:
            return tys[3] + numbers[number % 50]
print(integer_to_string(num))