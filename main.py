"""
10.Toate numerele sunt pare.
13.Toate numerele sunt formate din cifre prime.
11. Toate numerele au același număr de biți de 1 în reprezentarea binară.

"""


def get_longest_all_even(lst: list[int]):
    lst2 = []
    lstmax = []
    nr = 0
    nrmax = -1
    for i in lst:
        if i % 2 == 0:
            lst2.append(i)
            nr = nr + 1
            if nr > nrmax:
                lstmax = lst2
                nrmax = nr
        if i % 2 == 1:
            nr = 0
            lst2 = []
    return lstmax


def test_get_longest_all_even():
    assert get_longest_all_even([36, 11, 12, 28, 26, 19]) == [12, 28, 26]
    assert get_longest_all_even([36, 14, 12, 25, 23, 11]) == [36, 14, 12]
    assert get_longest_all_even([35, 11, 15, 23, 26, 19]) == [26]
    assert get_longest_all_even([36, 10, 12, 28, 26, 19]) == [36, 10, 12, 28, 26]


def cifprim(n):
    while (n != 0):
        if (n % 10 != 2 and n % 10 != 3 and n % 10 != 5 and n % 10 != 7):
            return False
        n = n // 10
    return True


def get_longest_prime_digits(lst: list[int]):
    lst2 = []
    lstmax = []
    nr = 0
    nrmax = -1
    for i in lst:
        if cifprim(i) == True:
            lst2.append(i)
            nr = nr + 1
            if nr > nrmax:
                lstmax = lst2
                nrmax = nr
        if cifprim(i) == False:
            nr = 0
            lst2 = []
    return lstmax


def test_get_longest_prime_digits():
    assert get_longest_prime_digits([22, 25, 337, 16, 29, 14]) == [22, 25, 337]
    assert get_longest_prime_digits([2, 3, 4, 5]) == [2, 3]
    assert get_longest_prime_digits([11, 22, 33, 55, 66]) == [22, 33, 55]
    assert get_longest_prime_digits([14]) == []


def nrbiti(n):
    nr = 0
    while (n != 0):
        if (n % 2 == 1):
            nr = nr + 1
        n = n // 2
    return nr


def get_longest_same_bit_counts(lst: list[int]):
    lst2 = []
    lstmax = []
    nr = 0
    nrmax = -1
    ok = 0
    for i in lst:
        if ok == 0:
            lst2.append(i)
            biti_anteriori = nrbiti(i)
            ok = 1
            lstmax = lst2
        else:
            if nrbiti(i) == biti_anteriori:
                lst2.append(i)
                nr = nr + 1
                if nr > nrmax:
                    lstmax = lst2
                    nrmax = nr
            if nrbiti(i) != biti_anteriori:
                nr = 0
                lst2 = []
                lst2.append(i)
                biti_anteriori = nrbiti(i)
    return lstmax


def test_get_longest_same_bit_counts():
    assert get_longest_same_bit_counts([16, 25, 36, 4, 28, 19, 17, 25]) == [28, 19]
    assert get_longest_same_bit_counts([18, 19, 20, 19, 22, 25, 17]) == [19, 22, 25]
    assert get_longest_same_bit_counts([4, 8, 11, 12]) == [4, 8]
    assert get_longest_same_bit_counts([14]) == [14]


def main():
    while True:
        print('1. Citire date')
        print('2. Determinare cea mai lungă subsecvență cu proprietatea 1 (Problema 10)')
        print('3. Determinare cea mai lungă subsecvență cu proprietatea 2 (Problema 13)')
        print('4. Determinare cea mai lungă subsecvență cu proprietatea 3 (Problema 11)')
        print('x. Iesire din program')
        optiune = input('Alege optiunea: ')
        if optiune == '1':
            print('Dati numarul de valori citite')
            lst = []
            n = int(input())
            print('Dati valorile')
            for i in range(n):
                lst.append(int(input()))
        elif optiune == '2':
            lstf = []
            lstf = get_longest_all_even(lst)
            print(lstf)
        elif optiune == '3':
            lstf = []
            lstf = get_longest_prime_digits(lst)
            print(lstf)
        elif optiune == '4':
            lstf = []
            lstf = get_longest_same_bit_counts(lst)
            print(lstf)
        elif optiune == 'x':
            break


if __name__ == '__main__':
    main()
