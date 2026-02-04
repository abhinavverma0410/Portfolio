import dash
from dash import html
import dash_bootstrap_components as dbc

def create_hero():
    layout = dbc.Container([
        # ML PORTFOLIO Heading (Already centered)
        dbc.Row([
            dbc.Col([
                html.H1("ML PORTFOLIO", 
                        className="display-4 fw-bold text-center",
                        style={
                            "letterSpacing": "4px",
                            "marginBottom": "2rem",
                            "fontWeight": "700"
                        })
            ], width=12)
        ], className="mb-4"),
        
        # Content Row - Single Column, Centered
        dbc.Row([
            dbc.Col([
                html.H1(["Hi, I'm ", html.B("Abhinav Verma")], 
                        className="display-5 fw-bold text-center mb-3"),
                
                html.P("Machine Learning Engineer | Data Scientist", 
                        className="lead text-center mb-4"),
                
                html.Hr(className="my-3 mx-auto", style={"width": "60%", "opacity": "0.3"}),
                
                html.P(
                    "Results-driven ML & Data Science Engineer with hands-on experience in predictive modeling, machine learning and deployment using Plotly Dash. "
                    "Skilled in Python, scikit-learn, and API integration. "
                    "Proven ability to build end-to-end ML pipelines and derive actionable insights from data.",
                    className="mb-5 text-center px-4",
                    style={"maxWidth": "800px", "marginLeft": "auto", "marginRight": "auto"} # Constrain width for readability
                ),
                
                html.Div([
                    dbc.Button(
                        "View My Work", color="primary", 
                        href="#projects-section", size="lg", 
                        className="me-3 mb-2",
                        style={"width": "220px"}),
                    dbc.Button(
                        [html.I(className="bi bi-file-earmark-pdf-fill me-2"), "Download CV"], 
                        color="outline-primary", 
                        size="lg", 
                        href="/assets/Abhinav Resume.pdf",
                        external_link=True,
                        className="me-3 mb-2 d-inline-flex align-items-center justify-content-center",
                        style={"width": "220px"}
                    )
                ], className="text-center")
                
            ], width=12, className="d-flex flex-column justify-content-center"),
            
            # REMOVED: The second column (Image) is deleted completely.
            
        ], className="align-items-center py-5")
    ], fluid=True, id="hero-section", className="px-3 px-md-5")
    return layout
