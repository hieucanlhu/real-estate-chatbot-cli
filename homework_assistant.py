#!/usr/bin/env python3
"""
Homework Assistant CLI - Giải bài tập và cung cấp giải thích chi tiết
"""
import sys
import logging
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from src.azure_client import AzureOpenAIClient

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

console = Console()


def display_welcome():
    """Hiển thị thông điệp chào mừng"""
    welcome_text = """
    # 🎓 TRỢ LÝ GIẢI BÀI TẬP
    
    Chào mừng bạn đến với Trợ lý Giải Bài Tập!
    
    **Tôi có thể giúp bạn:**
    - Phân tích và hiểu nội dung bài tập
    - Đưa ra giải pháp (solution) chi tiết
    - Cung cấp mã nguồn (source code) nếu cần
    - Giải thích chi tiết cách giải
    
    **Hướng dẫn sử dụng:**
    1. Nhập nội dung bài tập của bạn
    2. Gõ 'END' trên một dòng riêng khi hoàn tất
    3. Nhận giải pháp và giải thích chi tiết
    
    Gõ 'quit' hoặc 'exit' để thoát.
    """
    console.print(Panel(Markdown(welcome_text), border_style="green"))


def get_multiline_input():
    """Nhận input nhiều dòng từ người dùng"""
    console.print("\n[bold cyan]Nhập nội dung bài tập (gõ 'END' trên dòng riêng để kết thúc):[/bold cyan]")
    lines = []
    
    while True:
        try:
            line = input()
            if line.strip().upper() == 'END':
                break
            if line.strip().lower() in ['quit', 'exit']:
                return None
            lines.append(line)
        except EOFError:
            break
        except KeyboardInterrupt:
            console.print("\n[yellow]Đã hủy nhập liệu.[/yellow]")
            return None
    
    return '\n'.join(lines)


def main():
    """Hàm chính của chương trình"""
    try:
        # Initialize Azure OpenAI client
        client = AzureOpenAIClient()
        
        # Display welcome message
        display_welcome()
        
        while True:
            # Get homework content from user
            homework_content = get_multiline_input()
            
            if homework_content is None:
                console.print("\n[yellow]Tạm biệt! Chúc bạn học tốt! 👋[/yellow]")
                break
            
            if not homework_content.strip():
                console.print("[red]Vui lòng nhập nội dung bài tập![/red]")
                continue
            
            # Show processing message
            with console.status("[bold green]Đang phân tích và giải bài tập..."):
                solution = client.solve_homework(homework_content)
            
            # Display solution
            console.print("\n" + "="*80 + "\n")
            console.print(Panel(
                Markdown(solution),
                title="[bold green]📚 GIẢI ĐÁP BÀI TẬP[/bold green]",
                border_style="green"
            ))
            console.print("\n" + "="*80 + "\n")
            
            # Ask if user wants to continue
            console.print("[bold cyan]Bạn có muốn giải bài tập khác không? (nhập 'y' để tiếp tục, 'n' để thoát)[/bold cyan]")
            choice = input().strip().lower()
            
            if choice in ['n', 'no', 'không', 'khong']:
                console.print("\n[yellow]Tạm biệt! Chúc bạn học tốt! 👋[/yellow]")
                break
    
    except KeyboardInterrupt:
        console.print("\n[yellow]Tạm biệt! Chúc bạn học tốt! 👋[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"[red]Lỗi: {e}[/red]")
        logging.error(f"Lỗi trong chương trình: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
