# Nexus Nova: LangGraph Streamlit Chatbot

Nexus Nova is an advanced AI chatbot application built with LangGraph and Streamlit. It combines the power of large language models with a structured graph-based approach to create a versatile, multi-tool chatbot with knowledge retrieval capabilities.

## Features

- **Interactive Chat Interface**: Clean, user-friendly Streamlit interface for conversing with the AI
- **Multi-modal Support**: Upload and process images along with text queries
- **Knowledge Base Integration**: Query information from an AstraDB vector database
- **Web Search Capability**: Integrated Tavily search for retrieving up-to-date information
- **Document Processing**: Upload and embed PDF documents to enhance the knowledge base
- **Streaming Responses**: Real-time token streaming for a more interactive experience
- **Structured Tool Use**: LangGraph-powered decision making for appropriate tool selection

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd LangGraph-Streamlit
   ```

2. Create and activate a virtual environment:
   ```
   conda create -n chatbot python=3.10
   conda activate chatbot
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project root with the following variables:
   ```
   OPENAI_API_KEY=your_openai_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ASTRA_DB_API_ENDPOINT=your_astradb_endpoint
   ASTRA_DB_APPLICATION_TOKEN=your_astradb_token
   ASTRA_DB_NAMESPACE=your_astradb_namespace
   ```

   Alternatively, you can set up Streamlit secrets by creating a `.streamlit/secrets.toml` file with the same variables.

## Usage

1. Run the Streamlit application:
   ```
   streamlit run "Nexus Nova.py"
   ```

2. The application will open in your default web browser.

3. Use the chat interface to interact with the AI assistant.

4. Upload images by attaching them to your messages.

5. To add documents to the knowledge base, navigate to the "DataStore" page and upload PDF files.

## Project Structure

- `Nexus Nova.py`: Main Streamlit application file with the chat interface
- `graph.py`: LangGraph implementation with tool definitions and graph structure
- `st_callable_util_improved.py`: Utility for Streamlit callback handling and token streaming
- `pages/DataStore.py`: Streamlit page for uploading and embedding PDF documents
- `.env`: Environment variables for API keys and configuration

## Tools and Capabilities

The chatbot includes several tools:

1. **Weather Tool**: Provides weather information for specified locations
2. **Knowledge Base Query**: Retrieves information from the AstraDB vector database
3. **Tavily Search**: Performs web searches to find up-to-date information
4. **Image Processing**: Analyzes and processes uploaded images using GPT-4o vision capabilities

## Configuration

### AstraDB Setup

1. Create an account on [DataStax Astra](https://astra.datastax.com/)
2. Create a new vector database
3. Generate an application token
4. Update your environment variables with the database endpoint, token, and namespace

### API Keys

The application requires the following API keys:

- **OpenAI API Key**: For GPT-4o model access and embeddings
- **Tavily API Key**: For web search functionality

## Dependencies

This project relies on several key libraries:

- **Streamlit**: For the web interface
- **LangGraph**: For structured conversation flow and tool use
- **LangChain**: For LLM integrations and utilities
- **OpenAI**: For GPT-4o model access
- **AstraDB**: For vector storage
- **Pillow**: For image processing
- **PyPDF**: For PDF document processing

See `requirements.txt` for a complete list of dependencies.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgements

- OpenAI for GPT models
- LangChain and LangGraph teams for their excellent frameworks
- Streamlit for the intuitive UI framework
