def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace one with True.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    # """
    i=0
    
    while i<len(list1):
        if list1[i]==1:
            list1[i]=True
        else :
            list1[i]=False
        i+=1
    # if list1[0]==1:
    #     list1[0]=True
    # if list1[1]==1:
    #     list1[1]=True
    # if list1[2]==1:
    #     list1[2]=True
    # if list1[3]==1:
    #     list1[3]=True
    # if list1[4]==1:
    #     list1[4]=True
    

    return list1
print(main([1,0,1,0,0]))