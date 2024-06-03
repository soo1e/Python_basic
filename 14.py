# format()
# '{}'.format()

my_name = 'My name is %s' % 'Enzo'
print(my_name)

my_new_name = 'My name is {}'.format('Griezmann')
print(my_new_name)

my_lo = '{} x {} = {}'.format(2, 3, 2*3)
print(my_lo)

my_status = '{1} x {0} = {2}'.format(2, 3, 2*3)
print(my_status)