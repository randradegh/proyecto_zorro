import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.plotly as py
import plotly.graph_objs as go

app = dash.Dash()
server = app.server
app.config.supress_callback_exceptions = True

app.layout = html.Div([
    dcc.Graph(id='pie')
])

@app.callback(
    Output('pie', 'figure'),
    [Input('pie', 'value')])

def pie():
    
    fig = {
        "data": [
        {
          "values": [16, 15, 12, 6, 5, 4, 42],
          "labels": [
            "US",
            "China",
            "European Union",
            "Russian Federation",
            "Brazil",
            "India",
            "Rest of World"
          ],
          "domain": {"x": [0, .48]},
          "name": "GHG Emissions",
          "hoverinfo":"label+percent+name",
          "hole": .4,
          "type": "pie"
        },
        {
          "values": [27, 11, 25, 8, 1, 3, 25],
          "labels": [
            "US",
            "China",
            "European Union",
            "Russian Federation",
            "Brazil",
            "India",
            "Rest of World"
          ],
          "text":["CO2"],
          "textposition":"inside",
          "domain": {"x": [.52, 1]},
          "name": "CO2 Emissions",
          "hoverinfo":"label+percent+name",
          "hole": .4,
          "type": "pie"
        }],
      "layout": {
            "title":"Global Emissions 1990-2011",
            "annotations": [
                {
                    "font": {
                        "size": 20
                    },
                    "showarrow": False,
                    "text": "GHG",
                    "x": 0.20,
                    "y": 0.5
                },
                {
                    "font": {
                        "size": 20
                    },
                    "showarrow": False,
                    "text": "CO2",
                    "x": 0.8,
                    "y": 0.5
                }
            ]
        }
    return fig
#py.iplot(fig, filename='donut')

if __name__ == '__main__':
    app.run_server(debug=True)
