import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
from dash.dependencies import Input, Output
from app import app

from apps import potenciales_off, potenciales_on, potenciales_on_off
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
                dbc.NavLink("Potenciales ON", href="/", active="exact"),
                dbc.NavLink("Potenciales ON-OFF", href="/potenciales_on_on", active="exact"),
                dbc.NavLink("Potenciales OFF", href="/potenciales_off", active="exact"),
            
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)
content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url", refresh=False), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):

    if pathname == "/":
        return potenciales_on.layout
    elif pathname == "/potenciales_on_off":
        return potenciales_on_off.layout
    elif pathname == "/potenciales_off":
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
