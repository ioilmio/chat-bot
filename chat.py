# # # from langchain.callbacks.manager import CallbackManager
# # # from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
# # # from langchain.chat_models import ChatOllama
# # # from langchain.prompts.prompt import PromptTemplate
# # # from langchain.schema import HumanMessage
# # # from langchain.chains import LLMChain
# # # from langchain.memory import ConversationBufferMemory

# # # chat_model = ChatOllama(
# # #     model="llama2:7b-chat",
# # #     callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
# # #     temperatue=0.0
# # # )

# # # while True:
# # #     user_input = input("Ask me something: \n")
# # #     # Increase the maximum memory size to 20 messages
# # #     prompt = PromptTemplate(template="""
# # #     You are an expert Javascript developer, your asnwers are brief and professional
# # #     {chat_history}
# # #     Question: {question}
# # #     """, input_variables=["question"])
# # #     memory = ConversationBufferMemory(memory_key="chat_history", input_key="question", return_messages=True, max_memory_size=20)

# # #     chat_chain = LLMChain(llm=chat_model, prompt=prompt, memory=memory)
# # #     response = chat_chain.run(
# # #         question=user_input
# # #     )



# # from langchain.callbacks.manager import CallbackManager
# # from langchain.chat_models import ChatOllama
# # from langchain.prompts.prompt import PromptTemplate
# # from langchain.schema import HumanMessage
# # from langchain.chains import LLMChain
# # from langchain.memory import ConversationBufferMemory

# # chat_model = ChatOllama(
# #     model="llama2:7b-chat",
# #     callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
# #     temperatue=0.0
# # )

# # while True:
# #     user_input = input("Ask me something: \n")
# #     # Increase the maximum memory size to 20 messages
# #     prompt = PromptTemplate(template="""
# #     You are an expert Javascript developer, your asnwers are brief and professional
# #     {chat_history}
# #     Question: {question}
# #     """, input_variables=["question"])
# #     memory = ConversationBufferMemory(memory_key="chat_history", input_key="question", return_messages=True, max_memory_size=20)

# #     chat_chain = LLMChain(llm=chat_model, prompt=prompt, memory=memory)
# #     response = chat_chain.run(
# #         question=user_input
# #     )



# from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
# from langchain.chat_models import ChatOllama
# from langchain.prompts.prompt import PromptTemplate
# from langchain.schema import HumanMessage
# from langchain.chains import LLMChain
# from langchain.memory import ConversationBufferMemory

# chat_model = ChatOllama(
#     model="llama2:7b-chat",
#     callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
#     temperatue=0.0
# )

# while True:
    # user_input = input("Ask me something: \n")
#     # Increase the maximum memory size to 20 messages
#     prompt = PromptTemplate(template="""
#     You are an expert Javascript developer, your asnwers are brief and professional
#     {chat_history}
#     Question: {question}
#     """, input_variables=["question"])
#     memory = ConversationBufferMemory(memory_key="chat_history", input_key="question", return_messages=True, max_memory_size=20)

#     chat_chain = LLMChain(llm=chat_model, prompt=prompt, memory=memory)
#     response = chat_chain.run(
#         question=user_input
#     )


from langchain.llms import LlamaCpp
from langchain.chat_models import ChatOllama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain


chat_model = ChatOllama(
    model="llama2:7b-chat",
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
    temperatue=0.0
)

prompt = ChatPromptTemplate(
    messages=[
        MessagesPlaceholder(variable_name="chat_history"),  # Where the memory will be stored.
        HumanMessagePromptTemplate.from_template("{human_input}"),  # Where the human input will be injected
    ]
)
memory = ConversationBufferMemory(memory_key="chat_history")
conversation = LLMChain(llm=chat_model, prompt=prompt, memory=memory)
user_input = input("Ask me something: \n")

conversation.predict(human_input="Hi there my friend")