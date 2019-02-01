###
# Variable: Orden y Limpieza
# Proyecto Zorro Abarrotero
# Graph: Barras
# Roberto Andrade Fonseca (c)
# Inicio: jue ene 17 13:53:11 CST 2019
# Para: Avignon
###

# -*- coding: utf-8 -*-
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
data = pd.read_csv("../../data/data_levantamientos_diciembre_2018.csv")

data_set = data[['Municipio', 'Cadena', 'Tienda', 'Orden y Limpieza']]
data_set = data_set.sort_values(by=['Orden y Limpieza'], ascending=False)
data_set = data_set.reset_index(drop=True)

# Armamos los promedios por cadena y municipio.
data_scorpion=data_set.loc[data_set['Cadena'] == 'Scorpion']
mean_scorpion=data_scorpion.groupby(['Municipio'], as_index=False)['Orden y Limpieza'].mean()
municipios_scorpion = mean_scorpion['Municipio']
data_scorpion= mean_scorpion['Orden y Limpieza']

data_zorro=data_set.loc[data_set['Cadena'] == 'Zorro Abarrotero']
mean_zorro=data_zorro.groupby(['Municipio'], as_index=False)['Orden y Limpieza'].mean()
municipios_zorro = mean_zorro['Municipio']
data_zorro= mean_zorro['Orden y Limpieza']

##data_zorro=data_set.loc[data_set['Cadena'] == 'Zorro Abarrotero']
colors = {
    'background': 'black',
    'text': '#a3a3c2'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H3(
        children='Orden y Limpieza por Cadena',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    dcc.Graph(
        id='example-graph',
        figure={
   'data': [
       {'x': municipios_scorpion,'y': data_scorpion, 'type': 'bar', 'name': 'Scorpion','marker':{'color':'blue'}},
       {'x': municipios_zorro,'y': data_zorro, 'type': 'bar', 'name': 'Zorro Abarrotero','marker':{'color':'red'}},
            ],
            'layout': {
                'title': 'Promedio de Orden y Limpieza por Cadena y Municipio',
                 'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': { 'color': colors['text'] }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
