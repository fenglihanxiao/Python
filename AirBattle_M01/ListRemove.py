# lst1 = [1, 2, 3, 3, 4]
#
# for i in lst1:
#     if i == 3:
#         lst1.remove(i)
# ##################################################
# # Shift operation -> [1, 2, 3, 4]
# # Second 3 is left shift to remove 3's index
# print(lst1)

lst1 = [1, 2, 3, 3, 4]
remove_lst = []

for i in lst1:
    if i == 3:
        remove_lst.append(i)

##################################################
for j in remove_lst:
    lst1.remove(j)

print(lst1)


###################################################################
# 1. C++ remove an element
# for(vector<int>::iterator iter=veci.begin(); iter!=veci.end(); )
# {
#      if( *iter == 3)
#           iter = veci.erase(iter);
#       else
#             iter ++ ;
# }
