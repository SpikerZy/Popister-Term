class CommandHandler:
    """Handles user commands for the AI Agent."""
    
    def __init__(self, agent):
        self.agent = agent
    
    def handle_command(self, command):
        """
        Process a command and return the appropriate response.
        """
        if command.startswith("/help"):
            return self.show_help()
        elif command.startswith("/memory"):
            return self.show_memory()
        else:
            return self.agent.respond(command)
    
    def show_help(self):
        """Show available commands."""
        return "Available commands:\n/help - Show this help message\n/memory - Show conversation memory"
    
    def show_memory(self):
        """Display the agent's memory."""
        return "\n".join([f"You: {m[0]} | Agent: {m[1]}" for m in self.agent.memory])
