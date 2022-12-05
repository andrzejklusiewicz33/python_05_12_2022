# test
# pandas,numpy, matplotlib/seaborn
# netmico, paramico
# Selenium
# Pycharm, Visual Studio Code
# print('hello')
# print('hello')
# print("hello")
# print("Lubię Mc'Donalds")
# owoc='banan'
# kolor='żółty'
# print(owoc)
# print('Mój ulubiony owoc to '+owoc+". Jego kolor "+kolor)
# print('Mój ulubiony owoc to {}. Jego kolor {}'.format(owoc,kolor))
# print(f'Mój ulubiony owoc to {owoc}. Jego kolor {kolor}')
# String owoc='banan' #java
#
# owoc=input('Podaj swój ulubiony owoc:\n')
# kolor=input('Podaj kolor swojego ulubionego owocu:\n')
# print('Mój ulubiony owoc to '+owoc+". Jego kolor "+kolor)
# print('Mój ulubiony owoc to {}. Jego kolor {}'.format(owoc,kolor))
# print(f'Mój ulubiony owoc to {owoc}. Jego kolor {kolor}')
#


# 1. Napisz program który przyjmie od użyszkodnika imię oraz nazwisko, a następnie
# wypisze na konsoli komunikat typu "Witaj TwojeImie TwojeNazwisko!"

# imie=input('Podaj swoje imię:\n')
# nazwisko=input('Podaj swoje nazwisko:\n')
# print('Witaj '+imie+' '+nazwisko+'!' )
# print('Witaj {} {}!'.format(imie,nazwisko))
# print(f'Witaj {imie} {nazwisko}!')

# przerwa do 10:38

# liczba1=float(   input('podaj liczbę:\n')     )
# print(liczba1,type(liczba1))
# print(liczba1/2)

# x=1.5
# print(x,type(x))
# print('x='+str(x))
# print('x={}'.format(x))
# print(f'x={x}')

# 2. BMI= masa/(wzrost*wzrost) . Napisz program który odbierze od użytkownika jego masę
# w kilogramach i wzrost w metrach, wyliczy i wypisze BMI.

# print(pow(10,4))
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


# 3. Niech użytkownik poda jakąś liczbę. Jeśli poda dodatnią to chcemy wyświetlić tę wartość
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


# 4. Rozbuduj swój program do bmi w taki sposob by poza wyswietleniem obliczonego bmi
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

# przerwa do 11:45
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

# 5. Wyświetl 20 kolejnych potęg liczby 2

# print(pow(2,10))
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

# 6. Wydrukuj liczby w zakresie 1-100 wypisujac obok czy dana liczba jest
# parzysta czy nieparzysta

# print(11%2)

# for x in range(1,101):
#     if x%2==0:
#         print(f'{x} jest parzyste')
#     else:
#         print(f'{x} jest nieparzyste')

# 7. Napisz symulator lokaty. Symulator ma przyjmować przez zmienne:
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

# 8. Napisz pętlę while która będzie wyświetlała kolejne potęgi liczby 2 aż wartość  potęgi
# nie przekroczy wartości podanej przez użytkownika
#
# max=int(input('podaj max wartość:\n'))
# p=0
# wynik=0
# while wynik<max:
#     p+=1
#     wynik=pow(2,p)
#     print(p,wynik)


# max=int(input('podaj max wartość:\n'))
# p=0
# wynik=0
# while wynik<max:
#     print(p, wynik)
#     p+=1
#     wynik=pow(2,p)


#
# max=int(input('podaj max wartość:\n'))
# p=0
# wynik=0
# while True:
#     p+=1
#     wynik=pow(2,p)
#     if wynik>max:
#         break
#     print(p, wynik)

# 9.Napisz program który będzie dodawał kolejne losowe wartości z zakresu
# od 1 do 10 do zmiennej suma, tak dlugo az suma nie osiagnie wartosci wiekszej
# od wartosci podanej przez uzytkownika

# import random
# #print(random.randint(1,100))
# x=random.randint(1,100)
# print(x)
#
# import random
# suma=0
# max=int(input('podaj max zakres:\n'))
# while suma<max:
#     wylosowane=random.randint(1,10)
#     suma=suma+wylosowane
#     print(wylosowane,suma)

