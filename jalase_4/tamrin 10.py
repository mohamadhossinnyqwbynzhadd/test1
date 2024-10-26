def EvenNumber(number):
        if number % 2 == 0:
                return number
        if__name__== '__main__':
        list_numbers = []        
while True:
                try:
                     num = input('pleas enter your number')
                     if num =="done":
                           break
                     else:
                           num = int(num)
                      list_numbers.append(num)
                except ValueError:
                     print("adad vared konid")
                     filter_numbers = filter(EvenNumber, list_numbers)
print(f"list number zoj = {list(filter_numbers)}")                