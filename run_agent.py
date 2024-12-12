# run_agent.py
from agent.base_agent import BaseAgent
from agent.task_manager import TaskManager
from agent.plugins.nlp_plugin import NLPPlugin
from agent.plugins.blockchain_plugin import BlockchainPlugin
from agent.plugins.data_plugin import DataPlugin
from agent.utils.logger import log_info
from agent.utils.helper import get_random_agent_name

# Initialize the task manager and plugins
agent_name = get_random_agent_name()
agent = BaseAgent(name=agent_name)
task_manager = TaskManager()

# Initialize plugins
nlp_plugin = NLPPlugin(agent)
blockchain_plugin = BlockchainPlugin(agent)
data_plugin = DataPlugin(agent)

# Assign tasks
task_manager.assign_random_task()

# Perform tasks
task_manager.process_tasks()

# Use plugins
nlp_plugin.execute("This is an AI-powered agent.")
blockchain_plugin.execute("TX123456789")
data_plugin.execute()
