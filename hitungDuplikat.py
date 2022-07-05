def hitungDuplikat(buah1):
    asc = {}
    
    #sorting alphabetical order buah1
    for i in range(len(buah1)-1):
        for j in range(i+1,len(buah1)):
            if buah1[i]>buah1[j]:
                temp = buah1[i]
                buah1[i] = buah1[j]
                buah1[j] = temp
    
    #like set
    for i in buah1:
        a = 0
        for j in i:
            x = ord(j)
            a+=x
        if i not in asc:
            asc[a] = i
    
    print('jadi ada',len(asc),'macam buah yang harus dibeli Andi, yaitu:')
    for i, j in asc.items():
        hitung = 0
        for k in buah1:
            if k == j:
                hitung += 1
        print(j, ' ada',hitung, ' buah')
        
buah1 = ['semangka','semangka','durian','mangga','jeruk','mangga','mangga']

hitungDuplikat(buah1)
