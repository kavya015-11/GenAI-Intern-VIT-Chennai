import google.generativeai as genai

genai.configure(api_key="AIzaSyDqS9yLVkwqMRMMoF4iXyWnVpaunzjIyus")

models = genai.list_models()
for model in models:
    print(model.name)
