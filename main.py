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
#
# liczba=float(input('podaj liczbę:\n'))
# if liczba>0:
#     print(f'{liczba} jest dodatnia')
# elif liczba==0:
#     print(f'{liczba} jest zerem')
# else:
#     print(f'{liczba} jest ujemna')


#4. Rozbuduj swój program do bmi w taki sposob by poza wyswietleniem obliczonego bmi
#  wyświetlił nam również odpowiedni opis wg skali z Wikipedii.
#
# wzrost=float(input('podaj wzrost w metrach:\n'))
# masa=float(input('podaj masę w kilogramach:\n'))
# print(f'wzrost={wzrost}')
# print(f'masa={masa}')
# bmi=round(masa/pow(wzrost,2),2)
# print(f'bmi={bmi}')
# if bmi<16:
#     print('wygłodzenie')
#

#
# x=1
# y=1
# if x==1 and y==1:
#     print('oba są równe 1')


# wzrost=float(input('podaj wzrost w metrach:\n'))
# masa=float(input('podaj masę w kilogramach:\n'))
# print(f'wzrost={wzrost}')
# print(f'masa={masa}')
# bmi=round(masa/pow(wzrost,2),2)
# print(f'bmi={bmi}')
# if bmi<16:
#     print('wygłodzenie')
# elif bmi<17:
#     print('wychudzenie')
# elif bmi<18.5:
#     print('niedowaga')
# elif bmi<25:
#     print('masa ok')
# elif bmi<30:
#     print('nadwaga')
# elif bmi<35:
#     print('otyłość 1 stopnia')
# elif bmi<40:
#     print('otyłość 2 stopnia')
# else:
#     print('otyłość 3 stopnia')

#przerwa do 11:45
#
# for x in range(10):
#     print('siema!')
#
# while 1==1:
#     print('siema!')
#
# for x in range(10):
#     print('siema!')


# for x in range(10):
#     print(f'siema po raz {x}!')

# for x in range(1,11):
#     print(f'siema po raz {x}!')

# for x in range(1,11,2):
#     print(f'siema po raz {x}!')
#
# for x in range(1,11):
#     print(f'{x}*10={x*10}!')

#5. Wyświetl 20 kolejnych potęg liczby 2

#print(pow(2,10))
#
# for p in range(1,21):
#     print(p,pow(2,p))
#
# for x in range(-10,11):
#     if x<0:
#         print(f'{x} jest ujemne')
#     elif x==0:
#         print(f'{x} jest zerem')
#     else:
#         print(f'{x} jest dodatnie')
# print('koniec')

#6. Wydrukuj liczby w zakresie 1-100 wypisujac obok czy dana liczba jest
  # parzysta czy nieparzysta

#print(11%2)

# for x in range(1,101):
#     if x%2==0:
#         print(f'{x} jest parzyste')
#     else:
#         print(f'{x} jest nieparzyste')

#7. Napisz symulator lokaty. Symulator ma przyjmować przez zmienne:
  # - kwotę lokaty
  # - oprocentowanie w skali roku
  # - ilość miesięcy na jaką zakladamy lokatę
  # Symulator ma dla każdego miesiąca lokaty wypisać który to miesiąc
  # oraz ile mamy aktualnie zgromadzone na koncie po doliczeniu odsetek.
  # Kapitalizacja comiesięczna
#
# hajs=100000
# oprocentowanie=0.08
# ilosc_miesiecy=24
#
#
# for m in range(1,ilosc_miesiecy+1):
#     hajs=round(hajs+(hajs*oprocentowanie/12),2)
#     print(m,hajs)


# hajs=100000
# oprocentowanie=-0.2
# ilosc_miesiecy=60
#
#
# for m in range(1,ilosc_miesiecy+1):
#     hajs=round(hajs+(hajs*oprocentowanie/12),2)
#     print(m,hajs)

# for x in range(1,11):
#     if x==5:
#         continue
#     print(x)

#
# for x in range(1,11):
#     if x==5:
#         break
#     print(x)
# print('koniec')

#
# for x in range(1,11):
#     if x==5:
#         exit()
#     print(x)
# print('koniec')
#
# suma=0
# x=0
# while suma<1000:
#     x=x+1
#     suma=suma+x
#     print(x,suma)

#
# suma=0
# x=0
# while suma<1000:
#     #x=x+1
#     x+=1
#     #suma=suma+x
#     suma+=x
#     print(x,suma)

#8. Napisz pętlę while która będzie wyświetlała kolejne potęgi liczby 2 aż wartość  potęgi
# nie przekroczy wartości podanej przez użytkownika
