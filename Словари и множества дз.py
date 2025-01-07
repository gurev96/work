my_dict_ ={"Anton": 1996, 'Elena': 2000 }
print(my_dict_)
print('Год рождения Anton:', my_dict_['Anton'])
print('Год рождения Lea:', my_dict_.get('Lea', 'нет такого ключа'))
print(my_dict_)
my_dict_.update({'Andrey': 1995,
                'Sveta': 1966 })
removed_year=my_dict_.pop('Sveta')
print('удаленное значение "Sveta":', removed_year)
print(my_dict_)

#Множества

my_set_ = {1, 2, 3, 4, 5, 6, 7, 1, 2, 4, 3, 5, True, 'one', True, 'one'}
print(my_set_)
my_set_.add('string')
my_set_.add('float')
my_set_.discard(2)
print(my_set_)