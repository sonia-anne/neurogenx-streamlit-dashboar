import streamlit as st
import pandas as pd
import plotly.express as px

# TÍTULO PRINCIPAL
st.markdown("<h1 style='color: cyan; text-align: center;'>NEUROGEN-X: The Cure for Creutzfeldt-Jakob Disease</h1>", unsafe_allow_html=True)

# FONDO CON IMAGEN EN LÍNEA (funciona en Streamlit Cloud)
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://images.unsplash.com/photo-1581090700227-1e8a7ebc71b1?auto=format&fit=crop&w=1400&q=80");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    </style>
""", unsafe_allow_html=True)

# CARDS CON ICONOS
col1, col2, col3 = st.columns(3)
col1.metric("Prion Degradation", "94%", "Targeted")
col2.metric("Neuronal Regeneration", "40% ↑", "2 weeks")
col3.metric("Cost per dose", "$8,000", "vs $1.2M gene therapy")

st.markdown("---")

# MAPA DE MECANISMO DE ACCIÓN (GRÁFICO DE BARRAS)
st.subheader("Mechanism of Action: NEUROGEN-X vs Traditional Treatments")
mechanism_data = pd.DataFrame({
    "Process": ["Prion Detection", "Selective Degradation", "Regeneration", "Autodestruction"],
    "NEUROGEN-X": [100, 94, 85, 100],
    "Gene Therapy": [50, 0, 40, 0],
    "Gold Nanoparticles": [80, 48, 0, 0]
})
fig = px.bar(mechanism_data, x="Process", y=["NEUROGEN-X", "Gene Therapy", "Gold Nanoparticles"],
             title="Comparison of Treatment Mechanisms",
             barmode="group", color_discrete_sequence=px.colors.sequential.Viridis)
st.plotly_chart(fig)

# SLIDER COMPARATIVO DE EFICACIA
st.subheader("Efficacy Comparison")
efficacy = st.slider("Adjust NEUROGEN-X Degradation Rate", 50, 100, 94)
st.success(f"Simulated prion degradation rate: {efficacy}%")

# DIAGRAMA DE VENN (SIMULADO CON TEXTO)
st.subheader("Why NEUROGEN-X Works Where Others Failed")
st.markdown("""
- ✅ Selective Prion Targeting  
- ✅ Neuronal Regeneration  
- ✅ Autodestruction  
- ❌ Accumulation (MIT Gold Particles)  
- ❌ Systemic Toxicity (Gene Therapy)  
""")

# FOOTER CON FRASE FINAL
st.markdown("---")
st.markdown("<h4 style='text-align: center; color: white;'>From Ecuador, rewriting the future of neurodegenerative medicine.</h4>", unsafe_allow_html=True)
