from agent.core import LyretaAgent
from agent.commands import CommandHandler
from config import CONFIG

if __name__ == "__main__":
    # Initialize the AI Agent
    agent = SizerraAgent(name=CONFIG["agent_name"])
    command_handler = CommandHandler(agent)

    # Start the Agent
    print(f"Starting {agent.name}...")
    while True:
        user_input = input("You> ")
        if user_input.lower() in ["exit", "quit"]:
            print("Shutting down Aeura. Goodbye!")
            break
        response = command_handler.handle_command(user_input)
        print(f"Lyreta> {response}")
