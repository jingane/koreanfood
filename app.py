import streamlit as st
import requests
from bs4 import BeautifulSoup
import urllib.parse

def search_recipes(ingredients):
    base_url = 'https://m.10000recipe.com/recipe/list.html'
    params = {'q': '+'.join(ingredients)}
    url = base_url + '?' + urllib.parse.urlencode(params)
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    recipes = []
    results = soup.find_all('div', class_='common_sp_thumb')
    for result in results:
        title = result.find('h4').text.strip()
        link = 'https://m.10000recipe.com' + result.find('a')['href']
        recipes.append({'title': title, 'link': link})
    
    return recipes

st.title('냉장고를 지켜줘 - 반찬재료로 요리 레시피 검색하기')

ingredients = st.text_input('반찬재료를 입력하세요 (예: 김치, 계란, 두부)')

if st.button('검색'):
    if ingredients:
        recipes = search_recipes(ingredients.split(','))
        if recipes:
            st.header('검색 결과:')
            for recipe in recipes:
                st.markdown(f"[{recipe['title']}]({recipe['link']})")
        else:
            st.warning('레시피를 찾을 수 없습니다.')
    else:
        st.warning('반찬재료를 입력해주세요.')
