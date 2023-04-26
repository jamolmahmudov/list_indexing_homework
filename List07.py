def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace zero with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
 
    # if list1[0]==0:
    #     list1[0]=False
    # if list1[1]==0:
    #     list1[1]=False
    # if list1[2]==0:
    #     list1[2]=False
    # if list1[3]==0:
    #     list1[3]=False
    # if list1[4]==0:
    #     list1[4]=False
    i=0
    while i<len (list1):
        if list1[i]==0:
            list1[i]=False
        
        i+=1
    return list1
print(main([1,1,0,0,1]))