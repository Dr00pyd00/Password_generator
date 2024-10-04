
import random
import string

def main():
    
    '''Ask to the user some informations about the new passwords'''
    
    #lenght:
    user_lenght = is_int("What lenght do you want your password : ")

    #contain: upper, lower, digits, special signs:
    user_uppercase = yes_or_no_input('Do you want your password contain uppercases? ')
    user_lowercase = yes_or_no_input('Do you want your password contain lowercases? ')
    user_digit = yes_or_no_input('Do you want your password contain digitals numbers? ')
    user_special_char = yes_or_no_input('Do you want your password contain punctuation signs? ')


    #run the func for create a password with values asked:
    print(create_password(lenght= user_lenght, uppercase=user_uppercase, lowercase=user_lowercase, digit=user_digit, special_char=user_special_char))





def create_password(lenght = 6, uppercase = True, lowercase = True, digit = True, special_char = True ):
    '''  A function for create a password and can choose bank of char , user can choice it !!'''

    #empty str
    possibilities_as_str = ''
    password = ''

    #if statements : add some strings in my variable for grow the random choice of password

    if uppercase == True:
        possibilities_as_str = possibilities_as_str  + string.ascii_uppercase

    if lowercase == True:
        possibilities_as_str = possibilities_as_str  + string.ascii_lowercase

    if digit == True:
        possibilities_as_str = possibilities_as_str  + string.digits

    if special_char == True:
        possibilities_as_str = possibilities_as_str + string.punctuation


    #if no one selected go lowercase by default:
    if possibilities_as_str =='':
        print('You need to include at least one type of character! Default: lowercase letters.')
        possibilities_as_str += string.ascii_lowercase
    #use a for loop for output the correct length of password:
    for _ in range(lenght):
        password = password + random.choice(possibilities_as_str)


    return f'Your new password is : {password}'


def yes_or_no_input(arg):
    ''' This funct: if the input is not yes or no : them ask again and again '''
    while True:
        user_input = input(arg)

        if user_input.lower() == 'yes' or user_input.lower() == 'y':
            return  True

        if user_input.lower() == 'no' or user_input.lower() == 'n':
            return False

        else:
            print('Need a "Yes" or a "No')


def is_int(arg):
    ''' This funct check if the input is a integer , if it's not , it's ask again !'''
    while True:
        try:

            user_input = int(input(arg))
            if user_input > 0:
                return user_input

            else:
                print('Need more than 0 lenght !')

        except ValueError:
            print('Need a Integer please !')



if __name__ =='__main__':
    main()
