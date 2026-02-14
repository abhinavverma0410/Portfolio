from dash import Dash, html, dcc, Input, Output, State, ctx
import dash_bootstrap_components as dbc

from components.hero import create_hero
from components.experience import create_experience
from components.skills import create_skills
from components.projects import create_projects
from components.footer import create_footer

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.LUX, dbc.icons.BOOTSTRAP],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    title="Portfolio",
    update_title=None,
    suppress_callback_exceptions=True
)

server = app.server

# Custom Hamburger Menu (Prevents auto-close on click)
hamburger_menu = html.Div(
    [
        dbc.Button(
            html.I(className="bi bi-list fs-3 m-0 p-0"),
            id="hamburger-btn",
            className="custom-hamburger-toggle d-flex align-items-center justify-content-center",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(
                dbc.CardBody(
                    [
                        html.A("Profile", href="#hero-section", id="link-profile", className="custom-nav-link"),
                        html.A("Experience", href="#experience-section", id="link-experience", className="custom-nav-link"),
                        html.A("Skills", href="#skills-section", id="link-skills", className="custom-nav-link"),
                        html.A("Projects", href="#projects-section", id="link-projects", className="custom-nav-link"),
                        html.A("Contact", href="#contact-section", id="link-contact", className="custom-nav-link"),
                    ],
                    className="d-flex flex-column p-2 gap-1"
                ),
                className="border-0 shadow-lg custom-dropdown-card mt-2",
            ),
            id="hamburger-collapse",
            is_open=False,
            className="position-absolute end-0",
            style={"minWidth": "210px"}
        ),
    ],
    className="fixed-hamburger-wrapper"
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    hamburger_menu,
    dbc.Container(
        [
            create_hero(),
            create_experience(),
            create_skills(),
            create_projects(),
            create_footer()
        ],
        fluid=True,
        className="p-0"
    )
])

# 1. Callback to toggle the dropdown ONLY when the hamburger button is clicked,
#    and conditionally close it ONLY if navigating to a different section.
@app.callback(
    Output("hamburger-collapse", "is_open"),
    [Input("hamburger-btn", "n_clicks"),
     Input("link-profile", "n_clicks"),
     Input("link-experience", "n_clicks"),
     Input("link-skills", "n_clicks"),
     Input("link-projects", "n_clicks"),
     Input("link-contact", "n_clicks")],
    [State("hamburger-collapse", "is_open"),
     State("link-profile", "className"),
     State("link-experience", "className"),
     State("link-skills", "className"),
     State("link-projects", "className"),
     State("link-contact", "className")], 
    prevent_initial_call=True
)
def toggle_menu(btn, p, e, s, pr, c, is_open, class_p, class_e, class_s, class_pr, class_c):
    trigger_id = ctx.triggered_id
    
    if trigger_id == "hamburger-btn":
        # Toggle menu if the hamburger button is clicked
        return not is_open
        
    elif trigger_id:
        # Map the clicked link to its current class name State to avoid the URL race condition.
        class_mapping = {
            "link-profile": class_p,
            "link-experience": class_e,
            "link-skills": class_s,
            "link-projects": class_pr,
            "link-contact": class_c
        }
        
        clicked_class = class_mapping.get(trigger_id, "")
        
        # If the clicked link ALREADY has the active class, we are currently on this section.
        if "active-nav-item" in clicked_class:
            return is_open # Do not close the dropdown
        else:
            return False   # Navigating to a new section, close the dropdown
            
    return is_open

# 2. Callback to dynamically update active link styling based on URL hash
@app.callback(
    [Output("link-profile", "className"),
     Output("link-experience", "className"),
     Output("link-skills", "className"),
     Output("link-projects", "className"),
     Output("link-contact", "className")],
    [Input("url", "href")]
)
def update_active_links(href):
    # Parse the current section hash from the URL
    hash_val = ""
    if href and "#" in href:
        hash_val = "#" + href.split("#")[-1]
        
    # Define the base, active, and inactive CSS classes
    base_class = "custom-nav-link text-decoration-none px-4 py-2 rounded-3 transition-all d-block"
    
    # Replaced the heavy dark classes with a subtle custom active class
    active_class = base_class + " active-nav-item"
    inactive_class = base_class + " text-dark hover-bg-light"

    # Default all to inactive
    p, e, s, pr, c = inactive_class, inactive_class, inactive_class, inactive_class, inactive_class
    
    # Apply active styling based on current route
    if hash_val == "#experience-section":
        e = active_class
    elif hash_val == "#skills-section":
        s = active_class
    elif hash_val == "#projects-section":
        pr = active_class
    elif hash_val == "#contact-section":
        c = active_class
    else:
        p = active_class # Defaults to Profile on initial load or empty hash
        
    return p, e, s, pr, c

if __name__ == "__main__":
    app.run(debug=True, dev_tools_hot_reload=False)
