from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import datetime
from agent_base import Agent  # Assuming agent_base.py contains the base Agent class
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

load_dotenv()
class GPTplannerAgent(Agent):
    def __init__(self, model_name="planner-GPT"):
        self.name = model_name
        self.llm = ChatOpenAI(model="gpt-4", temperature=0.3)
        self.memory = ConversationBufferMemory(return_messages=True)
        self.chain = ConversationChain(
            llm=self.llm,
            memory=self.memory,
            verbose=True
        )

    def create_task(self, user_input):
        prompt = f"You are a planning assistant. Based on the following request, suggest a task and assign a priority (high, medium, low):\n\n{user_input}"
        response = self.llm([HumanMessage(content=prompt)])
        return{
            "description": response.content,
            "priority": "medium",  # Default priority, can be adjusted based on response
            "created_by": self.name,
            "timestamp": datetime.utcnow().isoformat()
        }