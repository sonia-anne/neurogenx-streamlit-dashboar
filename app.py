import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# CONFIGURACIÓN
st.set_page_config(page_title="NEUROGEN-X Interactive Dashboard", layout="wide")

# TÍTULO PRINCIPAL
st.markdown("<h1 style='text-align:center; color:#06b6d4;'>NEUROGEN-X: The Nanobot That Cures CJD</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color:#94a3b8;'>A fully interactive and scientific dashboard that visualizes the revolution of neuro-nanomedicine</h4>", unsafe_allow_html=True)
st.markdown("---")

# MÉTRICAS
col1, col2, col3 = st.columns(3)
col1.metric(label="Size", value="50 nm", delta="Smaller than virus")
col2.metric(label="Efficacy", value="94%", delta="Best result")
col3.metric(label="Degradation", value="72 hours", delta="No residue")

# COMPARACIÓN DE TAMAÑOS
st.subheader("How Small is NEUROGEN-X?")
size_df = pd.DataFrame({
    "Structure": ["Red Blood Cell", "Typical Virus", "NEUROGEN-X"],
    "Size (nm)": [7000, 100, 50]
})
fig_bar = px.bar(size_df, x="Structure", y="Size (nm)", color="Structure",
                 color_discrete_sequence=["red", "orange", "cyan"],
                 text="Size (nm)")
fig_bar.update_traces(textposition='outside')
fig_bar.update_layout(title="Relative Size Comparison", template="plotly_white")
st.plotly_chart(fig_bar, use_container_width=True)

# DETALLES DEL NANOROBOT
st.subheader("NEUROGEN-X Core Composition")
st.markdown("""
- **Shape**: Truncated icosahedron (like a nanoscale soccer ball)
- **Material**: Gold-platinum alloy + Peptidomimetic layer
- **Core**: AI Quantum CPU
- **Mechanism**:
    - Crosses Blood-Brain Barrier using transferrin ligands
    - Detects prions with molecular GPS
    - Cuts prions with CRISPR-Cas13d
    - Regenerates neurons with BDNF & NGF
    - Self-destructs in 72h to avoid toxicity
- **Injection**: IV saline with stabilizers
""")

# PIE DE FUNCIONES
st.subheader("Functional Composition")
fig = px.pie(
    names=["CRISPR Prion Cutting", "GPS Targeting", "Regeneration", "Self-Destruction"],
    values=[30, 25, 30, 15],
    color_discrete_sequence=px.colors.sequential.Rainbow
)
st.plotly_chart(fig, use_container_width=True)

# COMPARACIÓN CON OTRAS TERAPIAS
st.subheader("Therapeutic Comparison")
df = pd.DataFrame({
    "Treatment": ["NEUROGEN-X", "MIT Nanoparticles", "NIH ASO", "Quinacrine"],
    "Efficacy (%)": [94, 48, 70, 0],
    "Toxicity": ["Low", "High", "Moderate", "High"],
    "Immune Response": ["Minimal", "High", "Moderate", "Severe"],
    "Cost (USD)": [8000, 50000, 1200000, 12000]
})
st.dataframe(df.style
    .background_gradient(cmap="Blues", subset=["Efficacy (%)"])
    .highlight_max(color="lightgreen")
    .set_table_styles([{'selector': 'thead', 'props': [('background-color', '#0ea5e9'), ('color', 'white')]}]))

# LÍNEA DE TIEMPO DE ACCIÓN
st.subheader("Treatment Journey Timeline")
steps = ["Injection", "Circulation", "BBB Crossing", "Prion Detection", "CRISPR Action", "Neural Repair", "Destruction"]
progress = [10, 25, 45, 65, 80, 95, 100]
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=steps, y=progress, mode='lines+markers', line=dict(color='cyan', width=4)))
fig2.update_layout(title="NEUROGEN-X Timeline", template="plotly_dark")
st.plotly_chart(fig2, use_container_width=True)

# EXPLICACIÓN FINAL
st.subheader("Why NEUROGEN-X Succeeds")
st.markdown("""
- Smart targeting with AI
- Prion-specific enzyme system (no harm to healthy cells)
- Full neural regeneration with nanoscaffolds
- Natural degradation without toxicity
- Accessible cost, high scalability

> "Built by science, inspired by life."
""")

# PIE DE PÁGINA
st.markdown("---")
st.markdown("<p style='text-align:center;'>Created by NEUROGEN-X Team — Powered by AI, Nanotech & Ecuadorian Innovation.</p>", unsafe_allow_html=True)