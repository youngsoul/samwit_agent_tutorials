from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


if __name__ == '__main__':

    # Local Llama3
    llm = ChatOllama(
        model="llama3.2",
        keep_alive=-1, # keep the model loaded indefinitely
        temperature=0,
        max_new_tokens=512)

    prompt = ChatPromptTemplate.from_template("Write me a 100 word article on {topic} from the perspective of a {profession}. ")

    # using LangChain Expressive Language chain syntax
    chain = prompt | llm | StrOutputParser()

    # print(chain.invoke({"topic": "LLMs", "profession": "shipping magnate"}))

    for chunk in chain.stream({"topic": "LLMs", "profession": "shipping magnate"}):
        print(chunk, end="", flush=True)