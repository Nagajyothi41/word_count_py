def wordy(first,second):
    if(first==second):
        return "Yes"
    else:
        return "No"

def word(n,m):
    first,second=list(n), list(m)
    for i in range(len(first)-1):
        if (first[i]!=second[i]):
            temp=first[i]
            first[i]=first[i+1]
            first[i+1]=temp
            break
    re=wordy(first,second)
    return re 
def main():
    n,m=input(),input()