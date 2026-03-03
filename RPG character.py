full_dot = '●'
empty_dot = '○'
def create_character(n,s,i,c):
    if not isinstance(n,str):
        return 'The character name should be a string'
    if n=='':
        return 'The character should have a name'
    if len(n)>10:
        return 'The character name is too long'
    if n.find(' ') >0:
        return 'The character name should not contain spaces'
    if not isinstance(s,int) or not isinstance(i,int) or not isinstance(c,int):
        return 'All stats should be integers'
    if s < 1 or i < 1 or c < 1:
        return 'All stats should be no less than 1'
    if s>4 or i>4 or c>4:
        return 'All stats should be no more than 4'
    if s+i+c!=7:
        return 'The character should start with 7 points'
    if s+i+c==7 and isinstance(n,str):
        return f'{n}\n'f'STR {full_dot*s}{empty_dot*(10-s)}\nINT {full_dot*i}{empty_dot*(10-i)}\nCHA {full_dot*c}{empty_dot*(10-c)}'
print(create_character('ren', 4, 2, 1))
