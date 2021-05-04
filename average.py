def Average(lst):
    try:
        if not lst:
            return -1
        return sum(lst) / len(lst)
    except Exception:
        return None
  
# average = Average(lst = [1,2,3,4,5,6,7,8])
#print("Average of the list =", round(average, 2))