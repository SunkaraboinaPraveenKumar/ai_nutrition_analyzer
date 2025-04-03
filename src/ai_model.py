import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from loguru import logger  # Using loguru for logging
from langchain.document_loaders import DirectoryLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

logger.add("logs/app.log", rotation="10 MB")

# Build food index using LangChain's DirectoryLoader and FAISS vector store with Hugging Face embeddings
def build_food_index(data_path: str = "data") -> FAISS:
    try:
        # Load all text files from the directory (adjust glob pattern if necessary)
        loader = DirectoryLoader(data_path, glob="**/*.txt")
        documents = loader.load()
        
        # Initialize Hugging Face embeddings using a pre-trained model
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        
        # Build the FAISS vector store from the loaded documents
        index = FAISS.from_documents(documents, embeddings)
        logger.info("Food Knowledge index built successfully")
        return index
    except Exception as e:
        logger.error(f"Error building index: {str(e)}")
        return None

# Query the nutrition knowledge index using LangChain's RetrievalQA chain
def query_nutrition_knowledge(question: str) -> str:
    try:
        index = build_food_index()
        if not index:
            return "Unable to build Index"
        
        # Use the vector store as a retriever
        retriever = index.as_retriever()
        
        # Create a RetrievalQA chain with your ChatGroq LLM as the language model
        qa_chain = RetrievalQA.from_chain_type(
            llm=ChatGroq(model="llama-3.3-70b-versatile", api_key=api_key),
            chain_type="stuff",  # simple chain type; consider other types if needed
            retriever=retriever
        )
        response = qa_chain.run(question)
        logger.info(f"Query Executed: {question}")
        return response
    except Exception as e:
        logger.error(f"Error during Querying: {str(e)}")
        return "Unable to answer the question at the moment"

# Fetch detailed nutrition info directly from ChatGroq
def get_nutrition_info(food_item: str) -> str:
    try:
        client = ChatGroq(model="llama-3.3-70b-versatile", api_key=api_key)
        response = client.invoke(f"""
            You are a food nutrition expert.
            Give me detailed nutrition info for food item: {food_item}. 
            Mention various vitamins, minerals, their proportions, and use cases.
        """)
        nutrition_data = response.content
        logger.info(f"Fetched Nutrition Data for {food_item}")
        return nutrition_data
    except Exception as e:
        logger.error(f"Groq Error: {str(e)}")
        return "Unable to fetch Nutrition Info"
