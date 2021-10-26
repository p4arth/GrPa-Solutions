def merge(D1, D2, priority):
    '''
        Arguments: 
            - D1: first dictionary
            - D2: second dictionary
            - priority: string
        Returns: D; merged dictionary
    '''
    keys_1 = list(D1.keys())
    keys_2 = list(D2.keys())

    if priority == 'first':
      mer_dic = {}
      for key in D1:
        mer_dic[key] = D1[key]
      
      for key in D2:
        if key not in mer_dic:
          mer_dic[key] = D2[key]

    if priority == 'second':
      mer_dic = {}
      for key in D2:
        mer_dic[key] = D2[key]
      
      for key in D1:
        if key not in mer_dic:
          mer_dic[key] = D1[key]

    return mer_dic

        


print(merge({1: 2, 2: 3, 3: 4},{1: 10, 4: 15, 5:10},'first'))