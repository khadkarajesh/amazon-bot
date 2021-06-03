import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output
from dotenv import load_dotenv

from selenium_manager import SeleniumManager

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
load_dotenv()

app.layout = html.Div(className="column", children=[
    html.H1(children='''
        Amazon Bot
    '''),
    html.Div(className="row", children=[
        dcc.Input(id="product_name", type="text", placeholder="Enter product name", style={"margin-right": "10px"}),
        html.Button('Search', id='btn_search', n_clicks=0),
    ]),
    html.Div(id='display_container', style={"margin-top": "16px"})
], style={'justify-content': 'center',
          'display': 'flex',
          'align-items': 'center',
          'flex-direction': 'column',
          'height': '100vh'})


@app.callback(Output('display_container', 'children'),
              [dash.dependencies.Input('btn_search', 'n_clicks')],
              [dash.dependencies.State('product_name', 'value')])
def on_btn_click(n_clicks, value):
    if n_clicks > 0 and value is not None:
        selenium = SeleniumManager(base_url="https://www.amazon.com/")
        selenium.login()
        if selenium.search("cracking coding interview"):
            return f"Product: {value} added successfully to cart"
        else:
            return "Couldn't add to cart"


if __name__ == '__main__':
    app.run_server(debug=True)
