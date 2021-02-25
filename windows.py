import plotly.graph_objs as go
import dash_core_components as dcc 
import dash_html_components as html
import dash_bootstrap_components as dbc 
from dash.dependencies import Input, Output
from app import app
from app import server

from apps import potenciales_on, potenciales_off, potenciales_on_off
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#CCD7E3", 
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("APLICACIÓN - BME", className="display-5"),
        html.Hr(),
        html.P(
            "Control de la Corrosión", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Potenciales ON", href="/page-1", active="exact"),
                dbc.NavLink("Potenciales ON-OFF", href="/page-2", active="exact"),
                dbc.NavLink("Potenciales OFF", href="/page-3", active="exact"),
            
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)
content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/page-1":
        return potenciales_on.layout
    if pathname == "/page-2":
        return potenciales_on_off.layout
    if pathname == "/page-3":
        return potenciales_off.layout
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(port=8888)
