import streamlit as st
import pandas as pd

# El orden que vallas poniendo las cosas en en el codigo es el que aparecera en la pagina

#Configuracion de la pagina  https://docs.streamlit.io/library
st.set_page_config(
    page_title="My streamlit project",
    page_icon="🧊",
    layout="wide",
)

# Selector
option = st.sidebar.selectbox(
    'Selecciona la vista:',
    ('Home', 'Visualizaciones', 'Mapa'),
    index=0                # Por defecto cada vez que recargue la foto se pone en home.
    )    

# El sidebar es para que el selector se ponga en el lateral

# Cargar datos en dataframe
datos = pd.read_csv("data/red_recarga_acceso_publico_2021.csv", sep=";")

# Cargar datos manual
uploaded_file = st.sidebar.file_uploader("Elige el csv", type=["csv"])
if uploaded_file is not None:
    datos = pd.read_csv(uploaded_file)
    
st.title("CARGATRON")

if option == "Home":    

    # Titulo
    st.title("My APP - HOME")

    # Expander Descripcion que se expande
    with st.expander("Detalles de la aplicacion - Haz clic para expandir"):
        st.write("""
            Esto es una aplicacion....
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        """)

    # Imagen La imagen esta dentro del expander. Puedes ponerlo afuera tambien
        st.image("https://th.bing.com/th/id/R.e0bad63364a867fea652212c254bf869?rik=avtecz5aXVdevA&riu=http%3a%2f%2fwww.viajejet.com%2fwp-content%2fviajes%2fLago-Moraine-Parque-Nacional-Banff-Alberta-Canada.jpg&ehk=6qRhWDqqQAEkSFs%2bHP8p2Bl6XfPbjznSoORh%2bsEJ%2bQE%3d&risl=&pid=ImgRaw&r=0", 
            width=600, caption="Paisaje refrescante")


    # Mostrar datos    
    st.write(datos)

    st.balloons()  # globos en la pagina

    # Para mostrar el codigo en la página
    with st.echo():
        st.write(datos)

elif option == "Mapa": 
    st.title("My APP - MAPA")  
    # Visualizar mapa
    datos_mapa = datos[["latidtud", "longitud"]]    # Nombre de Columnas que tiene el dataset datos
    datos_mapa.columns = ["lat", "lon"]             # Columnas que hay que poner para que funcione el mapa

    st.subheader("Mapa Cargadores")
    st.map(datos_mapa)

elif option == "Visualizaciones":
    st.title("My APP - VISUALIZACIONES")
    datos_bar_chart = datos.groupby("DISTRITO")["Nº CARGADORES"].sum().reset_index()
    st.subheader("Numero de cargadores por distrito")
    st.bar_chart(datos_bar_chart, x = "DISTRITO", y = "Nº CARGADORES")
    
# Para crear requirements (generar librerias que utiliza en un proyecto)
# En consola ejecutas pip freeze > requirements.txt
# Inmediatamente en se genera las librerias. 
# Esto genera un problema con las @. Para esto se pone pip list --format=freeze >requirements.txt
# Esto genera muchas librerias que no hacen falta dejarla porque el user no va a instalar.