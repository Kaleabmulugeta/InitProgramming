def get_ones(num):
    str_num=str(num)
    numbers={
   "0":"",'1':'፩','2':'፪', '3':'፫', "4":'፬', "5":'፭', "6":'፮', "7":'፯', "8":'፰', "9":'፱',\
        "10":'፲', "20":'፳', "30":'፴', "40":'፵', "50":'፶', "60":'፷', "70":'፸', "80":'፹', "90":'፺', \
        "100":'፻',"10000":"፼"}
    if len(str_num)<3:
        if len(str_num) == 1 or num % 10 == 0:
            return numbers[str_num]
        else:
            return numbers[str((num // 10)*10)] + numbers[str(num % 10)]
    elif len(str_num) == 3:
        if str_num[0] == '1' or num == 100:
            try:return numbers[str_num]
            except: return f'{numbers["100"]}{get_ones(num%100)}'
        else:
            return f'{numbers[str(num//100)]}{numbers["100"]}{get_ones(num % 100)}'
input = input("num:")
numberr = int(input)
print(get_ones(numberr))
