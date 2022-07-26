######### Import your libraries #######
import dash
import dash_core_components as dcc
import dash_html_components as html
import os

###### Set up variables
list_of_choices=['banana', 'hug', 'kiss']
list_of_images=['banana-minions.gif', 'hug-minions.gif','kiss-minions.gif']
githublink = 'https://github.com/yibaiyilan/201-chuck-norris-callback'
image1='minions.jpg'
heading1='What will A Monion Give You?'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='Minions!'

####### Layout of the app ########
app.layout = html.Div([
    html.H2(heading1),
    html.Img(id='your-image-output', src=app.get_asset_url(image1), style={'width': 'auto', 'height': '10%'}),
	    dcc.Dropdown(id='your-input-here',	
                options=[{'label': list_of_choices[i], 'value': i} for i in range(len(list_of_choices))],	
                value=list_of_choices[0],	
                style={'width': '500px'}),
    html.Br(),
    html.Div(id='your-output-here', children=''),
    html.Br(),
    html.A('Check Out My AWESOME Code on Github', href=githublink),

])


######### Interactive callbacks go here #########
@app.callback(dash.dependencies.Output('your-output-here', 'children'),
              [dash.dependencies.Input('your-input-here', 'value')])
def display_value(whatever_you_chose):
    return f'The minion will now give you a {whatever_you_chose}.'

@app.callback(dash.dependencies.Output('your-image-output', 'src'),
              [dash.dependencies.Input('your-input-here', 'value')])
def display_value(whatever_you_chose):
    return app.get_asset_url(list_of_images[whatever_you_chose])
######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
