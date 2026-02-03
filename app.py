import dash
import dash_bootstrap_components as dbc
from dash import html

# Import components
from components.navbar import create_navbar
from components.hero import create_hero
from components.experience import create_experience
from components.skills import create_skills
from components.projects import create_projects
from components.footer import create_footer

# Initialize the app with updated configuration
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.LUX, dbc.icons.BOOTSTRAP],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    title="Portfolio",
    update_title=None,  # Disable the "Updating..." title
    suppress_callback_exceptions=True  # Suppress callback exceptions during initial load
)

server = app.server

# Define layout
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

if __name__ == "__main__":
    app.run(debug=True, dev_tools_hot_reload=False)