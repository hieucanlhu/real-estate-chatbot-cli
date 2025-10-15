# Hướng dẫn Sử dụng Trợ lý Giải Bài Tập

## Tổng quan

Trợ lý Giải Bài Tập là một tính năng mới của Real Estate Chatbot CLI, giúp bạn:
- Phân tích và hiểu rõ nội dung bài tập
- Đưa ra giải pháp (solution) chi tiết
- Cung cấp mã nguồn (source code) nếu cần
- Giải thích chi tiết cách giải

## Cách sử dụng

### 1. Chế độ Tương tác (Interactive Mode)

Phù hợp khi bạn muốn nhập bài tập nhiều dòng hoặc làm việc với nhiều bài tập liên tiếp:

```bash
python homework_assistant.py
```

**Quy trình:**
1. Nhập nội dung bài tập (có thể nhiều dòng)
2. Gõ `END` trên một dòng riêng khi hoàn tất
3. Chờ hệ thống phân tích và trả lời
4. Chọn tiếp tục hoặc thoát

**Ví dụ:**
```
Nhập nội dung bài tập (gõ 'END' trên dòng riêng để kết thúc):
Viết chương trình Python tính giai thừa của một số n.
Yêu cầu:
- Input: số nguyên dương n
- Output: n! (n giai thừa)
- Sử dụng cả đệ quy và vòng lặp
END
```

### 2. Chế độ Command Line

Phù hợp khi bạn có bài tập ngắn gọn hoặc muốn tự động hóa:

#### 2.1. Nhập trực tiếp từ command line

```bash
python solve_homework.py "Viết hàm kiểm tra số chẵn lẻ trong Python"
```

#### 2.2. Đọc từ file

```bash
python solve_homework.py -f examples/example1_sum.txt
```

#### 2.3. Lưu kết quả vào file

```bash
python solve_homework.py -f examples/example1_sum.txt -o solution.md
```

## Ví dụ Thực tế

### Ví dụ 1: Bài tập đơn giản

**Câu hỏi:**
```bash
python solve_homework.py "Viết hàm Python tính tổng các số chẵn từ 1 đến n"
```

**Kết quả sẽ bao gồm:**
- Phân tích bài toán
- Giải pháp với nhiều cách tiếp cận
- Source code Python có comments
- Giải thích chi tiết từng bước

### Ví dụ 2: Bài tập từ file

**File: homework.txt**
```
Bài tập: Thuật toán Binary Search

Yêu cầu:
1. Giải thích thuật toán Binary Search
2. Implement bằng Python (cả recursive và iterative)
3. Phân tích độ phức tạp
4. Cho ví dụ với mảng [1, 3, 5, 7, 9, 11, 13, 15]
```

**Chạy:**
```bash
python solve_homework.py -f homework.txt -o binary_search_solution.md
```

### Ví dụ 3: Bài tập phức tạp

```bash
python solve_homework.py -f examples/example3_quicksort.txt
```

## Định dạng Kết quả

Kết quả luôn được trình bày theo cấu trúc:

```markdown
## 1. PHÂN TÍCH BÀI TẬP
[Giải thích nội dung, yêu cầu]

## 2. GIẢI PHÁP (SOLUTION)
[Ý tưởng, các bước thực hiện]

## 3. MÃ NGUỒN (SOURCE CODE)
[Code hoàn chỉnh với comments]

## 4. GIẢI THÍCH CHI TIẾT
[Giải thích cách hoạt động]
```

## Tips & Tricks

### 1. Mô tả bài tập rõ ràng
```
❌ Kém: "Viết code tính tổng"
✅ Tốt: "Viết hàm Python tính tổng các số nguyên từ 1 đến n, với n là input từ người dùng"
```

### 2. Cung cấp ví dụ test case
```
Viết hàm is_palindrome(s) kiểm tra chuỗi palindrome.

Test cases:
- is_palindrome("radar") → True
- is_palindrome("hello") → False
- is_palindrome("A man a plan a canal Panama") → True (ignore case và space)
```

### 3. Yêu cầu cụ thể
```
Viết thuật toán Quick Sort:
1. Giải thích nguyên lý
2. Code Python với comments
3. Phân tích độ phức tạp O(n)
4. So sánh với Merge Sort
5. Cho ví dụ minh họa
```

## Các File Mẫu

Thư mục `examples/` chứa các file bài tập mẫu:

1. **example1_sum.txt** - Bài tập cơ bản về tính tổng
2. **example2_prime.txt** - Kiểm tra số nguyên tố
3. **example3_quicksort.txt** - Thuật toán Quick Sort

Bạn có thể sử dụng làm tham khảo:
```bash
python solve_homework.py -f examples/example1_sum.txt
python solve_homework.py -f examples/example2_prime.txt
python solve_homework.py -f examples/example3_quicksort.txt
```

## Lưu ý Quan trọng

1. **Cần Azure OpenAI API:**
   - Đảm bảo đã cấu hình file `.env` với thông tin API
   - Kiểm tra kết nối internet

2. **Thời gian xử lý:**
   - Bài tập đơn giản: 5-15 giây
   - Bài tập phức tạp: 20-40 giây

3. **Chi phí:**
   - Mỗi lần giải bài tập sẽ tiêu tốn token của Azure OpenAI
   - Bài tập phức tạp sẽ tốn nhiều token hơn

4. **Chất lượng đầu vào:**
   - Mô tả bài tập càng rõ ràng, kết quả càng chính xác
   - Cung cấp context và ví dụ để có giải pháp tốt nhất

## Khắc phục Sự cố

### Lỗi: "No module named 'openai'"
```bash
pip install -r requirements.txt
```

### Lỗi: "AZURE_OPENAI_ENDPOINT not found"
```bash
# Tạo file .env từ template
cp .env.template .env

# Chỉnh sửa .env với thông tin của bạn
nano .env
```

### Kết quả không như mong đợi
- Kiểm tra lại nội dung bài tập
- Thêm chi tiết và ví dụ
- Chỉ định rõ yêu cầu về ngôn ngữ lập trình, format output

## Liên hệ & Hỗ trợ

Nếu gặp vấn đề, vui lòng:
1. Kiểm tra lại cấu hình Azure OpenAI
2. Xem log để tìm lỗi chi tiết
3. Tạo Issue trên GitHub repository
