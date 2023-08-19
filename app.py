# Code source: https://dash-bootstrap-components.opensource.faculty.ai/examples/simple-sidebar/
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import dash_labs as dl
from dash.dependencies import Input, Output
import pandas as pd


df = pd.read_csv(
    'https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Bootstrap/Side-Bar/iranian_students.csv')

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# dataframes

# AUSTRALIA
df_AUS_GDP = pd.read_csv('GDP.csv')
df_AUS_GDP = df_AUS_GDP[df_AUS_GDP['LOCATION'] == 'AUS']
df_AUS_longTermEmp = pd.read_csv('Long_term_unemployment_rate.csv')
df_AUS_longTermEmp = df_AUS_longTermEmp[df_AUS_longTermEmp['LOCATION'] == 'AUS']
df_AUS_avgWage = pd.read_csv('Average_wage.csv')
df_AUS_avgWage = df_AUS_avgWage[df_AUS_avgWage['LOCATION'] == 'AUS']
df_AUS_EmpByEducatiob = pd.read_csv('Employment_by_education_level.csv')
df_AUS_EmpByEducatiob = df_AUS_EmpByEducatiob[df_AUS_EmpByEducatiob['LOCATION'] == 'AUS']
df_AUS_employmentRate = pd.read_csv('Employment_rate.csv')
df_AUS_employmentRate = df_AUS_employmentRate[df_AUS_employmentRate['LOCATION'] == 'AUS'].tail(
    50)
df_AUS_fertilityRate = pd.read_csv('Fertility_rates.csv')
df_AUS_fertilityRate = df_AUS_fertilityRate[df_AUS_fertilityRate['LOCATION'] == 'AUS']
df_AUS_govDebt = pd.read_csv('General_Government_debt.csv')
df_AUS_govDebt = df_AUS_govDebt[df_AUS_govDebt['LOCATION'] == 'AUS']
df_AUS_OldAgeDepedency = pd.read_csv('Old_age_dependency_ratio.csv')
df_AUS_OldAgeDepedency = df_AUS_OldAgeDepedency[df_AUS_OldAgeDepedency['LOCATION'] == 'AUS']
df_AUS_selfEmployed = pd.read_csv('Self_employment_rate.csv')
df_AUS_selfEmployed = df_AUS_selfEmployed[df_AUS_selfEmployed['LOCATION'] == 'AUS']
df_AUS_unemploment = pd.read_csv('Unemployment_rate.csv')
df_AUS_unemploment = df_AUS_unemploment[df_AUS_unemploment['LOCATION'] == 'AUS']
df_AUS_youngPopulation = pd.read_csv('Young_population.csv')
df_AUS_youngPopulation = df_AUS_youngPopulation[df_AUS_youngPopulation['LOCATION'] == 'AUS']
df_AUS_youthEmp = pd.read_csv('Youth_unemployment_rate.csv')
df_AUS_youthEmp = df_AUS_youthEmp[df_AUS_youthEmp['LOCATION'] == 'AUS']

# AUSTRIA
df_AUT_GDP = pd.read_csv('GDP.csv')
df_AUT_GDP = df_AUT_GDP[df_AUT_GDP['LOCATION'] == 'AUT']
df_AUT_longTermEmp = pd.read_csv('Long_term_unemployment_rate.csv')
df_AUT_longTermEmp = df_AUT_longTermEmp[df_AUT_longTermEmp['LOCATION'] == 'AUT']
df_AUT_avgWage = pd.read_csv('Average_wage.csv')
df_AUT_avgWage = df_AUT_avgWage[df_AUT_avgWage['LOCATION'] == 'AUT']
df_AUT_EmpByEducatiob = pd.read_csv('Employment_by_education_level.csv')
df_AUT_EmpByEducatiob = df_AUT_EmpByEducatiob[df_AUT_EmpByEducatiob['LOCATION'] == 'AUT']
df_AUT_employmentRate = pd.read_csv('Employment_rate.csv')
df_AUT_employmentRate = df_AUT_employmentRate[df_AUT_employmentRate['LOCATION'] == 'AUT'].tail(
    50)
