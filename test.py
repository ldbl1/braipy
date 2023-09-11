
# assign list
l = ['f', 'g', 'd', 's']
 
# assign string
s = 'f'
 
# check if string is present in list
if any(s in i for i in l):
    print(f'{s} is present in the list')
else:
    print(f'{s} is not present in the list')