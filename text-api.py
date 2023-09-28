model_url = "http://localhost:5000"

from langchain import PromptTemplate, LLMChain
from langchain.llms import TextGen

template = """Avoid repetition, don't loop. Develop the plot slowly, always stay in character. Describe all actions in full, elaborate, explicit, graphic, and vivid detail. Mention all relevant sensory perceptions.
### Input:
{char_name} Description:[{description}]
{history}
### Instruction:
{player_name}: {user_input}
### Response (2 paragraphs, engaging, natural, authentic, descriptive, creative):
{char_name}:"""

prompt = PromptTemplate(template=template,
                        input_variables=["char_name", "description", "history", "player_name", "user_input"])



def generate(user_input, player_name, char_name, description, history):
    llm = TextGen(model_url=model_url,
                  temperature=0.7,
                  top_p=0.9,
                  top_k=20,
                  max_new_tokens=200,
                  repetition_penalty=1.15,
                  stopping_strings=['\n'+player_name+':', '\n### Instruction:', '\n### Response'])
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    ai_output = llm_chain.run(char_name=char_name,
                              description=description,
                              history=history,
                              player_name=player_name,
                              user_input=user_input)
    return ai_output


