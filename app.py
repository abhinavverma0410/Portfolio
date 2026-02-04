from dash import Dash, Input, Output, State
import dash_bootstrap_components as dbc
from dash import html

from components.navbar import create_navbar
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

app.layout = html.Div([
    dbc.Container(
        [
            create_navbar(),
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

@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

if __name__ == "__main__":
    app.run(debug=True, dev_tools_hot_reload=False)
