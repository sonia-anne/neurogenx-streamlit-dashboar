import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="NEUROGEN-X Dashboard", layout="wide")

# TÍTULO
st.markdown("<h1 style='color:#00FFFF;text-align:center;'>NEUROGEN-X: Revolutionizing Prion Disease Treatment</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>A futuristic biomedical innovation against Creutzfeldt-Jakob Disease (CJD)</h4>", unsafe_allow_html=True)
st.markdown("---")

# SECCIÓN: COMPONENTES DEL NANOROBOT
st.subheader("Nanobot Composition and Specifications")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### Materials & Structure")
    st.markdown("""
    - **Structure**: Truncated icosahedron (like a soccer ball)
    - **Material**: Gold-Platinum alloy core, mimetic peptide coating
    - **Functional Compartments**:
        - CRISPR-Cas13d enzymes (red spheres)
        - BDNF/NGF neuroregenerative factors (green microcapsules)
        - AI-controlled quantum CPU (cyan luminous cube)
    - **Sensors**: Molecular GPS (purple blinking nodes)
    - **Release Pores**: 2nm openings in pentagonal faces
    """)

with col2:
    st.markdown("### Size and Delivery")
    st.markdown("""
    - **Size**: 50 nanometers (smaller than most viruses)
    - **Comparison**:
        - Red Blood Cell: 7,000 nm
        - Virus: 100 nm
        - NEUROGEN-X: 50 nm
    - **Injection**: Intravenous delivery with transferrin ligands
    - **Mechanism**: Mimetic camouflage to bypass immune detection
    """)

st.markdown("---")

# COMPARATIVA DE TAMAÑOS
st.subheader("Size Comparison: Why NEUROGEN-X Reaches Where Others Can't")
size_data = pd.DataFrame({
    "Element": ["Red Blood Cell", "Typical Virus", "NEUROGEN-X Nanobot"],
    "Size (nm)": [7000, 100, 50]
})
fig_size = px.bar(size_data, x="Element", y="Size (nm)", color="Element",
                  color_discrete_sequence=["red", "orange", "cyan"],
                  title="Relative Sizes in Nanometers")
st.plotly_chart(fig_size, use_container_width=True)

# MECANISMO DE ACCIÓN
st.subheader("Mechanism of Action: Step-by-Step Simulation")

steps = ["Injection", "Bloodstream Navigation", "BBB Penetration", "Prion Detection", 
         "CRISPR Activation", "Prion Degradation", "Regeneration Scaffold Release", 
         "BDNF/NGF Diffusion", "Synaptic Repair", "Autodestruction"]
completion = [10, 20, 30, 45, 55, 65, 75, 85, 95, 100]

fig_steps = go.Figure(data=[go.Scatter(x=steps, y=completion, mode='lines+markers',
                                       line=dict(color="cyan", width=4),
                                       marker=dict(size=12, color="purple"))])
fig_steps.update_layout(title="NEUROGEN-X Journey Through the Body",
                        xaxis_title="Phase",
                        yaxis_title="% Completion",
                        template="plotly_dark")
st.plotly_chart(fig_steps, use_container_width=True)

# COMPARADOR DE EFICACIA
st.subheader("Efficacy Comparison Against Other Treatments")
comparison_df = pd.DataFrame({
    "Treatment": ["NEUROGEN-X", "MIT Gold Nanoparticles", "NIH ASO", "Quinacrine"],
    "Efficacy (%)": [94, 48, 70, 0],
    "Toxicity": ["Low", "High (accumulation)", "Moderate", "High (hepatic)"],
    "Cost (USD)": [8000, 50000, 1200000, 12000]
})
fig_efficacy = px.bar(comparison_df, x="Treatment", y="Efficacy (%)", color="Treatment",
                      color_discrete_sequence=["cyan", "goldenrod", "lightblue", "gray"],
                      title="Degradation Efficacy Comparison")
st.plotly_chart(fig_efficacy, use_container_width=True)

# PIE CHART - FUNCIONES
st.subheader("Strategic Advantages of NEUROGEN-X")
fig_pie = px.pie(values=[25, 25, 25, 25], names=["Precision CRISPR Cutting", 
                                                  "Targeted Brain Delivery", 
                                                  "Tissue Regeneration", 
                                                  "Safe Autodestruction"],
                 title="Balanced Biomedical Functions",
                 color_discrete_sequence=px.colors.sequential.Tealgrn)
st.plotly_chart(fig_pie, use_container_width=True)

# FOOTER
st.markdown("---")
st.markdown("<p style='text-align:center;'>Developed with cutting-edge bioengineering, artificial intelligence and compassion from Ecuador to the world.</p>", unsafe_allow_html=True)