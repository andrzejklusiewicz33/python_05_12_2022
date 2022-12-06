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

# for linia in open('dane.csv',encoding='utf-8'):
#     lista=linia.strip().split(';')
#     print(lista[1].upper(),lista[2].upper())

#20. Korzystajac z list skladanych zaladuj do listy zawartosc pliku dane.csv w taki sposób
# by linie oczyścic z bialych znaków i rozbić na listy. Każdy z elementów listy sam
# powinien byc listą. Następnie przeiteruj po wyniku i wyświetl wszystkie elementy listy   linia po linii.
#
# lista=[]
# for linia in open('dane.csv',encoding='utf-8'):
#     lista.append(linia.strip().split(';'))
# print(lista)

# lista=[ linia.strip().split(';') for linia in open('dane.csv',encoding='utf-8')]
# print(lista)
#
# for e in lista:
#     print(e)

# for e in [ linia.strip().split(';') for linia in open('dane.csv',encoding='utf-8')]:
#     print(e[1],e[2])
#
# for linia in open('dane.csv',encoding='utf-8'):
#     lista=linia.strip().split(';')
#     print(lista[2])

# lista=[linia.strip().split(';') for linia in open('dane.csv',encoding='utf-8')]
# for e in lista:
#     print(e)

# for e in [linia.strip().split(';') for linia in open('dane.csv',encoding='utf-8')]:
#     print(e[3],type(e[3]),float(e[3])/2)

#21. Dla każdego wpisu w pliku dane.csv wyświetl na konsoli dane o
#   id, imieniu,nazwisku, wzroscie,masie oraz obliczonym bmi zawodnika
#
# for e in [linia.strip().split(';') for linia in open('dane.csv',encoding='utf-8')]:
#     bmi=round(float(e[4])/pow(float(e[3]),2),2)
#     print(*e,bmi)
#
#
# for e in [linia.strip().split(';') for linia in open('dane.csv',encoding='utf-8')]:
#     bmi=round(float(e[4])/pow(float(e[3]),2),2)
#     e.append(bmi)
#     print(e)

# lista=[4,7,2,1,8,2,3,4,5]
# lista.sort()
# print(lista)

# lista=[4,7,2,1,8,2,3,4,5]
# posortowana=sorted(lista)
# print(posortowana)

#
# lista=[4,7,2,1,8,2,3,4,5]
# lista.sort()
# lista.reverse()
# print(lista)

#
# lista=[4,7,2,1,8,2,3,4,5]
# lista.sort(reverse=True)
# print(lista)

# lista=[4,7,2,1,8,2,3,4,5]
# posortowana=sorted(lista,reverse=True)
# print(posortowana)

#22. Wygeneruj listę 10 elementów o losowej wartości liczbowej,
# posortuj listę i wyświetl jej zawartość linia po linii
#
# import random
# lista=[random.randint(1,100) for e in range(10)]
# print(lista)
# posortowana=sorted(lista)
# print(posortowana)
# lista.sort()
# print(lista)

#
# lista=[
#     [2,'A'],
#     [3,'B'],
#     [1,'D'],
#     [4,'C']
# ]
# print(lista)
# lista.sort()
# print(lista)

#
# import operator
#
# lista=[
#     [2,'A'],
#     [3,'B'],
#     [1,'D'],
#     [4,'C']
# ]
# lista.sort(key=operator.itemgetter(1))
# print(lista)


# import operator
#
# lista=[
#     [2,'A'],
#     [3,'B'],
#     [1,'D'],
#     [4,'C']
# ]
# lista.sort(key=operator.itemgetter(1),reverse=True)
# print(lista)

#
# lista=[
#     [2,'A'],
#     [3,'B'],
#     [1,'D'],
#     [4,'C']
# ]
# lista.sort(key=lambda x:x[1])
# print(lista)

# class Osoba:
#     def __init__(self,i,n):
#         self.imie=i
#         self.nazwisko=n
#     def __str__(self):
#         return str(self.__dict__)
#
# lista=[]
# lista.append(Osoba('Andrzej','Klusiewicz'))
# lista.append(Osoba('Abelard','Giza'))
# lista.append(Osoba('Twoja','Stara'))
# lista.sort(key=lambda x:x.nazwisko)
# for e in lista:
#     print(e)

