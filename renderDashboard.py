import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import pandas as pd
from dash.dependencies import Input, Output

# constants go here
BUTTON_STYLE = {
    'margin': '15px'
}
FILE_PATH='/home/covid19dashboard/Covid19India/output.csv'

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
df = pd.read_csv(FILE_PATH)
# print(df)

# Adding new columns for fatality and survival ratio
df['Fatality Rate %'] = round(df['Death'].astype(float) * 100 / (df['Confirmed cases (Foreigners)'] + df['Confirmed cases (Indians)']), 2)
df['Survival Rate %'] = round(df['Cured/Discharged'].astype(float) * 100 / (df['Confirmed cases (Foreigners)'] + df['Confirmed cases (Indians)']), 2)

total = df.tail(n=1)
df2 = df.iloc[:-1]

# Calculate KPIs here
states_effected = int(max(total['S. No.'])) - 1
confirmed = int(total['Confirmed cases (Foreigners)']) + int(total['Confirmed cases (Indians)'])
cured = int(total['Cured/Discharged'])
deaths = int(total['Death'])

recovered = int(cured * 100 / confirmed)
serious = confirmed - cured - deaths
fatality_ratio = round(float(deaths * 100 / confirmed), 2)

state_most_cases = df2[df2['Confirmed cases (Indians)'] == df2['Confirmed cases (Indians)'].max()]
state_kpi1 = state_most_cases['Name of State / UT'] + " " + str(state_most_cases['Confirmed cases (Indians)'].values)

state_most_cured = df2[df2['Cured/Discharged'] == df2['Cured/Discharged'].max()]

# If more than one state have same number of cured cases, pick one with `higher Survival Rate %`
if len(state_most_cured.index) > 1:
    state_most_cured = state_most_cured[state_most_cured['Survival Rate %'] == state_most_cured['Survival Rate %'].max()]
    
state_kpi2 = state_most_cured['Name of State / UT'] + " " + str(state_most_cured['Cured/Discharged'].values)
# print(df)

app.layout = html.Div([
    html.H1(children='COVID-19 India Impact Dashboard', style={'textAlign': 'center'}),
    dcc.Tabs([
        dcc.Tab(label='Table', children=[
            dash_table.DataTable(
                id='datatable-interactivity',
                columns=[
                    {"name": i, "id": i, "deletable": True, "selectable": True} for i in df.columns
                ],
                data=df.to_dict('records'),
                editable=False,
                filter_action="native",
                sort_action="native",
                sort_mode="single",
                column_selectable="single",
                row_selectable="multi",
                row_deletable=True,
                selected_columns=[],
                selected_rows=[],
                page_action="native",
                page_current=0,
                page_size=30,
                style_header={'fontWeight': 'bold'},
                style_cell={'textAlign': 'left', 'fontSize': 14, 'font-family': 'sans-serif', 'width': 'auto'}
            )
        ]),
        dcc.Tab(label='Bar-Graphs', children=[
            dcc.Loading(
                id="loading-icon",
                children=[
                    html.Div(id='datatable-interactivity-container')
                ],
                type="circle"
            )
        ]),
        dcc.Tab(label='KPIs', children=[
            dbc.Button(
                ["Confirmed Cases", dbc.Badge(confirmed, color="light", className="ml-1 h1")],
                color="dark", style=BUTTON_STYLE),
            html.Br(),
            dbc.Button(
                ["Serious", dbc.Badge(serious, color="light", className="ml-1 h1")],
                color="warning", style=BUTTON_STYLE),
            html.Br(),
            dbc.Button(
                ["Recovered Cases",
                 dbc.Badge(str(cured) + " (" + str(recovered) + "%)", color="light", className="ml-1 h1")],
                color="success", style=BUTTON_STYLE),
            html.Br(),
            dbc.Button(
                ["Deaths", dbc.Badge(int(total['Death']), color="light", className="ml-1 h1")],
                color="danger", style=BUTTON_STYLE),
            html.Br(),
            dbc.Button(
                ["Fatality Ratio", dbc.Badge(str(fatality_ratio) + "%", color="light", className="ml-1 h1")],
                color="primary", style=BUTTON_STYLE),
            html.Br(),
            dbc.Button(
                ["States/UT Effected", dbc.Badge(str(states_effected) + " / 36", color="light", className="ml-1 h1")],
                color="secondary", style=BUTTON_STYLE),
            html.Br(),
            dbc.Button(
                ["States/UT Most Cases", dbc.Badge(state_kpi1, color="light", className="ml-1 h1")],
                color="warning", style=BUTTON_STYLE),
            html.Br(),
            dbc.Button(
                ["States/UT Most Cured", dbc.Badge(state_kpi2, color="light", className="ml-1 h1")],
                color="success", style=BUTTON_STYLE)
        ])
    ])
])

@app.callback(Output("loading-icon", "children"))

@app.callback(
    Output('datatable-interactivity', 'style_data_conditional'),
    [Input('datatable-interactivity', 'selected_columns')]
)
def update_styles(selected_columns):
    return [{
        'if': {'column_id': i},
        'background_color': '#D2F3FF'
    } for i in selected_columns]


@app.callback(
    Output('datatable-interactivity-container', "children"),
    [Input('datatable-interactivity', "derived_virtual_data"),
     Input('datatable-interactivity', "derived_virtual_selected_rows")])
def update_graphs(rows, derived_virtual_selected_rows):
    # When the table is first rendered, `derived_virtual_data` and
    # `derived_virtual_selected_rows` will be `None`. This is due to an
    # idiosyncracy in Dash (unsupplied properties are always None and Dash
    # calls the dependent callbacks when the component is first rendered).
    # So, if `rows` is `None`, then the component was just rendered
    # and its value will be the same as the component's dataframe.
    # Instead of setting `None` in here, you could also set
    # `derived_virtual_data=df.to_rows('dict')` when you initialize
    # the component.
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []

    dff = df if rows is None else pd.DataFrame(rows)

    colors = ['#7FDBFF' if i in derived_virtual_selected_rows else '#0074D9'
              for i in range(len(dff))]

    return [
        dcc.Graph(
            id=column,
            figure={
                "data": [
                    {
                        "x": dff["Name of State / UT"],
                        "y": dff[column],
                        "type": "bar",
                        "text": dff[column],
                        "textposition": 'auto',
                        "marker": {"color": colors},
                        "hoverinfo": 'skip'
                    }
                ],
                "layout": {
                    "xaxis": {"automargin": True},
                    "yaxis": {
                        "automargin": True,
                    },
                    "title": {
                        "text": column,
                        'xanchor': 'center',
                        'yanchor': 'top'
                    },
                    "height": 250,
                    "margin": {"t": 20, "l": 10, "r": 10},
                },
            },
        )
        # check if column exists - user may have deleted it
        # If `column.deletable=False`, then you don't
        # need to do this check.
        for column in ["Confirmed cases (Indians)", "Confirmed cases (Foreigners)", "Cured/Discharged", "Death"] if
        column in dff
    ]


if __name__ == '__main__':
    app.run_server(debug=True)
