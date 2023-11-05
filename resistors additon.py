Resistor1=int(input('enter the first resistor value=='))
Resistor2=int(input('enter the secound resistor value=='))
print('\n \n READ THE FOLLOWING STATEMENTS CLEARLY TO PROCEED \n \n')
print('enter (S) if they are connected series \n [P] if they are connected parallel \n if to check both enter (SP)')
print('reply only in CAPITAL LETTERS__like P or S')
check_connections=input('THEY ARE CONNECTED IN ==')
def resistors(R1,R2,check_connection):
    if check_connection=='S' :
        R_EQ=R1+R2
        return'resistors when connected in series=',R_EQ
    elif check_connection=='P':
        R_EQ=(R1*R2)/(R1+R2)
        return 'resistors when connected in parallel=' , R_EQ
    elif check_connection=='SP':
        R_EQ=R1+R2
        R_EQ1=(R1*R2)/(R1+R2)
        return 'resistors when connected in parallel=' , R_EQ , 'and' ,'resistors when connected in series=',R_EQ1
    else:
        print("you did not responded in correct format please check again")
print(resistors(Resistor1,Resistor2,check_connections))