#23. Wczytaj do listy kolejne wiersze z pliku dane.csv. Dane posortuj po wadze i wyswietl linia po linii na konsoli

#
# lista=[linia.strip().split(';') for linia in open('dane.csv',encoding='utf-8')]
# lista.sort(key=lambda x:x[4])
# for e in lista:
#     print(e)
#
# import operator
# lista=[linia.strip().split(';') for linia in open('dane.csv',encoding='utf-8')]
# lista.sort(key=operator.itemgetter(4))
# for e in lista:
#     print(e)

#24. Wyświetl na konsoli linia po linii dane z pliku dane.csv ale posortowane  malejąco wg. bmi

# lista = [linia.strip().split(';') for linia in open('dane.csv', encoding='utf-8')]

# for e in lista:
#     wzrost=float(e[3])
#     masa=float(e[4])
#     bmi=round(masa/pow(wzrost,2),2)
#     e.append(bmi)
#
# lista.sort(key=lambda e:e[5],reverse=True)
#
# for x in lista:
#     print(x)
#
# lista = [linia.strip().split(';') for linia in open('dane.csv', encoding='utf-8')]
# for e in lista:
#     e.append(round(float(e[4])/pow(float(e[3]),2),2))
#
# lista.sort(key=lambda e:e[5],reverse=True)
#
# for x in lista:
#     print(x)

# import os
# for e in os.walk('e:\\'):
#     print(e)

#25. Napisz wyszukiwarkę plików która przyjmie od użytkownika szukaną frazę i katalog startowy.
# Wyszukiwarka ma wyswietlić wszystkie pliki i katalogi zawierajace w nazwie szukaną frazę - wraz ze ścieżkami.
# Wyszukiwarka ma być nieczuła na wielkość liter

# import os
# for e in os.walk('e:\\'):
#     print(e)
    #print(e[0]) #e jest krotką
#
# szukane=input('Podaj szukaną frazę:')
# katalog_startowy=input('Podaj katalog startowy: ')
# import os
# for e in os.walk(katalog_startowy):
#     katalogi=e[1]
#     for k in katalogi:
#         if szukane.upper() in k.upper():
#             print(os.path.join(e[0],k))
#     pliki=e[2]
#     for p in pliki:
#         if szukane.lower() in p.lower():
#             print(os.path.join(e[0],p))


#przerwa do 10:10

#PANDAS,NUMPY,MATPLOTLIB
#jupiter
#anaconda
# import matplotlib.pyplot as plt
# import random
# dane=[random.randint(1,30) for e in range(20)]
# dane2=[random.randint(1,30) for e in range(20)]
# plt.plot(dane,'#FF0000',label='czerwona kreska')
# plt.plot(dane2,'#00FF00',label='zielona kreska')
# plt.xlabel('podpis osi x')
# plt.ylabel('funkcja od x')
# plt.grid()
# plt.legend()
# plt.savefig('wykres.png')
# plt.show()

#bonus: Stwórz funkcję która przez argument przyjmie kwotę, ilość lat i wysokość inflacji,
# a następnie na wykresie przedstawi spadek wartości nabywczej podanej kwoty na przestrzeni lat.
#klusiewicz@jsystems.pl


# krotka=('1','koza','nietoperz','22 755 00 00')
# # print(krotka)
# # posortowane=sorted(krotka)
# # print(posortowane)
# # for k in krotka:
# #    print(k)
# print(krotka[1])
# print(krotka[0:3])

# lista=[1,5,4,2,3]
# krotka=tuple(lista)
# print(lista,type(lista))
# print(krotka,type(krotka))
# print(*krotka)
#
# krotka=(1,5,4,2,3)
# print(krotka)
# print(sorted(krotka))
# lista=list(krotka)
# lista.sort()
# print(lista)
# krotka=tuple(lista)
# print(krotka)
#
# list_args=[1,2,3]
# def funkcja(a,b,c):
#     print(a,b,c)
#
# funkcja(*list_args)

