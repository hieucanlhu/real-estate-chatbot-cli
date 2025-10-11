import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Azure OpenAI Configuration
    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
    AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")
    AZURE_DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME", "gpt-4")
    
    # Application Settings
    CONVERSATIONS_DIR = "data/conversations"
    MAX_TOKENS = 4000
    TEMPERATURE = 0.7
    
    # Real Estate System Prompt
    SYSTEM_PROMPT = """
    Bạn là một chuyên gia tư vấn bất động sản thông minh và am hiểu. Nhiệm vụ của bạn là:
    
    1. Tư vấn về mua bán, cho thuê bất động sản
    2. Phân tích thị trường bất động sản
    3. Đưa ra lời khuyên về đầu tư bất động sản
    4. Giải thích các thủ tục pháp lý liên quan
    5. Hỗ trợ định giá bất động sản
    
    Hãy trả lời một cách chuyên nghiệp, thân thiện và cung cấp thông tin hữu ích.
    Nếu không chắc chắn về thông tin nào đó, hãy thành thật nói rằng bạn cần thêm thông tin.
    """

settings = Settings()