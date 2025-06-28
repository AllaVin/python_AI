from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from bs4 import BeautifulSoup
import requests

# 1. Получаем текст из URL
def get_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text()

# 2. Шаблон промпта
prompt_template = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text:\n\n{text}\n\nSummary:"
)

# 3. Модель (нужен API-ключ OpenAI в переменной среды OPENAI_API_KEY)
llm = OpenAI(temperature=0.5)

# 4. Цепочка
summary_chain = LLMChain(llm=llm, prompt=prompt_template)

# 5. Пример использования
url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
text = get_text_from_url(url)
summary = summary_chain.run(text=text[:3000])  # ограничим длину

print("Summary:")
print(summary)
