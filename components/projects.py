from dash import html
import dash_bootstrap_components as dbc

def create_projects():
    projects_data = [
        {
            "title": "Car Price Predictor",
            "description": "Built a dataset-trained Car Price Predictor with Plotly Dash that estimates vehicle values using both manual input and web-scraped data from multiple car listing websites.",
            "tags": ["Plotly-Dash", "LightGBM", "BeautifulSoup", "JobLib"],
            "link": "https://github.com/abhinavverma0410/Car-Price-Predictor",
            "image": "https://github.com/abhinavverma0410/Car-Price-Predictor/raw/main/assets/CarPricePredictor.png"
        },
        {
            "title": "AI Text-to-Image Generator ",
            "description": "Built with Stable Diffusion and PyTorch that converts natural language prompts into high-quality images.",
            "tags": ["Plotly-Dash", "PyTorch", "Stable Diffusion", "Diffusers", "Transformers (CLIP)", "UNet", "VAE", "CUDA", "Hugging Face Hub"],
            "link": "https://github.com/abhinavverma0410/AI-Text-to-Image-Generator",
            "image": "https://github.com/abhinavverma0410/AI-Text-to-Image-Generator/raw/main/assets/AITextToImageGenerator.png"
        },
        {
            "title": "AI Resume Analyzer",
            "description": "Built using Dash and Ollama LLM that extracts insights from PDFs with custom loading states and real-time feedback.",
            "tags": ["Plotly-Dash", "Ollama Deepseek LLM"],
            "link": "https://github.com/abhinavverma0410/AI-Resume-Analyzer",
            "image": "https://github.com/abhinavverma0410/AI-Resume-Analyzer/raw/master/assets/SS1.png"
        },
        {
            "title": "AI Semantic Sketch Renderer",
            "description": "Converts sketches into high-quality images using Gemini semantic prompting, Stable Diffusion DreamShaper, and ControlNet edge guidance with GPU acceleration.",
            "tags": ["Plotly-Dash", "PyTorch","CUDA",  "Google Gemini 1.5 Flash", "Stable Diffusion (DreamShaper)", "ControlNet (Canny)"],
            "link": "https://github.com/abhinavverma0410/AI-Semantic-Sketch-Renderer",
            "image": "https://github.com/abhinavverma0410/AI-Semantic-Sketch-Renderer/raw/master/assets/SS2.png"
        }
    ]

    def build_project_card(project):
        return dbc.Col([
            dbc.Card([
                dbc.CardImg(
                    src=project["image"], 
                    top=True, 
                    className="img-fluid", 
                    style = {
                        "maxHeight": "300px",
                        "width": "100%",
                        "objectFit": "cover"
                    }
                ),
                dbc.CardBody([
                    html.H5(project["title"], className="card-title fw-bold text-center"),
                    html.P(project["description"], className="card-text text-secondary"),
                    html.Div([
                        dbc.Badge(tag, color="light", text_color="dark", className="me-2 border") 
                        for tag in project["tags"]
                    ], className="mb-4 text-center"),
                    
                    dbc.Button(
                        [html.I(className="bi bi-github me-2"), "View Code"], 
                        href=project["link"], 
                        color="dark", 
                        outline=True, 
                        target="_blank",
                        className="w-100"
                    )
                ])
            ], className="h-100 shadow-sm hover-shadow border-0")
        ], 
        width=12,
        md=6,
        lg=6,
        className="mb-4"
        )

    layout = dbc.Container([
        html.Div([
            html.Span("FEATURED PROJECTS", className="section-header d-inline-block"),
        ], className="text-center mb-5"),
        
        dbc.Row(
            [build_project_card(p) for p in projects_data], 
            className="justify-content-center g-4"
        )
    ], className="py-5", id="projects-section")
    
    return layout
