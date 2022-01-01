# pair_array = [array[i:i+2] for i in range(0,len(array),2)]

# for i in pair_array:
#     i[0], i[1] = i[1], i[0]

# out_array = [i for sublist in pair_array for i in sublist]

def f(validCandidates, votesCasted):

    if len(votesCasted)==0:
        return 'N/A'

    winner = validCandidates[0]
    cnt=0
    for i,c in enumerate(validCandidates):
        new_cnt=votesCasted.count(c)
        if new_cnt>cnt:
            cnt=new_cnt
            winner=c

        invalid_count = sum([0 if vote in validCandidates else 1 for vote in votesCasted ])
        if invalid_count>cnt:
            return 'N/A'
        else:
            return winner

if __name__=='__main__':

    print(f(['a','b','c'], ['a','a', 'a','b','c','d']))
