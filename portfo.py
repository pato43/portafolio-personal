# app.py
# Portafolio Profesional — Dark Edition
# Autor: (tu nombre)
# Stack: Streamlit (dark), Altair para gráficos, animación "typing" en insights de proyectos.

import streamlit as st
import pandas as pd
import altair as alt
import time
from pathlib import Path

# =========================
# CONFIGURACIÓN GLOBAL
# =========================
st.set_page_config(
    page_title="Portafolio de Alexander Rojas Garay",
    layout="wide",
    page_icon="🧠",
    initial_sidebar_state="expanded"
)

# =========================
# TEMA / ESTILOS (Dark + Neon)
# =========================
PRIMARY = "#7C3AED"   # Morado
ACCENT  = "#22D3EE"   # Cian
ACCENT2 = "#6EE7F9"   # Cian claro
BG      = "#0B1220"   # Fondo
CARD    = "#11182A"   # Cards
TEXT    = "#EAF2FF"   # Texto principal
MUTED   = "#9EB0CC"

st.markdown(f"""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800;900&display=swap" rel="stylesheet">
<style>
:root {{
  --bg: {BG};
  --card: {CARD};
  --text: {TEXT};
  --muted: {MUTED};
  --primary: {PRIMARY};
  --accent: {ACCENT};
  --accent2: {ACCENT2};
}}
html, body, [class*="css"] {{
  background: var(--bg) !important;
  color: var(--text) !important;
  font-family: 'Inter', system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif;
  font-size: 17px;
}}
.block-container {{ padding-top: 0.5rem; }}
header {{ visibility: hidden; }}
/* HERO */
.hero {{
  display:flex; align-items:center; gap:14px; flex-wrap:wrap;
  padding: 16px 14px; border-radius: 16px;
  background: linear-gradient(135deg, rgba(124,58,237,.15), rgba(34,211,238,.08));
  border: 1px solid rgba(255,255,255,.06);
}}
.hero-title {{ font-size: 1.6rem; font-weight: 900; letter-spacing: .2px; }}
.hero-sub   {{ color: var(--muted); font-weight: 600; }}
.badge {{
  font-size:.8rem; font-weight:800; padding:4px 10px; border-radius:999px; color:#03111A;
  background: linear-gradient(135deg, var(--primary), var(--accent));
}}
/* Tarjetas */
.card {{
  background: var(--card);
  border: 1px solid rgba(255,255,255,.06);
  border-radius: 14px;
  padding: 14px 16px;
}}
.kpi {{
  background: var(--card);
  border: 1px solid rgba(255,255,255,.06);
  border-radius: 16px;
  padding: 16px 18px;
}}
.kpi .kpi-title {{ font-size:.85rem; color: var(--muted); font-weight: 700; }}
.kpi .kpi-value {{ font-size:1.5rem; font-weight: 900; }}
.pill {{
  display:inline-block; padding:6px 12px; border-radius:999px; font-size:.85rem; font-weight:800;
  background: var(--accent); color:#02141A; margin:0 8px 8px 0;
}}
h1, h2, h3, h4 {{ color: var(--text) !important; }}
hr.section {{
  border:none; height:1px;
  background:linear-gradient(90deg, var(--accent), var(--accent2));
  margin:8px 0 16px;
}}
/* Inputs oscuros */
.stTextInput > div > div > input, .stTextArea textarea {{
  background:#0F172A !important; color:var(--text) !important;
  border:1px solid #1E2A44 !important; border-radius:10px; font-size:16px;
}}
.stSelectbox div[data-baseweb="select"] > div {{
  background:#0F172A !important; border:1px solid #1E2A44 !important; border-radius:10px;
}}
.stButton > button {{
  background: var(--primary); color: #fff; font-weight: 900; border: none;
  border-radius: 10px; font-size: 16px; padding: .5rem 1rem;
}}
.small {{ font-size: .9rem; color: var(--muted); }}
.explain {{
  margin-top:10px; border-left: 3px solid var(--accent);
  padding:10px 12px; background: #0E1A2C; border-radius: 10px;
}}
</style>
""", unsafe_allow_html=True)

# =========================
# DATOS BASE (edita libremente)
# =========================
PROFILE = {
    "name": "Alexander Eduardo Rojas Garay",
    "title": "Científico de Datos & Consultor IA",
    "tagline": "IA aplicada, analítica y automatización para acelerar decisiones y operación.",
    "location": "CDMX / Remoto",
    "email": "rojasalexander10@gmail.com",
    "phone": "+52 722 559 7963",
    "links": {
        "LinkedIn": "https://linkedin.com/in/alexander-eduardo-rojas-garay-b17471235",
        "GitHub": "https://github.com/",
        "Portafolio": "https://portafolio-personal-v1-es.streamlit.app/"
    },
    "summary": "Experto en AI/ML, ciencia de datos y automatización. Diseño agentes inteligentes que conectan datos, procesos y comunicación para entregar insights accionables y resultados medibles."
}

