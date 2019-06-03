#positional formatting
print('to {}. Lorem ipsum dolor sit amet, consectetur {} adipisicing elit, {} sed do eiusmod tempor incididunt ut labore {} et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. {} Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'.format('egoing', 12, 'egoing',15,658))

print()
#Named placeholder
print('''to {name}. Lorem ipsum dolor sit amet, consectetur {age} adipisicing elit, {name} sed do eiusmod tempor incididunt ut labore {name} et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. {age:d} Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'''.format(name= 'egoing', age = 12))