#26. Stwórz dwie krotki. Jedna ma zawierać 10 losowych liczb zakresu 1-10, druga 10 losowych liczb zakresu 11-20.
# Stwórz trzecią krotkę która ma zawierać dane z obu krotek. Trzecią krotkę wypisz na konsoli
#
# import random
# k1=tuple([random.randint(1,10) for e in  range(10)])
# k2=tuple([random.randint(11,20) for e in  range(10)])
# print(k1)
# print(k2)
# k3=(*k1,*k2)
# print(k3)

#27. Napisz kod ktora wyświetli w postaci listy krotek zawartość pliku dane.csv
# lista=[ tuple(e.strip().split(';')) for e in open('dane.csv',encoding='utf-8')]
# print(lista)
# for e in lista:
#     print(e)


#przerwa do 11:36

# s1={1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,4,4}
# print(s1)

# lista=[1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,4,4]
# print(lista)
# zbior=set(lista)
# print(zbior)
# lista=list(zbior)
# print(lista)
#
# lista=list(set([1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,4,4]))
# print(lista)


# s1={1,2,3,4,5,6,7,8}
# s2={5,6,7,8,9,0}
# print("część wspólna:",s1.intersection(s2))
# print("suma:",s1.union(s2))
# print("różnica s1-s2:",s1.difference(s2))
# print("różnica s2-s1:",s2.difference(s1))
#
# s=set()
# s.add(1)
# s.add('nietoperz')
# print(s)

#28. Wygeneruj dwa zestawy, dodaj do nich po 20 (w przypadku duplikatów lista może być mniejsza niż 20 elementów)
# losowych liczb z zakresu 1-40. Wyswietl ich sumę, różnicę i część wspólną
# import random
# lista=[random.randint(1,40) for e in range(20)]
# s1=set(lista)
# print(s1)

#
# import random
# s1={random.randint(1,40) for e in range(20)}
# print(s1)


#
# import random
# k1=tuple([random.randint(1,40) for e in range(20)])
# print(k1)

# import random
# s1={random.randint(1,40) for e in range(20)}
# s2={random.randint(1,40) for e in range(20)}
# print(s1)
# print(s2)
# print('suma:',s1.union(s2))
# print('część wspólna:',s1.intersection(s2))
# print('s1-s2:',s1.difference(s2))
# print('s2-s1:',s2.difference(s1))

#
# lista=['1','2','3','4','5','cos']
# lista.sort()


#29. Zduplikuj jeden z wierszy w pliku dane.csv.
# Napisz kod który zwróci do postaci listy krotek zawartość tego pliku z danymi bez powtórek.

# lista=list(set([ tuple(e.strip().split(';')) for e in open('dane.csv',encoding='utf-8')]))
# for e in lista:
#     print(e)

#
# for f in list(set([ tuple(e.strip().split(';')) for e in open('dane.csv',encoding='utf-8')])):
#     print(f)
#
# sl=dict()
# sl={}
# sl['klucz1']='wartość tekstowa'
# sl['klucz2']=12345
# sl['lista']=[1,2,3,4,5]
# print(sl)
# print( sl['klucz2'] )
# for k in sl:
#     print(k,sl[k])

#30. Stwórz plik ustawienia.conf i umieść w nim poniższe dane
# encoding=utf-8
# timezone=-2
# color=black
# Następnie wczytaj dane do słownika w ten sposób by pierwsza kolumna stanowila klucze a druga przypisane do nich
# wartości. Przeiteruj po słowniku i wypisz klucze oraz przypisane do nich wartości

#sl[ e[0] ]=e[1]
#
# lista=[e.strip().split('=') for e in open('ustawienia.conf',encoding='utf-8')]
# sl=dict()
# for f in lista:
#     sl[f[0]]=f[1]
#
# # for k in sl:
# #     print(k,sl[k])
#
# print(sl['encoding'])

#31. Wczytaj do słownika dane z pliku dane.csv tak by kluczem było imię sklejone z nazwiskiem rozdzielone spacja,
# a pozostałe dane znalazły się w wartości
#   jako krotka lub lista. Przeiteruj po slowniku i wyswietl jego zawartość.

# lista=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# sl=dict()
# for f in lista:
#     klucz=f[1]+" "+f[2]
#     wartosc=[f[0],f[3],f[4]]
#     sl[klucz]=wartosc
#
# for k in sl:
#     print(k,sl[k])

