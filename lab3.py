import streamlit as st
from transformers import pipeline
import torch

st.title("Работа с языковой моделью")

prompt = st.text_area("Промпт", "Сгенерируй описание для дисциплины «Программная инженерия» в магистратуре ТюмГУ")
max_length = st.slider("Максимум токенов", 50, 1024, 300)

if st.button("Запустить"):
    with st.spinner("Загрузка модели..."):
        device = 0 if torch.cuda.is_available() else -1
        generator = pipeline("text-generation", model="ai-forever/rugpt3small_based_on_gpt2", device=device)
        out = generator(prompt, max_new_tokens=max_length, do_sample=True, temperature=0.7)
        st.write(out[0]["generated_text"])
