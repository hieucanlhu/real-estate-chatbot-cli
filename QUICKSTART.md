# Quick Start Guide - Trợ lý Giải Bài Tập

## 🚀 Bắt đầu nhanh trong 3 bước

### Bước 1: Cài đặt
```bash
# Clone repository
git clone https://github.com/hieucanlhu/real-estate-chatbot-cli.git
cd real-estate-chatbot-cli

# Cài đặt dependencies
pip install -r requirements.txt

# Cấu hình Azure OpenAI
cp .env.template .env
nano .env  # Điền thông tin API của bạn
```

### Bước 2: Chọn cách sử dụng

#### Option A: Chế độ Tương tác (Dễ dàng nhất) 🎯
```bash
python homework_assistant.py
```

**Khi nào dùng:**
- Bài tập nhiều dòng, phức tạp
- Muốn giải nhiều bài liên tiếp
- Thích giao diện tương tác

#### Option B: Command Line (Nhanh nhất) ⚡
```bash
# Bài tập ngắn
python solve_homework.py "Viết hàm tính giai thừa"

# Từ file
python solve_homework.py -f examples/example1_sum.txt

# Lưu kết quả
python solve_homework.py -f homework.txt -o solution.md
```

**Khi nào dùng:**
- Bài tập ngắn gọn
- Có sẵn file bài tập
- Muốn lưu kết quả
- Automation/scripting

### Bước 3: Nhận kết quả

Kết quả luôn có 4 phần:

```
┌─────────────────────────────────────┐
│  1. PHÂN TÍCH BÀI TẬP               │
│     - Hiểu yêu cầu                  │
│     - Input/Output                   │
├─────────────────────────────────────┤
│  2. GIẢI PHÁP (SOLUTION)            │
│     - Ý tưởng                        │
│     - Các cách tiếp cận              │
├─────────────────────────────────────┤
│  3. MÃ NGUỒN (SOURCE CODE)          │
│     - Code hoàn chỉnh                │
│     - Comments chi tiết              │
├─────────────────────────────────────┤
│  4. GIẢI THÍCH CHI TIẾT             │
│     - Cách hoạt động                 │
│     - Độ phức tạp                    │
└─────────────────────────────────────┘
```

## 📝 Ví dụ Thực tế

### Ví dụ 1: Bài tập đơn giản
```bash
python solve_homework.py "Viết hàm Python kiểm tra số chẵn"
```

### Ví dụ 2: Bài tập từ file
```bash
# Tạo file homework.txt
cat > homework.txt << 'EOF'
Viết hàm binary_search(arr, target):
- Input: mảng đã sắp xếp arr, giá trị cần tìm target
- Output: index của target, hoặc -1 nếu không tìm thấy
- Sử dụng thuật toán Binary Search
- Implement cả recursive và iterative
EOF

# Giải bài tập
python solve_homework.py -f homework.txt -o solution.md
```

### Ví dụ 3: Chế độ tương tác
```bash
python homework_assistant.py

# Sau đó nhập:
Bài tập: Viết class Stack implement LIFO

Yêu cầu:
- push(item): thêm phần tử
- pop(): lấy và xóa phần tử cuối
- peek(): xem phần tử cuối
- is_empty(): kiểm tra stack rỗng

Implement bằng Python với list và linked list
END
```

## 🎓 Các file mẫu có sẵn

```bash
# Bài tập cơ bản - Tính tổng
python solve_homework.py -f examples/example1_sum.txt

# Bài tập trung bình - Số nguyên tố
python solve_homework.py -f examples/example2_prime.txt

# Bài tập nâng cao - Quick Sort
python solve_homework.py -f examples/example3_quicksort.txt
```

## 💡 Tips để có kết quả tốt nhất

### ✅ Mô tả rõ ràng
```
TỐT:
"Viết hàm Python tính Fibonacci số thứ n.
Input: số nguyên n >= 0
Output: số Fibonacci thứ n
Yêu cầu: Implement cả recursive và dynamic programming
Test: fib(5) = 5, fib(10) = 55"

KÉM:
"Code fibonacci"
```

### ✅ Cung cấp test cases
```
"Viết hàm is_palindrome(s)
Test cases:
- is_palindrome("radar") → True
- is_palindrome("hello") → False
- is_palindrome("A man a plan a canal Panama") → True (ignore case)"
```

### ✅ Chỉ định ngôn ngữ
```
"Implement QuickSort bằng Python với type hints"
"Viết class BinaryTree trong Java với generic types"
```

## 🔧 Khắc phục sự cố

### Lỗi thường gặp

**1. ModuleNotFoundError: No module named 'openai'**
```bash
pip install -r requirements.txt
```

**2. Azure OpenAI credentials not found**
```bash
# Kiểm tra file .env có tồn tại
ls -la .env

# Nếu chưa có, tạo từ template
cp .env.template .env

# Chỉnh sửa với thông tin của bạn
nano .env
```

**3. API Error hoặc timeout**
- Kiểm tra kết nối internet
- Verify Azure API key còn hoạt động
- Kiểm tra quota/credits của Azure account

## 📊 So sánh 2 CLI modes

| Tính năng | Interactive Mode | Command-line Mode |
|-----------|------------------|-------------------|
| **Nhập nhiều dòng** | ✅ Dễ dàng | ⚠️ Cần file |
| **Nhiều bài liên tiếp** | ✅ Rất tốt | ❌ Phải chạy lại |
| **Lưu file** | ❌ Không | ✅ Có (-o flag) |
| **Automation** | ❌ Không | ✅ Có |
| **User-friendly** | ✅ Rất tốt | ⚠️ Trung bình |
| **Tốc độ** | ⚠️ Trung bình | ✅ Nhanh |

## 🎯 Chọn mode phù hợp

```
┌─────────────────────────────────────┐
│  Bạn muốn gì?                       │
├─────────────────────────────────────┤
│  ☐ Giải 1 bài nhanh                 │
│    → solve_homework.py "..."        │
│                                      │
│  ☐ Bài tập nhiều dòng               │
│    → homework_assistant.py          │
│                                      │
│  ☐ Có file bài tập                  │
│    → solve_homework.py -f file.txt  │
│                                      │
│  ☐ Lưu kết quả vào file             │
│    → solve_homework.py -o out.md    │
│                                      │
│  ☐ Giải nhiều bài liên tiếp         │
│    → homework_assistant.py          │
└─────────────────────────────────────┘
```

## 🌟 Demo

Chạy demo để xem ví dụ output (không cần API):
```bash
python demo.py
```

## 📚 Tài liệu chi tiết

- **README.md**: Tổng quan và cài đặt
- **USAGE_GUIDE.md**: Hướng dẫn chi tiết
- **FEATURE_SUMMARY.md**: Tài liệu kỹ thuật

## 🆘 Cần trợ giúp?

1. Đọc USAGE_GUIDE.md
2. Xem các file example trong `examples/`
3. Chạy `python solve_homework.py --help`
4. Tạo Issue trên GitHub

---

**Chúc bạn học tốt! 🎓**