df_AUT_fertilityRate = pd.read_csv('Fertility_rates.csv')
df_AUT_fertilityRate = df_AUT_fertilityRate[df_AUT_fertilityRate['LOCATION'] == 'AUT']
df_AUT_govDebt = pd.read_csv('General_Government_debt.csv')
df_AUT_govDebt = df_AUT_govDebt[df_AUT_govDebt['LOCATION'] == 'AUT']
df_AUT_OldAgeDepedency = pd.read_csv('Old_age_dependency_ratio.csv')
df_AUT_OldAgeDepedency = df_AUT_OldAgeDepedency[df_AUT_OldAgeDepedency['LOCATION'] == 'AUT']
df_AUT_selfEmployed = pd.read_csv('Self_employment_rate.csv')
df_AUT_selfEmployed = df_AUT_selfEmployed[df_AUT_selfEmployed['LOCATION'] == 'AUT']
df_AUT_unemploment = pd.read_csv('Unemployment_rate.csv')
df_AUT_unemploment = df_AUT_unemploment[df_AUT_unemploment['LOCATION'] == 'AUT']
df_AUT_youngPopulation = pd.read_csv('Young_population.csv')
df_AUT_youngPopulation = df_AUT_youngPopulation[df_AUT_youngPopulation['LOCATION'] == 'AUT']
df_AUT_youthEmp = pd.read_csv('Youth_unemployment_rate.csv')
df_AUT_youthEmp = df_AUT_youthEmp[df_AUT_youthEmp['LOCATION'] == 'AUT']

# belarus
df_BEL_GDP = pd.read_csv('GDP.csv')
df_BEL_GDP = df_BEL_GDP[df_BEL_GDP['LOCATION'] == 'BEL']
df_BEL_longTermEmp = pd.read_csv('Long_term_unemployment_rate.csv')
df_BEL_longTermEmp = df_BEL_longTermEmp[df_BEL_longTermEmp['LOCATION'] =='BEL']
df_BEL_avgWage = pd.read_csv('Average_wage.csv')
df_BEL_avgWage =df_BEL_avgWage[df_BEL_avgWage['LOCATION'] == 'BEL']
df_BEL_EmpByEducatiob = pd.read_csv('Employment_by_education_level.csv')
df_BEL_EmpByEducatiob =df_BEL_EmpByEducatiob[df_BEL_EmpByEducatiob['LOCATION'] == 'BEL']
df_BEL_employmentRate = pd.read_csv('Employment_rate.csv')
df_BEL_employmentRate =df_BEL_employmentRate[df_BEL_employmentRate['LOCATION'] == 'BEL'].tail(50)
df_BEL_fertilityRate = pd.read_csv('Fertility_rates.csv')
df_BEL_fertilityRate =df_BEL_fertilityRate[df_BEL_fertilityRate['LOCATION'] == 'BEL']
df_BEL_govDebt = pd.read_csv('General_Government_debt.csv')
df_BEL_govDebt =df_BEL_govDebt[df_BEL_govDebt['LOCATION'] == 'BEL']
df_BEL_OldAgeDepedency = pd.read_csv('Old_age_dependency_ratio.csv')
df_BEL_OldAgeDepedency =df_BEL_OldAgeDepedency[df_BEL_OldAgeDepedency['LOCATION'] == 'BEL']
df_BEL_selfEmployed = pd.read_csv('Self_employment_rate.csv')
df_BEL_selfEmployed =df_BEL_selfEmployed[df_BEL_selfEmployed['LOCATION'] == 'BEL']
df_BEL_unemploment = pd.read_csv('Unemployment_rate.csv')
df_BEL_unemploment =df_BEL_unemploment[df_BEL_unemploment['LOCATION'] == 'BEL']
df_BEL_youngPopulation = pd.read_csv('Young_population.csv')
df_BEL_youngPopulation =df_BEL_youngPopulation[df_BEL_youngPopulation['LOCATION'] == 'BEL']
df_BEL_youthEmp = pd.read_csv('Youth_unemployment_rate.csv')
df_BEL_youthEmp =df_BEL_youthEmp[df_BEL_youthEmp['LOCATION'] == 'BEL']


