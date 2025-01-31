# Financial-Reporting-AI-Agent
Financial Reporting AI Agent using LangChain template

## Overview
This project is a **Financial Analysis Assistant** that utilizes **LangChain, OpenAI's GPT models, and financial datasets APIs** to provide insights into publicly traded companies. The assistant can fetch **balance sheets, income statements, and cash flow statements**, perform financial ratio analysis, and generate insights into a company's financial health.

Additionally, a **Dash web application** provides an interactive interface for users to enter financial queries and receive AI-generated responses in real-time.

## Features
- **Retrieve Financial Data**: Access balance sheets, income statements, and cash flow statements for publicly traded companies.
- **Analyze Financial Metrics**: Compute key financial ratios and trends.
- **Compare Performance**: Compare financials over time (YoY, QoQ, etc.).
- **Interactive Dashboard**: A Dash-based UI to input queries and receive AI-generated responses.
- **Natural Language Processing**: Uses OpenAI's GPT models to interpret user queries.

## Requirements
Before running the application, ensure you have the following installed:

### Dependencies:
- Python 3.8+
- `langchain`
- `langchain_openai`
- `dash`
- `dash-bootstrap-components`
- `re`
- `getpass`
- `os`
- `webbrowser`

### API Keys:
To use the assistant, you must set up API keys for:
- **LangSmith API**
- **Financial Datasets API**
- **OpenAI API**

These API keys are required and should be entered when prompted in the script.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/mdskinne/Financial_Reporting_AI_Agent.git
    cd Financial_Reporting_AI_Agent
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the application:
    ```bash
    python app.py
    ```

## Usage
### Command-Line Interface (CLI)
After running the script, users can enter financial queries in the command line, such as:
```bash
What was AAPL's revenue in 2023? What about its total debt in Q1 2024?
```
The assistant will process the query and return insights based on financial datasets.

### Web Application
Once the script runs, it will launch a **Dash web application** at:
```bash
http://127.0.0.1:8050
```

Users can enter their queries in the web interface and receive AI-generated responses based on financial data.

## Implementation Details
- **LangChain Integration**: Uses `langchain_openai` to interface with GPT models.
- **Financial Datasets API**: Fetches structured financial data.
- **Data Cleaning**: Includes regex-based cleaning functions to process AI-generated responses.
- **Dash Web App**: Provides a user-friendly interface for interactive queries.

## Example Query
```bash
What is TSLA's cash flow trend over the past 3 years?
```
The assistant will retrieve Tesla’s cash flow statements and generate insights on the trend over the given period.

## Contributing
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit changes and push.
4. Create a pull request.

## License
This project is licensed under the MIT License.

## Contact
For questions or contributions, feel free to reach out via GitHub Issues or contact the project maintainer.

