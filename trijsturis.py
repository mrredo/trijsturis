import math
inp = input().split(" ")
a = int(inp[0])
b = int(inp[1])
c = int(inp[2])


def isTriangle(a, b, c):
    if a+b<=c or c+b<=a or a+c<=a: 
        print("Ievadītie lielumi neatbilst pareizam trijstūrim")
        exit()
    
def lenkaLielums(a, b, c):
    return math.acos((b**2 + c**2 - a**2) / (2 * b * c)) * 180 / math.pi

def lenkis(a, b, c): 
    if a**2 + b**2 == c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        return "taisnlenķa"
    if lenkaLielums(a, b, c) > 90 or lenkaLielums(c, a, b) > 90 or lenkaLielums(b, a, c) > 90:
        return "platlenķa"
    
    return "šaurlenķa"
    
def mala(a, b, c): 
    def sanu(a, b, c): 
        if a == b and not c == a and not c == b:
            return True
        return False
    if a == b and a == c and b == c:
        return "regulārs"
    if not a == b and not a == c and not b == c:
        return "dažādmalu"
    if sanu(a, b, c) or sanu(a, c, b) or sanu(b, a, c) or sanu(b, c, a) or sanu(c, a, b) or sanu(c, b, a): 
        return "vienādsānu"

m = mala(a, b, c)
l = lenkis(a, b, c)
print(f"{m} {l} trijstūris")
