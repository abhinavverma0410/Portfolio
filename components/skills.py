from dash import html
import dash_bootstrap_components as dbc

def create_skills():
    def skill_badge(name):
        return dbc.Badge(name, className="skill-badge me-2 mb-2 p-2 fs-6 fw-normal text-dark")

    technical_skills = ["Python", "NoSQL", "EDA", "Machine Learning", "Deep Learning", "GenAI"]
    libraries = ["NumPy", "Pandas", "Plotly", "Seaborn", "Scikit-learn", "PyTorch"]
    tools = ["Jupyter", "VS Code", "Google Colab", "Git"]

    education_data = [
        {"degree": "B.Tech CSE (AI & Data Science)", "institute": "CT University", "location": "Ludhiana", "year": "2026"},
        {"degree": "Senior Secondary XII (CBSE)", "institute": "Tagore Public School", "location": "Ludhiana", "year": "2022"},
    ]

    certifications = [
        "Python | IBM",
        "Machine Learning | IBM",
        "Data Science | IBM",
        "Big Data | IBM",
        "Hackathon Participation | CT UNIVERSITY, 2023",
        "Hackathon Participation | CT UNIVERSITY & TechVerse, 2025"
        ]

    skills_layout = html.Div([
        html.H4("Technical Skills", className="mb-4 fw-bold", style={'textDecoration': 'underline','textUnderlineOffset': '5px', 'textDecorationThickness': '1px'}),
        html.Div([skill_badge(s) for s in technical_skills], className="mb-4"),
        html.Br(),
        html.H4("Libraries & Frameworks", className="mb-4 fw-bold", style={'textDecoration': 'underline','textUnderlineOffset': '5px', 'textDecorationThickness': '1px'}),
        html.Div([skill_badge(s) for s in libraries], className="mb-4"),
        html.Br(),
        html.H4("Tools & Platforms", className="mb-4 fw-bold", style={'textDecoration': 'underline','textUnderlineOffset': '5px', 'textDecorationThickness': '1px'}),
        html.Div([skill_badge(s) for s in tools], className="mb-4"),
    ])

    education_layout = html.Div([
        dbc.Card([
            dbc.CardBody([
                html.H4("Education", className="card-title fw-bold mb-4", style={'textDecoration': 'underline','textUnderlineOffset': '5px', 'textDecorationThickness': '0.5px', 'textDecorationColor': '#6D6D6D'}),
                html.Div([
                    html.Div([
                        html.H5(edu["degree"], className="fw-bold mb-1"),
                        html.P([edu["institute"],html.Span(', '), edu['location']], className="text-muted mb-0"),
                        html.Small(edu["year"], className="text-secondary"),
                        html.Hr(className="my-3") if i < len(education_data)-1 else None
                    ]) for i, edu in enumerate(education_data)
                ])
            ])
        ], className="shadow-sm mb-4 border-0"),

        dbc.Card([
            dbc.CardBody([
                html.H4("Certifications", className="card-title fw-bold mb-3", style={'textDecoration': 'underline','textUnderlineOffset': '5px', 'textDecorationThickness': '0.5px', 'textDecorationColor': '#6D6D6D'}),
                html.Ul([
                    html.Li([
                        html.I(className="bi bi-check-circle-fill text-dark me-2"), 
                        span
                    ], className="list-unstyled mb-2 text-secondary") for span in certifications
                ], className="ps-0 m-0")
            ])
        ], className="shadow-sm border-0")
    ])

    layout = dbc.Container([
        html.Div([
            html.Span("SKILLS & EDUCATION", className="section-header d-inline-block"),
        ], className="text-center mb-5"),
        
        dbc.Row([
            dbc.Col(skills_layout, width=12, lg=7, className="mb-5"),
            dbc.Col(education_layout, width=12, lg=5)
        ])
    ], fluid=True, className="py-5", id="skills-section")
    
    return layout
