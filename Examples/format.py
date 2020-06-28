#Строковые занчения
'{} {}'.format('one', 'two') #one two

#Числовые значения
'{} {}'.format(1, 2) #1 2

#порядок значений можно указывать
'{1} {0}'.format('one', 'two') #two one

#Можно так же подставлять значения классов
class Data(object):

    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'

'{0!s} {0!r}'.format(Data()) #str repr

#Отступы и выравнивания
#по правому краю
'{:>10}'.format('test') #      test

#по левому краю
'{:_<10}'.format('test') #test______

#по центру
'{:^10}'.format('test') #   test

#срезы
'{:.5}'.format('xylophone') #xylop

#срезы и отступы
'{:10.5}'.format('xylophone') #xylop

#числа
'{:d}'.format(42) #42
'{:f}'.format(3.141592653589793) #3.141593

#числа и отступы
'{:4d}'.format(42) #  42
'{:06.2f}'.format(3.141592653589793) #003.14
'{:04d}'.format(42) # 0042

#знаковые числа
'{:+d}'.format(42) #+42
'{: d}'.format((- 23)) #-23
'{: d}'.format(42) # 42
'{:=5d}'.format((- 23)) #-  23
'{:=+5d}'.format(23) #+  23

#можно вставлять значения по именам
data = {'first': 'Hodor', 'last': 'Hodor!'}
'{first} {last}'.format(**data) #Hodor Hodor!
'{first} {last}'.format(first='Hodor', last='Hodor!') #Hodor Hodor!

#Формат даты и времени
from datetime import datetime
'{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5)) #2001-02-03 04:05
