def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    i=0
    k=0
    while i<len(list1):
        if list1[i]==list1[0]:
           k+=1
        i+=1
    if k==len(list1):
        return True
    else:
        return False
         
print(main([2,2,3,2]))

    
