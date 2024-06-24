# Split Binary
# 2022 
# Nuha Abougoash

def SplitBinary(n):
  """For a positive integer n, this function will first convert n to binary form B.  Assume that the binary form has N digits.  Next, if L=1, then it will return B.  Otherwise, it will split the B into two equal parts: the first part will be the first ceiling(L/2) digits of B, call that F, and the second part will be the remaining (L-ceiling(L/2)) digits, call that S.  Next F and S will be converted to decimal form, and finally multipled together to form the output. """
  B = bin(n)[2:]
  if (len(B) == 1):
    return int(B)
  if (len(B)%2 == 0):
    Half = len(B)//2
    Second = Half
  else:
    Half = len(B)//2+1
    Second = Half-1
  F = int(B[:Half],2)
  S = int(B[Half:],2)
  return((F+1)*(S+1))

#for i in range(30):
#  print(i,SplitBinary(i))

n = int(input("Enter a starting value: "))
L = [n] 
EndLoop = False

for i in range(20):
    print(L[-1])
    if L[-1] in L[:-1]:
        # The last term also appeared somewhere else
        # which means we've found a "loop"
        EndLoop = True
        break
    Next = SplitBinary(L[-1])
    L.append(Next)


if EndLoop:
    print("Duplicate Found!")
else:
    print("20 iterations and no duplicates")
