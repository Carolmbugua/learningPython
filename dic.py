#dict is unordered design of object
#In dict we store in akey value pair
#we use {} to declare a dict

my_dict ={
    1:'orange',
    2:'bananas',
    3: 'grapes'
}
details ={
    'name' :'joshua',
    'id no' : '34677886',
    'parents': {
        'mom':'Nelly',
        'dad':'David'
    }
}
print(my_dict[2])

y = details['parents']
#y = details['parents']['mom']
print(y['mom'])
 #change or add elements in adict
 #delete