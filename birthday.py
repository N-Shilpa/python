def bdy(name):
    if name == 'Albert Einstein':
        print(name, 'birthday is', data['Albert Einstein'])
    elif name == 'Benjamin Franklin':
        print(name, 'birthday is', data['Benjamin Franklin'])
    elif name == 'Ada Lovelace':
        print(name, 'birthday is', data['Ada Lovelace'])
    else:
        print('no details')


data = {'Albert Einstein': '01/07/1965',
        'Benjamin Franklin': '05/09/1957',
        'Ada Lovelace': '10/05/1978'}
print('Welcome to the birthday dictionary. We know the birthdays of:')
name = str(input("Who's birthday do you want to look up?"))
bdy(name)
