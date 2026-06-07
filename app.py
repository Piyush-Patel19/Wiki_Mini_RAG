import streamlit as st
import wikipediaapi
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.6
)

st.set_page_config(
    page_title="Wikipedia AI Search",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Wikipedia AI Search")
st.write("Search any topic and get an AI-generated answer from Wikipedia.")

query = st.text_input(
    "What do you want to search?",
    placeholder="e.g. Who invented Cricket?"
)

if st.button("Search") and query:

    with st.spinner("Searching Wikipedia..."):

        generate_page = """
        You are a specialized Wikipedia Title Generator.

        Your sole task is to analyze the text provided by the user
        and determine the exact Wikipedia page title.

        Return ONLY the title.
        """

        text_template = """
        You are a helpful assistant.

        Answer the user's question ONLY using the context below.

        If the answer is not found in the context, reply:
        "I could not find that information in the provided context."

        Context:
        {text}
        """

        wiki = wikipediaapi.Wikipedia(
            user_agent="MyDataProject/1.0",
            language="en"
        )

        # Generate page title
        title_response = llm.invoke(
            generate_page + "\n\nUser Query:\n" + query
        )

        page_title = str(title_response.content).strip()

        st.subheader("Wikipedia Page")
        st.info(page_title)

        page = wiki.page(page_title)

        if page.exists():

            summary = page.summary

            prompt = ChatPromptTemplate.from_messages([
                ("system", text_template),
                ("human", "{question}")
            ])

            chain = prompt | llm

            response = chain.invoke({
                "question": query,
                "text": summary
            })

            st.subheader("Answer")
            st.success(response.content)

            with st.expander("Wikipedia Context"):
                st.write(summary)

        else:
            st.error("Wikipedia page not found.")