
from llama_index import PromptTemplate
import google.generativeai as palm
import os
from IPython.display import display
from IPython.display import Markdown
import textwrap


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


palm.configure(api_key='AIzaSyAUPvte86iecn23zfWaZOCORwovAm7EI7U')

model = palm.GenerativeModel(model_name="gemini-pro")
template = '''
  انت شاعر عربي فصيح اصيل.معروف بحبك لنظم الشعر الموزون.
  انظم لي  قصيدة على البحر الطويل.
  ان هذه القصيدة يجب ان تتحدث عن {name}.
  ان هذا الشعر يجب ان يكون {type}.
  معلومات عامة:

  {con}

'''
promt_template = PromptTemplate(template)

def Palm_request(type,name,con):
    prompt =promt_template.format(name = name, type = type, con = con )
    response = model.generate_content(prompt)
    return response.text

