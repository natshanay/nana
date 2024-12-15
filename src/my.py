class Stack:
    stack = []
    pointer = -1

    def push(self,element):
        self.stack.append(element)
        self.pointer+=1
    def pop(self):
        if (self.pointer==-1):
            print("stack under flow")
        else:
            value = self.stack[self.pointer]
            self.stack = self.stack[:-1]
            self.pointer -=1
            return value
        
    def peek(self):
        if (self.pointer==-1):
            print ("stack underflow")
        else:
            return self.stack[self.pointer]
# stack = Stack()
# stack.push(5)
# stack.push(55)
# stack.push(535)
# stack.push(53)
# stack.push(15)
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()

# print(stack.peek())

class Q:
    queue = []
    front=rear = -1
    
    def enque(self,element):
        if (self.front==-1 and self.rear==-1):
            self.queue.append(element)
            self.front=self.rear=0
        else:
            self.queue.append(element)
            self.rear+=1
    def deque(self):
        if (self.front ==-1 and self.rear==-1):
            print("stack under flow")
        elif (self.front==self.rear):
            self.front = self.rear =-1
        else:
            self.rear+=1
    def peek(self):
        if (self.front ==-1 and self.rear==-1):
            print("stack under flow")
        else:
            return self.queue[self.front]
# qu = Q()
# qu.enque(6)
# qu.deque()
# print(qu.peek())
class Que:
    front = rear = -1
    
    qu = []
    def enq(self,element):
        if (self.front==-1 and self.rear==-1):
            self.qu.append(element)
            self.front+=1
            self.rear+=1
        else:
            
            self.qu.append(element)
            self.rear+=1
      
            
    def deq(self):
        if (self.front==-1 and self.rear==-1):
            print("STACK UNDER FLOW")
        elif(self.front==self.rear):
            self.front=self.rear=-1
        else:
            self.rear+=1
       
    def peek(self):
        if (self.front==-1 and self.rear == -1):
            print("stack underflow")
        else:
            return self.qu[self.rear]
        
print("something is here")

# queueu = Que()

# queueu.enq(5)
# queueu.enq(75)
# queueu.deq()
# print(queueu.peek())    
# print(queueu.peek())    
class Queue:
    front = rear = -1
    
    queu = []
    
    def enque(self, element):
        if (self.front == -1 and self.rear == -1):
            self.queu.append(element)
            
            self.front+=1
            self.rear+=1
        else:
            self.queu.append(element)
            self.rear+=1
    def deque(self):
        if (self.front == -1 and self.rear ==-1):
            print("stack under flow ")
        elif(self.front == self.rear):
            self.front = self.rear=-1   
        else:
            self.front+=1
    def peek(self):
        if (self.front==-1 and self.rear==-1):
            print("under flow")
        else:
            return self.queu[self.rear]
            
# queue = Queue()
# queue.enque(5)
# queue.enque(45)
# queue.enque(55)
# queue.enque(59)
# queue.deque()
# print(queue.peek()) 


class Stack:
    
    pointer = -1
    stack = []
    res = []
    
    def push(self, element):
        self.stack.append(element)
        self.pointer+=1
    def pop(self):
        if (self.pointer==-1):
            print("Stack underflow")
        else:
            self.stack = self.stack[:-1]
            self.pointer -=1
           
            
    def peek(self):
        if (self.pointer==-1):
            print("empty stack")
        else:
            return self.stack[self.pointer]
    def display(self):
        for  i in range(len(self.stack)):
            self.res.append(self.stack[i])
        print(self.res)
            
            
            # how it should be ? 
            # 1. ask : man, how is it that 
            # now, yeah , work on it same hting by stress + and a lot more
            #  you know you can do it , but you fear to do it , no matter the reason is:
            # you want to work at, bakos and at same time you do not wana have the responsibility to go 
            # there and work , 
            # you are always thinking something that does not exist and have not ever been , 
            # why do not you go there , ask them and then work why are you trying to get same meker 
            # from someone out side , 
            # meaning what are trying to expect man , take a loook at your self man , when will be 
            # the last time you are goings to be ten free , work do change and get the right money tell 
            # is it not goings to be possible if you are not going the right way tell me man , 
            # first ... and added ... 
            
            
            
# nana = Stack()
# nana.push(7)
# nana.push(777)
# nana.push(77)
# nana.push(47)
# nana.pop()
# nana.display()
# print(nana.peek()) 



# and we also need to read books watch movie , then Addis Ababa , and also the so things and whole hasattr
# this means you need the extra things and so on things that is so awesome and we are goings to sum up now 


