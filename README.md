# Real Estate Chatbot CLI

Một hệ thống chatbot CLI thông minh hỗ trợ tư vấn bất động sản và giải bài tập sử dụng Azure OpenAI.

## Tính năng

### 1. Tư vấn Bất động sản
- Tư vấn về mua bán, cho thuê bất động sản
- Phân tích thị trường bất động sản
- Đưa ra lời khuyên về đầu tư bất động sản
- Giải thích các thủ tục pháp lý liên quan
- Hỗ trợ định giá bất động sản

### 2. Trợ lý Giải Bài tập
- Phân tích và hiểu rõ nội dung bài tập
- Đưa ra giải pháp (solution) chi tiết và đầy đủ
- Cung cấp mã nguồn (source code) nếu bài tập yêu cầu lập trình
- Giải thích nội dung bài tập một cách rõ ràng
- Giải thích giải pháp và mã nguồn đã đưa ra

## Cài đặt

### Yêu cầu
- Python 3.8+
- Azure OpenAI API key và endpoint

### Các bước cài đặt

1. Clone repository:
```bash
git clone https://github.com/hieucanlhu/real-estate-chatbot-cli.git
cd real-estate-chatbot-cli
```

2. Cài đặt dependencies:
```bash
pip install -r requirements.txt
```

3. Cấu hình Azure OpenAI:
```bash
cp .env.template .env
```

Sau đó chỉnh sửa file `.env` với thông tin Azure OpenAI của bạn:
```
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_API_KEY=your-api-key-here
AZURE_OPENAI_API_VERSION=2024-02-15-preview
AZURE_DEPLOYMENT_NAME=gpt-4
```

## Sử dụng

### Trợ lý Giải Bài tập

#### Chế độ tương tác (Interactive Mode)

Chạy chương trình ở chế độ tương tác để nhập bài tập nhiều dòng:

```bash
python homework_assistant.py
```

Sau đó:
1. Nhập nội dung bài tập của bạn
2. Gõ `END` trên một dòng riêng khi hoàn tất
3. Nhận giải pháp và giải thích chi tiết

Ví dụ:
```
Nhập nội dung bài tập (gõ 'END' trên dòng riêng để kết thúc):
Viết chương trình Python tính tổng các số từ 1 đến n.
Input: n (số nguyên dương)
Output: Tổng các số từ 1 đến n
END
```

#### Chế độ command line

Giải bài tập trực tiếp từ command line:

```bash
python solve_homework.py "Viết chương trình tính tổng từ 1 đến n"
```

Giải bài tập từ file:

```bash
python solve_homework.py -f homework.txt
```

Lưu kết quả vào file:

```bash
python solve_homework.py -f homework.txt -o solution.md
```

### Ví dụ sử dụng

#### Ví dụ 1: Bài tập lập trình Python

```bash
python solve_homework.py "Viết hàm Python kiểm tra số nguyên tố. Input: một số nguyên n. Output: True nếu n là số nguyên tố, False nếu không phải."
```

#### Ví dụ 2: Bài tập từ file

Tạo file `homework.txt`:
```
Bài tập: Thuật toán sắp xếp

Yêu cầu:
1. Giải thích thuật toán Quick Sort
2. Viết code Python implement Quick Sort
3. Phân tích độ phức tạp thời gian và không gian
4. So sánh với Merge Sort
```

Chạy:
```bash
python solve_homework.py -f homework.txt -o quicksort_solution.md
```

#### Ví dụ 3: Chế độ tương tác

```bash
python homework_assistant.py
```

## Cấu trúc dự án

```
real-estate-chatbot-cli/
├── config/
│   └── settings.py          # Cấu hình ứng dụng và system prompts
├── src/
│   ├── __init__.py
│   ├── azure_client.py      # Client tương tác với Azure OpenAI
│   └── conversation_manager.py  # Quản lý hội thoại
├── homework_assistant.py     # CLI tương tác giải bài tập
├── solve_homework.py        # CLI đơn giản giải bài tập
├── requirements.txt         # Python dependencies
├── .env.template           # Template cho file cấu hình
└── README.md               # Tài liệu hướng dẫn
```

## Định dạng kết quả

Khi giải bài tập, hệ thống sẽ trả về kết quả theo cấu trúc:

```markdown
## 1. PHÂN TÍCH BÀI TẬP
[Giải thích nội dung bài tập, yêu cầu cần đạt được]

## 2. GIẢI PHÁP (SOLUTION)
[Trình bày ý tưởng giải quyết, các bước thực hiện]

## 3. MÃ NGUỒN (SOURCE CODE)
[Cung cấp code hoàn chỉnh nếu có, với comments giải thích]

## 4. GIẢI THÍCH CHI TIẾT
[Giải thích cách hoạt động của giải pháp và code]
```

## Lưu ý

- Đảm bảo có kết nối internet để truy cập Azure OpenAI API
- API key cần có quyền sử dụng GPT-4 hoặc model tương đương
- Tùy theo độ phức tạp của bài tập, thời gian xử lý có thể từ vài giây đến vài chục giây

## License

MIT License

## Đóng góp

Mọi đóng góp đều được chào đón! Vui lòng tạo Pull Request hoặc Issue để cải thiện dự án.