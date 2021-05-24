L=["Network","Math","Programming","Physics","Music"]
longest_item="Network"
for i in L:
    if len(i)>len(longest_item):
        longest_item=i
print("the longest item is: ",longest_item)