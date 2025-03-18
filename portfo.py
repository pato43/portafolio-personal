import streamlit as st
import pandas as pd
import numpy as np
import time
import random

# Configuración de la página
st.set_page_config(
    page_title="Portafolio de Consultoría Interactivo",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inyección de CSS personalizado para una experiencia visual mejorada
custom_css = """
<style>
    body {
        background-color: #f8f9fa;
        font-family: 'Arial', sans-serif;
    }
    .sidebar .sidebar-content {
        background-color: #343a40;
        color: #ffffff;
    }
    .stButton button {
        background-color: #007bff;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 4px;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #0056b3;
    }
    h1, h2, h3, h4 {
        color: #343a40;
    }
    .expander-header {
        font-size: 1.1rem;
        font-weight: bold;
    }
    .title {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .description {
        font-size: 1rem;
        line-height: 1.5;
    }
    /* Estilos para mejorar la visibilidad de los sliders y botones */
    .css-1aumxhk {
        background-color: #e9ecef;
        border-radius: 4px;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Título y descripción principal
st.title("Portafolio de Consultoría AleteIA")
st.markdown(
    "Explora una amplia gama de proyectos en áreas como transformación digital, ciencia de datos, desarrollo web y estrategias financieras. "
    "Utiliza el menú lateral para navegar, filtrar y descubrir cada proyecto de forma interactiva."
)

# Placeholder para el contenido principal (será actualizado dinámicamente en las partes siguientes)
main_placeholder = st.empty()

# Definición del portafolio con muchos proyectos (cada proyecto usará la misma imagen simulada)
portfolio = {
    "Transformación Digital y Automatización": [
        {
            "title": "📌 Automatización de Procesos en Holtmont México",
            "description": "Desarrollo de un sistema de automatización en **Google Sheets** con **Apps Script** para gestionar la distribución de tareas, seguimiento de tiempos y consolidación de datos en Holtmont México. Se integraron scripts personalizados para reportes automáticos en **Google Drive**, notificaciones vía **Gmail API** y validaciones dinámicas en hojas de cálculo.\n\n🔗 **Beneficio:** Reducción del **40%** en tiempos administrativos, mejora en trazabilidad de datos y eliminación de errores en reportes.",
            "image": "/home/nichi/Imágenes/holtmont.png",
            "link": "https://example.com/holtmont"
        },
        {
            "title": "💳 Sistema de Punto de Venta Inteligente para Carbis",
            "description": "Desarrollo de un **POS interactivo** en **Google Sheets y Apps Script** para **Carbis**, con interfaz intuitiva, actualización automática de stock y panel de ventas en tiempo real. Se integraron botones dinámicos, validaciones y cálculos automatizados de costos.\n\n🔗 **Beneficio:** **30% menos errores de cobro**, reducción de **60% en el tiempo de facturación** y mejor gestión de inventario.",
            "image": "/home/nichi/Imágenes/carbis.png",
            "link": "https://example.com/carbis"
        },
        {
            "title": "🏢 Digitalización de Trámites en Tenancingo",
            "description": "Desarrollo de un **portal de trámites en línea** con asistencia por **WhatsApp API**. Se implementó una base de datos en **Google Firebase**, formularios interactivos y automatización de respuestas.\n\n🔗 **Beneficio:** **80% menos tiempo de espera**, reducción de costos administrativos y acceso digital sin desplazamientos.",
            "image": "/home/nichi/Imágenes/tramites_tenancingo.png",
            "link": "https://example.com/tenancingo"
        }
    ],
    "Ciencia de Datos y Análisis de Información": [
        {
            "title": "📊 Análisis Financiero con APIs de Banxico",
            "description": "Desarrollo de un sistema en **Python y SQL** que extrae datos de **Banxico API** y otras fuentes financieras, con dashboards en **Streamlit** y gráficos dinámicos en **Looker Studio**.\n\n🔗 **Beneficio:** Análisis financiero en tiempo real, optimización de inversiones y predicciones basadas en datos históricos.",
            "image": "/home/nichi/Imágenes/banxico.png",
            "link": "https://example.com/banxico"
        },
        {
            "title": "🔮 Predicción de Ventas con Series de Tiempo",
            "description": "Modelo de predicción usando **Taipy y Prophet** con carga de datos en **Google Sheets** y análisis de tendencias en **Power BI**.\n\n🔗 **Beneficio:** **25% menos pérdidas por sobreinventario**, optimización en compras y mejora en planeación de producción.",
            "image": "/home/nichi/Imágenes/prediccion_ventas.png",
            "link": "https://example.com/prediccion"
        }
    ],
    "Desarrollo Web y Digitalización Empresarial": [
        {
            "title": "🛒 Marketplace Digital para Comerciantes de Tenancingo",
            "description": "Desarrollo de una plataforma de e-commerce multivendedor en **Django y React**, con pasarelas de pago en **Stripe** y herramientas de gestión de inventario.\n\n🔗 **Beneficio:** **35% más ventas**, digitalización de comercios informales y acceso a clientes externos.",
            "image": "/home/nichi/Imágenes/marketplace_tenancingo.png",
            "link": "https://example.com/marketplace"
        },
        {
            "title": "💼 Portal de Servicios Empresariales",
            "description": "Plataforma en **Flask y Bootstrap** para conectar profesionales con clientes, con filtros avanzados y sistema de reservas.\n\n🔗 **Beneficio:** Optimización de contratación y automatización de citas.",
            "image": "/home/nichi/Imágenes/portal_servicios.png",
            "link": "https://example.com/portal_servicios"
        }
    ],
    "Educación y Capacitación Tecnológica": [
        {
            "title": "🎓 Curso de Data Analytics con Python y SQL",
            "description": "Curso integral con **SQL, Python, Looker Studio y Streamlit**, incluyendo ejercicios prácticos en **Google Colab** y dashboards en **Looker**.\n\n🔗 **Beneficio:** Formación de **100+ alumnos**, generación de reportes automatizados y análisis en tiempo real.",
            "image": "/home/nichi/Imágenes/curso_data_analytics.png",
            "link": "https://example.com/curso_data_analytics"
        },
        {
            "title": "👨‍💻 Bootcamp TECISTEM - Certificación en Desarrollo Web",
            "description": "Bootcamp de **Microsoft y Mozilla** con tecnologías **HTML, CSS, JavaScript, React y Django**.\n\n🔗 **Beneficio:** Desarrollo de portafolios digitales y certificaciones verificables.",
            "image": "/home/nichi/Imágenes/tecistem.png",
            "link": "https://example.com/bootcamp_tecistem"
        }
    ],
    "Estrategia de Negocio y Modelos Innovadores": [
        {
            "title": "🏦 SOFIPO Digital para Locatarios",
            "description": "Modelo financiero con herramientas de análisis crediticio en **Streamlit**, integrando educación financiera y reportes de riesgo.\n\n🔗 **Beneficio:** Inclusión financiera de pequeños empresarios y acceso a créditos accesibles.",
            "image": "/home/nichi/Imágenes/sofipo.png",
            "link": "https://example.com/sofipo"
        },
        {
            "title": "📈 Optimización Financiera en PYMEs",
            "description": "Consultoría para la **automatización de reportes financieros** con **Google Sheets, Python y Power BI**, optimizando costos y tiempos de análisis.\n\n🔗 **Beneficio:** **20% menos costos administrativos** y toma de decisiones basada en datos.",
            "image": "/home/nichi/Imágenes/optimizacion_financiera.png",
            "link": "https://example.com/optimizacion"
        }
    ]
}

# Menú lateral con filtros y opciones interactivas para una navegación óptima
st.sidebar.title("Navegación y Filtros")
selected_category = st.sidebar.selectbox("Selecciona una Categoría", list(portfolio.keys()))
search_text = st.sidebar.text_input("Buscar proyecto por título:")

# Widgets adicionales en el sidebar para personalizar la experiencia
st.sidebar.markdown("### Opciones Adicionales")
project_slider = st.sidebar.slider("Número de proyectos a mostrar:", min_value=1, max_value=25, value=10, step=1)
refresh_time = st.sidebar.checkbox("Actualizar hora en tiempo real", value=True)
if refresh_time:
    current_time = time.strftime("%H:%M:%S")
    st.sidebar.markdown(f"**Hora Actual:** {current_time}")

# Consejo del día dinámico
st.sidebar.markdown("### Consejo del Día")
tips = [
    "Actualiza tu portafolio regularmente.",
    "La innovación es la clave del éxito.",
    "Mantén tus proyectos bien documentados.",
    "Siempre busca nuevas tendencias tecnológicas."
]
st.sidebar.write(random.choice(tips))

# Información adicional y enlace de ayuda en el sidebar
st.sidebar.markdown("---")
st.sidebar.info("Utiliza los filtros y opciones para explorar nuestros proyectos. ¡Disfruta la experiencia interactiva!")

# Botón para refrescar algunos widgets del sidebar
if st.sidebar.button("Refrescar Widgets"):
    st.sidebar.success(f"Widgets actualizados a las {time.strftime('%H:%M:%S')}")

# Nota: En esta parte aún no se muestra la imagen, pero en las partes siguientes se utilizará:
# st.image(..., use_container_width=True) para mostrar las imágenes de cada proyecto

# Confirmación de carga de la Parte 1
st.markdown("### [Parte 1 de 3 cargada]")
# Parte 2: Visualización dinámica de proyectos y elementos interactivos

st.markdown("## Visualización de Proyectos")
st.markdown("Descubre cada proyecto de la categoría seleccionada a través de una interfaz interactiva. Ajusta el filtro y el slider para ver la cantidad de proyectos que desees.")

# Filtrar proyectos según la categoría seleccionada y el texto de búsqueda
selected_projects = portfolio[selected_category]
if search_text:
    selected_projects = [proj for proj in selected_projects if search_text.lower() in proj["title"].lower()]

if not selected_projects:
    st.warning("No se encontraron proyectos que coincidan con la búsqueda.")
else:
    max_projects = len(selected_projects)
    num_projects = st.slider("Número de proyectos a mostrar:", min_value=1, max_value=max_projects, value=min(project_slider, max_projects), step=1)
    
    st.markdown("---")
    # Iterar sobre los proyectos filtrados y mostrarlos en expanders dinámicos
    for i, project in enumerate(selected_projects[:num_projects]):
        with st.expander(f"{i+1}. {project['title']}", expanded=False):
            col_img, col_details = st.columns([1, 2])
            with col_img:
                st.image(project["image"], caption=project["title"], use_container_width=True)
            with col_details:
                st.subheader(project["title"])
                st.write(project["description"])
                st.markdown(f"[Ver más detalles]({project['link']})")
                if st.button(f"Explorar {project['title']}", key=f"explore_{i}"):
                    st.info(f"Redirigiendo a {project['title']} - [Link Simulado]({project['link']})")
            
            st.markdown("---")
            
            # Widgets interactivos adicionales dentro de cada proyecto
            st.markdown("### Califica este proyecto:")
            rating = st.radio("¿Qué tan interesante es este proyecto?",
                              options=["Excelente", "Bueno", "Regular", "Malo"], key=f"rating_{i}")
            st.write(f"Calificación seleccionada: **{rating}**")
            
            st.markdown("### Progreso del Proyecto:")
            progress_val = random.randint(0, 100)
            st.progress(progress_val)
            
            st.markdown("### Comentarios:")
            comment = st.text_area("Deja tu comentario aquí:", key=f"comment_{i}")
            if st.button("Enviar comentario", key=f"send_comment_{i}"):
                if comment.strip():
                    st.success("¡Gracias por tu comentario!")
                else:
                    st.error("Por favor, escribe un comentario antes de enviarlo.")
            st.markdown("---")
    
    # Sección adicional: análisis interactivo y visualización de datos
    st.markdown("## Análisis Interactivo de Proyectos")
    st.markdown("Visualiza datos resumidos de los proyectos de la categoría seleccionada.")
    
    # Crear un DataFrame simulando análisis: longitud de los títulos de los proyectos
    project_titles = [proj["title"] for proj in selected_projects]
    df_projects = pd.DataFrame({
        "Proyecto": project_titles,
        "Longitud del Título": [len(title) for title in project_titles],
        "Índice": list(range(1, len(project_titles) + 1))
    })
    
    st.dataframe(df_projects)
    
    # Selección del tipo de gráfico a visualizar
    chart_type = st.selectbox("Selecciona el tipo de gráfico:", ["Línea", "Barras"], key="chart_type")
    
    st.markdown("### Gráfico: Longitud del Título de Proyectos")
    if chart_type == "Línea":
        st.line_chart(df_projects.set_index("Índice")["Longitud del Título"])
    else:
        st.bar_chart(df_projects.set_index("Índice")["Longitud del Título"])
    
    st.markdown("---")
    
    # Sección para ver detalles específicos de un proyecto seleccionado
    st.markdown("## Detalle Específico del Proyecto")
    project_options = {proj["title"]: proj for proj in selected_projects}
    selected_project_title = st.selectbox("Selecciona un proyecto para ver más detalles:", list(project_options.keys()), key="detail_select")
    selected_project = project_options[selected_project_title]
    
    st.subheader(f"Detalle del Proyecto: {selected_project['title']}")
    st.image(selected_project["image"], caption=selected_project["title"], width=300)
    st.write(selected_project["description"])
    st.markdown(f"[Acceder a la página del proyecto]({selected_project['link']})")
    
    # Widget interactivo: contador de likes para el proyecto seleccionado
    st.markdown("### Likes del Proyecto")
    if "like_count" not in st.session_state:
        st.session_state["like_count"] = {}
    if selected_project_title not in st.session_state["like_count"]:
        st.session_state["like_count"][selected_project_title] = 0
    if st.button("¡Me gusta!", key="like_btn"):
        st.session_state["like_count"][selected_project_title] += 1
    st.write(f"Total de likes: {st.session_state['like_count'][selected_project_title]}")
    
    st.markdown("---")
    
    # Encuesta interactiva sobre preferencias en proyectos
    st.markdown("## Encuesta Rápida")
    survey_choice = st.radio("¿Cuál es la característica más importante en un proyecto?", 
                             options=["Innovación", "Eficiencia", "Diseño", "Impacto"], key="survey")
    st.write(f"Has seleccionado: **{survey_choice}** como la característica más importante.")
    
    st.markdown("---")
    
    # Simulación de una animación: mensajes de actualización progresiva
    st.markdown("### Actualización en Progreso")
    anim_placeholder = st.empty()
    for j in range(3):
        anim_placeholder.info(f"Actualizando detalles... ({j+1}/3)")
        time.sleep(0.5)
    anim_placeholder.success("¡Actualización completada!")

st.markdown("### [Parte 2 de 3 cargada]")
# Parte 3: Funcionalidades adicionales, sección de contacto, descargas y estadísticas avanzadas

st.markdown("## Funcionalidades Adicionales y Sección de Contacto")
st.markdown("Explora secciones adicionales que enriquecen la experiencia del portafolio, incluyendo información sobre mí, formas de contacto, descarga del portafolio y análisis avanzado de datos.")

# Selector para elegir entre diferentes secciones adicionales
additional_section = st.radio("Selecciona una sección adicional:", 
                                ["Acerca de", "Contacto", "Descargar Portafolio", "Estadísticas Avanzadas"],
                                key="additional_section")

if additional_section == "Acerca de":
    st.markdown("### Acerca de Mí")
    st.write("Soy un consultor con amplia experiencia en transformación digital, ciencia de datos, desarrollo web y estrategias financieras. Mi misión es impulsar la innovación en cada proyecto y ofrecer soluciones que marquen la diferencia.")
    st.image("/home/nichi/Imágenes/tecoo.png", caption="Mi Imagen Profesional", use_container_width=True)
    st.write("Con un enfoque en resultados y una pasión por la tecnología, me dedico a ayudar a empresas a adaptarse y prosperar en un entorno digital en constante cambio.")
    # Testimonio dinámico simulado
    testimonial = random.choice([
        "¡Excelente profesional, muy innovador!",
        "Su enfoque es realmente transformador.",
        "Gran capacidad para resolver problemas complejos.",
        "Su visión digital ha revolucionado nuestra operación."
    ])
    st.markdown(f"**Testimonio Destacado:** *{testimonial}*")

elif additional_section == "Contacto":
    st.markdown("### Contáctame")
    st.write("Si deseas comunicarte, por favor completa el siguiente formulario y me pondré en contacto contigo a la brevedad.")
    with st.form(key="contact_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Nombre:")
        with col2:
            email = st.text_input("Correo Electrónico:")
        message = st.text_area("Mensaje:")
        submit_contact = st.form_submit_button("Enviar Mensaje")
        if submit_contact:
            if name.strip() and email.strip() and message.strip():
                st.success("¡Gracias por tu mensaje! Me pondré en contacto contigo muy pronto.")
            else:
                st.error("Por favor, completa todos los campos antes de enviar.")

elif additional_section == "Descargar Portafolio":
    st.markdown("### Descargar Portafolio")
    st.write("Descarga una versión en PDF de mi portafolio completo para revisarlo sin conexión.")
    # Simulación del contenido PDF del portafolio
    portfolio_pdf_content = (
        "Este documento PDF contiene una recopilación detallada de proyectos de transformación digital, "
        "análisis de datos, desarrollo web y estrategias de negocio. "
        "Incluye descripciones, resultados y testimonios que reflejan mi experiencia en consultoría."
    )
    st.download_button("Descargar Portafolio en PDF", 
                       data=portfolio_pdf_content, 
                       file_name="portafolio_consultoria.pdf", 
                       mime="application/pdf")

elif additional_section == "Estadísticas Avanzadas":
    st.markdown("### Estadísticas Avanzadas")
    st.write("Revisa estadísticas simuladas de los proyectos del portafolio para obtener una visión global de la actividad y tendencias.")
    # Crear un DataFrame simulando estadísticas avanzadas
    advanced_stats = pd.DataFrame({
        "Categoría": list(portfolio.keys()),
        "Proyectos": [len(portfolio[cat]) for cat in portfolio.keys()],
        "Impacto (Simulado)": np.random.randint(50, 100, size=len(portfolio))
    })
    st.dataframe(advanced_stats)
    st.markdown("### Gráfico: Número de Proyectos por Categoría")
    # Usar Altair para gráficos avanzados
    import altair as alt
    chart = alt.Chart(advanced_stats).mark_bar().encode(
        x=alt.X("Categoría:N", title="Categoría"),
        y=alt.Y("Proyectos:Q", title="Número de Proyectos"),
        color=alt.Color("Categoría:N")
    ).properties(width=600, height=400)
    st.altair_chart(chart, use_container_width=True)

# Sección de Redes Sociales y Conexión
st.markdown("---")
st.markdown("### Conéctate Conmigo")
st.write("Encuéntrame en mis redes sociales para conocer más sobre mis proyectos y actividades:")
st.markdown("[LinkedIn](https://www.linkedin.com) | [GitHub](https://github.com) | [Twitter](https://twitter.com)")

# Información de la Sesión y Datos del Portafolio
st.markdown("---")
total_projects = sum(len(proyectos) for proyectos in portfolio.values())
st.write(f"**Total de Proyectos en el Portafolio:** {total_projects}")
st.write("**Fecha y Hora de Acceso:**", time.strftime("%Y-%m-%d %H:%M:%S"))

# Mensaje final con widget interactivo y selección aleatoria de despedida
st.markdown("### Mensaje Final")
farewell_options = [
    "¡Gracias por visitar mi portafolio, hasta la próxima!",
    "¡Espero que disfrutes explorando mis proyectos!",
    "¡Vuelve pronto para más innovaciones!",
    "¡Que tengas un excelente día!"
]
selected_farewell = random.choice(farewell_options)
st.write(selected_farewell)

# Widget interactivo adicional: encuesta rápida para mejorar la experiencia del usuario
st.markdown("### ¿Cómo calificarías tu experiencia en este portafolio?")
experience_rating = st.slider("Califica de 1 (malo) a 10 (excelente):", min_value=1, max_value=10, value=7, step=1)
st.write(f"Tu calificación: **{experience_rating}**")
if experience_rating >= 8:
    st.balloons()

# Información adicional sobre la sesión y estado de los likes acumulados
st.markdown("### Resumen de la Sesión")
if "like_count" in st.session_state:
    total_likes = sum(st.session_state["like_count"].values())
else:
    total_likes = 0
st.write(f"**Total de Likes Acumulados en la Sesión:** {total_likes}")

st.markdown("### [Parte 3 de 3 cargada]")
