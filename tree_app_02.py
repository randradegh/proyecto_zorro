import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go
import squarify

app = dash.Dash()
server = app.server
app.config.supress_callback_exceptions = True

app.layout = html.Div([
    dcc.Graph(id='treemap')
])

@app.callback(
    Output('treemap', 'figure'),
    [Input('treemap', 'value')])
def treemap(value):
    
    x = 0.
    y = 0.
    width = 100.
    height = 100.
    
    values = [500, 433, 78, 25, 25, 7]
    tiendas= ['S1', 'S2', 'Z3', 'Z4', 'Z5', 'Z6']

    normed = squarify.normalize_sizes(values, width, height)
    rects = squarify.squarify(normed, x, y, width, height)

    # Choose colors from http://colorbrewer2.org/ under "Export"
    color_brewer = ['rgb(166,206,227)','rgb(31,120,180)','rgb(178,223,138)',
                    'rgb(51,160,44)','rgb(251,154,153)','rgb(227,26,28)']
    shapes = []
    annotations = []
    counter = 0

    for r in rects:
        shapes.append( 
            dict(
                type = 'rect', 
                x0 = r['x'], 
                y0 = r['y'], 
                x1 = r['x']+r['dx'], 
                y1 = r['y']+r['dy'],
                line = dict( width = 2 ),
                fillcolor = color_brewer[counter]
            ) 
        )
        annotations.append(
            dict(
                x = r['x']+(r['dx']/2),
                y = r['y']+(r['dy']/2),
                text = 'Attn. a Clientes: ' + str(values[counter]),
                #text = 'Tienda',
                showarrow = False
            )
        )
        counter = counter + 1
        if counter >= len(color_brewer):
            counter = 0

    figure = {
    'data': [go.Scatter(
        x = [ r['x']+(r['dx']/2) for r in rects ], 
        y = [ r['y']+(r['dy']/2) for r in rects ],
        #text = [ str(v) for v in values ], 
        text = [ 'Tienda: ' + str(t) for t in tiendas], 
        #text = 'Hola', 
        mode = 'none',
        hoverinfo='text'
        )
    ],
    'layout': go.Layout(
        'title': 'Dashboard de Atención en Cajas por Tienda',
        height=700, 
        #width=700,
        width=1000,
        xaxis={'showgrid':False, 'zeroline':False, 'showticklabels': False},
        yaxis={'showgrid':False, 'zeroline':False, 'showticklabels': False},
        shapes=shapes,
        annotations=annotations,
        hovermode='closest'
        )
    }
    return figure

if __name__ == '__main__':
    app.run_server(debug=True)
