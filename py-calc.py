import colorama #line:1:import colorama
from colorama import Fore ,Back ,Style #line:2:from colorama import Fore, Back, Style
colorama .init (autoreset =True )#line:3:colorama.init(autoreset=True)
def add (OO0OO0OO0O0OOO0O0 ,OOOO0O00000O0000O ):#line:5:def add(x, y):
    return OO0OO0OO0O0OOO0O0 +OOOO0O00000O0000O #line:6:return x + y
def div (O0O0000OO0O0OOOO0 ,O00000OO00OO000O0 ):#line:7:def div(x, y):
    return O0O0000OO0O0OOOO0 -O00000OO00OO000O0 #line:8:return x - y
def mul (OO000000O0OOO00O0 ,OO00O0OO0O000O0OO ):#line:9:def mul(x, y):
    return OO000000O0OOO00O0 *OO00O0OO0O000O0OO #line:10:return x * y
def sub (OOO0O000O0OOO000O ,OO00O00O00O00O00O ):#line:11:def sub(x, y):
    return OOO0O000O0OOO000O /OO00O00O00O00O00O #line:12:return x / y
print ('\033[31m'+'Calculator | What do you want?')#line:13:print('\033[31m' + 'Calculator | What do you want?')
print ('\033[32m'+'1. Addition')#line:14:print('\033[32m' + '1. Addition')
print ('\033[32m'+'2. Division')#line:15:print('\033[32m' + '2. Division')
print ('\033[32m'+'3. Multiplication')#line:16:print('\033[32m' + '3. Multiplication')
print ('\033[32m'+'4. Subtraction')#line:17:print('\033[32m' + '4. Subtraction')
choice =input ('Input the number shown on the left of the options: ')#line:18:choice = input('Input the number shown on the left of the options: ')
num1 =int (input ('Choose First Number: '))#line:19:num1 = int(input('Choose First Number: '))
num2 =int (input ('Choose Second Number: '))#line:20:num2 = int(input('Choose Second Number: '))
if choice =='1':#line:21:if choice == '1':
    print (f'{num1} + {num1} = {add(num1, num2)}')#line:22:print(f'{num1} + {num1} = {add(num1, num2)}')
if choice =='2':#line:23:if choice == '2':
    print (f'{num1} - {num1} = {add(num1, num2)}')#line:24:print(f'{num1} - {num1} = {add(num1, num2)}')
if choice =='3':#line:25:if choice == '3':
    print (f'{num1} x {num1} = {add(num1, num2)}')#line:26:print(f'{num1} x {num1} = {add(num1, num2)}')
if choice =='4':#line:27:if choice == '4':
    print (f'{num1} / {num1} = {add(num1, num2)}')#line:28:print(f'{num1} / {num1} = {add(num1, num2)}')
input ('Press enter to exit')