import math

class Fraction:
    def __init__(self, num, den):
        #properties
        self.numerator = num         #soorate kasr
        self.denominator = den        #makhraje kasr

    #methods
    def sum(self, k2):
        num = self.numerator * k2.denominator + k2.numerator * self.denominator
        denom = self.denominator * k2.denominator
        
        x = Fraction(num, denom)
        return x
    
    def sub(self, k2):
        new_num = self.numerator * k2.denominator - k2.numerator * self.denominator
        new_denom = self.denominator * k2.denominator

        x = Fraction(new_num, new_denom)
        return x

    def mul(self, k1):
        result_num = k1.numerator * self.numerator
        result_denom = k1.denominator * self.denominator

        x = Fraction (result_num, result_denom)
        return x
    
    def div(self, k2):
        num = self.numerator * k2.denominator
        denom = self.denominator * k2.numerator

        x = Fraction(num, denom)
        return x

    def fraction_to_decimal(self):
        decimal = self.numerator / self.denominator

        return decimal
    
    def simplified(self):
        g = math.gcd(self.numerator, self.denominator)      
        sim_numerator = self.numerator / g
        sim_denominator = self.denominator / g

        x = Fraction(sim_numerator, sim_denominator)
        return x

    def show(self):
        print (self.numerator,"/", self.denominator)

a = Fraction (5, 6)
a.show()
b = Fraction (9, 3)
b.show()
c = Fraction (756, 336)


w = a.sum(b)
w.show()

z = b.mul(a)
z.show()

y = a.sub(b)
y.show()

v = a.div(b)
v.show()

d = a.fraction_to_decimal()
print (d)


s = c.simplified()
s.show()