import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# ChatGPT 모델과 토크나이저 초기화
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

def generate_recipe(ingredients):
    # 사용자 입력을 기반으로 요리 레시피 생성
    input_text = "요리를 만드는 법: {}.".format(", ".join(ingredients))
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # ChatGPT 모델을 사용하여 요리 레시피 생성
    output = model.generate(input_ids, max_length=300, num_return_sequences=5, no_repeat_ngram_size=2)

    recipes = [tokenizer.decode(o, skip_special_tokens=True) for o in output]

    return recipes

def main():
    st.title("냉장고를 지켜줘 - 반찬 재료 기반 요리 레시피 생성기")

    # 반찬 재료 입력 받기
    ingredient1 = st.text_input("반찬 재료 1:")
    ingredient2 = st.text_input("반찬 재료 2:")
    ingredient3 = st.text_input("반찬 재료 3:")
    ingredient4 = st.text_input("반찬 재료 4:")
    ingredient5 = st.text_input("반찬 재료 5:")

    if st.button("레시피 생성하기"):
        ingredients = [ingredient1, ingredient2, ingredient3, ingredient4, ingredient5]
        recipes = generate_recipe(ingredients)

        st.subheader("생성된 요리 레시피:")
        for i, recipe in enumerate(recipes):
            st.markdown(f"**레시피 {i+1}:**")
            st.write(recipe)

if __name__ == "__main__":
    main()
