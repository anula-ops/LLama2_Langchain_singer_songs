from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain_community.llms import CTransformers
#Llama2

llm = CTransformers(
        model = "TheBloke/Llama-2-7B-Chat-GGML",
        model_type="llama",
        max_new_tokens = 1024,
        temperature = 0.5
    )

def generate_singer_name_and_songs(country):
    # Chain 1: Restaurant Name
    prompt_template_name = PromptTemplate(
        input_variables=['country'],
        template="Tell me the name of the one famous singer of {country}."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="singer_name")

    # Chain 2: Menu Items
    prompt_template_items = PromptTemplate(
        input_variables=['singer_name'],
        template="""Suggest some songs of {singer_name}. Return it as a comma separated string"""
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="songs")

    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['country'],
        output_variables=['singer_name', "songs"]
    )

    response = chain({'country': country})

    return response

if __name__ == "__main__":
    print(generate_singer_name_and_songs("Italy"))