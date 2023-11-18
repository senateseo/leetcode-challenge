class Solution:
    def intToRoman(self, num: int) -> str:
        
        ans=""
        # From 1 to 10, 100, 1000...
        digits_arr=[]

        while num > 0:
            digits_arr.insert(0, num % 10)
            num= num//10
            

   
        max_digits=len(digits_arr) # 4
        # 

        cur_str=""
        for i in range(len(digits_arr)):
           
            d = digits_arr[i]

            # 1000
            if max_digits-i == 4:
                cnt = d
                while cnt >0:
                    cur_str+="M"
                    cnt-=1
            # 100
            elif max_digits-i == 3:
                if d <=3:
                    cnt=d
                    while cnt >0:
                        cur_str+="C"
                        cnt-=1
                elif d == 4:
                    cur_str+="CD"
                elif d == 5:
                    cur_str+="D"
                elif d > 5 and d<=8:
                    base="D"
                    cnt=d-5
                    while cnt > 0:
                        base+="C"
                        cnt-=1
                    cur_str+=base
                elif d == 9:
                    cur_str+="CM"
            # 10
            elif max_digits-i ==2 :
                if d <=3:
                    cnt=d
                    while cnt > 0:
                        cur_str+="X"
                        cnt-=1
                elif d == 4:
                    cur_str+="XL"
                elif d == 5:
                    cur_str+="L"
                elif d > 5 and d<=8:
                    base="L"
                    cnt=d-5
                    while cnt > 0:
                        base+="X"
                        cnt-=1
                    cur_str+=base
                elif d == 9:
                    cur_str+="XC"
            # 1
            else:
                if d <=3:
                    cnt=d
                    while cnt >0:
                        cur_str+="I"
                        cnt-=1
                elif d == 4:
                    cur_str+="IV"
                elif d == 5:
                    cur_str+="V"
                elif d > 5 and d<=8:
                    base="V"
                    cnt=d-5
                    while cnt > 0:
                        base+="I"
                        cnt-=1
                    cur_str+=base
                elif d == 9:
                    cur_str+="IX"

        return cur_str

# TC: O(N) when N is number of digits
# SC: O(1)
        