###
# Variable: Ofertas y precios
# Proyecto Zorro Abarrotero
# Graph: Sectores o dona 
# Roberto Andrade Fonseca (c)
# Inicio: mar ene 15 17:05:54 CST 2019
# Para: Avignon
###
# -*- coding: utf-8 -*-
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
data = pd.read_csv("../../data/data_levantamientos_diciembre_2018.csv")

data_set = data[['Cadena', 'Tienda', 'Ofertas y precios']]
data_set = data_set.sort_values(by=['Ofertas y precios'], ascending=False)
data_set = data_set.reset_index(drop=True)

ofertas_precios=pd.Series(data_set['Ofertas y precios'])
tiendas=pd.Series(data_set['Tienda'])
cadenas=pd.Series(data_set['Cadena']).sort_values()
promedios = data_set.groupby(['Cadena'])['Ofertas y precios'].mean()
#print(promedios)

values = [data[data['Cadena'] == 'Scorpion']['Ofertas y precios'].mean(), data[data['Cadena'] == 'Zorro Abarrotero']['Ofertas y precios'].mean()]

colors = {
    'background': 'black',
    'text': '#a3a3c2'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H3(
        children='Ofertas y Precios por Cadena',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [
                {
                'labels': pd.Series(data_set['Cadena'].unique()), 
                'values': values,
                'marker': {'colors':['blue', 'red']},
                'hole': 0.6,
                'type':'pie'},
            ],
            'layout': {
            'title': 'Calificación promedio de Ofertas y Precios.',
                 'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': { 'color': colors['text'] }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)


