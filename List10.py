def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:list_num
        int: return answer
    """
#     if list_num[0]>list_num[-1]:
#         return list_num[0]
#     else:
#         return list_num[-1]
# print(main([2,5,6,7,8,2]))
    i=0
    k=0
    a=len(list_num)
    while i<a:
        if list_num[i]>k:
            k=list_num[i]
        i+=1
    return k
print(main([1,4,8,3]))