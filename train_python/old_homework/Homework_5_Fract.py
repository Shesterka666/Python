class Fraction:
    #a = "Я фрактино"
    def __init__(self, *args):
        if len(args) == 1:
            try:
                self.num = int(args[0].split('/')[0])
                self.denum = int(args[0].split('/')[1])
                self.unar_minus()
            except: 
                self.num = int(args[0])
                self.denum = int("1")
                self.unar_minus()       
        else: 
            self.num = int(args[0])
            self.denum = int(args[1])
            self.reduction_of_drob()
            self.unar_minus()

    def nod(self):
        n = int((min(abs(self.num),abs(self.denum))))
        g = []
        i = 2
        fack = []
        while i <= n:
            if n % i ==0:
                g.append(i)
                n /= i
            else:
                i+=1
        return g

    def reduction_of_drob(self):
        glist_nod = self.nod()
        #print(glist_nod)
        for i in range(len(glist_nod)):
            if self.num % glist_nod[i] == 0:
                if self.denum % glist_nod[i] == 0:
                    self.num = int (self.num / glist_nod[i]) 
                    self.denum = int (self.denum / glist_nod[i]) 
            
    #@staticmethod
    #@classmethod
    def unar_minus(self):
        #print(self.a)
        if self.denum == 1:
            if self.num < 0:
                self.minus = True
            else: 
                self.minus = False
        else:
            if self.num < 0 and self.denum < 0:
                self.minus = False
                self.num *= -1
                self.denum *= -1
            else: 
                if self.denum < 0:
                    self.num = -abs(self.num)
                    self.denum = abs(self.denum)
                    self.minus = True
                elif self.num < 0: 
                    self.minus = True
                else:  self.minus = False

    def numerator(self, number = None):
        if not number:
            return self.num
        else:
            self.num = number
        
    def denominator(self, number = None):
        if not number:
            return self.denum
        else: self.denum = number

    def __str__(self):
        return f"{self.num}/{self.denum}"
    
    def __repr__(self) -> str:
        return f"Fraction({self.num},{self.denum})"
    
    def sum(self,other):# для чего я хотел юзать self.plus но придумал как без него
        print(self.minus)#оствил как есть, чтобы логика была видна
        print(other.minus)     
        if self.minus == False and other.minus == False:  #оба +
            buuf_num = self.num*other.denum + other.num*self.denum 
            buuf_denum = self.denum*other.denum
            return Fraction(buuf_num,buuf_denum)
        
        elif self.minus == False and other.minus == True:#первый отриц второй отриц    
            
            buuf_num = self.num*other.denum - other.num*self.denum 
            buuf_denum = self.denum*other.denum
            return Fraction(buuf_num,buuf_denum)
        
        elif self.minus == True and other.minus == False:#первый полож второй отриц
            buuf_num = -1*(self.num*other.denum) + other.num*self.denum 
            buuf_denum = self.denum*other.denum
            return Fraction(buuf_num,buuf_denum)
        
        else: # оба отриц
            buuf_num = -1*(self.num*other.denum) - other.num*self.denum 
            buuf_denum = self.denum*other.denum
            return Fraction(buuf_num,buuf_denum)

    def __add__(self, other):
        print(other)
        print("sdgdfggs")
        if isinstance(other,int):
            other = Fraction(other)      
        buuf_num = self.num*other.denum + other.num*self.denum 
        buuf_denum = self.denum*other.denum
        return Fraction(buuf_num,buuf_denum)

    def __iadd__(self,other):
        if isinstance(other,int):
            other = Fraction(other)      
        buuf_num = self.num*other.denum + other.num*self.denum 
        buuf_denum = self.denum*other.denum
        return Fraction(buuf_num,buuf_denum)

    def __sub__(self,other):
        if isinstance(other,int):
            other = Fraction(other)
        buuf_num = self.num*other.denum - other.num*self.denum 
        buuf_denum = self.denum*other.denum
        return Fraction(buuf_num,buuf_denum)

    def __isub__(self,other):
        if isinstance(other,int):
            other = Fraction(other)
        buuf_num = self.num*other.denum - other.num*self.denum 
        buuf_denum = self.denum*other.denum
        return Fraction(buuf_num,buuf_denum)
    
    def __mul__(self, other):
        if isinstance(other,int):
            other = Fraction(other)
        buuf_num = self.num*other.num
        buuf_denum = self.denum*other.denum
        return Fraction(buuf_num,buuf_denum)

    def __imul__(self, other):
        if isinstance(other,int):
            other = Fraction(other)
        buuf_num = self.num*other.num
        buuf_denum = self.denum*other.denum
        return Fraction(buuf_num,buuf_denum)

    def __truediv__(self, other):
        if isinstance(other,int):
            other = Fraction(other)
        buuf_num = self.num*other.denum
        buuf_denum = self.denum*other.num
        return Fraction(buuf_num,buuf_denum)

    def __Itruediv__(self, other):
        if isinstance(other,int):
            other = Fraction(other)
        buuf_num = self.num*other.denum
        buuf_denum = self.denum*other.num
        return Fraction(buuf_num,buuf_denum)

    def reverse(self):
        buuf_num = self.denum
        buuf_denum = self.num
        return Fraction(buuf_num,buuf_denum)

    def __lt__(self, other):# — <;
        if isinstance(other,int):
            other = Fraction(other)
        buuf_num_self = self.num*other.denum
        buuf_num_other = self.denum*other.num
        return buuf_num_self < buuf_num_other

    def __le__(self, other):# — <=;
        if isinstance(other,int):
            other = Fraction(other)
        buuf_num_self = self.num*other.denum
        buuf_num_other = self.denum*other.num
        return buuf_num_self <= buuf_num_other
    
    def __eq__(self, other):# — ==;
        if isinstance(other,int):
            other = Fraction(other)
        buuf_num_self = self.num*other.denum
        buuf_num_other = self.denum*other.num
        return buuf_num_self == buuf_num_other
    
    def __ne__(self, other):# — !=;
        if isinstance(other,int):
            other = Fraction(other)
        buuf_num_self = self.num*other.denum
        buuf_num_other = self.denum*other.num
        return buuf_num_self != buuf_num_other
    
    def __gt__(self, other): #— >;
        if isinstance(other,int):
            other = Fraction(other)
        buuf_num_self = self.num*other.denum
        buuf_num_other = self.denum*other.num
        return buuf_num_self > buuf_num_other
    
    def  __ge__(self, other):# — >=
        if isinstance(other,int):
            other = Fraction(other)
        buuf_num_self = self.num*other.denum
        buuf_num_other = self.denum*other.num
        return buuf_num_self >= buuf_num_other