#PRZERWA OBIADOWA DO 13:08

# Tadeusz
# Tadeusz.
# Tadeusz!
# Tadeusz?
#
# tadeusz
# Tadeusz
#32. Napisz system który zwróci nam ilość wystąpień każdego ze słow w pliku w postaci listy krotek.
# [  (slowo,ilosc_wystapien),(slowo,ilosc_wystapien)   ]. Nazwa pliku ma zostać przekazana przez zmienną.
#    Wynik powinien byc posortowany malejąco wg ilosci wystapien
#    a) odczytaj wszystkie linie z pliku i rozbij na słowa. Każde ze słów dodaj do osobnej listy.
#       Zadbaj o usunięcie po drodze znaków specjalnych czyli kropek, przecinków, wykrzykników etc.
        # i unifikację wielkości tekstu
#    b) stwórz słownik i dla każdego słowa w liście sprawdz czy istnieje juz wpis dotyczący tego słowa
#       w słowniku. Jeśli nie ma to dodaj do słownika wpis o kluczu takim jak sprawdzane słowo i wartości 1
#       dla ilości wystąpień. Jeśli takie słowo pojawia się już w kluczach słownika to trzeba zwiększyc wartośc o 1
#    c) Przepakuj dane ze słownika do listy i posortuj.
# import time
# p=time.time()
# calosc=open('tadzio.txt',encoding='utf-8').read().lower()
# niechciane=['!','?','.',',',":","/","(",")",'-','…']
# for n in niechciane:
#     calosc=calosc.replace(n,'')
# slowa=calosc.split()
# sl=dict()
# for s in slowa:
#     if s in sl:
#         sl[s]+=1
#     else:
#         sl[s]=1
# wynik=[]
# for k in sl:
#     element=[k,sl[k]]
#     wynik.append(element)
# wynik.sort(key=lambda x:x[1], reverse=True)
# for w in wynik:
#     print(w)
# k=time.time()
#print(f'całość trwała {k-p}s')
#lista=calosc.split()
#
# sl=dict()
# sl['klucz1']='cos'
# if 'klucz1' in sl:
#     print('jest taki klucz')
# else:
#     print('nie ma takiego klucza')

# tekst="abc !?., def"
# niechciane=['!','?','.',',']
# for n in niechciane:
#     tekst=tekst.replace(n,'')
# print(tekst)

# sl=dict()
# klucz='klucz1'
# if klucz in sl:
#     sl[klucz]=sl[klucz]+1
# else:
#     sl[klucz]=1



#cowsay i easygui
#
# import cowsay
# cowsay.cow('Lubię pierogi')

#x=input('podaj coś:\n')
#
# import easygui
# x=easygui.enterbox('podaj wartość dla X:')
# print(x)

#przerwa do 14:28

#33. Wyświetl wynik dzielenia 1 przez kolejne liczby z zakresu -10 do 10.
#
# for x in range(-10,11):
#     print(x,1/x)

# try:
#     print(1/0)
# except:
#     print('jakiś wyjątek....')
# print('cośtam jeszcze')

# try:
#     print(1/0)
# except IndexError:
#     print('to się nie ma prawa zdarzyć')
# except EOFError:
#     print('eof')
# # except ZeroDivisionError:
# #     print('dzielenie przez zero...')
# except:
#     print('jakiś inny wyjątek')
#
# try:
#     print(1/0)
# except Exception as e:
#     print(f'wyjątek {e}')


#raise ZeroDivisionError
#raise Exception('kij Ci w oko')


#34. Wyświetl wynik dzielenia 1 przez kolejne liczby z zakresu -10 do 10 w taki sposob
# by w przypadku wyjatku nie przerywac dzialania petli a po prostu wyswietlic na konsoli
# informację o błędzie i przejsc do dalszego przetwarzania


# for x in range(-10,11):
#     print(x,1/x)

# try: #fuuuuuu
#     for x in range(-10,11):
#         print(x,1/x)
# except ZeroDivisionError:
#     print('dzielenie przez zero!')

# for x in range(-10,11):
#     try:
#         print(x,1/x)
#     except ZeroDivisionError:
#         print(f'dzielenie przez zero przy x={x}')

