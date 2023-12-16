import pandas as pd
import streamlit as st
import numpy

archivo_csv = "/workspaces/songpedia/base.csv"
df = pd.read_csv(archivo_csv)

st.title('Songpedia')
st.text("Aprende más acerca de tus canciones")


artistas_input = st.text_input('Ingresa artista:')


artistas_elegidos = [artista.strip().lower() for artista in artistas_input.split(',') if artista.strip()]


df['track_artist'] = df['track_artist'].str.lower()


df_filtrado_por_artistas = df[df['track_artist'].isin(artistas_elegidos)]


canciones_elegidas = st.multiselect('Selecciona canciones:', df_filtrado_por_artistas['track_name'].str.lower().unique())


df_filtrado_por_artistas['track_name'] = df_filtrado_por_artistas['track_name'].str.lower()


df_filtrado_por_canciones = df_filtrado_por_artistas[df_filtrado_por_artistas['track_name'].isin(canciones_elegidas)]


for index, row in df_filtrado_por_canciones.iterrows():
    tono = row['key']
    modo = row['mode']
    tempo = row['tempo']
    año = row['track_album_release_date']
    artista = row['track_artist']
    cancion = row['track_name']

    st.success(f'Información para la canción "{cancion}" del artista "{artista}":')
    st.write(f'- Tono: {tono}')
    st.write(f'- Modo: {modo}')
    st.write(f'- Tempo: {tempo}')
    st.write(f'- Año: {año}')
