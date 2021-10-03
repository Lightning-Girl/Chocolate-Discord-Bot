names = []

def ship(al1,bl1):
  #names = []
  al = al1.lower()
  bl = bl1.lower()
  CA = ""
  for a in al:
    CA += a
    #CA2 = ""
    NCA = a
    CB = ""
    for b in bl:
      CB += b
      NCB = b
      NC = NCA + NCB
      NCC = NCA + CB
      CA1 = CA + NCB
      CA2 = CA + CB
      
      names.append(NC)
      names.append(NCC)
      names.append(CA1)
      names.append(CA2)
  for i in names:
    num = 0
    for o in i:
      num += 1
      if o == i[0]:
        o1 = o.upper()
        #i[0] = o1
    if num <= 2:
      #print(i)
      #print('LESS')
      names.remove(i)
  #names.remove('L')




