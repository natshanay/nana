# def bbb(arr):
#     left = 0
#     right = 1
#     maxp = 0
    
#     while right < len(arr):
#         if arr[left] < arr[right]:
#             profit  = arr[right]-arr[left]
#             maxp = max(maxp, profit)
#         else:
#             left+=1
#         right+=1
        
#     return maxp
# n =[1,2,3,4,5]
# print(bbb(n))
            
    
# def lls(s):
#     left = 0
#     maxl = 0
#     charset = set()
#     for r in range(len(s)):
#         while s[r] in charset:
#             charset.remove(s[left])
#             left += 1
#         charset.add(s[r])
#         maxl = max(maxl, r-left+1)
#     return maxl
            
# b = "abcabcbb"
# print(lls(b))


# def fu(s,k):
#     count = 0
#     ss = set()
#     left = 0
#     maxl = 0
    
#     for i in range(len(s)): 
#         if s[i] == 0:
#             count+=1
#         while count > k:
#             if s[left] == 0:
#                 ss.remove(s[left])
#                 count-=1
#             left+=1
            
#         ss.add(s[i])
#         maxl = max(maxl,i-left+1)
#     return maxl
# a  = [1,1,1,1,1,0,0,0,1,0,0,1]
# k = 2
# print(fu(a,k))
# from collections import Counter

# def minWindow(s: str, t: str) -> str:
#     if not t or not s:
#         return ""
    
#     # Step 1: Frequency map for t
#     target = Counter(t)
#     window_counts = {}
    
#     # Step 2: Initialize two pointers
#     left, right = 0, 0
#     required = len(target)  # Number of unique characters in t
#     formed = 0  # Tracks how many characters meet the requirement in the window
    
#     min_len = float("inf")
#     min_window = (None, None)
    
#     while right < len(s):
#         # Add character from the right pointer into the window
#         char = s[right]
#         window_counts[char] = window_counts.get(char, 0) + 1
        
#         # If this character's frequency matches the target's frequency, update 'formed'
#         if char in target and window_counts[char] == target[char]:
#             formed += 1
        
#         # Try to shrink the window from the left while it's valid
#         while left <= right and formed == required:
#             char = s[left]
            
#             # Update the result if this window is smaller
#             if right - left + 1 < min_len:
#                 min_len = right - left + 1
#                 min_window = (left, right)
            
#             # Remove character from the left and shrink the window
#             window_counts[char] -= 1
#             if char in target and window_counts[char] < target[char]:
#                 formed -= 1
            
#             left += 1  # Shrink from the left
        
#         # Expand the window by moving the right pointer
#         right += 1
    
#     # Step 3: Return the smallest window
#     return "" if min_len == float("inf") else s[min_window[0]:min_window[1] + 1]
# s = "ADOBECODEBANC"
# t = "ABC"
# print(minWindow(s,t))
# def solution(s,t):
    
#     c = Counter(t)
#     overall = len(c)
    
#     r = 0
#     l = 0
    
#     res = ""
    
    
#     while r < len(s):
#         if s[r] in c:
#             c[s[r]] -= 1           
#             if c[s[r]] == 0:
#                 overall-=1             
#         while overall == 0: 
#             if not res:
#                 res = s[l:r+1]
#             elif r-l+1 < len(res):
#                 res = s[l:r+1]        
#             if s[l] in c:
#                 c[s[l]] +=1
#                 if c[s[l]]>0:
#                     overall+=1                
#             l+=1
#         r+=1
#     return res
# def minimum(s,t):
#     from collections import Counter
#     c = Counter(t)
#     l = 0
#     r = 0
#     res= ""
#     overall = len(t)
#     while r < len(s):
#         if s[r] in c:
#             c[s[r]] -= 1
#             if c[s[r]] == 0:
#                 overall-=1
#                 # valid 
#         while overall ==0:
#             if not res:
#                 res = s[l:r+1]
#             elif r - 1+1 < len(res):
#                 res = s[l:r+1]    
#             if s[l] in c:
#                 c[s[l]] +=1
#                 if c[s[l]] > 0:
#                     overall+=1
#             l+=1
#         r+=1
#     return res
# a = "ABDCHDBHDBANC"
# t = "ABC"
# print(minimum(a,t)) 
# def nana(s,k):
#     res = 0
#     left = 0
#     count = {}    
#     for r in range(len(s)):
#         if s[r] in count:
#             count[s[r]] +=1
#         else:
#             count[s[r]] = 1
#         while len(count) > k:
#             count[s[left]] -=1
#             if count[s[left]] == 0:
#                 del count[s[left]]
#             left+=1
#         res = max(res,r-left+1)
#     return res
# a  = "abebebbe"
# k = 2
# print(nana(a,k))
# def mmm(s,k):
#     left = 0
#     count = {}
#     res = 0
#     for r in range(len(s)):
#         if s[r] in count:
#             count[s[r]]+=1
#         else:
#             count[s[r]] = 1
#         while len(count) > k:
#             count[s[left]]-=1
#             if count[s[left]] == 0:
#                 del count[s[left]]
#             left+=1
#         res = max(res,r-left+1)
#     return res
# a = "abcccccch"
# k = 3
# print(mmm(a,k))
# def desta(a,k):
#     left = 0
#     count = {}
#     res = 0
#     for r in range(len(a)):
#         if a[r] in count:
#             count[a[r]]+=1
#         else:
#             count[a[r]]=1
#         while len(count) > k:
#             count[a[left]]-=1
#             if count[a[left]]==0:
#                 del count[a[left]]
#             left+=1
#         res = max(res,r-left+1)
#     return res
# a = "abcabbcjhdnbcjdncj"
# k = 5
# print(desta(a,k))   
# print("alemelesem")
# def newapi(s,k):
#     left = 0
#     counter = {}
#     res = 0
#     for r in range(len(s)):
#         if s[r] in counter:
#             counter[s[r]] += 1
#         else:
#             counter[s[r]] = 1
#         while len(counter) > k:
#             counter[s[r]]-=1
#             if counter[s[r]] ==0:
#                 del counter[s[r]]   
#             left+=1
#         res = max(res,r-left+1)
#     return res

