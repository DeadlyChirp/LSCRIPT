#ex3.txt
import random
def multiple(n) :
    return [x for x in range(n) if (x%5==0) or (x%7 ==0)]




def multiple_l( L) :
    return [x for x in L if (x%5==0) or (x%7 ==0)]

def zipping(l,m) :
    return [(l[i], m[i]) for i in range(min(len(l), len(m)))]



def transpose(matrix) :
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def tens(n):
    return [[i*10+k for k in range (10)] for i in range(n)]


def flatten(input) :
#    new_list = []
   # for i in input :
  #      for j in i : new_list.append(j)
 #   return new_list
    return [x for i in input for x in i]


def myqs(L):
    if len(L) <= 1:
        return L
    return myqs([x for x in L[1:] if x < L[0]]) + [L[0]] + myqs([x for x in L[1:] if x >= L[0]])
#       tmp = L[0]
#        left = [x for x in L[1:] if x < tmp]
#        right = [x for x in L[1:] if x >= tmp]
#        return myqs(left) + [tmp] + myqs(right)



def without_e(word_list):
    # Returns a list of words that do not contain the letter 'e'
    return [word for word in word_list if 'e' not in word]

def nstutter(text):
  mots = text.split()
  mots2 = mots[1:]
  res = [x for (x,y) in zipping(mots,mots) if x!=y + mots[-1]]
  return " ".join(res)

# Example usage:
test_words = ['hello', 'world', 'example', 'test', 'python', 'programming']
test_text = 'This is is a test test sentence sentence with with repeated repeated words words.'

# Call the functions with the example inputs
without_e_result = without_e(test_words)
nstutter_result = nstutter(test_text)

# Display the results
print(without_e_result)  # Output: ['world', 'python', 'programming']
print(nstutter_result)  # Output: 'This is a test sentence with repeated words words.'


# print(multiple(7))
# a = [1,2,3,4,5,6,7,8,9]
# b = [11,22,33,44,55,66,77,88,99]
# print(zipping(a,b))
# matrixx = [[12,7],
#     [4 ,5],
#     [3 ,8]]
# print(transpose(matrixx))
#
# flattens = [[1,2], [3,4,5], [-6]]
# print(flatten(flattens))
#
#
# arr = [1,4,3,6,8,9,0,7,5,4,3,2,5,6,7]
# print(myqs(arr))
