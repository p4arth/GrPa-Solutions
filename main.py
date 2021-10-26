def minor_matrix(M, i, j):
  m = M

  m.remove(m[i])
  print(m)

  for k in range(len(m)):
    for h in range(len(m)):
      if h == j:
        print(m[k][h])
        m[k].remove(m[k][h])
  return m


print(minor_matrix([[1,2,3],[4,5,6],[7,8,9]],2,0))