KPI_CARDS = [
    {"title": "Alumnos formados", "value": "+150"},
    {"title": "Eficiencia ERP (Holtmont)", "value": "+25%"},
    {"title": "Ahorro anual (migr. BI)", "value": "15,000 USD"},
    {"title": "Mejora precisión ML", "value": "+40%"},
]

# Proyectos (agrega/edita; image puede ser URL o ruta local)
PROJECTS = [
    {
        "title": "Agentes ADK + MCP + LLM (Enterprise Ops)",
        "about": "Entorno de trabajo unificado con agentes ADK, MCPs abiertos y LLM (Gemini) para agenda, inventarios, mensajería y análisis visual en tiempo real.",
        "impact": "Coordinación cross-funcional en un solo flujo, insights por gráfico y acciones sobre Jira, Slack, WhatsApp y Calendar.",
        "tech": ["Streamlit", "Plotly/Altair", "Postgres/SQL Server/Spark", "Jira API", "Slack API", "WhatsApp templates"],
        "tags": ["IA Aplicada", "Operaciones", "BI Conversacional"],
        "link": "https://example.com/agentes_adk_mcp_llm",
        "image": ""
    },
    {
        "title": "TESSENA IA — Plataforma Médica",
        "about": "Consulta de 65k+ medicamentos desde COFEPRIS/FDA/OpenDrugs; historias clínicas y mensajería omnicanal.",
        "impact": "Atención rápida con contexto clínico y trazabilidad.",
        "tech": ["LangChain", "Supabase", "Twilio", "Reflex"],
        "tags": ["Salud", "NLP", "Integraciones"],
        "link": "https://example.com/tessena",
        "image": ""
    },
    {
        "title": "Forecast de Ventas — Central de Abasto",
        "about": "Modelos de series de tiempo para anticipar demanda y planear compras.",
        "impact": "Reducción de quiebres ~20% y mejor rotación.",
        "tech": ["Python", "Prophet", "Taipy"],
        "tags": ["Time Series", "Retail", "Forecast"],
        "link": "https://example.com/forecast_ceda",
        "image": ""
    },
    {
        "title": "E-commerce Mercado Xochiquetzal",
        "about": "Marketplace multivendedor con pagos y control de inventario.",
        "impact": "Ventas online +25%, nuevos canales para locatarios.",
        "tech": ["Django", "React", "Stripe"],
        "tags": ["E-commerce", "Pagos", "Full-stack"],
        "link": "https://example.com/mercado_xqz",
        "image": ""
    },
    {
        "title": "Automatización Holtmont México",
        "about": "Apps Script + Sheets para distribución de tareas, reporteo y notificaciones.",
        "impact": "−40% tiempos admvos, +trazabilidad.",
        "tech": ["Google Apps Script", "Sheets", "Drive"],
        "tags": ["RPA", "Back-office"],
        "link": "https://example.com/holtmont",
        "image": ""
    },
]

EXPERIENCE = [
    {
        "role": "Consultor Independiente — Científico de Datos & Arquitecto IA",
        "when": "2023 — Presente",
        "bullets": [
            "Diseño de agentes y analítica aplicada (retail, salud, finanzas).",
            "Migración de dashboards a apps interactivas (Streamlit) con ahorro OPEX.",
            "Integraciones: Jira, Slack, WhatsApp, Google Workspace."
        ]
    },
    {
        "role": "Científico de Datos — Instituto de Matemáticas, UNAM",
        "when": "2022 — 2023",
        "bullets": [
            "Modelado estadístico y computación científica.",
            "Prototipos ML para análisis de series y clasificación."
        ]
    },
    {
        "role": "Machine Learning Engineer — Colmena Space / AAE UNAM",
        "when": "2019 — 2021",
        "bullets": [
            "Procesamiento de señales e imágenes.",
            "Mejoras de precisión ML para misión experimental."
        ]
    }
]

CERTS = [
    "Microsoft: Data Scientist, Data Analyst, Azure, SQL",
    "Google: IA aplicada, GCP para Ciencia de Datos",
    "UNAM: Data-Driven Astronomy",
    "LPIC-1: Linux Professional",
    "Santander: Python y Análisis Empresarial"
]

