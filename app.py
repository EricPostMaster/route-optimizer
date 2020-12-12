import dash
from dash.dependencies import Input, Output
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv').sort_values(by=['pop'], ascending=False)

daily_inspections=8  # This will eventually be populated by a text input field
num_inspections = list(range(0,daily_inspections))

app = dash.Dash(__name__)

app.layout = html.Div([
    dash_table.DataTable(
        id='datatable-interactivity',
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": True} for i in df.columns
        ],
        data=df.to_dict('records'),
        # editable=True,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        # row_deletable=True,
        selected_columns=[],
        selected_rows=num_inspections,
        page_action="native",
        page_current= 0,
        page_size= 20,
    ),
])


if __name__ == '__main__':
    app.run_server(debug=True)