#35. Przetwórz wszystkie wiersze z dane.csv wyswietlajac na konsoli dane z wiersza wzbogacone o bmi.
# Nie podmieniaj przecinków etc w tekscie. W przypadku pojawienia się wyjątku na rzutowaniu na float dla
# któregoś wiersza chcemy go zapisać (cały wiersz) w osobnym pliku bledy.csv wzbogacony o informację o rodzaju błędu
#4;Andrzej;1,89;90;zero division error
#
# plik=open('wynik.txt',encoding='utf-8',mode='w')
# for x in range(1,11):
#     plik.write(f'element numer {x}\n')
# plik.close()


# with open('wynik.txt',encoding='utf-8',mode='w') as plik:
#     for x in range(1,11):
#         plik.write(f'element numer {x}\n')
#
# lista=['1','Andrzej','Klusiewicz','1.76','80','25']
# linia=";".join(lista)
# print(linia)
# linia=f"{lista[0]};{lista[1]};"

#35. Przetwórz wszystkie wiersze z dane.csv wyswietlajac na konsoli dane z wiersza wzbogacone o bmi.
# Nie podmieniaj przecinków etc w tekscie. W przypadku pojawienia się wyjątku na rzutowaniu na float dla
# któregoś wiersza chcemy go zapisać (cały wiersz) w osobnym pliku bledy.csv wzbogacony o informację o rodzaju błędu
#4;Andrzej;1,89;90;zero division error
#
#
# dane=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# for d in dane:
#     try:
#         d.append(round(float(d[4])/pow(float(d[3]),2)))
#         print(d)
#     except ValueError:
#         with open('bledy.csv',encoding='utf-8',mode='w') as plik:
#             linia=';'.join(d)+";ValueError\n"
#             plik.write(linia)

#
# def funkcja():
#     print('siema!')
#
# funkcja()

# def dodaj(a,b):
#     print(a+b)
#
# dodaj(10,20)
#
# def dodaj(a,b):
#     return a+b

#
# def dodaj(a,b):
#     wynik=a+b
#     return wynik
#     print('dupa')
#
# print(dodaj(1,2))
# x=dodaj(1,2)
# print(x)

#36.Stwórz funkcję która przyjmie wzrost i masę a zwróci zaokraglone do 2 miejsc po przecinku BMI.
# W przypadku pojawienia się wyjątku, wyświetl na konsoli jaki wystąpił problem a z funkcji zwróć -1.
#
# def bmi(w,m):
#     try:
#         bmi=round(m/pow(w,2),2)
#         return bmi
#     except ZeroDivisionError:
#         print('podałeś zerowy wzrost')
#         return -1
#     except TypeError:
#         print('podałeś nieliczbowe dane')
#         return -1
#
# print(bmi(1.76,80))
# print(bmi(0,80))
# print(bmi('koza',80))
#

# def witacz(imie,nazwisko):
#     print(f'Witaj {imie} {nazwisko}')
#
# witacz('Andrzej','Klusiewicz')

# def witacz(imie,nazwisko='nie podano'):
#     print(f'Witaj {imie} {nazwisko}')
#
# witacz('Andrzej')

# def witacz(nazwisko='nie podano',imie): #fuuuuu
#     print(f'Witaj {imie} {nazwisko}')
#
# witacz('Andrzej')

#37.  Napisz funkcję która zwróci pod postacią listy krotek zawartość pliku
#   którego nazwę przekażemy przez pierwszy argument funkcji. Plik ma być otwarty z kodowaniem
#   podanym jako drugi argument funkcji. Jeśli kodowanie nie zostanie pdane ma przyjac utf-8

# def get_data(filename,enc='utf-8',divider=';'):
#     return [e.strip().split(divider) for e in open(filename,encoding=enc)]
#
# for e in get_data('dane.csv'):
#     print(e)

#38. Napisz funkcję która bedzie w stanie przyjąć taką listę jaka jest zwracana
 # przez funkcję z poprzedniego ćwiczenia. Funkcja ta ma przeiterować po otrzymanej
 # liście i wyświetlić każdy element na konsoli. Odbierz dane z funkcji z ćwiczenia
 # poprzedniego i przekaz do nowo powstalej funkcji.