PUBS = [
    "El Nobel de Física 2024 y las Redes Neuronales — ensayo de divulgación sobre IA/Física moderna."
]

SKILLS = {
    "IA/ML": ["Python", "Scikit-learn", "Prophet", "LangChain"],
    "Datos": ["SQL (Postgres/SQL Server)", "Spark (PySpark)", "ETL/ELT"],
    "Apps": ["Streamlit", "Django", "React (básico)"],
    "Cloud": ["GCP", "Azure", "Supabase"],
    "Integraciones": ["Jira", "Slack", "WhatsApp", "Google Workspace"]
}

# =========================
# UTILIDADES
# =========================
def safe_image(path_or_url: str, **kwargs):
    if not path_or_url:
        return
    try:
        if str(path_or_url).startswith(("http://", "https://")):
            st.image(path_or_url, **kwargs)
        else:
            p = Path(path_or_url)
            if p.exists():
                st.image(str(p), **kwargs)
    except Exception:
        pass

def typing(md: str, speed: float = 0.01):
    """Animación estilo 'typing' para insights. Desactivar en sidebar si se requiere."""
    if not st.session_state.get("animate_insights", True):
        st.markdown(md, unsafe_allow_html=True)
        return
    box = st.empty()
    acc = ""
    for ch in md:
        acc += ch
        box.markdown(acc, unsafe_allow_html=True)
        time.sleep(speed)

# =========================
# HERO
# =========================
hero_l, hero_r = st.columns([2.7, 1.3], gap="large")
with hero_l:
    st.markdown(
        f"""
        <div class="hero">
          <div class="badge">Portafolio</div>
          <div class="hero-title">{PROFILE['name']}</div>
          <div class="hero-sub">{PROFILE['title']} • {PROFILE['location']}</div>
          <div class="small">{PROFILE['tagline']}</div>
        </div>
        """, unsafe_allow_html=True
    )
with hero_r:
    st.markdown(
        f"""
        <div class="card">
          <div style="font-weight:900;">Contacto</div>
          <div class="small">✉️ {PROFILE['email']}</div>
          <div class="small">📱 {PROFILE['phone']}</div>
          <div style="margin-top:6px;">
            <a href="{PROFILE['links']['LinkedIn']}" target="_blank">LinkedIn</a> •
            <a href="{PROFILE['links']['GitHub']}" target="_blank">GitHub</a> •
            <a href="{PROFILE['links']['Portafolio']}" target="_blank">Web</a>
          </div>
        </div>
        """, unsafe_allow_html=True
    )

st.markdown('<hr class="section"/>', unsafe_allow_html=True)

# =========================
# KPI STRIP
# =========================
k1, k2, k3, k4 = st.columns(4, gap="large")
for col, k in zip([k1, k2, k3, k4], KPI_CARDS):
    with col:
        st.markdown(
            f"""
            <div class="kpi">
              <div class="kpi-title">{k["title"]}</div>
              <div class="kpi-value">{k["value"]}</div>
            </div>
            """, unsafe_allow_html=True
        )

# =========================
# SIDEBAR (Navegación + opciones)
# =========================
st.sidebar.markdown("### Navegación")
section = st.sidebar.radio("", ["Proyectos", "Experiencia", "Certificaciones", "Publicaciones", "Habilidades", "Contacto"], index=0)

st.sidebar.markdown("---")
st.sidebar.markdown("### Opciones")
st.session_state["animate_insights"] = st.sidebar.toggle("Animar insights", value=True)
search = st.sidebar.text_input("Buscar proyecto")
tag_filter = st.sidebar.multiselect("Filtrar por tag", sorted({t for p in PROJECTS for t in p["tags"]}))

