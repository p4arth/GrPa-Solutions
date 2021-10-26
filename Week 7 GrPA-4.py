# Week 7 GrPA-4

n = int(input())

main_dict = {}
for i in range(n):

  train_name = input()
  main_dict[train_name] = {}

  compartments = int(input())

  for i in range(compartments):
    comp_name = input().split(',')
    main_dict[train_name][comp_name[0]] = int(comp_name[1])


print(main_dict)
