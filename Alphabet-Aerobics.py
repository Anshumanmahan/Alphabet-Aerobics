s1 = raw_input()
s = list(s1)
n = int(raw_input())
w = []
for i in range(n):
      w1 = raw_input()
      w.append(w1)
      if n > 12:
        break;
        
for i in range(len(w)):
        temp = 0
        flag = list(w[i])
        for k in range(len(flag)):
                for j in range(len(s)):
                        if(flag[i] == s[j]):
                                temp += 1
                                break
          
        if temp != len(w[i]):
                print ('NO')
        else:
                print('YES')          	
