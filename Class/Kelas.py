class c :
    att1 = "attribut1 public" # atribut statis publik
    _att2 = "attribut2 protect?" # atribut statis
    __att3 = "attribut3 private" # atribut statis private
    #self.att4 = "attribut4 public self" # NameError: name 'self' is not defined
    #self._att5 = "attribut5 protect self" # NameError: name 'self' is not defined
    #self.__att6 = "attribut6 private self" # NameError: name 'self' is not defined

    def __init__(self):
        self.att7 = "attribut7 didalam __init__"
        self._att8 = "attribut8 didalam __init__"
        self.__att9 = "attribut9 didalam __init__"

    def metode(self):
        self.att10 = "attribut10 didalam metode setelah memanggil metode"
        self._att11 = "attribut11 didalam metode setelah memanggil metode"
        self.__att12 = "attribut12 didalam metode setelah memanggil metode"
        var_lokal = "variabel lokal"
        self.att13 = var_lokal
        
    def print_private(self):
        return self.__att3 + " " + self.__att12

    @staticmethod
    def print_statis():
        return "print_statis"

    def print_statis2():
        return "print_statis2"

    print_statis2 =staticmethod(print_statis2)

print(c.att1 + " tanpa instansiasi")
print(c._att2  + " tanpa instansiasi")

print(c.print_statis()+ " tanpa instansiasi")
print(c.print_statis2()+ " tanpa instansiasi")


c =c() # Instansiasi
print(c.att1)
print(c._att2)
# print(c.__att3) # AttributeError: 'c' object has no attribute '__att3'

print(c.att7)
print(c._att8)
# print(c.__att9) # AttributeError: 'c' object has no attribute '__att9'

# Gagal karena metode belum dipanggil
# print(c.att10) # AttributeError: 'c' object has no attribute '__att10'
# print(c._att11) # AttributeError: 'c' object has no attribute '__att11'
# print(c.__att12) # AttributeError: 'c' object has no attribute '__att12'

c.metode()
print(c.att10)
print(c._att11)
# print(c.__att12) # AttributeError: 'c' object has no attribute '__att12'
print(c.att13)

print(c.print_private())

