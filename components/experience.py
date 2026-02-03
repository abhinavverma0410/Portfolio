from dash import html
import dash_bootstrap_components as dbc

def create_experience():
    def build_exp_card(role, company, date, location, description):
        return dbc.Card([
            dbc.CardBody([
                html.Div([
                    # Date
                    html.H6(date, className="text-secondary mb-2 text-uppercase fw-bold small"),
                    # Role & Company
                    html.H4(role, className="card-title fw-bold mb-1"),
                    html.H5(f"{company} | {location}", className="text-muted mb-3 h6"),
                    # Description
                    html.P(description, className="card-text text-secondary")
                ], className="ms-3") 
            ])
        ], className="experience-card h-100 border-0 shadow-sm")

    experiences = [
        {
            "role": "Machine Learning Trainee",
            "company": "Toxsl Technologies Pvt. Ltd.",
            "location": "Mohali, Punjab",
            "date": "June 2025 - August 2025",
            "desc": "Working on real-time ML projects, model tuning, and pipeline automation using Python and Scikit-learn."
        },
        {
            "role": "Data Science Tainee",
            "company": "Ansh Infotech Pvt. Ltd.",
            "location": "Ludhiana, Punjab",
            "date": "June 2024 - July 2025",
            "desc": "Built and deployed a Sentiment Analysis syst"
        },
        {
            "role": "Python Developer Trainee",
            "company": "PG Tech Pvt. Ltd.",
            "location": "Chandigarh, Punjab",
            "date": "June 2023 - July 2023",
            "desc": "Developed Python based automation tools and handled API integrations for process optimization."
        }
    ]

    layout = dbc.Container([
        # Header with thin faded gray line
        html.Div([
            html.Span("EXPERIENCE & TRAINING", className="section-header d-inline-block"),
        ], className="text-center mb-5"),
        
        dbc.Row([
            dbc.Col(build_exp_card(exp["role"], exp["company"], exp["date"], exp["location"], exp["desc"]), width=12, className="py-3") 
            for exp in experiences
        ], className="px-md-2 gy-4")
    ], fluid=True, className="py-5", id="experience-section")
    
    return layout