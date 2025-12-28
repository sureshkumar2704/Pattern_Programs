# ⭐ Right Angled Pattern Program

## 📌 Description
This program prints a right-angled triangle star pattern based on the number entered by the user.

## 🧠 Logic Explained
- The outer loop runs `num` times (number of rows).
- The inner loop prints stars (`*`) equal to the current row number.
- `end=""` ensures stars print on the same line.
- `print()` moves to the next line after each row.

## 💻 Code
```python
num = int(input("Enter the number: "))

for i in range(num):
    for j in range(i + 1):
        print("*", end=" ")
    print()
```

## 📤 Output
![Output](/outputs/right_angled_triangle.png)
