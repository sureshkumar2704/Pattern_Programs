# Inverted Right Angled Traingle

## 📌 Description
This Python program prints an inverted right-angled triangle star pattern based on the number entered by the user.

The pattern starts with the maximum number of stars and decreases line by line.

---

## 🧠 Logic Explanation
- The user enters a number (`num`) that represents the number of rows.
- The outer loop runs **from `num-1` down to `0`**, decreasing each time.
- The inner loop prints stars (`*`) based on the current value of `i`.
- `end=' '` ensures stars appear on the same line with spaces.

---

## 💻 Python Code
```python
num = int(input('Enter the number: '))

for i in range(num - 1, -1, -1):
    for j in range(i + 1):
        print('*', end=' ')
    print()
```

---

## 📤 Output
![Output](/outputs/inverted_right_angled_triangle.png)
