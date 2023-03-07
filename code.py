
def cutTheTree(data, edges): # CORRECTION TO SETUP: data 0-indexed

    T, L, d,D = {a:set() for a in range(1,1+n)}, {1}, 0, [0]*(1+n)
    for a,b in edges : T[a].add(b) ; T[b].add(a) # start symmetric
    while L : # decycle graph T into a tree and calculate depths D
        L1 = set() # becomes all visited nodes at depth level d
        for a in L :
            D[a] = d ; L1 |= T[a]
            for b in T[a] : T[b].remove(a)
        d += 1 ; L = L1
    for a in sorted( range(1,1+n), key=lambda x:-D[x] ):#bottom up
        data[a-1] += sum( data[b-1] for b in T[a] ) #find subtotal
    return min( abs(data[0]-2*data[x]) for x in range(1,n) )
  
