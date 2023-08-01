import os, config
import openai

# from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader
# new version replaces GPTSimpleVectorIndex with GPTVectorStoreIndex

from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader

os.environ['OPENAI_API_KEY'] = config.OPENAI_API_KEY

openai.api_key = os.environ['OPENAI_API_KEY']
documents = SimpleDirectoryReader('articles').load_data()

index = GPTVectorStoreIndex.from_documents(documents)

index.storage_context.persist()