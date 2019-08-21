# A Function that accepts an array of 10 integers (between 0 and 9),
# that returns a string of those numbers in the form of a phone number.
# eg: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] ==>> (123) 456-7890


def create_phone_number_1(n):
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


def create_phone_number_2(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


print(create_phone_number_2([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
