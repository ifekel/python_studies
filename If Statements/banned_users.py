banned_users = ['Maria', 'John', 'Timothy', 'Samuel']
user = 'Ifeanyi'
print(banned_users)

if user != banned_users:
    print(f'"{user.upper()}" you can leave a message')
    print('If you disobey the instruction you will be banned from replying')
else:
    print('BANNED!!!')