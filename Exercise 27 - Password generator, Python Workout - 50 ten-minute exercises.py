# Call the function create_password _generator with a string.
# That string will return a function, which itself takes an integer
# argument.Calling this function will return a password of the
# specified length, using the string from which it was created;
# for example alpha_password = create_password_generator('abcdef')
# symbol_password = create_password_generator('!@#$%')
#
# print(alpha_password(5))  # efeaa
# print(alpha_password(10))  # cacdacbada
#
# print(symbol_password(5))  # %#@%@
# print(symbol_password(10))  # @!%%$%$%%#

#Book solution:

import random


def create_password_generator(characters):


        def create_password(length):


            output = []

            for i in range(length):
                output.append(random.choice(characters))
            return ''.join(output)
        return create_password

alpha_password = create_password_generator('abcdef')
symbol_password = create_password_generator('!@#$%')

print(alpha_password(5))
print(alpha_password(10))

print(symbol_password(5))
print(symbol_password(10))

