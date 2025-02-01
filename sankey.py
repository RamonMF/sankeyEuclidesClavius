import pandas as pd
import plotly.graph_objects as go

# Llegeix el fitxer .txt sense encapçalaments
df = pd.read_csv('llati-grec-oc.txt', delimiter='\t', header=None, names=["Traducció_Llatina", "Lema_Grec", "Ocurrències"])

# Crea un diccionari per assignar un índex únic a cada terme (tant llatí com grec)
unique_terms = list(df['Traducció_Llatina'].unique()) + list(df['Lema_Grec'].unique())
term_to_index = {term: i for i, term in enumerate(unique_terms)}

# Prepara les dades per al diagrama de Sankey
sources = []
targets = []
values = []

# Recorre el DataFrame per crear les connexions
for _, row in df.iterrows():
    sources.append(term_to_index[row['Traducció_Llatina']])  # Índex de la traducció llatina
    targets.append(term_to_index[row['Lema_Grec']])  # Índex del lema grec
    values.append(row['Ocurrències'])  # Ocurrències

# Crea el diagrama de Sankey
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,  # Espai entre nodes
        thickness=20,  # Gruix dels nodes
        line=dict(color="black", width=0.5),  # Línia dels nodes
        label=unique_terms,  # Etiquetes dels nodes (tots els termes únics)
        color="blue"  # Color dels nodes
    ),
    link=dict(
        source=sources,  # Fonts (traduccions llatines)
        target=targets,  # Destins (lemes grecs)
        value=values  # Valors (occurrències)
    )
)])

# Configura el títol i la mida de la font
fig.update_layout(
    title_text="Diagrama de Sankey: Traduccions Llatines i Lemes Grecs (agrupat)",
    font_size=14,
    autosize=False,  # Permet que el gràfic s'ajusti automàticament
    width=1500,  # Amplada del gràfic
    height=4500,  # Alçada del gràfic
)

# Guarda el gràfic com a pàgina web HTML
fig.write_html("sankey_diagram.html")

# Mostra el diagrama (opcional)
fig.show()
