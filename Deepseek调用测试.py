import os
from openai import OpenAI
import HamidashiModels
import BlueArchiveModels

#选择模型
model = HamidashiModels.Asumi

name = model.Name
persona = model.Persona

cont = input('...')
#创建交互客户端
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", 'content':persona},
        {"role": "user", "content": cont}
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

print(name,':',response.choices[0].message.content)
print('')
print('本次消耗',response.usage.total_tokens,'tokens,大约{:.4f}分，请注意花费！'.format(int(response.usage.total_tokens)*0.0003))