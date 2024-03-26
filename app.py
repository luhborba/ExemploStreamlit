import streamlit  as st
import pandas as pd


def main():
    st.set_page_config(page_title="Cadastra Usuários", layout="wide")
    st.title('Cadastro de Usuários')


    with st.expander("Realizar cadastros: "):
        nome = st.text_input('Nome')
        email = st.text_input('Email')
        idade = st.number_input('Idade', min_value=0, max_value=150)
        cidade = st.text_input('Cidade')

        if st.button('Registrar'):
            novo_usuario = {
                'Nome': nome,
                'Email': email,
                'Idade': idade,
                'Cidade': cidade
            }

            try:
                df = pd.read_csv('usuarios.csv')
            except FileNotFoundError:
                df = pd.DataFrame(columns=['Nome', 'Email', 'Idade', 'Cidade'])


            df = pd.concat([df, pd.DataFrame([novo_usuario])], ignore_index=True)

            df.to_csv('usuarios.csv', index=False)
            st.success('Usuário registrado com sucesso!')

    with st.expander('Listar Cadastros: '):
        try:
            st.dataframe(pd.read_csv('usuarios.csv'))
        except:
            st.warning('Nenhum registro encontrado!')

if __name__ == '__main__':
    main()