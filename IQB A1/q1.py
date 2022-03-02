Match_score = 2
Missmatch_score = -1
Gap_score = -1
# Gap_score=-2

# seq1=input()
# seq2=input()
seq1 = "ATCAGAGTA"
seq2 = "TTCAGTA"
seq1 = seq1.upper()
seq2 = seq2.upper()

sol1list=[]
sol2list=[]
scorelist=[]

# print(seq1)
# print(seq2)
elemets = ['A', 'G', 'C', 'T']

#function to initialise matrix
def createmat(seq1, seq2):
    for i in seq1:
        if (i not in elemets):
            print("Error")
    for i in seq2:
        if (i not in elemets):
            print("Error")
    dim1, dim2 = (len(seq1) + 1, len(seq2) + 1)
    mat = [[0 for i in range(dim1)] for j in range(dim2)]
    score = 0
    for i in range(dim1):
        mat[0][i] = score
        score += Gap_score
    score = 0
    for i in range(dim2):
        mat[i][0] = score
        score += Gap_score
    score = 0
    return mat

#function to fill matrix
def filMat(seq1, seq2, mat):
    UtoD = 0
    LtoR = 0
    diag = 0
    for i in range(1, len(seq2) + 1):
        for j in range(1, len(seq1) + 1):
            UtoD = mat[i - 1][j] + Gap_score
            LtoR = mat[i][j - 1] + Gap_score
            if (seq2[i - 1] == seq1[j - 1]):
                diag = mat[i - 1][j - 1] + Match_score
            else:
                diag = mat[i - 1][j - 1] + Missmatch_score
            mat[i][j] = max(UtoD, LtoR, diag)
    return mat

T = createmat(seq1, seq2)
T = filMat(seq1, seq2, T)

#function to print the created matrix
def prinMat(T):
    for r in T:
        for c in r:
            if (c < 0):
                print(c, end=" ")
            else:
                print(c, end="  ")
            # print(c,end = "  ")
        print()

#funtion to print the sequence in desired form
def prinSeq(s1, s2):
    print(s1)
    print(s2)
    print("----------------")

print("a> The matrix for global alignment : ")
prinMat(T)

#function to find the sequences
def bestseq(seq1, seq2, sol1, sol2, mat, ind1, ind2,score):
    dia = mat[ind1 - 1][ind2 - 1]
    le = mat[ind1][ind2 - 1]
    upp = mat[ind1 - 1][ind2]
    if (ind1 <0 or ind2 < 0):
        sol1list.append(sol1)
        sol2list.append(sol2)
        scorelist.append(score)
        return sol1, sol2,score
    if (ind1 == 0 and ind2 == 0):
        sol1list.append(sol1)
        sol2list.append(sol2)
        scorelist.append(score)
        return sol1, sol2,score
    if(ind1==0):
        return bestseq(seq1, seq2, seq1[ind2 - 1] + sol1 ,"-"+sol2 , mat, ind1, ind2 - 1,score+Gap_score)
    if(ind2==0):
        return bestseq(seq1, seq2, "-" + sol1, seq2[ind1 - 1] + sol2, mat, ind1 - 1, ind2,score+Gap_score)
    ifMisMatch=mat[ind1][ind2]-Missmatch_score
    ifGap=mat[ind1][ind2]- Gap_score
    ifMatch=mat[ind1][ind2]-Match_score

    if (seq2[ind1 - 1] == seq1[ind2 - 1]):
        bestseq(seq1, seq2, seq1[ind2 - 1] + sol1, seq2[ind1 - 1] + sol2, mat, ind1 - 1, ind2 - 1, score + Match_score)
    else:
        bestseq(seq1, seq2, seq1[ind2 - 1] + sol1, seq2[ind1 - 1] + sol2, mat, ind1 - 1, ind2 - 1,
                score + Missmatch_score)
    if (ifGap == upp):
        bestseq(seq1, seq2, "-" + sol1, seq2[ind1 - 1] + sol2, mat, ind1 - 1, ind2, score + Gap_score)
        # print(bestseq(seq1, seq2, "-" + sol1, seq2[ind1 - 1] + sol2, mat, ind1 - 1, ind2, score + Gap_score))
    if (ifGap == le):
        bestseq(seq1, seq2, seq1[ind2 - 1] + sol1, "-" + sol2, mat, ind1, ind2 - 1, score + Gap_score)
        # print(bestseq(seq1, seq2, seq1[ind2 - 1] + sol1, "-" + sol2, mat, ind1, ind2 - 1, score + Gap_score))

bestseq(seq1, seq2, "", "", T, 7, 9,0)      #here we are calling our function to match the sequences

finalsol1=[]
finalsol2=[]
maxv=0
for i in range(len(scorelist)):
    if(maxv<scorelist[i]):
        maxv=scorelist[i]

# here we are storing the sequences with maximum score
for i in range(len(scorelist)):
    if(maxv==scorelist[i]):
        finalsol1.append(sol1list[i])
        finalsol2.append(sol2list[i])
print("Part b>")
if(len(finalsol2)>1):
    print("There were more than one alignment,all with maximum score =",maxv)
else:
    print("There was a single alignment with maximum score =",maxv)

print("Part c>")
for i in range(len(finalsol2)):
    prinSeq(finalsol1[i],finalsol2[i])
# print(finalsol1,finalsol2)