# 1 , {t[if :_+ go and eat somehting !] , toi + charge }
# 2 , {phone call }
# 3,  {submit them all,}
# 4, {identify somehthings and then also these things and so on things and the so on !}
# 5, {that something! and what is that somethings telll me about it and it is goings to be so amzing}
# 6. {we are done here, if you wana is and this is town man }
# 7. {let us do the rest things got that right and that is gouings to be so amazing1}

# what is next here!
# so lets's start it eh !

# there for we are goings to do them 1 by one 
# so i think we have to begin like from here and here we have so many to tell what is that things  
# lets just began doing them one by one and we have so a lot to do here than what we can say so more!
# nata
# that is i think the status
# sying you have never been right!

# we are goings to solve in the medium probelms : 
#     the problem : 









# string all as b 
# only one ss 
# with out 
# out put should be 1 

# a b c  a b c b b 

# 12 minute : 
# abc 1 st sub string 
# b , bca the 2nd substring tlen as 3 
# c , cab and len is 3 
# a abc again 3 then 
# b bc 2 
# c cb 2 
# move 
# b , last 1 
# all the possible , all have same len 
# incase , out should be 3 .as_integer_ratio

# use sliding window , 

# we have to find that , 
# abc 
# start and end index 

# max  = 0 

# 0  0 
# we put a condition here that means alreday there in the list  
# move
# check the condition and so things *args
# abcabcbb
# abc
# bca 

# we do not need to do these the size of the list 
# max of somehting like htat 
# iteration
# remain *argsht
# when we remove 3 i wil and that is the thing and that is the thing and that is repeating and then remove the start index 

# charachter and that is remaing the same 
# that is the hting and that means we jave already
# keep increamenting ad/n


# def lee(s):
#     start  = 0 
#     charset = set()
    
#     maxL = 0
  
#     for end in range(len(s)):
#         while s[end] in charset:
#             charset.remove(s[start])
#             start+=1
#         charset.add(s[end])
#         maxL = max(maxL, end-start+1)
#     return maxL
# s = "abcabcbb"
# print(lee(s))
    
            
# def rm(s):
#     start = 0
    
#     charset = set()
#     maxL = 0
#     for end in range(len(s)):
#         while s[end] in charset:
#             charset.remove(s[start])
#             start +=1
#         charset.add(s[end])
#         maxL = max(maxL,end-start+1)
#     return maxL
# n = "abcabcbb"
# print(rm(n))
    
# i wa to hun, ss
# oo am good , stop and go here 
# here voice ..... 
# cjksadkjcnfhlvshndkjncjkadsncjdsnhbfdhvjb
# i am gona think 
# if it is not , i ma not loc
# fear to start 

def charreplacement(s,k):
    charcount = {}
    maxL = 0
    maxF = 0
    left = 0
    
    for right in range(len(s)):
        char = s[right]
        
        charcount[char] = charcount.get(char,0)+1
        
        maxF = max(maxF,charcount[char])
    
        window_size = right- left+1
        
        # shrink
        if window_size - maxF > k:
            left_char = s[left]
            charcount[left_char] -=1
            
            left+=1
        maxL = max(maxL,right-left+1)
    return maxL
n = "ABAB"
# hel i m on th pla , i do lik , it its n but i cur on her wh s
# i m go , ta pea , go , comin get som adv , the cycl cont , not ha , feelng sth, gd m of the crime
# just the crm
# goal: [so:-> my goal , => a2sv + know that it is for biggi things //done// save and send to sura! ]

# next, things here is that , 
# growth and rank is something that is something so amazinzg everywhere you are goings you have got that right 

# they are weak !
# k = 2
# print(charreplacement(n,k))
# n = [5,5,5,5,5]
# for i in range(len(n)):
# what is my task now !
# is it reading python or doing some other thing else

print('i am good , i am feeling so alright')

# what are the media things here and how are they all doing their thing and i can say it is 
# working!

# media : 
# storage media and device andwhat are they : 
# magnetic disk":
# {read and write , uses a random acces method:}

# faster than magnetic tape: 
# 2: floppy {}
# 1: hard disk 

# intrusion detection system 

# what isint det sys? 
# it is the process of identefying and respomding to maliciouse activities targeted at resources!
# it uses , predefined information and also collected information and also predefined to reason about the       
# possibility of , of intrudets 
# will provide a service like : 
# giving an alarm 
# activating the programs to try to deal with deal with the intrusion etc . . .
# the function of ids : 
# detect the problem as soon as possinle and 
# take appropriate , resposnze 
# does not usually take, preventive detecting mechanism , when attack is detected!
# it is reactive rather than pro - active !
#  major componets of ids : 
# 1 , detecting devices 
# 2 , alarm / notification device 
# 3 , central processing system 
# the detection methods in ids

# 1,  signiture based : 
#   matching {known }
# matching signiture of well known attacks with the changes in the system or stream of packet with in a network!
# effective aagainst known treats , 


# 