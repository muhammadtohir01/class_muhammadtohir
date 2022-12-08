class Number:
    def __init__(self,num):
        self.num=num
    def get_number(self):
        return f'{self.num}'
    def is_even(self):
        if self.num%2==0:
            return True 
        else: False
    def is_odd(self):
        if self.num%2==0:
            return True
        else: False
    def is_prime(self):
        a=[]
        for i in range(2,self.num-1):
            if self.num%i==0:
                a.append(self.num)
                if 2<len(a):
                    return True
        else: False
    def get_divisors(self):
        a=[]
        for i in range(1,self.num+1):
            if self.num%i==0:
                a.append(i)
        return a
    def get_lenght(self):
        a=[]
        d=self.num
        s=str(d)
        for i in s:
            a.append(int(i))
            u=len(a)
        return u
    def get_sum(self):
        s=0
        for i in str(self.num):
            s+=int(i)
        return s     
    def get_product(self):
        return type(self.num)
    def get_reverse(self):
        self.num.reverse()
        return self.num
    def get_digits(self):
        s=" "
        d=0
        for i in self.num:
            s+=str(i)
        return int(s)
    def get_max(self):
        a=[]
        d=self.num
        s=str(d)
        for i in s:
            a.append(int(i))
        return max(a)
    def get_min(self):
          a=[]
          d=self.num
          s=str(d)
          for i in s:
            a.append(int(i))
          return min(a)
    def get_average(self):
        a=[]
        f=0
        x=0
        q=0
        d=self.num
        s=str(d)
        for i in s:
            f+=int(i)
            x=len(s)
            q=f/x
        return q
    def  get_median(self):
        s=self.num
        d=str(s)
        ans = ' '
        n = len(d)
        if n%2 != 0:
            ans += d[len(d)//2]
        else:
            ans+= d[(len(d)//2)-1:len(d)//2+1]
        return int(ans)
    def get_mode(self):
        d=self.num
        return abs(d)
    def get_range(self):
        d=self.num
        return range(d+1)
y=Number(4)
print(y.get_range())