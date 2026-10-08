

def count_occurences(a,b):
  hash_map={}
  for i in b:
      count=0
      for j in a:
          if i == j:
              count+=1
      hash_map[i] = count
  return hash_map

    
    
########### 2nd way ##############
def count_occurences1(a,b):
  hash_map1={}
  result={}
  for i in a:
      hash_map1[i] = hash_map1.get(i,0)+1
  for j in b:
    # if j in hash_map1:
    #     result[j]=hash_map1[j]
    # else:
    #     result[j] = 0
    result[j] = hash_map1.get(j,0)
    
  return result

def count_chars(string,arr):
  hashmap={}
  result={}
  for i in string:
    hashmap[i] = hashmap.get(i,0)+1
  for j in arr:
    # print(j)
    result[j] = hashmap.get(j,0)
    
  return result

a = [1,2,3,4,5,6,7,3,4,23,4,34,3,2,3,7]
b = [1,2,5,4,11,3,8]
d="abcdefzab"
e=["a","b","c","z"]

print(count_occurences(a,b))
print(count_occurences1(a,b))
print(count_chars(d,e))