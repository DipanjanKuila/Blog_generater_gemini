import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os


os.environ["GOOGLE_API_KEY"] = "YOUR API KEY"

def getLLM(Blog_topic,no_words,blog_style):
    llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    
)

    template="""
        Write a good descriptive blog for {blog_style} job profile for a topic {Blog_topic}
        within {no_words} words.
            """
    
    prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_words'],
                          template=template)
    
    ## Generate  ressponse from the Gemini model
    response=llm.invoke(prompt.format(blog_style=blog_style,Blog_topic=Blog_topic,no_words=no_words))
    ai_answer=response.content
    print(ai_answer)
    return ai_answer






st.set_page_config(page_title="Blogs Generater",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

Blog_topic=st.text_input("Enter the Blog Topic")

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('No of Words')
with col2:
    blog_style=st.selectbox('Writing the blog for',
                            ('Researchers','Common People'),index=0)
    
submit=st.button("Generate")

# Final response
if submit:
    st.write(getLLM(Blog_topic,no_words,blog_style))

