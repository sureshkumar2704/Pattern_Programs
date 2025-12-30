# Centered Pyramid Star Pattern

## 📌 Description
This program prints a **centered pyramid-shaped star pattern** based on the number entered by the user.  
The pyramid grows row by row, with stars centered using leading spaces.

---

## 🧠 Logic Explained
- The outer loop runs from `1` to `num` (number of rows).
- The first inner loop prints spaces to center-align the pyramid.
- The second inner loop prints stars (`*`) in an odd-number pattern (`2*i - 1` stars).
- `end=" "` ensures characters are printed on the same line.
- `print()` moves to the next line after each row.

---

## 💻 Code
```python
num = int(input("Enter the number: "))

for i in range(1, num + 1):
    for j in range(num - i):
        print(" ", end=" ")
    for k in range(1, i * 2):
        print("*", end=" ")
    print()
---

## 📤 Output
![Output](/outputs/3_centered_pyramid.png)