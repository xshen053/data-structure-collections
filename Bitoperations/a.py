def printPalindromeOfLength5():
    res = []
    fst = ""
    snd = ""
    thd = ""
    for i in range(0, 26):
        fst = chr(ord("a") + i)
        for j in range(0, 26):
            snd = chr(ord("a") + j)
            for k in range(0, 26):
                thd = chr(ord("a") + k)
                print(fst + snd + thd + snd + fst)


printPalindromeOfLength5()        
