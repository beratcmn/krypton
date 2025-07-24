# 🔧 Krypton – Product Requirements Document (PRD)

**Version:** v0.1
**Date:** 2025-07-24
**Author:** \[Konvotech]

---

## 1. 📌 Product Overview

**Krypton** is a beginner-friendly, Turkish-localized programming language that is a subset of Python. It retains Python’s syntax while replacing English keywords and built-in functions with Turkish equivalents. `.kr` source files are transpiled into Python code and executed within a bundled virtual environment. The main goal is to lower the barrier of entry to programming for Turkish-speaking newcomers.

---

## 2. 🎯 Target Audience

* First-time programmers with no English background
* High school and university students
* Individuals interested in coding literacy
* Anyone intimidated by English-heavy programming environments

---

## 3. 🧱 Features

### 3.1 Language Features

* Turkish keywords (`eğer`, `iken`, `tanım`, `yazdır`)
* Turkish built-ins (`uzunluk()`, `aralık()`, `liste()`)
* Python-compatible syntax (indentation-based, colon usage)
* `.kr` file extension
* Simplified, beginner-friendly error messages (in Turkish)

### 3.2 Transpilation

* `.kr` files are transpiled to `.py` (Python 3)
* `krypton build file.kr` generates a `.py` output
* `krypton run file.kr` compiles and runs directly

### 3.3 Standard Library

* Custom `kstd` (Krypton Standard Library)
* Turkish-named helper APIs (`oku_dosya`, `zaman.now()`, `yaz()`)
* Bundled within an isolated Python virtual environment
* Bridges to Python standard modules as needed

### 3.4 CLI Tool

* Command-line interface: `krypton`

  * Commands: `build`, `run`, `help`, `show-output`, `explain-error`
* Auto-compiles `.kr` files
* Optional output display of transpiled Python code
* Turkish error messages and usage tips

---

## 4. 🔧 Technical Architecture

| Component         | Description                                                            |
| ----------------- | ---------------------------------------------------------------------- |
| **Lexer/Parser**  | Custom syntax parser using `lark` or `ply`                             |
| **Transpiler**    | Token mapping + optional AST transformation                            |
| **Runtime**       | Embedded Python 3.10+ virtual environment                              |
| **CLI Interface** | Built with `Typer` or `Click`                                          |
| **Packaging**     | Delivered via PyInstaller or zipapp                                    |
| **Modules**       | `kstd` folder contains Turkish-friendly modules (e.g., `kstd/file.py`) |

---

## 5. ✅ MVP Scope (Minimum Viable Product)

* Core language constructs: `eğer`, `değilse`, `iken`, `her`, `tanım`
* Basic built-in functions: `yazdır()`, `uzunluk()`, `aralık()`
* `krypton build` and `krypton run` commands
* `kstd` library with at least 5 core modules
* Turkish-language error messages and a `help()` system

---

## 6. 📝 Examples

### 6.1 Basic Syntax: Variables, Comments, and I/O

This shows variable assignment, comments, and the most basic function, `yazdır()`.

**Krypton Kodu (`ornek1.kr`)**
```krypton
# Bu bir Krypton programıdır.
# Değişken tanımlayalım ve ekrana yazdıralım.
selam_mesajı = "Merhaba, Krypton!"
kullanıcı_adı = "Ahmet"

yazdır(selam_mesajı)
yazdır("Hoş geldin,", kullanıcı_adı)
```

**Transpiled Python Code (`ornek1.py`)**
```python
# Bu bir Krypton programıdır.
# Değişken tanımlayalım ve ekrana yazdıralım.
selam_mesajı = "Merhaba, Krypton!"
kullanıcı_adı = "Ahmet"

print(selam_mesajı)
print("Hoş geldin,", kullanıcı_adı)
```
**Açıklama (Explanation):**
*   Comments (`#`) are preserved.
*   Variable names are preserved exactly as the user wrote them.
*   `yazdır` is directly mapped to `print`.

---

### 6.2 Conditionals: `eğer`, `yoksaeğer`, `değilse`

This demonstrates conditional logic. `yoksaeğer` is our `elif`.

**Krypton Kodu (`ornek2.kr`)**
```krypton
puan = 85

eğer puan >= 90:
    yazdır("Notunuz: A")
yoksaeğer puan >= 80:
    yazdır("Notunuz: B")
değilse:
    yazdır("Notunuz: C veya altı")
```

**Transpiled Python Code (`ornek2.py`)**
```python
puan = 85

if puan >= 90:
    print("Notunuz: A")
elif puan >= 80:
    print("Notunuz: B")
else:
    print("Notunuz: C veya altı")
```
**Açıklama:**
*   `eğer` -> `if`
*   `yoksaeğer` -> `elif`
*   `değilse` -> `else`
*   Indentation and operators (`>=`) are identical to Python, ensuring structural similarity.

---

### 6.3 Functions: `tanımla` and `döndür`

Defining reusable blocks of code. We'll use `tanımla` (define) and `döndür` (return).

**Krypton Kodu (`ornek3.kr`)**
```krypton
tanımla kare_al(sayı):
    sonuç = sayı * sayı
    döndür sonuç

sayı_1 = 5
sayı_1_karesi = kare_al(sayı_1)
yazdır(f"{sayı_1} sayısının karesi: {sayı_1_karesi}")
```

