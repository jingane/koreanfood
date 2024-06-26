import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# ChatGPT 모델 로드
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# ChatGPT 생성
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Streamlit 애플리케이션 정의
st.title("냉장고를 지켜줘 - 요리 레시피 추천 프로그램")

# 반찬 재료 입력
st.header("반찬 재료 입력")
ingredient1 = st.text_input("1번 반찬 재료")
ingredient2 = st.text_input("2번 반찬 재료")
ingredient3 = st.text_input("3번 반찬 재료")
ingredient4 = st.text_input("4번 반찬 재료")
ingredient5 = st.text_input("5번 반찬 재료")

# 사용자가 반찬 재료를 입력하고 확인 버튼을 클릭한 경우
if st.button("레시피 찾기"):
    ingredients = [ingredient1, ingredient2, ingredient3, ingredient4, ingredient5]
    input_text = " ".join(ingredients)
    
    # ChatGPT를 통해 요리 레시피 생성
    st.header("추천된 요리 레시피")
    response = generator(input_text, max_length=150, num_return_sequences=5)
    for i, resp in enumerate(response):
        st.subheader(f"레시피 {i+1}")
        st.write(resp["generated_text"])
