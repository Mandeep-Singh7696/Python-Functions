##Solution 9
def speed(s):
    if s<=70:
        return 'ok'
    else:
        sp=(s-70)//5
        if sp<=12:
            return sp
        else:
            return 'license suspended'
sp=int(input('Enter the Speed :'))
sol=speed(sp)
print(sol)