# CANADA
df_CAN_GDP = pd.read_csv('GDP.csv')
df_CAN_GDP = df_CAN_GDP[df_CAN_GDP['LOCATION'] == 'CAN']
df_CAN_longTermEmp = pd.read_csv('Long_term_unemployment_rate.csv')
df_CAN_longTermEmp = df_CAN_longTermEmp[df_CAN_longTermEmp['LOCATION'] =='CAN']
df_CAN_avgWage = pd.read_csv('Average_wage.csv')
df_CAN_avgWage =df_CAN_avgWage[df_CAN_avgWage['LOCATION'] == 'CAN']
df_CAN_EmpByEducatiob = pd.read_csv('Employment_by_education_level.csv')
df_CAN_EmpByEducatiob =df_CAN_EmpByEducatiob[df_CAN_EmpByEducatiob['LOCATION'] == 'CAN']
df_CAN_employmentRate = pd.read_csv('Employment_rate.csv')
df_CAN_employmentRate =df_CAN_employmentRate[df_CAN_employmentRate['LOCATION'] == 'CAN'].tail(50)
df_CAN_fertilityRate = pd.read_csv('Fertility_rates.csv')
df_CAN_fertilityRate =df_CAN_fertilityRate[df_CAN_fertilityRate['LOCATION'] == 'CAN']
df_CAN_govDebt = pd.read_csv('General_Government_debt.csv')
df_CAN_govDebt =df_CAN_govDebt[df_CAN_govDebt['LOCATION'] == 'CAN']
df_CAN_OldAgeDepedency = pd.read_csv('Old_age_dependency_ratio.csv')
df_CAN_OldAgeDepedency =df_CAN_OldAgeDepedency[df_CAN_OldAgeDepedency['LOCATION'] == 'CAN']
df_CAN_selfEmployed = pd.read_csv('Self_employment_rate.csv')
df_CAN_selfEmployed =df_CAN_selfEmployed[df_CAN_selfEmployed['LOCATION'] == 'CAN']
df_CAN_unemploment = pd.read_csv('Unemployment_rate.csv')
df_CAN_unemploment =df_CAN_unemploment[df_CAN_unemploment['LOCATION'] == 'CAN']
df_CAN_youngPopulation = pd.read_csv('Young_population.csv')
df_CAN_youngPopulation =df_CAN_youngPopulation[df_CAN_youngPopulation['LOCATION'] == 'CAN']
df_CAN_youthEmp = pd.read_csv('Youth_unemployment_rate.csv')
df_CAN_youthEmp =df_CAN_youthEmp[df_CAN_youthEmp['LOCATION'] == 'CAN']

# DENMARK
df_DEN_GDP = pd.read_csv('GDP.csv')
df_DEN_GDP = df_DEN_GDP[df_DEN_GDP['LOCATION'] == 'DNK']
df_DEN_longTermEmp = pd.read_csv('Long_term_unemployment_rate.csv')
df_DEN_longTermEmp = df_DEN_longTermEmp[df_DEN_longTermEmp['LOCATION'] =='DNK']
df_DEN_avgWage = pd.read_csv('Average_wage.csv')
df_DEN_avgWage =df_DEN_avgWage[df_DEN_avgWage['LOCATION'] == 'DNK']
df_DEN_EmpByEducatiob = pd.read_csv('Employment_by_education_level.csv')
df_DEN_EmpByEducatiob =df_DEN_EmpByEducatiob[df_DEN_EmpByEducatiob['LOCATION'] == 'DNK']
df_DEN_employmentRate = pd.read_csv('Employment_rate.csv')
df_DEN_employmentRate =df_DEN_employmentRate[df_DEN_employmentRate['LOCATION'] == 'DNK'].tail(50)
df_DEN_fertilityRate = pd.read_csv('Fertility_rates.csv')
df_DEN_fertilityRate =df_DEN_fertilityRate[df_DEN_fertilityRate['LOCATION'] == 'DNK']
df_DEN_govDebt = pd.read_csv('General_Government_debt.csv')
df_DEN_govDebt =df_DEN_govDebt[df_DEN_govDebt['LOCATION'] == 'DNK']
df_DEN_OldAgeDepedency = pd.read_csv('Old_age_dependency_ratio.csv')
df_DEN_OldAgeDepedency =df_DEN_OldAgeDepedency[df_DEN_OldAgeDepedency['LOCATION'] == 'DNK']
df_DEN_selfEmployed = pd.read_csv('Self_employment_rate.csv')
df_DEN_selfEmployed =df_DEN_selfEmployed[df_DEN_selfEmployed['LOCATION'] == 'DNK']
df_DEN_unemploment = pd.read_csv('Unemployment_rate.csv')
df_DEN_unemploment =df_DEN_unemploment[df_DEN_unemploment['LOCATION'] == 'DNK']
df_DEN_youngPopulation = pd.read_csv('Young_population.csv')
df_DEN_youngPopulation =df_DEN_youngPopulation[df_DEN_youngPopulation['LOCATION'] == 'DNK']
df_DEN_youthEmp = pd.read_csv('Youth_unemployment_rate.csv')
df_DEN_youthEmp =df_DEN_youthEmp[df_DEN_youthEmp['LOCATION'] == 'DNK']

