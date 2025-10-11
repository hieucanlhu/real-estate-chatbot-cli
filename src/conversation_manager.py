import json
from typing import List, Dict, Any

class ConversationManager:
    def __init__(self, storage_file: str):
        self.storage_file = storage_file
        self.conversations = self.load_conversations()

    def create_conversation(self) -> str:
        conversation_id = str(len(self.conversations) + 1)
        self.conversations[conversation_id] = {'messages': []}
        self.save_conversations()
        return conversation_id

    def add_message(self, conversation_id: str, message: str) -> None:
        if conversation_id in self.conversations:
            self.conversations[conversation_id]['messages'].append(message)
            self.save_conversations()
        else:
            raise ValueError(f"Conversation ID {conversation_id} does not exist.")

    def save_conversations(self) -> None:
        with open(self.storage_file, 'w') as file:
            json.dump(self.conversations, file)

    def load_conversations(self) -> Dict[str, Any]:
        try:
            with open(self.storage_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def list_conversations(self) -> List[str]:
        return list(self.conversations.keys())

# Example usage:
# cm = ConversationManager('conversations.json')
# conv_id = cm.create_conversation()
# cm.add_message(conv_id, 'Hello, how can I help you?')
# print(cm.list_conversations())