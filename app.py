import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="FurtidoApp",page_icon="🤖", layout="wide")
email_contact = "furtidoapp@gmail.com"

def css_load(css_file):
    with open(css_file) as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)

css_load("Style/style.css")
url = "https://lottie.host/e165d6aa-940e-41ea-98df-e5975bacd686/gGcRJhvrYf.json"

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie = load_lottie(url)

#intro
with st.container():
    st.header("Hola somos FurtidoApp 🤝")
    st.title("Creamos soluciones tecnologicas para tu negocio")
    st.write("somos una startup apasionada por la tecnologia y la inovacion")
    st.write("[Saber mas >](https://furtidoapp.com/)")

#sobre nosotros
with st.container():
    st.write("---")
    text_column, animation_column = st.columns(2)
    with text_column:
        st.header("Sobre nosotros")
        st.write(
        """
        En Furtidoapp:

        - Nos especializamos en el desarrollo web y de software, ofreciendo soluciones a medida para satisfacer las necesidades únicas de cada cliente.
        - Nuestro equipo está formado por profesionales apasionados y altamente capacitados con amplia experiencia en el campo.
        - Nos mantenemos a la vanguardia de las últimas tecnologías y tendencias del mercado para ofrecer soluciones efectivas y escalables.
        - Trabajamos en estrecha colaboración con nuestros clientes para comprender sus objetivos y convertir sus ideas en realidad.
        - Nos distinguimos por nuestra atención al detalle, enfoque centrado en el cliente y capacidad para entregar proyectos en tiempo y forma.
        - Ofrecemos una amplia gama de servicios, desde sitios web elegantes y funcionales hasta aplicaciones móviles intuitivas y software empresarial personalizado.
        - Nuestro compromiso es impulsar el éxito de nuestros clientes a través de soluciones tecnológicas de la más alta calidad.

        ***Únete a nosotros en este emocionante viaje tecnológico***
        """
        )
        st.write("[Mas sobre nosotros >](https://furtidoapp.com/about/)")
    with animation_column:
        st_lottie(lottie, height = 400)
    
#servicios
with st.container():
    st.write("---")
    st.header("Servicios")
    st.write('##')
    image_column, text_column = st.columns ((1,2))
    with image_column:
        image = Image.open("images/pepe.jpg")
        st.image(image,use_column_width=True)
    with text_column:
        st.subheader("Diseño de aplicaciones")
        st.write(
            """
            diseñamos de acuerdo a tus necesidades
            """
        )
        st.write("[Ver servicios >](https://furtidoapp.com/services/)")


#contacto

with st.container():
    st.write("---")
    st.header("Contacta con nosotros")
    st.write("##")
    contact_form = f"""
    <form action="https://formsubmit.co/{email_contact}" method="POST">
     <input type ="hidden" name="_captcha" value="false"
     <input type="text" name="name" placeholder = "tu nombre" required>
     <input type="email" name="email" placeholder = "tu email" required>
     <textarea type="message" name="message" placeholder = "tu mensaje aqui" required></textarea>
     <button type="submit">Send</button>
    </form> 
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()