# CZECH REPUBLIC
df_CZE_GDP = pd.read_csv('GDP.csv')
df_CZE_GDP = df_CZE_GDP[df_CZE_GDP['LOCATION'] == 'CZE']
df_CZE_longTermEmp = pd.read_csv('Long_term_unemployment_rate.csv')
df_CZE_longTermEmp = df_CZE_longTermEmp[df_CZE_longTermEmp['LOCATION'] =='CZE']
df_CZE_avgWage = pd.read_csv('Average_wage.csv')
df_CZE_avgWage =df_CZE_avgWage[df_CZE_avgWage['LOCATION'] == 'CZE']
df_CZE_EmpByEducatiob = pd.read_csv('Employment_by_education_level.csv')
df_CZE_EmpByEducatiob =df_CZE_EmpByEducatiob[df_CZE_EmpByEducatiob['LOCATION'] == 'CZE']
df_CZE_employmentRate = pd.read_csv('Employment_rate.csv')
df_CZE_employmentRate =df_CZE_employmentRate[df_CZE_employmentRate['LOCATION'] == 'CZE'].tail(50)
df_CZE_fertilityRate = pd.read_csv('Fertility_rates.csv')
df_CZE_fertilityRate =df_CZE_fertilityRate[df_CZE_fertilityRate['LOCATION'] == 'CZE']
df_CZE_govDebt = pd.read_csv('General_Government_debt.csv')
df_CZE_govDebt =df_CZE_govDebt[df_CZE_govDebt['LOCATION'] == 'CZE']
df_CZE_OldAgeDepedency = pd.read_csv('Old_age_dependency_ratio.csv')
df_CZE_OldAgeDepedency =df_CZE_OldAgeDepedency[df_CZE_OldAgeDepedency['LOCATION'] == 'CZE']
df_CZE_selfEmployed = pd.read_csv('Self_employment_rate.csv')
df_CZE_selfEmployed =df_CZE_selfEmployed[df_CZE_selfEmployed['LOCATION'] == 'CZE']
df_CZE_unemploment = pd.read_csv('Unemployment_rate.csv')
df_CZE_unemploment =df_CZE_unemploment[df_CZE_unemploment['LOCATION'] == 'CZE']
df_CZE_youngPopulation = pd.read_csv('Young_population.csv')
df_CZE_youngPopulation =df_CZE_youngPopulation[df_CZE_youngPopulation['LOCATION'] == 'CZE']
df_CZE_youthEmp = pd.read_csv('Youth_unemployment_rate.csv')
df_CZE_youthEmp =df_CZE_youthEmp[df_CZE_youthEmp['LOCATION'] == 'CZE']

# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "Number of students per education level", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("AUSTRALIA", href="/ca_AUSTRALIA", active="exact"),
                dbc.NavLink("AUSTRIA", href="/ca_AUSTRIA", active="exact"),
                dbc.NavLink("BELARUS", href="/ca_BELARUS", active="exact"),
                dbc.NavLink("CANADA", href="/ca_CANADA", active="exact"),
                dbc.NavLink("DENMARK", href="/ca_DENMARK", active="exact"),
                dbc.NavLink("CZECH REPUBLIC", href="/ca_CZECHREPUBLIC", active="exact"),
                dbc.NavLink("Page 2", href="/page-2", active="exact"),

            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content
])


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return [
            html.H1('Kindergarten in Iran',
                    style={'textAlign': 'center'}),
            dcc.Graph(id='bargraph',
                      figure=px.bar(df, barmode='group', x='Years',
                                    y=['Girls Kindergarten', 'Boys Kindergarten']))
        ]
    elif pathname == "/ca_AUSTRALIA":
        # australia
        return html.Div([
            html.H1("AUSTRALIA", style={'textAlign': 'center'}),
            # GDP
            dcc.Graph(
                figure={
                    'data': [
                       {'x': df_AUS_GDP['TIME'], 'y': df_AUS_GDP['Value'],
                           'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'AUSTRALIA GDP',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'GDP',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # LONG TERM UNEMPLOYEMENT
            dcc.Graph(
                figure={
                    'data': [
                       {'x': df_AUS_longTermEmp['TIME'], 'y': df_AUS_longTermEmp['Value'],
                           'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'AUSTRALIA LONG TERM UNEMPLOYMENT RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'PEOPLE UNEMPLOYED',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # AVERAGE WAGE
            dcc.Graph(
                figure={
                    'data': [
                       {'x': df_AUS_avgWage['TIME'], 'y': df_AUS_avgWage['Value'],
                           'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'AUSTRALIA AVERAGE WAGE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'AVERAGE WAGE',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # employement by education
            dcc.Graph(
                figure={
                    'data': [
                       {'x': df_AUS_EmpByEducatiob['TIME'], 'y': df_AUS_EmpByEducatiob['Value'],
                           'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'AUSTRALIA EMPLOYMENT BY EDUCATION',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'PEOPLE EMPLOYED',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # EMPLOYEMENT RATE
            dcc.Graph(
                figure={

                    'data': [
                       {'x': df_AUS_employmentRate['TIME'], 'y': df_AUS_employmentRate['Value'],
                           'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'AUSTRALIA EMPLOYMENT RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'PEOPLE EMPLOYED',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # fertilityRate
            dcc.Graph(
                figure={
                    'data': [
                       {'x': df_AUS_fertilityRate['TIME'], 'y': df_AUS_fertilityRate['Value'],
                           'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': ' FERITILITY RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'NEW BORNS',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # gov debt
            dcc.Graph(
                figure={
                    'data': [
                       {'x': df_AUS_govDebt['TIME'], 'y': df_AUS_govDebt['Value'],
                           'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'GENERAL GOVERNMENT DEBT',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'Gov. Debt',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # old age dependency
            dcc.Graph(
                figure={
                    'data': [
                       {'x': df_AUS_OldAgeDepedency['TIME'], 'y': df_AUS_OldAgeDepedency['Value'],
                           'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'OLD AGE DEPENDENCY RATIO',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'OLD age people > 50 years',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # self employment / self owned business
            dcc.Graph(
                figure={
                    'data': [
                       {'x': df_AUS_OldAgeDepedency['TIME'], 'y': df_AUS_OldAgeDepedency['Value'],
                           'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'OLD AGE DEPENDENCY RATIO',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'OLD age people > 50 years',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # df_AUS_selfEmployed
            dcc.Graph(
                figure={
                    'data': [
                       {'x': df_AUS_selfEmployed['TIME'], 'y': df_AUS_selfEmployed['Value'],
                           'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'SELF EMPLOYMENT RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'Self Employement/ Business Owners',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # df_AUS_youngPopulation
            dcc.Graph(
                figure={
                    'data': [
                       {'x': df_AUS_youngPopulation['TIME'], 'y': df_AUS_youngPopulation['Value'],
                           'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'YOUNG POPULATION',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'YOUNG POPULATION',
                        },

                    }
                }, style={'width': '100%', 'float': 'center', 'margin-left': '2%'}
            ),
            # df_AUS_unemploment
            dcc.Graph(
                figure={
                    'data': [
                       {'x': df_AUS_unemploment['TIME'], 'y': df_AUS_unemploment['Value'],
                           'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'UNEMPLOYMENT RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'Unemployement rate',
                        },

                    }
                }, style={'width': '100%', 'float': 'left', 'margin-left': '2%'}
            ),
            # df_AUS_youthEmp
            dcc.Graph(
                figure={
                    'data': [
                       {'x': df_AUS_youthEmp['TIME'], 'y': df_AUS_youthEmp['Value'],
                           'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'YOUTH EMPLOYEMENT',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'YOUTH EMPLOYMENT',
                        },

                    }
                }, style={'width': '100%', 'float': 'center', 'margin-left': '2%'}
            )

        ])
    elif pathname == "/ca_AUSTRIA":
        # austria
        return html.Div([
            html.H1("AUSTRIA", style={'textAlign': 'center'}),
            # GDP
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_AUT_GDP['TIME'], 'y': df_AUT_GDP['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'AUSTRIA GDP',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'GDP',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # LONG TERM UNEMPLOYEMENT
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_AUT_longTermEmp['TIME'], 'y': df_AUT_longTermEmp['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'AUSTRIA LONG TERM UNEMPLOYMENT RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'PEOPLE UNEMPLOYED',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # AVERAGE WAGE
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_AUT_avgWage['TIME'], 'y': df_AUT_avgWage['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'AUSTRIA AVERAGE WAGE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'AVERAGE WAGE',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # employement by education
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_AUT_EmpByEducatiob['TIME'], 'y': df_AUT_EmpByEducatiob['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'AUSTRIA EMPLOYMENT BY EDUCATION',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'PEOPLE EMPLOYED',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # EMPLOYEMENT RATE
            dcc.Graph(
                figure={

                    'data': [
                        {'x': df_AUT_employmentRate['TIME'], 'y': df_AUT_employmentRate['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'AUSTRIA EMPLOYMENT RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'PEOPLE EMPLOYED',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # fertilityRate
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_AUT_fertilityRate['TIME'], 'y': df_AUT_fertilityRate['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': ' FERITILITY RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'NEW BORNS',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # gov debt
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_AUT_govDebt['TIME'], 'y': df_AUT_govDebt['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'GENERAL GOVERNMENT DEBT',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'Gov. Debt',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # old age dependency
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_AUT_OldAgeDepedency['TIME'], 'y': df_AUT_OldAgeDepedency['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'OLD AGE DEPENDENCY RATIO',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'OLD age people > 50 years',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # self employment / self owned business
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_AUT_OldAgeDepedency['TIME'], 'y': df_AUT_OldAgeDepedency['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'OLD AGE DEPENDENCY RATIO',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'OLD age people > 50 years',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # df_AUS_selfEmployed
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_AUT_selfEmployed['TIME'], 'y': df_AUT_selfEmployed['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'SELF EMPLOYMENT RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'Self Employement/ Business Owners',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # df_AUS_youngPopulation
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_AUT_youngPopulation['TIME'], 'y': df_AUT_youngPopulation['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'YOUNG POPULATION',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'YOUNG POPULATION',
                        },

                    }
                }, style={'width': '100%', 'float': 'center', 'margin-left': '2%'}
            ),
            # df_AUS_unemploment
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_AUT_unemploment['TIME'], 'y': df_AUT_unemploment['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'UNEMPLOYMENT RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'Unemployement rate',
                        },

                    }
                }, style={'width': '100%', 'float': 'left', 'margin-left': '2%'}
            ),
            # df_AUS_youthEmp
            dcc.Graph(
                figure={
                    'data': [
                       {'x': df_AUT_youthEmp['TIME'], 'y': df_AUT_youthEmp['Value'],
                           'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'YOUTH EMPLOYEMENT',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'YOUTH EMPLOYMENT',
                        },

                    }
                }, style={'width': '100%', 'float': 'center', 'margin-left': '2%'}
            )
        ])
    elif pathname == "/ca_BELARUS":
         return html.Div([
            html.H1("BELARUS", style={'textAlign': 'center'}),
            # GDP
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_BEL_GDP['TIME'], 'y': df_BEL_GDP['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'BELARUS GDP',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'GDP',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # LONG TERM UNEMPLOYEMENT
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_BEL_longTermEmp['TIME'], 'y': df_BEL_longTermEmp['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'BELARUS LONG TERM UNEMPLOYMENT RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'PEOPLE UNEMPLOYED',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # AVERAGE WAGE
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_BEL_avgWage['TIME'], 'y': df_BEL_avgWage['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'BELARUS AVERAGE WAGE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'AVERAGE WAGE',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # employement by education
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_BEL_EmpByEducatiob['TIME'], 'y': df_BEL_EmpByEducatiob['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'BELARUS EMPLOYMENT BY EDUCATION',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'PEOPLE EMPLOYED',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # EMPLOYEMENT RATE
            dcc.Graph(
                figure={

                    'data': [
                        {'x': df_BEL_employmentRate['TIME'], 'y': df_BEL_employmentRate['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'BELARUS EMPLOYMENT RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'PEOPLE EMPLOYED',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # fertilityRate
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_BEL_fertilityRate['TIME'], 'y': df_BEL_fertilityRate['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': ' FERITILITY RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'NEW BORNS',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # gov debt
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_BEL_govDebt['TIME'], 'y': df_BEL_govDebt['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'GENERAL GOVERNMENT DEBT',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'Gov. Debt',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # old age dependency
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_BEL_OldAgeDepedency['TIME'], 'y': df_BEL_OldAgeDepedency['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'OLD AGE DEPENDENCY RATIO',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'OLD age people > 50 years',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # self employment / self owned business
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_BEL_OldAgeDepedency['TIME'], 'y': df_BEL_OldAgeDepedency['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'OLD AGE DEPENDENCY RATIO',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'OLD age people > 50 years',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # df_AUS_selfEmployed
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_BEL_selfEmployed['TIME'], 'y': df_BEL_selfEmployed['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'SELF EMPLOYMENT RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'Self Employement/ Business Owners',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # df_AUS_youngPopulation
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_BEL_youngPopulation['TIME'], 'y': df_BEL_youngPopulation['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'YOUNG POPULATION',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'YOUNG POPULATION',
                        },

                    }
                }, style={'width': '100%', 'float': 'center', 'margin-left': '2%'}
            ),
            # df_AUS_unemploment
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_BEL_unemploment['TIME'], 'y': df_BEL_unemploment['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'UNEMPLOYMENT RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'Unemployement rate',
                        },

                    }
                }, style={'width': '100%', 'float': 'left', 'margin-left': '2%'}
            ),
            # df_AUS_youthEmp
            dcc.Graph(
                figure={
                    'data': [
                       {'x': df_BEL_youthEmp['TIME'], 'y': df_BEL_youthEmp['Value'],
                           'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'YOUTH EMPLOYEMENT',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'YOUTH EMPLOYMENT',
                        },

                    }
                }, style={'width': '100%', 'float': 'center', 'margin-left': '2%'}
            )
        ])
    elif pathname == "/ca_CANADA":
         return html.Div([
            html.H1("CANADA", style={'textAlign': 'center'}),
            # GDP
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_CAN_GDP['TIME'], 'y': df_CAN_GDP['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'CANADA GDP',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'GDP',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # LONG TERM UNEMPLOYEMENT
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_CAN_longTermEmp['TIME'], 'y': df_CAN_longTermEmp['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'CANADA LONG TERM UNEMPLOYMENT RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'PEOPLE UNEMPLOYED',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # AVERAGE WAGE
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_CAN_avgWage['TIME'], 'y': df_CAN_avgWage['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'CANADA AVERAGE WAGE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'AVERAGE WAGE',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # employement by education
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_CAN_EmpByEducatiob['TIME'], 'y': df_CAN_EmpByEducatiob['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'CANADA EMPLOYMENT BY EDUCATION',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'PEOPLE EMPLOYED',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # EMPLOYEMENT RATE
            dcc.Graph(
                figure={

                    'data': [
                        {'x': df_CAN_employmentRate['TIME'], 'y': df_CAN_employmentRate['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'CANADA EMPLOYMENT RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'PEOPLE EMPLOYED',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # fertilityRate
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_CAN_fertilityRate['TIME'], 'y': df_CAN_fertilityRate['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': ' FERITILITY RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'NEW BORNS',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # gov debt
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_CAN_govDebt['TIME'], 'y': df_CAN_govDebt['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'GENERAL GOVERNMENT DEBT',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'Gov. Debt',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # old age dependency
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_CAN_OldAgeDepedency['TIME'], 'y': df_CAN_OldAgeDepedency['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'OLD AGE DEPENDENCY RATIO',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'OLD age people > 50 years',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # self employment / self owned business
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_CAN_OldAgeDepedency['TIME'], 'y': df_CAN_OldAgeDepedency['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'OLD AGE DEPENDENCY RATIO',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'OLD age people > 50 years',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # df_AUS_selfEmployed
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_CAN_selfEmployed['TIME'], 'y': df_CAN_selfEmployed['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'SELF EMPLOYMENT RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'Self Employement/ Business Owners',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # df_AUS_youngPopulation
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_CAN_youngPopulation['TIME'], 'y': df_CAN_youngPopulation['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'YOUNG POPULATION',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'YOUNG POPULATION',
                        },

                    }
                }, style={'width': '100%', 'float': 'center', 'margin-left': '2%'}
            ),
            # df_AUS_unemploment
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_CAN_unemploment['TIME'], 'y': df_CAN_unemploment['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'UNEMPLOYMENT RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'Unemployement rate',
                        },

                    }
                }, style={'width': '100%', 'float': 'left', 'margin-left': '2%'}
            ),
            # df_AUS_youthEmp
            dcc.Graph(
                figure={
                    'data': [
                       {'x': df_CAN_youthEmp['TIME'], 'y': df_CAN_youthEmp['Value'],
                           'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'YOUTH EMPLOYEMENT',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'YOUTH EMPLOYMENT',
                        },

                    }
                }, style={'width': '100%', 'float': 'center', 'margin-left': '2%'}
            )
        ])
    elif pathname == "/ca_DENMARK":
         return html.Div([
            html.H1("DENMARK", style={'textAlign': 'center'}),
            # GDP
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_DEN_GDP['TIME'], 'y': df_DEN_GDP['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'DENMARK GDP',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'GDP',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # LONG TERM UNEMPLOYEMENT
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_DEN_longTermEmp['TIME'], 'y': df_DEN_longTermEmp['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'DENMARK LONG TERM UNEMPLOYMENT RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'PEOPLE UNEMPLOYED',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # AVERAGE WAGE
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_DEN_avgWage['TIME'], 'y': df_DEN_avgWage['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'DENMARK AVERAGE WAGE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'AVERAGE WAGE',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # employement by education
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_DEN_EmpByEducatiob['TIME'], 'y': df_DEN_EmpByEducatiob['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'DENMARK EMPLOYMENT BY EDUCATION',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'PEOPLE EMPLOYED',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # EMPLOYEMENT RATE
            dcc.Graph(
                figure={

                    'data': [
                        {'x': df_DEN_employmentRate['TIME'], 'y': df_DEN_employmentRate['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'DENMARK EMPLOYMENT RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'PEOPLE EMPLOYED',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # fertilityRate
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_DEN_fertilityRate['TIME'], 'y': df_DEN_fertilityRate['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': ' FERITILITY RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'NEW BORNS',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # gov debt
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_DEN_govDebt['TIME'], 'y': df_DEN_govDebt['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'GENERAL GOVERNMENT DEBT',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'Gov. Debt',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # old age dependency
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_DEN_OldAgeDepedency['TIME'], 'y': df_DEN_OldAgeDepedency['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'OLD AGE DEPENDENCY RATIO',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'OLD age people > 50 years',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # self employment / self owned business
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_DEN_OldAgeDepedency['TIME'], 'y': df_DEN_OldAgeDepedency['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'OLD AGE DEPENDENCY RATIO',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'OLD age people > 50 years',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # df_AUS_selfEmployed
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_DEN_selfEmployed['TIME'], 'y': df_DEN_selfEmployed['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'SELF EMPLOYMENT RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'Self Employement/ Business Owners',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # df_AUS_youngPopulation
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_DEN_youngPopulation['TIME'], 'y': df_DEN_youngPopulation['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'YOUNG POPULATION',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'YOUNG POPULATION',
                        },

                    }
                }, style={'width': '100%', 'float': 'center', 'margin-left': '2%'}
            ),
            # df_AUS_unemploment
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_DEN_unemploment['TIME'], 'y': df_DEN_unemploment['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'UNEMPLOYMENT RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'Unemployement rate',
                        },

                    }
                }, style={'width': '100%', 'float': 'left', 'margin-left': '2%'}
            ),
            # df_AUS_youthEmp
            dcc.Graph(
                figure={
                    'data': [
                       {'x': df_DEN_youthEmp['TIME'], 'y': df_DEN_youthEmp['Value'],
                           'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'YOUTH EMPLOYEMENT',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'YOUTH EMPLOYMENT',
                        },

                    }
                }, style={'width': '100%', 'float': 'center', 'margin-left': '2%'}
            )
        ])
    elif pathname == "ca_CZECHREPUBLIC":
        return html.Div([
            html.H1("CZECH REPUBLIC", style={'textAlign': 'center'}),
            # GDP
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_CZE_GDP['TIME'], 'y': df_CZE_GDP['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'CZECH REPUBLIC GDP',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'GDP',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # LONG TERM UNEMPLOYEMENT
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_CZE_longTermEmp['TIME'], 'y': df_CZE_longTermEmp['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'CZECH REPUBLIC LONG TERM UNEMPLOYMENT RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'PEOPLE UNEMPLOYED',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # AVERAGE WAGE
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_CZE_avgWage['TIME'], 'y': df_CZE_avgWage['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'CZECH REPUBLIC AVERAGE WAGE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'AVERAGE WAGE',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # employement by education
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_CZE_EmpByEducatiob['TIME'], 'y': df_CZE_EmpByEducatiob['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'CZECH REPUBLIC EMPLOYMENT BY EDUCATION',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'PEOPLE EMPLOYED',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # EMPLOYEMENT RATE
            dcc.Graph(
                figure={

                    'data': [
                        {'x': df_CZE_employmentRate['TIME'], 'y': df_CZE_employmentRate['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'CZECH REPUBLIC EMPLOYMENT RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'PEOPLE EMPLOYED',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # fertilityRate
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_CZE_fertilityRate['TIME'], 'y': df_CZE_fertilityRate['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': ' FERITILITY RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'NEW BORNS',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # gov debt
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_CZE_govDebt['TIME'], 'y': df_CZE_govDebt['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'GENERAL GOVERNMENT DEBT',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'Gov. Debt',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # old age dependency
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_CZE_OldAgeDepedency['TIME'], 'y': df_CZE_OldAgeDepedency['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'OLD AGE DEPENDENCY RATIO',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'OLD age people > 50 years',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # self employment / self owned business
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_CZE_OldAgeDepedency['TIME'], 'y': df_CZE_OldAgeDepedency['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'OLD AGE DEPENDENCY RATIO',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'OLD age people > 50 years',
                        },

                    }
                }, style={'width': '45%', 'float': 'right', 'margin-left': '2%'}
            ),
            # df_AUS_selfEmployed
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_CZE_selfEmployed['TIME'], 'y': df_CZE_selfEmployed['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'SELF EMPLOYMENT RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'Self Employement/ Business Owners',
                        },

                    }
                }, style={'width': '45%', 'float': 'left', 'margin-left': '2%'}
            ),
            # df_AUS_youngPopulation
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_CZE_youngPopulation['TIME'], 'y': df_CZE_youngPopulation['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'YOUNG POPULATION',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'YOUNG POPULATION',
                        },

                    }
                }, style={'width': '100%', 'float': 'center', 'margin-left': '2%'}
            ),
            # df_AUS_unemploment
            dcc.Graph(
                figure={
                    'data': [
                        {'x': df_CZE_unemploment['TIME'], 'y': df_CZE_unemploment['Value'],
                            'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'UNEMPLOYMENT RATE',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'Unemployement rate',
                        },

                    }
                }, style={'width': '100%', 'float': 'left', 'margin-left': '2%'}
            ),
            # df_AUS_youthEmp
            dcc.Graph(
                figure={
                    'data': [
                       {'x': df_CZE_youthEmp['TIME'], 'y': df_CZE_youthEmp['Value'],
                           'label-x': 'YEAR', 'label-y': 'VALUE', 'type': 'bar'}
                    ],
                    'layout':{
                        'title': 'YOUTH EMPLOYEMENT',
                        'colorway': ["#5293ff"],
                        'xaxis':{
                            'title': 'year',
                        },
                        'yaxis': {
                            'title': 'YOUTH EMPLOYMENT',
                        },

                    }
                }, style={'width': '100%', 'float': 'center', 'margin-left': '2%'}
            )
        ])
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

# app.layout = dbc.Container(
#       [sidebar , dl.plugins.page_container],
#       fluid = True,
# )


if __name__ == '__main__':
    app.run_server(debug=True, port=3000)
