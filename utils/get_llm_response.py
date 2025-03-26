from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
# from langchain_anthropic import ChatAnthropic
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from utils.tools import TOOLS
import os
load_dotenv()
import  streamlit as st

groq_api_key = st.secrets["GROQ_API_KEY"]
google_api_key = st.secrets["GOOGLE_API_KEY"]

# os.environ["GROQ_API_KEY"] =  os.getenv('GROQ_API_KEY')
# os.environ["ANTHROPIC_API_KEY"] = config("ANTHROPIC_API_KEY")
# os.environ["GOOGLE_API_KEY"] = os.getenv('GOOGLE_API_KEY')

def get_openai_llm_response(transcribed_text):
    # Define the prompt template using LCEL
    _prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant. Your name is Rica who answer the questions concisely and short yet meaningfully, reflecting a balance of professional expertise, personal growth, and unique qualities. Structure each response clearly, providing specific examples where relevant. Maintain a confident and engaging tone !NONE OF THE RESPONSE SHOULD EXCEED TWO PARAGRAPHS"),
            ("human", "{input}"),
        ]
    )

    # Initialize the OpenAI Chat model (e.g., GPT-4)
    _model = ChatOpenAI(model="gpt-3.5-turbo")
    
    # Create the ReAct agent
    agent = initialize_agent(
    tools=TOOLS,  # Add more tools as needed
    llm=_model,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)
    agent = _prompt|agent
    response = agent.invoke(transcribed_text)
    return response['output']



def get_groq_llm_response(transcribed_text):
    # Define the prompt template using LCEL
    _prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant. Your name is Rica who answer the questions concisely and short yet meaningfully, reflecting a balance of professional expertise, personal growth, and unique qualities. Structure each response clearly, providing specific examples where relevant. Maintain a confident and engaging tone !NONE OF THE RESPONSE SHOULD EXCEED TWO PARAGRAPHS"),
            ("human", "{input}"),
        ]
    )

    # Initialize the Meta AI model (e.g., Llama 3.1 70b versetile)
    _model = ChatGroq(
        model="deepseek-r1-distill-llama-70b",
        temperature=0,
        max_tokens=1024,
        timeout=None,
        max_retries=2,
    )
    # Chain the prompt with the model using LCEL
    chain = _prompt | _model

    # Execute the chain to get the response
    response = chain.invoke(input=transcribed_text)
    
    return response.content

def get_gemini_llm_response(transcribed_text):
    # Define the prompt template using LCEL
    _prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant. Your name is Rica who answer the questions concisely and short yet meaningfully, reflecting a balance of professional expertise, personal growth, and unique qualities. Structure each response clearly, providing specific examples where relevant. Maintain a confident and engaging tone !NONE OF THE RESPONSE SHOULD EXCEED TWO PARAGRAPHS"),
            ("human", "{input}"),
        ]
    )

    # Initialize the Google Deep Mind model (e.g., Gemini Pro 1.5)
    _model = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0,
        max_tokens=1024,
        timeout=None,
        max_retries=2,
    )

    # Chain the prompt with the model using LCEL
    chain = _prompt | _model

    # Execute the chain to get the response
    response = chain.invoke(input=transcribed_text)
    
    return response.content

