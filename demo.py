"""
Demo script to show the homework assistant functionality
This demonstrates the structure and flow without requiring Azure OpenAI credentials
"""

def demo_homework_assistant():
    """Demonstrate the homework assistant structure"""
    
    print("=" * 80)
    print("🎓 TRỢ LÝ GIẢI BÀI TẬP - DEMO")
    print("=" * 80)
    print()
    
    # Example homework input
    homework = """
Bài tập: Viết chương trình Python tính tổng các số từ 1 đến n

Yêu cầu:
1. Nhận vào một số nguyên dương n
2. Tính tổng các số từ 1 đến n
3. In ra kết quả

Ví dụ:
- Input: n = 5
- Output: 15 (vì 1 + 2 + 3 + 4 + 5 = 15)
"""
    
    print("📖 NỘI DUNG BÀI TẬP:")
    print("-" * 80)
    print(homework)
    print("-" * 80)
    print()
    
    # Example solution structure (what the AI would return)
    solution = """
## 1. PHÂN TÍCH BÀI TẬP

Bài tập yêu cầu viết chương trình tính tổng các số nguyên liên tiếp từ 1 đến n.

**Đầu vào:** Số nguyên dương n
**Đầu ra:** Tổng S = 1 + 2 + 3 + ... + n
**Ràng buộc:** n phải là số nguyên dương (n > 0)

## 2. GIẢI PHÁP (SOLUTION)

Có 3 cách tiếp cận chính:

### Cách 1: Sử dụng vòng lặp
- Khởi tạo biến tổng = 0
- Lặp từ 1 đến n, cộng dồn từng số vào tổng
- Độ phức tạp: O(n)

### Cách 2: Sử dụng công thức toán học
- Công thức: S = n * (n + 1) / 2
- Độ phức tạp: O(1) - tối ưu nhất

### Cách 3: Sử dụng hàm built-in
- Python có hàm sum() và range()
- Độ phức tạp: O(n)

## 3. MÃ NGUỒN (SOURCE CODE)

```python
# Cách 1: Sử dụng vòng lặp
def sum_to_n_loop(n):
    \"\"\"
    Tính tổng từ 1 đến n sử dụng vòng lặp
    
    Args:
        n (int): Số nguyên dương
        
    Returns:
        int: Tổng các số từ 1 đến n
    \"\"\"
    if n < 1:
        return 0
    
    total = 0
    for i in range(1, n + 1):
        total += i
    
    return total


# Cách 2: Sử dụng công thức toán học (Tối ưu nhất)
def sum_to_n_formula(n):
    \"\"\"
    Tính tổng từ 1 đến n sử dụng công thức
    
    Công thức: S = n * (n + 1) / 2
    
    Args:
        n (int): Số nguyên dương
        
    Returns:
        int: Tổng các số từ 1 đến n
    \"\"\"
    if n < 1:
        return 0
    
    return n * (n + 1) // 2


# Cách 3: Sử dụng hàm built-in
def sum_to_n_builtin(n):
    \"\"\"
    Tính tổng từ 1 đến n sử dụng hàm sum()
    
    Args:
        n (int): Số nguyên dương
        
    Returns:
        int: Tổng các số từ 1 đến n
    \"\"\"
    if n < 1:
        return 0
    
    return sum(range(1, n + 1))


# Chương trình chính
def main():
    \"\"\"Hàm main để test các hàm\"\"\"
    try:
        n = int(input("Nhập số nguyên dương n: "))
        
        if n < 1:
            print("Vui lòng nhập số nguyên dương!")
            return
        
        # Tính tổng bằng cách 1
        result1 = sum_to_n_loop(n)
        print(f"Cách 1 (vòng lặp): Tổng từ 1 đến {n} = {result1}")
        
        # Tính tổng bằng cách 2
        result2 = sum_to_n_formula(n)
        print(f"Cách 2 (công thức): Tổng từ 1 đến {n} = {result2}")
        
        # Tính tổng bằng cách 3
        result3 = sum_to_n_builtin(n)
        print(f"Cách 3 (built-in): Tổng từ 1 đến {n} = {result3}")
        
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên!")


if __name__ == "__main__":
    main()
```

## 4. GIẢI THÍCH CHI TIẾT

### Cách 1: Vòng lặp
- **Ưu điểm:** Dễ hiểu, trực quan
- **Nhược điểm:** Chậm với n lớn (O(n))
- **Cách hoạt động:** Duyệt qua tất cả số từ 1 đến n và cộng dồn

### Cách 2: Công thức toán học ⭐ (Khuyên dùng)
- **Ưu điểm:** Nhanh nhất (O(1)), không phụ thuộc vào n
- **Công thức:** S = n × (n + 1) ÷ 2
- **Nguồn gốc:** Đây là công thức của dãy số học
- **Ví dụ:** n=5 → S = 5 × 6 ÷ 2 = 15

### Cách 3: Hàm built-in
- **Ưu điểm:** Code ngắn gọn, dễ đọc
- **Nhược điểm:** Vẫn phải duyệt qua n phần tử (O(n))
- **Sử dụng:** Kết hợp sum() và range()

### Test Cases

```python
# Test
assert sum_to_n_formula(5) == 15
assert sum_to_n_formula(10) == 55
assert sum_to_n_formula(100) == 5050
assert sum_to_n_formula(0) == 0
```

### Kết luận

Với bài toán này, **Cách 2 (công thức toán học)** là tối ưu nhất vì:
- Độ phức tạp O(1) - không phụ thuộc vào n
- Code ngắn gọn, dễ hiểu
- Không tốn bộ nhớ cho vòng lặp
"""
    
    print("📚 GIẢI ĐÁP BÀI TẬP:")
    print("=" * 80)
    print(solution)
    print("=" * 80)
    print()
    
    print("✅ Demo hoàn tất!")
    print()
    print("ℹ️  Lưu ý: Đây là ví dụ về cấu trúc output mà trợ lý sẽ cung cấp.")
    print("   Để sử dụng thực tế, cần cấu hình Azure OpenAI API trong file .env")
    print()


if __name__ == "__main__":
    demo_homework_assistant()
