# Blog Generator using Google Generative AI

This project is a **Streamlit** web application that generates descriptive blogs using **Google's Gemini-1.5-pro** model. The model is accessed via the **LangChain** framework to dynamically create blog content based on user input, such as the topic, number of words, and desired writing style.

## Features
- **Generate Blogs**: Automatically create blogs based on your input.
- **Customizable Inputs**:
  - `Blog Topic`: The main subject of the blog.
  - `Number of Words`: Define the word limit for the generated blog.
  - `Blog Style`: Specify the writing style (e.g., formal, casual, technical).
  
- **Google Generative AI Integration**: Uses Google's Gemini model to generate the blog content.
- **LangChain Prompt Template**: Utilizes LangChain’s prompt template to format the inputs into an appropriate prompt for the AI model.

## How It Works
1. **User Inputs**: 
   - The user provides the blog topic, the desired number of words, and the preferred blog style.
   
2. **LLM Invocation**:
   - The application calls the `getLLM` function, which uses **LangChain** to interface with the Google Generative AI model (`Gemini-1.5-pro`) to generate content.
   
3. **Content Generation**:
   - A structured prompt is created using `PromptTemplate` and passed to the model, which returns the generated blog content.
   
4. **Output**:
   - The generated blog is displayed in the Streamlit application interface.

## Setup Instructions

### Prerequisites
- Python 3.8+
- Google API Key with access to Google Generative AI (Gemini-1.5-pro)

### Run
streamlit run app.py