**Transpiled Python Code (`ornek3.py`)**
```python
def kare_al(sayı):
    sonuç = sayı * sayı
    return sonuç

sayı_1 = 5
sayı_1_karesi = kare_al(sayı_1)
print(f"{sayı_1} sayısının karesi: {sayı_1_karesi}")
```
**Açıklama:**
*   `tanımla` -> `def`
*   `döndür` -> `return`

---

### 6.4 Loops: `her...için` and `tekrarla`

This is our improved, more readable loop syntax.

**Part A: Iterating over a list with `her...için`**

**Krypton Kodu (`ornek4a.kr`)**
```krypton
isimler = ["Ali", "Veli", "Ayşe"]

her isim için isimler:
    yazdır(f"Listedeki isim: {isim}")
```

**Transpiled Python Code (`ornek4a.py`)**
```python
isimler = ["Ali", "Veli", "Ayşe"]

for isim in isimler:
    print(f"Listedeki isim: {isim}")
```
**Açıklama:**
*   The structure `her <variable> için <collection>:` transpiles to `for <variable> in <collection>:`. This is much more readable in Turkish than a direct `for...in` translation.

**Part B: Simple repetition with `tekrarla...kez`**

**Krypton Kodu (`ornek4b.kr`)**
```krypton
# Sayaçlı tekrar
tekrarla i, 5 kez:
    yazdır(f"{i}. kez merhaba!")
```

**Transpiled Python Code (`ornek4b.py`)**
```python
# Sayaçlı tekrar
for i in range(5):
    print(f"{i}. kez merhaba!")
```
**Açıklama:**
*   `tekrarla <variable>, <number> kez:` transpiles to `for <variable> in range(<number>):`. This is extremely intuitive for beginners.

---

### 6.5 Using the Standard Library: `kstd`

This demonstrates how a user would import and use our custom, Turkish-named library.

**Krypton Kodu (`ornek5.kr`)**
```krypton
# kstd'den rastgele modülünü içe aktaralım
içeaktar kstd.rastgele

yazdır("1 ile 100 arasında rastgele bir sayı tutuluyor...")
rastgele_sayı = kstd.rastgele.tamsayı(1, 100)
yazdır("Tuttuğum sayı:", rastgele_sayı)
```

**Transpiled Python Code (`ornek5.py`)**
```python
# kstd'den rastgele modülünü içe aktaralım
# The transpiler smartly handles the import to work with the bundled library
from kstd import rastgele

print("1 ile 100 arasında rastgele bir sayı tutuluyor...")
rastgele_sayı = rastgele.tamsayı(1, 100) # This calls our wrapper function
print("Tuttuğum sayı:", rastgele_sayı)
```
**Açıklama:**
*   `içeaktar kstd.rastgele` is intelligently transpiled to `from kstd import rastgele` to make the module directly usable.
*   The user code `kstd.rastgele.tamsayı(1, 100)` is invalid Python, so the `içeaktar` has to be smart. **Correction:** A simpler way is `içeaktar kstd.rastgele` -> `import kstd.rastgele`. Then the user code `kstd.rastgele.tamsayı` would work. Even better: `kstd içinden rastgele içeaktar` -> `from kstd import rastgele`. Let's stick with the simplest for now: `içeaktar kstd.rastgele` -> `import kstd.rastgele`. We can refine this logic. *Let's go with the `from...import` for now as it's cleaner.*

---

### 6.6 Putting It All Together: A Number Guessing Game

This example combines everything: loops, conditionals, I/O, type casting, and standard library usage.

**Krypton Kodu (`oyun.kr`)**
```krypton
içeaktar kstd.rastgele

gizli_sayı = kstd.rastgele.tamsayı(1, 20)
yazdır("1 ile 20 arasında bir sayı tuttum. Bakalım bulabilecek misin?")

iken Doğru:
    kullanıcı_girişi = giriş("Tahminin nedir? ")
    tahmin = tamsayı(kullanıcı_girişi)

    eğer tahmin < gizli_sayı:
        yazdır("Çok alçak! Daha yüksek bir sayı dene.")
    yoksaeğer tahmin > gizli_sayı:
        yazdır("Çok yüksek! Daha alçak bir sayı dene.")
    değilse:
        yazdır(f"Tebrikler! Gizli sayı {gizli_sayı} idi.")
        kır # Döngüyü sonlandır
```

**Transpiled Python Code (`oyun.py`)**
```python
from kstd import rastgele

gizli_sayı = rastgele.tamsayı(1, 20)
print("1 ile 20 arasında bir sayı tuttum. Bakalım bulabilecek misin?")

while True:
    kullanıcı_girişi = input("Tahminin nedir? ")
    tahmin = int(kullanıcı_girişi)

    if tahmin < gizli_sayı:
        print("Çok alçak! Daha yüksek bir sayı dene.")
    elif tahmin > gizli_sayı:
        print("Çok yüksek! Daha alçak bir sayı dene.")
    else:
        print(f"Tebrikler! Gizli sayı {gizli_sayı} idi.")
        break # Döngüyü sonlandır
```
**Açıklama:**
*   This example uses `iken Doğru` for an infinite loop, which transpiles to `while True`.
*   It uses built-in functions `giriş` (`input`) and `tamsayı` (`int`).
*   It introduces a new keyword, `kır` (`break`), which is essential for loop control. We should add this to our PRD.
