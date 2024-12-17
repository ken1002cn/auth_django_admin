import os
from openai import OpenAI
class AiCallHandler:
   @staticmethod
   def call(message, prompt):
       try:
           client = OpenAI(
               # api-key
               api_key='sk-ff638ce19f92495c98aaffde9432798a',
               base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
           )

           completion = client.chat.completions.create(
               model="qwen-turbo",  # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
               messages=[
                   {'role': 'system', 'content': prompt},
                   {'role': 'user', 'content': message}
               ]
           )
           return completion.choices[0].message.content
       except Exception as e:
           print(f"错误信息：{e}")
           print("请参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code")
           return "ai调用出现问题"