# przerwa obiadowa do 13:21
#
# tekst="siała BABA mak, dostała 10 lat bo nie płaciła VAT"
# print(tekst.upper())
# print(tekst.lower())
# print(tekst.title())
# print(tekst.replace('a','X'))
# print(tekst.lower().replace('a','X'))
# print(tekst.upper().replace('A','X'))
# print(tekst.count('a'))
# print(tekst.lower().count('a'))
# print(len(tekst))
# lista=[1,2,3,4]
# print(len(lista))
# #print(tekst.len())
# for literka in tekst:
#     print(literka)
# print('hajs '*10)
# x=input('podaj x:\n')
# print(x*10)
# if "Java">"Python":
#     print('chyba śnisz')
# else:
#     print('no rejczel...')
#
# tekst="siała BABA mak, dostała 10 lat bo nie płaciła VAT"
# print(tekst[0:11])
#
# for x in range(1,11):
#     pass
#
# tekst="siała BABA mak, dostała 10 lat bo nie płaciła VAT"
# for literka in tekst:
#     print(literka)

# 10. Napisz program który przyjmie od użyszkodnika ciąg tekstowy a następnie usunie
# z niego znaki ,.!? i wyświetli powiększony do dużych liter na konsoli
# tekst="cośtam ,.!? cośtam"
# tekst=input('daj tekst:\n')
# print(tekst.replace(',','').replace('.','').replace('!','').replace('?','').upper())
#
# for linia in open('tadzio.txt',encoding='utf-8'):
#     print(len(linia.strip()),linia.strip())

# 11. Napisz program który wyświetli na konsoli niepuste linie z pliku tekstowego
# którego nazwę poda użytkownik

# nazwa_pliku=input('podaj nazwę pliku:\n')
# for linia in open(nazwa_pliku,encoding='utf-8'):
#     if len(linia.strip())>0:
#         print(len(linia.strip()),linia.strip())


# calosc=open('tadzio.txt',encoding='utf-8').read()
# print(calosc.replace('a','X'))

# 12. Napisz program który zliczy ilość wystąpień małej lub dużej wersji ciagu
# tekstowego podanego przez użytkownika w pliku którego nazwę również poda użytkownik.

# tekst="siała BABA mak"
# print(tekst.count('a'))
# print(tekst.lower().count('baba'))
#
# nazwa_pliku=input('podaj nazwę pliku:\n')
# szukane=input('podaj szukaną frazę:\n')
# calosc=open(nazwa_pliku,encoding='utf-8').read().lower()
# print(calosc.count(szukane))


# tekst="siała baba mak"
# if tekst.count('baba')>0:
#     print('jest szukane')
# else:
#     print('nie ma')
#
# tekst="siała baba mak"
# szukane='BABA'
# if szukane.lower() in tekst.lower():
#     print('jest')
# else:
#     print('nie ma ')

# 13. Napisz wyszukiwarkę plikową. Wyszukiwarka powinna odebrać od użytkownika
# poszukiwaną frazę, oraz nazwę pliku. Wyszukiwarka powinna wyświetlić
#  linie w których znalazła poszukiwaną frazę wraz z numerem linii.
#  Wyszukiwarka powinna być nieczula na wielkosc liter.
#
# if szukana.lower() in linia.lower():
#     print(linia.strip())
#
# szukane=input('podaj szukaną frazę:\n')
# plik=input('podaj nazwę pliku:\n')
# x=0
# for linia in open(plik,encoding='utf-8'):
#     x+=1
#     if szukane.upper() in linia.upper():
#         print(x,linia.strip())


# przerwa do 14:36
#
# lista=[]
# lista=list()
# lista=[1,2,3,4]
# lista.append(5)
# print(lista)
# for e in lista:
#     print(e)
#
# lista=[]
# for x in range(1,11):
#     lista.append(f'element numer {x}')
#
# for e in lista:
#     print(e)
#
# print(len(lista))

# 14. Napisz kod który umieści w liście 10 kolejnych potęg liczby 2.
# Następnie przeiteruj po tej liście i każdy z jej elementów wyświetl
# na konsoli w osobnej linii.
#
# lista=[]
# for p in range(1,11):
#     potega=pow(2,p)
#     print(potega)

#
# lista=[]
# for p in range(1,11):
#     potega=pow(2,p)
#     lista.append(potega)
#
# for l in lista:
#     print(l)

#
# lista=[]
# for p in range(0,11):
#     lista.append(pow(2,p))
#
# for l in lista:
#     print(l)

# lista1=[1,2,3,4,5]
# lista2=lista1
# lista1.clear()
# print(lista1)
# print(lista2)

