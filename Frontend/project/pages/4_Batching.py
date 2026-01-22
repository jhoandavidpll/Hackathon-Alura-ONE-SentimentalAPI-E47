import streamlit as st
from menu import generar_menu 
import sys
import os
from funciones import *

def main():
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    st.set_page_config(page_title="Batching", layout="centered", page_icon=":brain:")

    estilo()
    generar_menu()

if __name__ == "__main__":
    main()