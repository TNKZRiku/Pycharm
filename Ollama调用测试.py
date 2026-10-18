import ollama
import HamidashiModels
import BlueArchiveModels



model = BA_GDDModels.Arisu

name = model.Name
persona = model.Persona

cont = input('...')

response = ollama.chat(
    model='huihui_ai/deepseek-r1-abliterated:8b',
    messages=[
        {
            "role": "system",
            'content': persona
        },
        {
            'role': 'user',
         'content': cont
         }
    ]
)

print(name,':',response['message']['content'])
print('本次消耗0tokens,大约0元，请注意花费！')