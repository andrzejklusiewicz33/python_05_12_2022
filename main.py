#test
#pandas,numpy, matplotlib/seaborn
#netmico, paramico
#Selenium
#Pycharm, Visual Studio Code
#print('hello')
# print('hello')
# print("hello")
# print("Lubię Mc'Donalds")
# owoc='banan'
# kolor='żółty'
# print(owoc)
# print('Mój ulubiony owoc to '+owoc+". Jego kolor "+kolor)
# print('Mój ulubiony owoc to {}. Jego kolor {}'.format(owoc,kolor))
# print(f'Mój ulubiony owoc to {owoc}. Jego kolor {kolor}')
#String owoc='banan' #java
#
# owoc=input('Podaj swój ulubiony owoc:\n')
# kolor=input('Podaj kolor swojego ulubionego owocu:\n')
# print('Mój ulubiony owoc to '+owoc+". Jego kolor "+kolor)
# print('Mój ulubiony owoc to {}. Jego kolor {}'.format(owoc,kolor))
# print(f'Mój ulubiony owoc to {owoc}. Jego kolor {kolor}')
#


#1. Napisz program który przyjmie od użyszkodnika imię oraz nazwisko, a następnie
# wypisze na konsoli komunikat typu "Witaj TwojeImie TwojeNazwisko!"

# imie=input('Podaj swoje imię:\n')
# nazwisko=input('Podaj swoje nazwisko:\n')
# print('Witaj '+imie+' '+nazwisko+'!' )
# print('Witaj {} {}!'.format(imie,nazwisko))
# print(f'Witaj {imie} {nazwisko}!')

#przerwa do 10:38

# liczba1=float(   input('podaj liczbę:\n')     )
# print(liczba1,type(liczba1))
# print(liczba1/2)

# x=1.5
# print(x,type(x))
# print('x='+str(x))
# print('x={}'.format(x))
# print(f'x={x}')

#2. BMI= masa/(wzrost*wzrost) . Napisz program który odbierze od użytkownika jego masę
# w kilogramach i wzrost w metrach, wyliczy i wypisze BMI.

#print(pow(10,4))
#
# x=float(input('podaj x:\n'))
# print(x)
#
# wzrost=float(input('podaj wzrost w metrach:\n'))
# masa=float(input('podaj masę w kilogramach:\n'))
# print(f'wzrost={wzrost}')
# print(f'masa={masa}')
# bmi=round(masa/pow(wzrost,2),2)
# print(f'bmi={bmi}')

#
# wzrost=float(input('podaj wzrost w metrach:\n'))
# masa=float(input('podaj masę w kilogramach:\n'))
# print(f'wzrost={wzrost}')
# print(f'masa={masa}')
# print(f'bmi={round(masa/pow(wzrost,2),2)}')


# wzrost=float(input('podaj wzrost w metrach:\n'))
# masa=float(input('podaj masę w kilogramach:\n'))
# print(f'wzrost={wzrost}')
# print(f'masa={masa}')
# print(f'bmi='+str(round(masa/pow(wzrost,2),2)))

# wzrost=float(input('podaj wzrost w metrach:\n'))
# masa=float(input('podaj masę w kilogramach:\n'))
# print(f'wzrost={wzrost}')
# print(f'masa={masa}')
# bmi=round(masa/pow(wzrost,2),2)
# print(f'bmi={bmi}')

#
# x=2
# if x==1:
#     print('jeden!')
#     print('jeden!')
# else:
#     print('nie jeden!')
# print('koniec')


#
# x=2
# if x==1:
#     print('jeden!')
# elif x==2:
#     print('dwa!')
# elif x==3:
#     print('trzy!')
# else:
#     print('poza zakresem')
# print('koniec')


#3. Niech użytkownik poda jakąś liczbę. Jeśli poda dodatnią to chcemy wyświetlić tę wartość
# z informacją "wartość dodatnia", jeśli zero to wyświetlamy z informacją "równe zero",
# jeśli ujemna to wyświetlamy "wartość ujemna".

# if x<0:
#     print(f'{x} jest ujemne')