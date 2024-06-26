import streamlit as st

def main():
    st.title('냉장고를 지켜줘 - 반찬 재료로 요리 추천하기')
    st.write('반찬 재료를 입력하세요.')

    # 사용자에게 입력 받기
    ingredient1 = st.text_input('재료 1:')
    ingredient2 = st.text_input('재료 2:')
    ingredient3 = st.text_input('재료 3:')
    ingredient4 = st.text_input('재료 4:')
    ingredient5 = st.text_input('재료 5:')

    if st.button('레시피 찾기'):
        # 여기서 레시피 추천 및 표시 로직을 구현합니다
        # 추천된 레시피를 화면에 보여줍니다
        st.write('추천된 레시피들을 표시합니다.')

if __name__ == '__main__':
    main()
