# AI-Powered-Travel-Planner
AI-Powered Travel Planner
# AI-Powered Travel Planner

## Project Overview
The AI-Powered Travel Planner is an AI-powered travel planning application designed to assist users in finding optimal travel options between a given source and destination. The system leverages LangChain and Google GenAI to process user inputs and generate various travel choices such as cab, train, bus, and flights, along with their estimated costs.

## Objectives
- Develop an AI application that efficiently fetches travel information.
- Utilize LangChain to manage LLM-based interactions for user queries.
- Integrate Google GenAI for intelligent data processing and response generation.
- Ensure an intuitive user interface for seamless interaction.

## System Architecture

### Components
- **User Interface (UI):** A web-based application interface to collect user input.
- **LangChain Framework:** For managing LLM-based conversation flow.
- **Google GenAI Model:** To generate intelligent travel recommendations.

### Workflow
1. User inputs source and destination in the application.
2. The system processes the input using LangChain and Google GenAI.
3. The model generates a structured response containing different travel modes and their estimated prices.
4. The user receives the response with travel recommendations.

## Tech Stack
- **Programming Language:** Python
- **User Interface:** Streamlit
- **Framework:** LangChain
- **AI Model:** Google GenAI

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Streamlit
- LangChain
- Google GenAI API access

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ai-powered-travel-planner.git
    cd ai-powered-travel-planner
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables for Google GenAI API access:
    ```bash
    export GOOGLE_GENAI_API_KEY='YOUR_API_KEY_HERE'
    ```

### Running the Application
1. Start the Streamlit application:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501` to access the application.

### Usage
1. Enter the source and destination locations in the input fields.
2. Click on the "Get Travel Options" button.
3. The application will display various travel options along with their estimated costs.

