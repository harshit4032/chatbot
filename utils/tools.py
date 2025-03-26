from langchain_core.tools import tool

from langchain_community.tools import TavilySearchResults
from dotenv import load_dotenv
import os
import streamlit as st
load_dotenv()

# os.environ["TAVILY_API_KEY"] =  os.getenv('TAVILY_API_KEY')
# tavily_api_key = st.secrets["TAVILY_API_KEY"]

@tool
def add(a: int, b: int):
    """Add two numbers. Please let the user know that you're adding the numbers BEFORE you call the tool"""
    return a + b


# tavily_tool = TavilySearchResults(
#     max_results=5,
#     include_answer=True,
#     description=(
#         "This is a search tool for accessing the internet.\n\n"
#         "Let the user know you're asking your friend Tavily for help before you call the tool."
#     ),
# )

TOOLS = [add]
