import os

import weaviate
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.pydantic_v1 import BaseModel
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnablePassthrough
from langchain.vectorstores import Weaviate

if os.environ.get("WEAVIATE_API_KEY", None) is None:
    raise Exception("Missing `WEAVIATE_API_KEY` environment variable.")

if os.environ.get("WEAVIATE_ENVIRONMENT", None) is None:
    raise Exception("Missing `WEAVIATE_ENVIRONMENT` environment variable.")

WEAVIATE_INDEX_NAME = os.environ.get("WEAVIATE_INDEX", "langchain-test")

client = weaviate.Client(
    url=os.environ["WEAVIATE_ENVIRONMENT"],
    additional_headers = {
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

vectorstore = Weaviate(client, WEAVIATE_INDEX_NAME, text_key="text")
retriever = vectorstore.as_retriever()

# RAG prompt
template = """Answer the question based only on the following context:
{context}
Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

# RAG
model = ChatOpenAI()
chain = (
    RunnableParallel({"context": retriever, "question": RunnablePassthrough()})
    | prompt
    | model
    | StrOutputParser()
)


# Add typing for input
class Question(BaseModel):
    __root__: str


chain = chain.with_types(input_type=Question)
