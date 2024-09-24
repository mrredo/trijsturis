inp = input().split(" ")
a = int(inp[0])
b = int(inp[1])
c = int(inp[2])
def lenkis(a, b, c): 
    if a**2 + b**2 == c**2:
        return "taisnlenķa trijstūris"
    
    return ""
def mala(a, b, c): 
    c = int(inp[2])
    def sanu(a, b, c): 
        if a == b and not c == a and not c == b:
            return True
        return False
    if a == b and a == c and b == c:
        return "regulārs šaurlenķa"
    if not a == b and a == c and b == c:
        return "dažādmalu"
    if sanu(a, b, c) or sanu(a, c, b) or sanu(b, a, c) or sanu(b, c, a) or sanu(c, a, b) or sanu(c, b, a): 
        return "vienādsānu"

m = mala(a, b, c)
l = lenkis(a, b, c)
print(f"{m}{l} trijstūris")
