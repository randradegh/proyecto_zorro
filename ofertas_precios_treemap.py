###
# Variable: Ofertas y precios 
# Proyecto Zorro Abarrotero
# Graph: Treemap
# Roberto Andrade Fonseca (c)
# Inicio: mar ene 15 15:29:58 CST 2019
# Para: Avignon
###
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go
import squarify

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server
app.config.supress_callback_exceptions = True

colors = {
    'background': 'black',
    'text': 'white'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[

    html.H3(children='Proyecto Zorro Abarrotero', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(id='treemap')
])

@app.callback(
    Output('treemap', 'figure'),
    [Input('treemap', 'value')])

def treemap(value):
    data = pd.read_csv("../../data/data_levantamientos_diciembre_2018.csv")
    
    data_set = data[['Cadena', 'Tienda', 'Ofertas y precios']]
    data_set = data_set.sort_values(by=['Ofertas y precios'], ascending=False)
    data_set = data_set.reset_index(drop=True)
    dd = data_set[['Tienda', 'Cadena']]
    x = 0.
    y = 0.
    width = 100.
    height = 100.

    #tiendas= ['SECAGV', 'SCADE', 'SCADE2', 'SEC', 'ZTM', 'ZTC', 'ZES', 'ZE3', 'SN3', 'ZTL', 'STL', 'SAT', 'ZN2', 'ZTN', 'ZNR', 'ZAT', 'SN2', 'ZAN', 'CNA', 'ZEC', 'ZPR', 'ZE2', 'ZLG', 'ZRH']

    values=pd.Series(data_set['Ofertas y precios'])
    tiendas=pd.Series(data_set['Tienda'])
    cadenas=pd.Series(data_set['Cadena'])
    #print(data_set)

    normed = squarify.normalize_sizes(values, width, height)
    rects = squarify.squarify(normed, x, y, width, height)

    # Choose colors from http://colorbrewer2.org/ under "Export"
    #http://colorbrewer2.org/?type=sequential&scheme=Reds&n=3
    color_brewer = ['red', 'blue']
    colores = {'Zorro Abarrotero':0, 'Scorpion':1}
    shapes = []
    annotations = []
    counter = 0
    i = 0
    for r in rects:
        #print(i)
        #print(tiendas[i])
        #print(values[i])
        #print(cadenas[i])
        #print(color_brewer[colores[cadenas[i]]])
        shapes.append( 
            dict(
                type = 'rect', 
                x0 = r['x'], 
                y0 = r['y'], 
                x1 = r['x']+r['dx'], 
                y1 = r['y']+r['dy'],
                line = dict( width = 2 ),
                fillcolor = color_brewer[colores[cadenas[i]]]
            ) 
        )
        annotations.append(
            dict(
                x = r['x']+(r['dx']/2),
                y = r['y']+(r['dy']/2),
                #text = tiendas[i] + ': ' + '\n' + str(values[i]),
                text = str(values[i]),
                showarrow = False
            )
        )
        counter = counter + 1
        i = i + 1
        if counter >= len(color_brewer):
            counter = 0

    figure = {
    'data': [go.Scatter(
        x = [ r['x']+(r['dx']/2) for r in rects ], 
        y = [ r['y']+(r['dy']/2) for r in rects ],
        text = [ 'Tienda: ' + str(c) for c in tiendas], 
        mode = 'none',
        hoverinfo='text'
        )
    ],
    'layout': go.Layout(
        title='Treemap de Ofertas y Precios por Tienda',
        height=900, 
        width=1200,
        xaxis={'showgrid':False, 'zeroline':False, 'showticklabels': False},
        yaxis={'showgrid':False, 'zeroline':False, 'showticklabels': False},
        shapes=shapes,
        annotations=annotations,
        hovermode='closest',
        plot_bgcolor= colors['background'],
        paper_bgcolor= colors['background'],
        font= {
                    'color': colors['text']
                }
        )
    }
    return figure

if __name__ == '__main__':
    app.run_server(debug=True)
