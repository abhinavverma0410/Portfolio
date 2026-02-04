import dash_bootstrap_components as dbc

def create_navbar():
    navbar = dbc.Navbar(
        dbc.Container(
            [
                dbc.NavbarToggler(id="navbar-toggler", n_clicks=0, className="border-0"),
                
                dbc.Collapse(
                    dbc.Nav(
                        [
                            dbc.NavItem(dbc.NavLink("Profile", href="#hero-section", external_link=True)),
                            dbc.NavItem(dbc.NavLink("Experience", href="#experience-section", external_link=True)),
                            dbc.NavItem(dbc.NavLink("Skills", href="#skills-section", external_link=True)),
                            dbc.NavItem(dbc.NavLink("Projects", href="#projects-section", external_link=True)),
                            dbc.NavItem(dbc.NavLink("Contact", href="#contact-section", external_link=True)),
                        ],
                        className="mx-auto text-center py-3 py-lg-0", 
                        navbar=True,
                    ),
                    id="navbar-collapse",
                    navbar=True,
                    className="w-100" 
                ),
            ],
            fluid=True,
            className="d-flex justify-content-center" 
        ),
        fixed="top",
        dark=True,
        color="dark",
        className="custom-navbar py-5 shadow-sm",
    )
    return navbar
