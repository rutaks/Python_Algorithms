def create_phone_number(n):
    phone_number = '('
    count = 1
    if(len(n) == 10):
        for i in n:
            if isinstance(i, int):
                if count == 4:
                    phone_number += ') ' + str(i)
                elif count == 7:
                    phone_number += '-' + str(i)
                else:
                    phone_number += str(i)
                count += 1
    return phone_number


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
