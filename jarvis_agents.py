import os
import subprocess
import urllib.parse
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from tavily import TavilyClient

# Load environment credentials securely
load_dotenv(dotenv_path="private.env")

# Initialize API clients
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
groq_api_key = os.getenv("GROQ_API_KEY")

@tool
def execute_mac_command(command: str) -> str:
    """Executes an automated search command on the local Mac system by opening Safari."""
    try:
        search_query = command.strip()
        encoded_query = urllib.parse.quote(search_query)
        target_url = f"https://google.com{encoded_query}"
        command_to_run = f"open -a Safari '{target_url}'"
        
        subprocess.run(command_to_run, shell=True, capture_output=True, text=True)
        return f"Successfully executed macro search command for: '{search_query}'"
    except Exception as e:
        return f"Hardware Fault: {str(e)}"

@tool
def generate_design_file(filename: str, file_contents: str) -> str:
    """Automatically creates or writes a structural design code file."""
    try:
        safe_filename = os.path.basename(filename)
        with open(safe_filename, "w", encoding="utf-8") as f:
            f.write(file_contents)
        return f"Successfully generated design file: '{safe_filename}'"
    except Exception as e:
        return f"File Generation Exception: {str(e)}"

@tool
def deep_web_research(query: str) -> str:
    """Searches the live web using advanced scraping agents for real-time data."""
    try:
        response = tavily_client.search(query=query, search_depth="advanced")
        results = [f"Data Point: {r['content']} (Source: {r['url']})" for r in response.get('results', [])]
        return "\n".join(results) if results else "No semantic real-time matches found."
    except Exception as e:
        return f"Web Search Error: {str(e)}"

# --- MAIN AUTOMATED REASONING PIPELINE CALLED BY UI ---
def run_autonomous_agent(user_prompt: str) -> str:
    """Main execution engine processing the prompt through Llama3 models."""
    if not groq_api_key:
        return "CORE FAULT: GROQ_API_KEY CONTEXT UNRESOLVED."
        
    try:
                # FIX HERE: Changed to the active supported model ID
        llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama-3.1-8b-instant")

        
        # Bind all custom tools to your model
        tools = [execute_mac_command, generate_design_file, deep_web_research]
        llm_with_tools = llm.bind_tools(tools)
        
        # Define Jarvis System Rules & Persona
        messages = [
            SystemMessage(content=(
                "You are J.A.R.V.I.S., an ultra-sophisticated AI assistant with a natural South Indian accent. "
                "Naturally pepper your dialogue with words like 'sir chepandi', 'chudandi', and 'Boss'. "
                "Always call the 'deep_web_research' or 'execute_mac_command' tools whenever the user asks for "
                "real-time data, stocks, market updates, or current news events."
            )),
            HumanMessage(content=user_prompt)
        ]
        
        # Invoke agent reasoning graph loop
        response = llm_with_tools.invoke(messages)
        
        # Handle autonomous tool executions if requested by the LLM
        if response.tool_calls:
            for tool_call in response.tool_calls:
                if tool_call["name"] == "execute_mac_command":
                    return execute_mac_command.invoke(tool_call["args"])
                elif tool_call["name"] == "deep_web_research":
                    search_data = deep_web_research.invoke(tool_call["args"])
                    return search_data
                    
        return response.content
    except Exception as e:
        return f"Intelligence Engine Fault: {str(e)}"
