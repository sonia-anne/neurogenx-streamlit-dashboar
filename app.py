import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="NEUROGEN-X Dashboard", layout="wide", page_icon="🧬")

st.title("NEUROGEN-X: Revolutionizing the Cure for CJD")

st.markdown("""
#### **Nanorobot Description**
A revolutionary treatment for Creutzfeldt-Jakob Disease.  
NEUROGEN-X is a 50-nanometer programmable nanorobot designed with:
- **Gold-Platinum alloy body** (invisible to the immune system)
- **Peptidomimetic coating** to simulate human proteins
- **CRISPR-Cas13d** enzymes to destroy prions
- **Reservoirs of BDNF/NGF** to regenerate neurons
- **AI-guided molecular GPS** for precise targeting
- **Autodestruct system** after 72h with 0% toxicity
""")

# Tamaño
st.header("Size Comparison of NEUROGEN-X Nanobot")
size_data = pd.DataFrame({
    'Object': ['Human Hair', 'Red Blood Cell', 'Virus', 'NEUROGEN-X'],
    'Size (nm)': [80000, 7000, 100, 50]
})
fig1 = px.bar(size_data, x='Object', y='Size (nm)', color='Object', text='Size (nm)',
              title="Relative Size of NEUROGEN-X Nanobot")
st.plotly_chart(fig1, use_container_width=True)

# Fases del tratamiento
st.header("NEUROGEN-X Treatment Phases")
phases = {
    "1. Injection": "Injected intravenously. Millions of nanobots travel with blood.",
    "2. Navigation": "AI system finds misfolded prions using 3D protein structure recognition.",
    "3. Degradation": "CRISPR-Cas13d enzymes cut prions with 94% accuracy.",
    "4. Regeneration": "BDNF/NGF molecules and nanoscaffolds restore damaged brain circuits.",
    "5. Autodestruction": "Nanobot detects neutral pH and safely dissolves in cerebrospinal fluid."
}
for k, v in phases.items():
    st.markdown(f"**{k}**: {v}")

# Comparativa
st.header("Comparison with Other Therapies")
data = pd.DataFrame({
    'Therapy': ['NEUROGEN-X', 'Gene Therapy (NIH)', 'Gold Nanoparticles (MIT)', 'Quinacrine'],
    'Efficacy (%)': [94, 70, 48, 0],
    'Cost (USD)': [8000, 1200000, 150000, 300],
    'Issue': ['None', 'No regeneration', 'Immune reaction', 'Toxic to liver']
})
fig2 = px.scatter(data, x='Cost (USD)', y='Efficacy (%)', color='Therapy',
                  size='Efficacy (%)', hover_name='Issue',
                  title="Efficacy vs Cost of Neurological Therapies")
st.plotly_chart(fig2, use_container_width=True)

st.success("NEUROGEN-X unites nanotech, AI, and bioengineering to deliver a complete cure.")
