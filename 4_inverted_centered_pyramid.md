# Inverted Centered Pyramid Star Pattern

## 📌 Description
This program prints an **inverted centered pyramid-shaped star pattern** based on the number entered by the user.  
The pattern starts with the maximum number of stars at the top and gradually decreases while remaining center-aligned.

---

## 🧠 Logic Explained
- The outer loop runs from `num` down to `1`, controlling the number of rows.
- The first inner loop prints leading spaces to keep the pyramid centered.
- The second inner loop prints stars (`*`) in an odd-number sequence (`2*i - 1` stars).
- `end=" "` ensures all characters print on the same line.
- `print()` moves the cursor to the next line after completing each row.

---

## 💻 Code
```python
num = int(input("Enter the number: "))

for i in range(num, 0, -1):
    for j in range(num - i):
        print(" ", end=" ")
    for k in range(1, i * 2):
        print("*", end=" ")
    print()

---

## 📤 Output
![Output](/outputs/4_inverted_centered_pyramid.png)