def find_last(haystack,needle):
    len_needle = len(needle)
    ind = haystack.find(needle) # Initial index
    end_ind = -1
    while 1:
        if ind == -1:
            break
        else:
            end_ind=ind
            ind=haystack.find(needle,ind + len_needle)
    if end_ind != -1:
        return end_ind  # Return final index
    else:
        return -1
print find_last("aaaa","a")