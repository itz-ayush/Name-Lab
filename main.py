import os
from sec_keys import HuggingFace_API_Token
os.environ['HUGGINGFACEHUB_API_TOKEN'] = HuggingFace_API_Token

from langchain_huggingface import HuggingFaceEndpoint

llm = HuggingFaceEndpoint(repo_id="mistralai/Mistral-7B-Instruct-v0.3")

from langchain.prompts import PromptTemplate
prompt_template_name = PromptTemplate(
    input_variables = [{'business','genre','keyword'}],
    template = "I am looking for a name for my {business} which is about {genre} and should include the keyword {keyword}. Return only 5 names without any description and they should be separated by commas"
)
# prompt_template_name.format(business = "Yotube channel",genre = "Gaming", keyword = "Ayush")
from langchain.chains import LLMChain
chain = LLMChain(llm = llm, prompt = prompt_template_name)


def generate_names(business, genre, keyword=""):
    # Prepare the input for the prompt
    prompt_input = {
        'business': business,
        'genre': genre,
        'keyword': keyword
    }
    # Generate the names using the chain
    response = chain.run(prompt_input)
    return response