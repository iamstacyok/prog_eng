import streamlit as st
import pandas as pd


st.title('Лабораторная работа 3')
st.header('Подсчет кол-ва погибших мужчин старше указанного возраста')

# uploaded_file = st.file_uploader("Загрузите файл", type=["csv"])
uploaded_file = "data.csv"

df = pd.read_csv(uploaded_file)

required_cols = {'Sex', 'Age', 'Survived', 'Embarked'}


def change_port_names(df):
    port_names = {
        'C': 'Шербур',
        'Q': 'Квинстаун',
        'S': 'Саутгемптон',
    }
    df['Embarked'] = df['Embarked'].map(port_names)
    return df


df = change_port_names(df)

# Элемент управления: выбор возраста
min_age = int(df['Age'].min())
max_age = int(df['Age'].max())

age_limit = st.slider(
    "Выберите возрастной порог:",
    min_value=min_age,
    max_value=max_age,
    value=30,
)


def filter_by_age(df, age_limit):
    filtered = df[
        (df['Sex'] == 'male')
        & (df['Age'] > age_limit)
        & (df['Survived'] == 0)
    ]
    return filtered


filtered = filter_by_age(df, age_limit)


def get_results(filtered):
    result = (
        filtered.groupby('Embarked')
        .size()
        .reset_index(name='Погибших мужчин старше указанного возраста')
    )
    return result


result = get_results(filtered)

st.subheader("Результаты:")
st.dataframe(result)

st.info(f"Всего погибших мужчин старше {age_limit} лет: {len(filtered)}")
