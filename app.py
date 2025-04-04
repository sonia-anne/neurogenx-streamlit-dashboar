import streamlit as st
from PIL import Image
import base64

# --- CONFIGURACIÓN INICIAL ---
st.set_page_config(page_title="NEUROGEN-X | Cure ECJ", layout="wide")

# --- FONDO PERSONALIZADO ---
def set_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        base64_img = base64.b64encode(f.read()).decode()
    css_code = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{base64_img}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """
    st.markdown(css_code, unsafe_allow_html=True)

set_bg_from_local("assets/dna_background.jpg")

# --- TÍTULO ---
st.markdown("<h1 style='color: cyan; text-align: center;'>NEUROGEN-X: The Cure for Creutzfeldt-Jakob</h1>", unsafe_allow_html=True)
st.markdown("---")

# --- TARJETAS DE FUNCIÓN ---
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### 🧬 Molecular GPS")
    st.info("Detects prions using AI-driven 3D protein scans.")
with col2:
    st.markdown("### ✂️ CRISPR-Cas13d")
    st.info("Cuts prions with 94% precision using RNA-guided enzymes.")
with col3:
    st.markdown("### 🌱 Brain Regeneration")
    st.info("Rebuilds neurons using BDNF and nanofiber scaffolds.")

# --- IMAGEN PRINCIPAL (INFOGRAFÍA DE FASES) ---
st.markdown("### **Complete Action Cycle**")
img1 = Image.open("assets/neurogenx_infographic.png")
st.image(img1, use_column_width=True)

# --- SLIDER INTERACTIVO: Comparador de Tratamientos ---
st.markdown("### **Compare NEUROGEN-X vs. Previous Treatments**")
option = st.slider("Slide to compare", 0, 2, 0,
                   format="%d", help="0: MIT, 1: NIH, 2: NEUROGEN-X")

if option == 0:
    st.warning("MIT: Nanoparticles failed due to immune response and liver accumulation.")
elif option == 1:
    st.info("NIH: ASOs only prevent prions but do not regenerate tissue.")
else:
    st.success("NEUROGEN-X: Degrades prions, regenerates neurons, auto-destructs safely.")

# --- ANIMACIÓN PASO A PASO (Texto) ---
with st.expander("🧠 Mecanism of Action - Step by Step"):
    st.markdown("""
    **1. Injection:** Delivered intravenously inside blue lipid solution.
    **2. Navigation:** Crosses BBB using transferrin ligands.
    **3. Detection:** Scans prions via AI-based molecular GPS.
    **4. Attack:** CRISPR-Cas13d cuts prions into safe fragments.
    **5. Regeneration:** Releases BDNF/NGF + nanofibers for neuron growth.
    **6. Autodestruction:** 72h later, dissolves into amino acids.
    """)

# --- IMAGEN DEL NANORROBOT ---
st.markdown("### **Nanorobot Design**")
img2 = Image.open("assets/nanorobot_models.png")
st.image(img2, caption="NEUROGEN-X: Icosahedron-shaped nanobot (50 nm)", use_column_width=True)

# --- DIAGRAMA COMPARATIVO ---
with st.expander("📊 Comparative Table"):
    st.markdown("""
    | Treatment            | Year | Efficacy | Problems                     | NEUROGEN-X Solves It By...                 |
    |----------------------|------|----------|------------------------------|--------------------------------------------|
    | **Quinacrine**       | 2012 | 0%       | Liver toxicity               | Biodegradable materials only               |
    | **MIT Nanoparticles**| 2024 | 48%      | Organ accumulation           | Auto-destruction in 72h                    |
    | **NIH ASOs**         | 2023 | 70%      | No regeneration, only prevention | Dual function: degradation + repair   |
    """)

# --- FOOTER ---
st.markdown("---")
st.markdown("<small style='color: lightgray;'>Created by a young scientist from Ecuador – NEUROGEN-X is the future of neurodegeneration treatment.</small>", unsafe_allow_html=True)
