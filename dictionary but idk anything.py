import random
d={}
num=random.randint(1,6)
print(num)
while True:
    print('1. idk 1')
    print('2. idk 2')
    print('3. idk 3')
    print('4. idk 4')
    print('5. idk 5')
    print('6. idk 6')
    print('7. idk 7')
    
    option = input('choose any chapter but 2 because 2 is broken lol :  ')
    
    if option == '6' :
        print('nice?')
        break
    
    elif option == '1' :
        print('e')
    
        while True:
            voc = input('idk lel')        
            if voc == '0' :
                break
            if voc not in d:
                voc_ch = input('still dont know :/')
                d[voc] = voc_ch   
            else:
                print('YOU FELL FOR IT FOOL! THUNDER-CROSS SPLIT ATTACK! *write number please ty*')
            
            if option == '2' :
                s=sorted(d)
            
            for i in s:
                print(i,':',d[i])
                
    elif option == '3' :
        while True:
            voc = input('number lol　　:')
            if voc == '0':
                break
            if voc in d :
                print(voc,'no minecraft noob ez',d[voc])
        else:
            print('explainnnnnnn also gib me numba or bad             ')
    elif option == '4' :
        while True:
            got = 'false'
            ch = input('snfdkjsnfdsjnfjsd')
            if ch == '0':
                break
            for k,v in d.items():
                if ch == v:
                    print(ch,'asohfdoashdoasihdohasod',k)
                    
    elif option == '7' :
        while True:
            e = int(input("numbas u have reached hidden place!?!?!"))
            if e >= 900 :
                print('kekekekekekekekekekekek not secret noob get recked ez')
                break
        else: 
            print('wannabruh')
            break