# %%
import getpass
import os

os.environ["LANGSMITH_API_KEY"] = getpass.getpass()
os.environ["FINANCIAL_DATASETS_API_KEY"] = getpass.getpass()
os.environ["OPENAI_API_KEY"] = getpass.getpass()

# %%
LANGSMITH_TRACING="true"
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
LANGSMITH_PROJECT="pr-rundown-waiter-11"

# %%
from langchain_openai import ChatOpenAI

# %%
llm = ChatOpenAI(api_key=OPENAI_API_KEY)
print(llm.invoke("Hello, world!"))

# %%
import re
from langchain_community.agent_toolkits.financial_datasets.toolkit import (
    FinancialDatasetsToolkit,
)
from langchain_community.utilities.financial_datasets import FinancialDatasetsAPIWrapper

api_wrapper = FinancialDatasetsAPIWrapper(
    financial_datasets_api_key=os.environ["FINANCIAL_DATASETS_API_KEY"]
)
toolkit = FinancialDatasetsToolkit(api_wrapper=api_wrapper)

tools = toolkit.get_tools()

system_prompt = """
You are an advanced financial analysis AI assistant equipped with specialized tools
to access and analyze financial data. Your primary function is to help users with
financial analysis by retrieving and interpreting income statements, balance sheets,
and cash flow statements for publicly traded companies.

You have access to the following tools from the FinancialDatasetsToolkit:

1. Balance Sheets: Retrieves balance sheet data for a given ticker symbol.
2. Income Statements: Fetches income statement data for a specified company.
3. Cash Flow Statements: Accesses cash flow statement information for a particular ticker.

Your capabilities include:

1. Retrieving financial statements for any publicly traded company using its ticker symbol.
2. Analyzing financial ratios and metrics based on the data from these statements.
3. Comparing financial performance across different time periods (e.g., year-over-year or quarter-over-quarter).
4. Identifying trends in a company's financial health and performance.
5. Providing insights on a company's liquidity, solvency, profitability, and efficiency.
6. Explaining complex financial concepts in simple terms.

When responding to queries:

1. Always specify which financial statement(s) you're using for your analysis.
2. Provide context for the numbers you're referencing (e.g., fiscal year, quarter).
3. Explain your reasoning and calculations clearly.
4. If you need more information to provide a complete answer, ask for clarification.
5. When appropriate, suggest additional analyses that might be helpful.

Remember, your goal is to provide accurate, insightful financial analysis to
help users make informed decisions. Always maintain a professional and objective tone in your responses.
"""


from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o")

# Display an example query to guide the user
print("\nExample query: 'What was AAPL's revenue in 2023? What about its total debt in Q1 2024?'")

# Prompt the user for their financial query
query = input("Enter your financial query: ").strip()

# Validate the input
if not query:
    print("Error: Query cannot be empty. Please try again.")
else:
    # Confirm the query back to the user
    print(f"\nYou asked: {query}")

    # Placeholder for further processing (e.g., querying APIs or running your AI agent)
    print("Processing your query...")

from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
        # Placeholders fill up a **list** of messages
        ("placeholder", "{agent_scratchpad}"),
    ]
)


def clean_latex(response):
    """
    Cleans LaTeX math delimiters but keeps the calculations intact.
    
    Args:
        response (str): The chatbot's response containing LaTeX.

    Returns:
        str: The cleaned response without LaTeX math delimiters but with calculations preserved.
    """
    # Remove the \[ and \] delimiters but keep the content inside
    response = re.sub(r"\\\[|\]", "", response)
    
    # Remove the \( and \) delimiters but keep the content inside
    response = re.sub(r"\\\(|\\\)", "", response)
    
    # Remove \text{} but keep the content inside
    response = re.sub(r"\\text\{(.*?)\}", r"\1", response)
    
    # Return the cleaned response
    return response.strip()


def format_response(response_data):
    """
    Formats and cleans the chatbot's response for better readability.

    Args:
        response_data (dict): The chatbot response containing 'input' and 'output'.

    Returns:
        str: A formatted and cleaned response string.
    """
    input_query = response_data.get("input", "No query provided.")
    raw_output = response_data.get("output", "No output provided.")

    # Clean LaTeX from the raw output
    cleaned_output = clean_latex(raw_output)

    # Create formatted response
    formatted_output = f"""
    === User Query ===
    {input_query}

    === Chatbot Response ===
    {cleaned_output}

    === End of Response ===
    """
    return formatted_output

agent = create_tool_calling_agent(model, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)
agent_executor.invoke({"input": query})

response = agent_executor.invoke({"input": query})

# Format and display the response
formatted_response = format_response(response)
print(formatted_response)

# %%
