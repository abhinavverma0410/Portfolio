from dash import html, dcc
import dash_bootstrap_components as dbc

def create_footer():
    layout = dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H3("Let's Connect", className="text-white mb-4"),

                html.Div([
                    html.A([html.I(className="bi bi-linkedin me-2"), "LinkedIn"], 
                            href="https://linkedin.com/in/abhinav-verma-48331a250/", 
                            target="_blank", 
                            className="footer-link lead mb-3 mb-md-0 me-md-4"),
                    
                    html.A([html.I(className="bi bi-github me-2"), "GitHub"], 
                            href="https://github.com/abhinavverma0410", 
                            target="_blank", 
                            className="footer-link lead mb-3 mb-md-0 me-md-4"),
                    
                    html.A([html.I(className="bi bi-envelope-fill me-2"), "Email Me"], 
                            href="mailto:abhinavverma1005@gmail.com", 
                            className="footer-link lead mb-3 mb-md-0"),
                    ], className="d-flex flex-column flex-md-row justify-content-center align-items-center mb-4"),

                html.Div([
                    html.I(className="bi bi-telephone-fill me-2 text-white"),
                    html.Span("+91 62393-24309", className="lead text-white me-3"),
                    dcc.Clipboard(
                        id="copy-btn",
                        target_id="phone-number-hidden",
                        style={"display": "inline-block", "color": "white", "cursor": "pointer", "border": "1px solid white", "borderRadius": "5px", "padding": "5px 10px"}
                    ),
                    dbc.Tooltip("Phone Number Copied!", target="copy-btn", trigger="click", placement="top"),
                    html.Div("+916239324309", id="phone-number-hidden", style={"display": "none"})
                ], className="d-flex justify-content-center align-items-center mb-4"),

                html.Hr(className="mt-4 mb-3 text-white-50"),
                html.P("© 2026 Abhinav Verma. Built with Plotly Dash & Bootstrap.", className="text-white-50 small")
            ], className="text-center")
        ])
    ], fluid=True, className="bg-dark p-5 mt-5", id="contact-section")
    
    return layout
