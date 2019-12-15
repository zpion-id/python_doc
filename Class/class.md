## _CLASS_ PYTHON ##

### Mendefinisikan Class ###
```python
# Definisi kelas
class nama_class :
   attribut1
   attribut2
   attribut_dst
   
   def metode1(self):
   def metode2(self):
   def metode_dst(self):
   
# Membuat objek kelas (instansiasi)
objek1 = nama_class()
objek2 = nama_class() # Objek dapat dibuat lebih dari satu dari kelas yang sama
```

### Attribut ###
```python
class nama_class:
    attribut = ""
    
    def __init__(self):
        self.attribut2=""
        self.attribut3=""
        
    def metode(self):
       self.attribut4=""
       self.attribut5=""
       
# Instansiasi
objek = nama_class()
objek.attribut
objek.attribut2
objek.attribut3
objek.attribut4
objek.attribut5
```

### Class Turunan (inheritance) ###
```python
class kelas_turunan(kelas_induk):
    attribut
    def metode(self):
```

### Multi Inheritance ###
```python
class kelas_turunan(kelas_induk1, kelas_induk2):
    attribut
    def metode(self):
```

### Konstruktor ###
```python
class nama_class:
    def __init__(self):
        # konstruktor tidak boleh menggunakan return
        
# Membuat objek dari class
objek = nama_class()
```

### Konstruktor dengan argumen default ###
```python
class nama_class:
    def __init__(self,arg1=1, arg2="teks", arg_dst="teks2"):
        # konstruktor tidak boleh menggunakan return
        
# Membuat objek dari class
objek = nama_class() # tanpa argumen
objek2 = nama_class(4,"teks arg 2", "teks arg 3") # dengan argumen
```
### Enkapsulasi ###
```python
class nama_class:
   variabel_public = ""
   _varibel_protect = ""
   __variabel_private = ""
   
   def fungsi_public(self):
   def _fungsi_protect(self):
   def __fungsi_private(self):
   
```    
