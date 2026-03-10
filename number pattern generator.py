def number_pattern(n):
    if isinstance(n,int)==False:
        return 'Argument must be an integer value.'
    if n<1:
        return 'Argument must be an integer greater than 0.'
    ans=''
    for i in range(1,n+1):
        ans+=str(i)+' '
    return ans.strip()   
print(number_pattern(69))
