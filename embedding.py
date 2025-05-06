import ollama

txt1 = "Olá me chamo Raul"

res = ollama.embeddings(model='llama3.2', prompt=txt1)

print(txt1)
print(len(res.embedding))
print(res.embedding[:10])

txt2 = "Essa atividade é para a diciplina tópicos avançados em sistemas para internet I"

res2 = ollama.embeddings(model='llama3.2', prompt=txt2)

print(txt2)
print(len(res2.embedding))
print(res2.embedding[:10])