# a = "ancjhdncjdncjd"
# k =2
# print(newapi(a,k))
# def minimum(s,t):
#     from collections import Counter
#     l , r = 0 ,0 
#     c = Counter(t)
#     overall = len(t)
#     while r < len(s):
#         if s[r] in c:
#             c[s[r]]-=1
#             if c[s[r]]==0:
#                 overall-=1
#         while overall == 0:
#            if not res:
#                res = s[l,r+1]
#            elif r-l+1 < len(res):
#                res = s[l,r+1]
#            if s[l] in c:
#                 c[s[l]] +=1
#                 if c[s[l]] > 0:
#                     overall+=1
#            l+=1
#         r+=1
#     return res
# s = "abbacbabcabba"
# k = "abc"
# print(minimum(s,k))
# def minw(s,t):
#     from collections import Counter
#     l, r = 0, 0 
#     res = 0
#     c = Counter(t)
#     overall = len(t)
#     while r < len(s):
#         if s[r] in c:
#             c[s[r]]-=1
#             if c[s[r]] == 0:
#                 overall-=1
#         while overall == 0:
#             if not res:
#                 res = s[l:r+1]
#             elif r-l+1 > len(res):
#                 res = s[l:r+1]
#             if s[l] in c:
#                 c[s[l]]+=1
#                 if c[s[l]]>0:
#                     overall +=1
#             l+=1
#         r+=1
# a  = "iodasjcidmcjdsnjc"
# t = "djm"
# print(minw(a,t))
# def minimum(s,t):
#     from collections import Counter
#     c = Counter(t)
#     res = 0
#     overall = len(t)
#     l , r = 0,0
#     while r < len(s):
#         if s[r] in c:
#             c[s[r]]-=1
#             if c[s[r]] == 0:
#                 overall-=1
#         while(overall == 0):
#             if not res:
#                 res = s[l:r+1]
#             elif r-l+1 < len(res):
#                 res = s[l:r+1]
#             if s[l] in c:
#                 c[s[l]] +=1
#                 if c[s[l]]>0:
#                     overall+=1
#             l+=1        
#         r+=1
#     return res

# a = "njncgdjkncjd"
# y = "kjng"
# print(minimum(a,y))
# print("nana")
# print("love evangadi!!! like wise!!")
# hte fear of yalqebgnal! gona end from me , i think the issue we have got was that we are not be able to do the things that are not app;icable for we peopple!
# we have got make money , and at same time we wana , enjoy moment of the time specially when we are so intersted about it , and 
# we want it so bad ! and much of as are being mod every tim and we have that tend ! like we growing 
# we are good at the things we do most o the time 
# we much of us looks like where we have grown ! so i think and thing is possible if we really think , where we are originally created or else it can also if it is goings that way it is kind o more intersting so 
# if you really want it to get it , if you have to just want it so badly!

# def nana(nums,k):
#     l_far,l_near = 0,0
#     res = 0
#     from collections import Counter
#     r = 0 
    
    
#     c = Counter(nums)
    
#     while r < len(nums):
        
#         while len(c) > k:
#             c[nums[l_near]]-=1
#             if c[nums[l_near]]==0:
#                 c.pop(nums[l_near])
                
#             l_near+=1
#             l_far=l_near
#         while c[nums[l_near]] > 1:
#             c[nums[l_near]]-=1
#             l_near+=1
            
#         if len(c) == k:
#             res += l_near-l_far+1
#         r+=1
    
#     return res
# a = [1,2,1,2,3]
# k = 2
# print(nana(a,k))

# print("something awesome is happening right now!")
# n = [5,4,3]
# for i in n:
#     print(i*"*")








# for i in range(17):
#     print("nana" * i)
# for i in range(17,-1,-1):
#     print("nana" * i)

print("i am good i am feeling so alright!!")







