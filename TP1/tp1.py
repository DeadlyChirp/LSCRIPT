

# ex1.1
# >>> import math
# >>> 3/4
# 0.75
# >>> 4/2
# 2.0

#  3//4
# >>> import math
# >>> 3//4
# 0
# >>> 4//2
# 2

# >>> type(3/4)
# <class 'float'>
# >>> type(3//4)
# <class 'int'>



# >>> type(3j+1)
# <class 'complex'>

# 1.3
# 1j**2 evaluates to (-1+0j), which means squaring the imaginary unit j results in -1. In Python, j is used to denote the imaginary part of a complex number.
# (1+2j).imag gives 2.0, which is the imaginary part of the complex number 1+2j.
# (1+2j).real gives 1.0, which is the real part of the complex number 1+2j.

# ex3.txt
# >>> (19875+77569)%7
# 4


# >>> 3 ** 2 + 56/9 * abs(-1/4)
# 10.555555555555555

# >>> num1 = 3 ** 2
# >>> num2 = 56/9
# >>> num3 = abs(-1/4)
# >>> print(num3)
# 0.25
# >>> res=num1 + num2 * num3
# >>> print(res)
# 10.555555555555555


# ex4.txt
# >>> hex(30)
# '0x1e'

# 4.2
# >>> int('101',2)
# 5
# 101 en base 2 est 5

# >>> int('101',8)
# 65

# >>> int('101',10)
# 101

# >>> int('101',16)
# 257

# >>> int('101')
# 101


# 4.3
# >>> hex(int('111001',2))
# '0x39'

# ecrire une suite d'’instructions permettant de lire un
# entier puis d’afficher le double de sa valeur.

# 4.4
# >>> nbr = int(input("Enter number : "))
# Enter number : 11001101
# >>> double = nbr * 2
# >>> print("le double de nbr est :", double)
# le double de nbr est : 22002202


# ex5 :

# >>> h = 'hello'
# >>> w = 'World'
# >>> hw = h + ' ' + w
# >>> print(hw)
# hello World

# >>> h+2*(h+2*w)
# 'hellohelloWorldWorldhelloWorldWorld'

# >>> hw2 = "Hello World"
# >>> hw3= h + w
# >>> print(hw2)
# Hello World
# >>> print(hw3)
# helloWorld

# ex6
# >>> line1 = """Dans le viel etang,Une grenouille saute, Bruit dans l'eau line1"""
# >>> line2 = 'Dans le viel etang,\n Une chip line 2,\n line 2 line 2'
# >>> print(line1)
# Dans le viel etang,Une grenouille saute, Bruit dans l'eau line1
# >>> print(line2)
# Dans le viel etang,
#  Une chip line 2,
#  line 2 line 2


# les chaines de caracteres qui sont entourees par " ou ', le \n represente un retour a la ligne

# ex7 :
# >>> len("hello")
# 5

# >>> "e" in "hello"
# True

# >>> "E" in "hello"
# False

# in sert a verifier si le caractere est bien present dans le str ou non.
# qui renvoie true ou false


# ex8

# 8.1
# >>> s[4]
# '4'

# >>> s[-4]
# '6'

# >>> s[:4]
# '0123'

# >>> s[-4:]
# '6789'

# >>> s[:]
# '0123456789'

# >>> s[:4] + s[4:]
# '0123456789'

# 8.2
# >>> UnsurDeux = s[::2]
# >>> print(UnsurDeux)
# 02468

# 8.3
# >>> q2 = s[::-1]
# >>> print(q2)
# 9876543210


# ex9

# 9.1
# x == y and x == z and y == z se simplifie en x == y and y == z. En effet, si x est égal à y, et que x est aussi égal à z, cela signifie par transitivité que y est égal à z. Donc, la troisième condition y == z est redondante.
#
# x == 17 or (x != 17 and x == 42) se simplifie en x == 17 or x == 42. L'expression dans la parenthèse (x != 17 and x == 42) peut seulement être vraie si x est 42, mais si x est 42, la première condition x == 17 sera fausse. Ainsi, l'expression entière est vraie si x est soit 17, soit 42.
#
# x > 5 or (x <= 5 and y > 5) se simplifie en x > 5 or y > 5. Si x est supérieur à 5, l'expression est vraie. Si x est inférieur ou égal à 5, alors la seule autre condition qui pourrait rendre l'expression vraie est que y soit supérieur à 5.
#
# not (x > 3 and x == 5) or not (x < 5 or x > 5) se simplifie en not (x == 5) or not (True), ce qui revient finalement à not (x == 5). L'expression x < 5 or x > 5 est toujours vraie parce qu’un nombre est toujours inférieur ou supérieur à 5, ce qui rend not (x < 5 or x > 5) toujours faux. Donc, l'expression se réduit à not (x > 3 and x == 5), ce qui est équivalent à not (x == 5) car x > 3 est toujours vrai si x == 5.
#
# Pour résumer, les expressions simplifiées sont :
#
# x == y and y == z
# x == 17 or x == 42
# x > 5 or y > 5
# not (x == 5)


#ex12 :
#0, 1, 2, 3, 4, 5, 6, 7, 8, 9

#0, 3, 6, 9

#9, 8, 7, 6, 5, 4, 3, 2, 1, 0
#8203;``【oaicite:0】``&#8203;
