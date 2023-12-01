from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.schema import StrOutputParser

template = PromptTemplate(template="""
You are an expert Javascript/Typescript developer
Your role is to assist me in debugging and writing new code
Respond using best approaches and practices.

Tell me about the following feature: {feature}
""", input_variables=["feature"])

llm = Ollama(model="llama2", temperature=0.0, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))

prompt=input('Ask me something')



llm_chain = LLMChain(
    llm=llm,
    prompt=template,
    output_parser=StrOutputParser()
)
response = llm_chain.run(feature=prompt)

print(response)