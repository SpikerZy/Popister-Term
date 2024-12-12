# nlp_plugin.py
class NLPPlugin:
    def __init__(self, agent):
        self.agent = agent

    def process_text(self, text):
        """Process text using NLP techniques."""
        # For simplicity, just count the words in the text
        word_count = len(text.split())
        print(f"NLP Plugin processed the text: {word_count} words.")
        return word_count
    
    def execute(self, text):
        """Execute NLP task."""
        print(f"Executing NLP task for {self.agent.name}")
        return self.process_text(text)