# =========================
# PROYECTOS
# =========================
if section == "Proyectos":
    st.subheader("🚀 Proyectos Destacados")
    st.caption(PROFILE["summary"])

    # Filtros
    projects_view = PROJECTS.copy()
    if search:
        s = search.strip().lower()
        projects_view = [p for p in projects_view if s in p["title"].lower() or s in p["about"].lower()]
    if tag_filter:
        projects_view = [p for p in projects_view if any(t in tag_filter for t in p["tags"])]

    if not projects_view:
        st.info("No hay proyectos con esos filtros.")
    else:
        for p in projects_view:
            card_l, card_r = st.columns([1.3, 2.7], gap="large")
            with card_l:
                st.markdown(f"<div class='card'><div style='font-weight:900;font-size:1.1rem;'>{p['title']}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='small' style='margin-top:4px;'>{' • '.join(p['tags'])}</div>", unsafe_allow_html=True)
                safe_image(p.get("image",""), use_container_width=True)
                st.markdown("</div>", unsafe_allow_html=True)
            with card_r:
                st.markdown(f"<div class='card'><b>Descripción</b><br>{p['about']}<br><br><b>Impacto</b><br>{p['impact']}<br><br><b>Tecnologías</b><br>{', '.join(p['tech'])}<br><br><a href='{p['link']}' target='_blank'>Ver más</a></div>", unsafe_allow_html=True)
                # Insight del “agente”
                st.markdown("<div class='card explain'><b>🧠 Explicación del LLM</b><br>", unsafe_allow_html=True)
                typing(f"Este proyecto prioriza entregables con métricas claras. Las integraciones y el pipeline de datos permiten decisiones rápidas con mínimo cambio de contexto. ")
                st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<hr class="section"/>', unsafe_allow_html=True)

        # Pequeña analítica del portafolio (tags más usados)
        st.subheader("📊 Analítica del Portafolio")
        tag_rows = []
        for p in projects_view:
            for t in p["tags"]:
                tag_rows.append({"Tag": t, "Proyecto": p["title"]})
        if tag_rows:
            df_tags = pd.DataFrame(tag_rows)
            tag_counts = df_tags.groupby("Tag").agg(Proyectos=("Proyecto","nunique")).reset_index()
            chart = alt.Chart(tag_counts).mark_bar().encode(
                x=alt.X("Tag:N", sort='-y'),
                y=alt.Y("Proyectos:Q"),
                tooltip=["Tag","Proyectos"]
            ).properties(height=280)
            st.altair_chart(chart, use_container_width=True)

# =========================
# EXPERIENCIA
# =========================
elif section == "Experiencia":
    st.subheader("💼 Experiencia Profesional")
    for e in EXPERIENCE:
        st.markdown(f"<div class='card'><b>{e['role']}</b><br><span class='small'>{e['when']}</span><ul>", unsafe_allow_html=True)
        for b in e["bullets"]:
            st.markdown(f"<li>{b}</li>", unsafe_allow_html=True)
        st.markdown("</ul></div>", unsafe_allow_html=True)

# =========================
# CERTIFICACIONES
# =========================
elif section == "Certificaciones":
    st.subheader("📜 Certificaciones")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    for c in CERTS:
        st.markdown(f"• {c}")
    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# PUBLICACIONES
# =========================
elif section == "Publicaciones":
    st.subheader("📰 Publicaciones")
    for p in PUBS:
        st.markdown(f"<div class='card'>{p}</div>", unsafe_allow_html=True)

# =========================
# HABILIDADES
# =========================
elif section == "Habilidades":
    st.subheader("🛠️ Habilidades")
    cols = st.columns(3, gap="large")
    buckets = list(SKills:=SKILLS.items())
    for i, col in enumerate(cols):
        if i < len(buckets):
            cat, items = buckets[i]
            with col:
                st.markdown(f"<div class='card'><b>{cat}</b><br>", unsafe_allow_html=True)
                st.markdown("".join([f"<span class='pill'>{x}</span>" for x in items]), unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
    # Si quedan categorías, muéstralas abajo
    if len(buckets) > 3:
        left, right = st.columns(2, gap="large")
        for j, (cat, items) in enumerate(buckets[3:]):
            with (left if j % 2 == 0 else right):
                st.markdown(f"<div class='card'><b>{cat}</b><br>", unsafe_allow_html=True)
                st.markdown("".join([f"<span class='pill'>{x}</span>" for x in items]), unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

# =========================
# CONTACTO
# =========================
elif section == "Contacto":
    st.subheader("📬 Contacto")
    st.markdown(f"<div class='card'>Estoy disponible para colaboraciones, consultoría y proyectos de IA/Datos. Escríbeme a <b>{PROFILE['email']}</b> o agenda una llamada.</div>", unsafe_allow_html=True)

    with st.form("contacto_form"):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Nombre")
        with c2:
            email = st.text_input("Correo")
        message = st.text_area("Mensaje")
        sent = st.form_submit_button("Enviar")
        if sent:
            if name.strip() and email.strip() and message.strip():
                st.success("¡Gracias! Me pondré en contacto muy pronto.")
            else:
                st.error("Completa todos los campos, por favor.")

    st.markdown('<hr class="section"/>', unsafe_allow_html=True)
    st.markdown(f"[LinkedIn]({PROFILE['links']['LinkedIn']})  •  [GitHub]({PROFILE['links']['GitHub']})  •  [Web]({PROFILE['links']['Portafolio']})")

