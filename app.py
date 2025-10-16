import streamlit as st

st.set_page_config(page_title="Spotify Power BI Dashboard", layout="wide")

st.title("🎧 Spotify Top 50 Power BI Dashboard")
st.write("This dashboard integrates Power BI visuals inside a Streamlit web app for interactive analytics exploration.")

# Replace with your actual Power BI embed URL
powerbi_url = "https://app.powerbi.com/reportEmbed?reportId=ba3151a7-8143-4dad-aa12-f18691f76509&autoAuth=true&ctid=f372731b-ab11-4425-ae60-7130988374fd"

st.markdown(
    f"""
    <div style="position: relative; padding-bottom: 65%; height: 0; overflow: hidden;">
      <iframe src="{powerbi_url}" 
              style="position: absolute; top:0; left:0; width:100%; height:100%; border:none;" 
              allowFullScreen="true"></iframe>
    </div>
    """,
    unsafe_allow_html=True
)
