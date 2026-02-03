import dash_bootstrap_components as dbc
from dash import html

def create_navbar():
    navbar = dbc.Navbar(
        dbc.Container(
            [
                # Left spacer
                html.Div(style={"width": "100px"}),
                
                # Navigation Links
                dbc.Nav(
                    [
                        dbc.NavItem(dbc.NavLink("Profile", href="#hero-section", external_link=True)),
                        dbc.NavItem(dbc.NavLink("Experience", href="#experience-section", external_link=True)),
                        dbc.NavItem(dbc.NavLink("Skills", href="#skills-section", external_link=True)),
                        dbc.NavItem(dbc.NavLink("Projects", href="#projects-section", external_link=True)),
                        dbc.NavItem(dbc.NavLink("Contact", href="#contact-section", external_link=True)),
                    ],
                    className="mx-auto gap-4", # Added gap-4 for cleaner spacing
                    navbar=True,
                ),
                
                # Right spacer
                html.Div(style={"width": "100px"}),
            ],
            fluid=True,
        ),
        fixed="top",
        className="custom-navbar py-3",
    )
    return navbar