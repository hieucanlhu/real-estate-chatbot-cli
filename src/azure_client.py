from openai import AzureOpenAI
from config.settings import settings
import logging

class AzureOpenAIClient:
    def __init__(self):
        self.client = AzureOpenAI(
            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
            api_key=settings.AZURE_OPENAI_API_KEY,
            api_version=settings.AZURE_OPENAI_API_VERSION
        )
        self.deployment_name = settings.AZURE_DEPLOYMENT_NAME
    
    def chat_completion(self, messages, temperature=None):
        """
        Gửi yêu cầu chat completion tới Azure OpenAI
        """
        try:
            response = self.client.chat.completions.create(
                model=self.deployment_name,
                messages=messages,
                max_tokens=settings.MAX_TOKENS,
                temperature=temperature or settings.TEMPERATURE
            )
            return response.choices[0].message.content
        except Exception as e:
            logging.error(f"Lỗi khi gọi Azure OpenAI: {e}")
            return "Xin lỗi, tôi gặp sự cố kỹ thuật. Vui lòng thử lại sau."
    
    def summarize_conversation(self, conversation_text):
        """
        Tóm tắt cuộc hội thoại
        """
        summarize_prompt = f"""
        Hãy tóm tắt cuộc hội thoại về bất động sản sau đây thành 2-3 câu ngắn gọn, 
        tập trung vào các điểm chính mà người dùng quan tâm:
        
        {conversation_text}
        
        Tóm tắt:
        """
        
        try:
            messages = [{"role": "user", "content": summarize_prompt}]
            return self.chat_completion(messages, temperature=0.3)
        except Exception as e:
            logging.error(f"Lỗi khi tóm tắt hội thoại: {e}")
            return "Không thể tóm tắt hội thoại này."