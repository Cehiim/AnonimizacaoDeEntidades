import streamlit as st
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(r'model')
    model = AutoModelForTokenClassification.from_pretrained(r'model')
    pipe = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="average")
    return pipe

def ner(input, pipe):
    result = pipe(input)
    return result

def filter_entities(entities, group):
    return [ent for ent in entities if ent["entity_group"] == group]

def print_entities(entities):
    for ent in entities:
        st.markdown(f"- {ent['word']}")

with st.spinner("Ativando...", show_time=True):
    pipe = load_model()

st.markdown("# Reconhecimento de Entidades")

ner_tags = [
    'Data',
    'Local',
    'Organização',
    'Pessoa',
    'Profissão'
]

output = ''
if input := st.text_area("Digite aqui"):
    with st.spinner("Aguarde...", show_time=True):
        output = ner(input, pipe)

tabs = st.tabs(ner_tags)
data = filter_entities(output, 'Data')
local = filter_entities(output, 'Local')
organizacao = filter_entities(output, 'Organizacao')
pessoa = filter_entities(output, 'Pessoa')
profissao = filter_entities(output, 'Profissao')

with tabs[0]:
    if output:
        print_entities(data)

with tabs[1]:
    if output:
        print_entities(local)

with tabs[2]:
    if output:
        print_entities(organizacao)

with tabs[3]:
    if output:
        print_entities(pessoa)

with tabs[4]:
    if output:
        print_entities(profissao)