# lista1=[1,2,3,4,5]
# lista2=lista1.copy()
# lista1.clear()
# print(lista1)
# print(lista2)
#
# lista1=[1,2,3]
# lista2=[4,5,6]
# wynik=lista1+lista2
# print(wynik)

#
# lista1=[1,2,3]
# lista2=[4,5,6]
# print(lista1)
# print(*lista1)
# wynik=[*lista1,*lista2]
# print(wynik)

# def funkcja(*args):
#     pass


# lista1=[1,2,3]
# lista2=[4,5,6]
# wynik=[*lista1,*lista2]
# print(wynik)

# lista1=[1,2,3]
# lista2=[4,5,6]
# lista1.extend(lista2)
# print(lista1)

# 15. Stwórz dwie listy. Każda z list ma zawierać 10 liczb losowych z zakresu 1-10.
# Połącz te dwie listy do jednej i wyswietl na konsoli (extend albo *lista)

# import random
#
# lista1 = []
# lista2 = []
# for x in range(10):
#     lista1.append(random.randint(1, 10))
#     lista2.append(random.randint(1, 10))
# print(lista1)
# print(lista2)
# suma=[*lista1,*lista2]
# print(suma)
# suma=lista1+lista2
# print(suma)
# lista1.extend(lista2)
# print(lista1)
#
# lista=[1,2,3,4]
# lista=[
#     [1,2],
#     [2,4],
#     [3,8]
# ]
# for l in  lista:
#     print(l)
#
# wynik=[]
# for x in range(1,11):
#     podlista=[x,x*1000]
#     wynik.append(podlista)
#
# for w in wynik:
#     print(w)

#
# wynik=[]
# for x in range(1,11):
#     wynik.append( [x,x*1000] )
#
# for w in wynik:
#     print(w)

#16. Korzystajac z petli stworz liste zawierajaca elementy same bedace listami.
# Kazdy taki element ma zawierac numer potegi oraz wartosc tej potegi dla liczby 2.
#
# lista=[]
# for x in range(1,11):
#     podlista=[x,pow(2,x)]
#     lista.append(podlista)
# print(lista)
# for e in lista:
#     print(e)

# lista=[]
# for x in range(1,11):
#     lista.append([x,pow(2,x)])
# print(lista)
# for e in lista:
#     print(e)
#
# lista=[]
# for e in range(1,11):
#     lista.append(e)
#
# print(lista)

# lista=[e for e in range(1,11)]
#
# print(lista)

# lista=[]
# for e in range(1,11):
#     lista.append(e*1000)
# print(lista)
#
# lista=[e*1000 for e in range(1,11)]
# print(lista)
#
# print([e*1000 for e in range(1,11)])
#
# import random
# lista=[random.randint(1,50) for e in range(1,11)]
# print(lista)
#
# lista=[1,2,3,4,5,6,7,8]
# wynik=[]
# for e in lista:
#     if e%2==0:
#         wynik.append(e)
#
# print(wynik)
#
# wynik=[e for e in lista if e%2==0]
# print(wynik)
#
# wynik=[e*1000 for e in lista if e%2==0]
# print(wynik)

#17. Korzystając z list składanych wygeneruj listę zawierajaca 10 kolejnych poteg 2

# lista=[]
# for p in range(1,11):
#     lista.append(pow(2,p))
# print(lista)
#
# lista=[pow(2,p) for p in range(1,11)]
# print(lista)
#
# print([pow(2,p) for p in range(1,11)])

#18.  Korzystając z list składanych wygeneruj listę 10 elementow której każdy element
# również będzie listą. Pierwszy element tej podlisty to numer potegi,
# a drugi to wartosc tej potegi dla liczby 2

#
# lista=[]
# for x in range(1,11):
#     podlista=[x,pow(2,x)]
#     lista.append(podlista)
# print(lista)
#
#
# lista=[ [x,pow(2,x)] for x in range(1,11)]
# print(lista)
#
# print([ [x,pow(2,x)] for x in range(1,11)])

# lista=[ [x,pow(2,x)] for x in range(1,11)]
# for e in lista:
#     print(e)


# for e in [ [x,pow(2,x)] for x in range(1,11)]:
#     print(e)
#
# linia='1;Andrzej;Klusiewicz;1.76;80'
# lista=linia.split(';')
# print(lista)
# print(lista[1])
# print(lista[1].lower())


#19. Napisz program który z pliku dane.csv wyświetli powiekszone imiona i nazwiska
