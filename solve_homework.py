#!/usr/bin/env python3
"""
Homework Solver - Simple CLI to solve homework from command line or file
Usage:
    python solve_homework.py "Nội dung bài tập"
    python solve_homework.py -f homework.txt
"""
import sys
import argparse
import logging
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from src.azure_client import AzureOpenAIClient

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

console = Console()


def solve_homework_from_text(homework_content):
    """
    Giải bài tập từ nội dung text
    """
    try:
        client = AzureOpenAIClient()
        
        console.print("\n[bold cyan]📖 Nội dung bài tập:[/bold cyan]")
        console.print(Panel(homework_content, border_style="blue"))
        
        with console.status("[bold green]Đang phân tích và giải bài tập..."):
            solution = client.solve_homework(homework_content)
        
        console.print("\n" + "="*80 + "\n")
        console.print(Panel(
            Markdown(solution),
            title="[bold green]📚 GIẢI ĐÁP BÀI TẬP[/bold green]",
            border_style="green"
        ))
        console.print("\n" + "="*80 + "\n")
        
        return solution
        
    except Exception as e:
        console.print(f"[red]Lỗi: {e}[/red]")
        logging.error(f"Lỗi khi giải bài tập: {e}")
        sys.exit(1)


def main():
    """Hàm chính"""
    parser = argparse.ArgumentParser(
        description='Homework Solver - Giải bài tập và cung cấp giải thích chi tiết',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ví dụ sử dụng:
  python solve_homework.py "Viết chương trình tính tổng từ 1 đến n"
  python solve_homework.py -f homework.txt
  python solve_homework.py -f homework.txt -o solution.md
        """
    )
    
    parser.add_argument(
        'homework',
        nargs='?',
        help='Nội dung bài tập cần giải'
    )
    
    parser.add_argument(
        '-f', '--file',
        help='Đọc nội dung bài tập từ file'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='Lưu kết quả vào file (markdown format)'
    )
    
    args = parser.parse_args()
    
    # Determine homework content source
    homework_content = None
    
    if args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                homework_content = f.read()
        except FileNotFoundError:
            console.print(f"[red]Lỗi: Không tìm thấy file '{args.file}'[/red]")
            sys.exit(1)
        except Exception as e:
            console.print(f"[red]Lỗi khi đọc file: {e}[/red]")
            sys.exit(1)
    elif args.homework:
        homework_content = args.homework
    else:
        console.print("[yellow]Vui lòng cung cấp nội dung bài tập hoặc file chứa bài tập.[/yellow]")
        parser.print_help()
        sys.exit(1)
    
    if not homework_content.strip():
        console.print("[red]Nội dung bài tập không được để trống![/red]")
        sys.exit(1)
    
    # Solve homework
    solution = solve_homework_from_text(homework_content)
    
    # Save to file if requested
    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(f"# Bài tập\n\n{homework_content}\n\n")
                f.write(f"# Giải đáp\n\n{solution}\n")
            console.print(f"\n[green]✓ Đã lưu giải đáp vào file: {args.output}[/green]")
        except Exception as e:
            console.print(f"[red]Lỗi khi lưu file: {e}[/red]")
            logging.error(f"Lỗi khi lưu file: {e}")


if __name__ == "__main__":
    main()
