
#An OpenAI Module For Tokens
import tiktoken 
import json

#Create a encode for which tool like openai,gpt,gemini..etc
#gpt-6 base encoding Vocabulary
encoding=tiktoken.get_encoding("o200k_base")

document={
  "user":" A story is an account of real or imagined events "
  "told through written words, spoken language, or visual media. It usually features characters,"
  " a setting, and a plot with a beginning, middle, and end"
}


#COUNT THE TOKEN 
for count_token,text in document.items():
    tokens=encoding.encode(text)
    token_count=len(tokens)
    print(f"{count_token}:{token_count} tokens")


#Pricing The Input Cost Per Unit:
input_cost_per_unit= 1,50,000/1,28,000
for count,text in document.items():
    token_counts=len(encoding.encode(text))
#calculate the exact cost per processing
total_cost=token_counts* input_cost_per_unit

print(f"-------Total COST-------")
print(f"Token Count:{token_counts}")
print(f"Enhancing Total Cost:{total_cost}")
