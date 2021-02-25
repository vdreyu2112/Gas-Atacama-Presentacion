import dash_bootstrap_components as dbc
import dash_core_components as dcc
import plotly.graph_objs as go
import dash_html_components as html
import plotly.io as pio
import pandas as pd
import dash_table
import plotly_express as px
from plotly.subplots import make_subplots
from dash.dependencies import Input, Output
import psycopg2

from app import app

param_dic = {
    "host"      : "localhost",
    "database"  : "gas_atacama",
    "user"      : "postgres",
    "password"  : "c1b21ch"
}
def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        SystemExit(1)
    print("Connection successful")
    return conn

def postgresql_to_dataframe(conn, select_query, column_names):
    """
    Tranform a SELECT query into a pandas dataframe
    """
    cursor = conn.cursor()
    try:
        cursor.execute(select_query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1
    
    # Naturally we get a list of tupples
    tupples = cursor.fetchall()
    cursor.close()
    
    # We just need to turn it into a pandas dataframe
    df = pd.DataFrame(tupples, columns=column_names)
    return df

conn = connect(param_dic)
column_names = ["fecha", "potencial", "cmp", "ma10"]

pio.templates.default = "simple_white"
# Execute the "SELECT *" query
df1 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 006' ", column_names)
df1['ma10'] = df1['potencial'].rolling(10).mean()
df2 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 010' ", column_names)
df2['ma10'] = df2['potencial'].rolling(10).mean()
df3 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 017' ", column_names)
df3['ma10'] = df3['potencial'].rolling(10).mean()
df4 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 021' ", column_names)
df4['ma10'] = df4['potencial'].rolling(10).mean()
df5 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 034' ", column_names)
df5['ma10'] = df5['potencial'].rolling(10).mean()
df6 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 043' ", column_names)
df6['ma10'] = df6['potencial'].rolling(10).mean()
df7 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 056' ", column_names)
df7['ma10'] = df7['potencial'].rolling(10).mean()
df8 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 071' ", column_names)
df8['ma10'] = df8['potencial'].rolling(10).mean()
df9 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 084' ", column_names)
df9['ma10'] = df9['potencial'].rolling(10).mean()
df10 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 090' ", column_names)
df10['ma10'] = df10['potencial'].rolling(10).mean()
df11 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 101' ", column_names)
df11['ma10'] = df11['potencial'].rolling(10).mean()
df12 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 105' ", column_names)
df12['ma10'] = df12['potencial'].rolling(10).mean()
df13 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 122' ", column_names)
df13['ma10'] = df13['potencial'].rolling(10).mean()
df14 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 143' ", column_names)
df14['ma10'] = df14['potencial'].rolling(10).mean()
df15 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 153' ", column_names)
df15['ma10'] = df15['potencial'].rolling(10).mean()
df16 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 173' ", column_names)
df16['ma10'] = df16['potencial'].rolling(10).mean()
df17 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 184' ", column_names)
df17['ma10'] = df17['potencial'].rolling(10).mean()
df18 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 203' ", column_names)
df18['ma10'] = df18['potencial'].rolling(10).mean()
df19 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 220' ", column_names)
df19['ma10'] = df19['potencial'].rolling(10).mean()
df20 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 221 02AN' ", column_names)
df20['ma10'] = df20['potencial'].rolling(10).mean()
df21 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 236' ", column_names)
df21['ma10'] = df21['potencial'].rolling(10).mean()
df22 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 245' ", column_names)
df22['ma10'] = df22['potencial'].rolling(10).mean()
df23 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 249' ", column_names)
df23['ma10'] = df23['potencial'].rolling(10).mean()
df24 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 259' ", column_names)
df24['ma10'] = df24['potencial'].rolling(10).mean()
df25 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 271' ", column_names)
df25['ma10'] = df25['potencial'].rolling(10).mean()
df26 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 278' ", column_names)
df26['ma10'] = df26['potencial'].rolling(10).mean()
df27 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 284' ", column_names)
df27['ma10'] = df27['potencial'].rolling(10).mean()
df28 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 289' ", column_names)
df28['ma10'] = df28['potencial'].rolling(10).mean()
df29 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 295' ", column_names)
df29['ma10'] = df29['potencial'].rolling(10).mean()
df30 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 300' ", column_names)
df30['ma10'] = df30['potencial'].rolling(10).mean()
df31 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 307' ", column_names)
df31['ma10'] = df31['potencial'].rolling(10).mean()
df32 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 312' ", column_names)
df32['ma10'] = df32['potencial'].rolling(10).mean()
df33 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 318' ", column_names)
df33['ma10'] = df33['potencial'].rolling(10).mean()
df34 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 326' ", column_names)
df34['ma10'] = df34['potencial'].rolling(10).mean()
df35 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 332' ", column_names)
df35['ma10'] = df35['potencial'].rolling(10).mean()
df36 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 337' ", column_names)
df36['ma10'] = df36['potencial'].rolling(10).mean()
df37 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 345' ", column_names)
df37['ma10'] = df37['potencial'].rolling(10).mean()
df38 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 350' ", column_names)
df38['ma10'] = df38['potencial'].rolling(10).mean()
df39 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 363' ", column_names)
df39['ma10'] = df39['potencial'].rolling(10).mean()
df40 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 368' ", column_names)
df40['ma10'] = df40['potencial'].rolling(10).mean()
df41 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 375' ", column_names)
df41['ma10'] = df41['potencial'].rolling(10).mean()
df42 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 380' ", column_names)
df42['ma10'] = df42['potencial'].rolling(10).mean()
df43 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 388' ", column_names)
df43['ma10'] = df43['potencial'].rolling(10).mean()
df44 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 389' ", column_names)
df44['ma10'] = df44['potencial'].rolling(10).mean()
df45 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 395' ", column_names)
df45['ma10'] = df45['potencial'].rolling(10).mean()
df46 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 405' ", column_names)
df46['ma10'] = df46['potencial'].rolling(10).mean()
df47 = postgresql_to_dataframe(conn, "select * from potenciales_on where cmp='CMP 412' ", column_names)
df47['ma10'] = df47['potencial'].rolling(10).mean()

fig1 = make_subplots(specs=[[{"secondary_y": True}]])
fig1.add_trace(go.Scatter(x=df1['fecha'], y=df1['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig1.add_trace(go.Scatter(x=df1['fecha'], y=df1['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig1.update_layout(title="Potencial ON CMP 006", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig1.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico1 = dbc.Card(
            [dcc.Graph(id='cmp006', figure=fig1)], body=True)

fig2 = make_subplots(specs=[[{"secondary_y": True}]])
fig2.add_trace(go.Scatter(x=df2['fecha'], y=df2['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig2.add_trace(go.Scatter(x=df2['fecha'], y=df2['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig2.update_layout(title="Potencial ON CMP 010", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig2.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico2 = dbc.Card(
            [dcc.Graph(id='cmp010', figure=fig2)], body=True)

fig3 = make_subplots(specs=[[{"secondary_y": True}]])
fig3.add_trace(go.Scatter(x=df3['fecha'], y=df3['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig3.add_trace(go.Scatter(x=df3['fecha'], y=df3['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig3.update_layout(title="Potencial ON CMP 017", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig3.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico3 = dbc.Card(
            [dcc.Graph(id='cmp017', figure=fig3)], body=True)

fig4 = make_subplots(specs=[[{"secondary_y": True}]])
fig4.add_trace(go.Scatter(x=df4['fecha'], y=df4['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig4.add_trace(go.Scatter(x=df4['fecha'], y=df4['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig4.update_layout(title="Potencial ON CMP 021", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig4.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico4 = dbc.Card(
            [dcc.Graph(id='cmp021', figure=fig4)], body=True)

fig5 = make_subplots(specs=[[{"secondary_y": True}]])
fig5.add_trace(go.Scatter(x=df5['fecha'], y=df5['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig5.add_trace(go.Scatter(x=df5['fecha'], y=df5['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig5.update_layout(title="Potencial ON CMP 034", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig5.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico5 = dbc.Card(
            [dcc.Graph(id='cmp034', figure=fig5)], body=True)

fig6 = make_subplots(specs=[[{"secondary_y": True}]])
fig6.add_trace(go.Scatter(x=df6['fecha'], y=df6['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig6.add_trace(go.Scatter(x=df6['fecha'], y=df6['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig6.update_layout(title="Potencial ON CMP 043", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig6.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico6 = dbc.Card(
            [dcc.Graph(id='cmp043', figure=fig6)], body=True)

fig7 = make_subplots(specs=[[{"secondary_y": True}]])
fig7.add_trace(go.Scatter(x=df7['fecha'], y=df7['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig7.add_trace(go.Scatter(x=df7['fecha'], y=df7['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig7.update_layout(title="Potencial ON CMP 056", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig7.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico7 = dbc.Card(
            [dcc.Graph(id='cmp056', figure=fig7)], body=True)

fig8 = make_subplots(specs=[[{"secondary_y": True}]])
fig8.add_trace(go.Scatter(x=df8['fecha'], y=df8['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig8.add_trace(go.Scatter(x=df8['fecha'], y=df8['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig8.update_layout(title="Potencial ON CMP 071", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig8.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico8 = dbc.Card(
            [dcc.Graph(id='cmp071', figure=fig8)], body=True)

fig9 = make_subplots(specs=[[{"secondary_y": True}]])
fig9.add_trace(go.Scatter(x=df9['fecha'], y=df9['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig9.add_trace(go.Scatter(x=df9['fecha'], y=df9['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig9.update_layout(title="Potencial ON CMP 084", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig9.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico9 = dbc.Card(
            [dcc.Graph(id='cmp084', figure=fig9)], body=True)

fig10 = make_subplots(specs=[[{"secondary_y": True}]])
fig10.add_trace(go.Scatter(x=df10['fecha'], y=df10['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig10.add_trace(go.Scatter(x=df10['fecha'], y=df10['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig10.update_layout(title="Potencial ON CMP 090", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig10.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico10 = dbc.Card(
            [dcc.Graph(id='cmp090', figure=fig10)], body=True)

fig11 = make_subplots(specs=[[{"secondary_y": True}]])
fig11.add_trace(go.Scatter(x=df11['fecha'], y=df11['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig11.add_trace(go.Scatter(x=df11['fecha'], y=df11['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig11.update_layout(title="Potencial ON CMP 101", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig11.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico11 = dbc.Card(
            [dcc.Graph(id='cmp101', figure=fig11)], body=True)

fig12 = make_subplots(specs=[[{"secondary_y": True}]])
fig12.add_trace(go.Scatter(x=df12['fecha'], y=df12['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig12.add_trace(go.Scatter(x=df12['fecha'], y=df12['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig12.update_layout(title="Potencial ON CMP 105", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig12.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico12 = dbc.Card(
            [dcc.Graph(id='cmp105', figure=fig12)], body=True)

fig13 = make_subplots(specs=[[{"secondary_y": True}]])
fig13.add_trace(go.Scatter(x=df13['fecha'], y=df13['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig13.add_trace(go.Scatter(x=df13['fecha'], y=df13['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig13.update_layout(title="Potencial ON CMP 122", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig13.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico13 = dbc.Card(
            [dcc.Graph(id='cmp122', figure=fig13)], body=True)

fig14 = make_subplots(specs=[[{"secondary_y": True}]])
fig14.add_trace(go.Scatter(x=df14['fecha'], y=df14['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig14.add_trace(go.Scatter(x=df14['fecha'], y=df14['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig14.update_layout(title="Potencial ON CMP 143", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig14.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico14 = dbc.Card(
            [dcc.Graph(id='cmp143', figure=fig14)], body=True)

fig15 = make_subplots(specs=[[{"secondary_y": True}]])
fig15.add_trace(go.Scatter(x=df15['fecha'], y=df15['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig15.add_trace(go.Scatter(x=df15['fecha'], y=df15['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig15.update_layout(title="Potencial ON CMP 153", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig15.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico15 = dbc.Card(
            [dcc.Graph(id='cmp153', figure=fig15)], body=True)

fig16 = make_subplots(specs=[[{"secondary_y": True}]])
fig16.add_trace(go.Scatter(x=df16['fecha'], y=df16['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig16.add_trace(go.Scatter(x=df16['fecha'], y=df16['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig16.update_layout(title="Potencial ON CMP 173", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig16.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico16 = dbc.Card(
            [dcc.Graph(id='cmp173', figure=fig16)], body=True)

fig17 = make_subplots(specs=[[{"secondary_y": True}]])
fig17.add_trace(go.Scatter(x=df17['fecha'], y=df17['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig17.add_trace(go.Scatter(x=df17['fecha'], y=df17['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig17.update_layout(title="Potencial ON CMP 184", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig17.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico17 = dbc.Card(
            [dcc.Graph(id='cmp184', figure=fig17)], body=True)

fig18 = make_subplots(specs=[[{"secondary_y": True}]])
fig18.add_trace(go.Scatter(x=df18['fecha'], y=df18['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig18.add_trace(go.Scatter(x=df18['fecha'], y=df18['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig18.update_layout(title="Potencial ON CMP 203", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig18.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico18 = dbc.Card(
            [dcc.Graph(id='cmp203', figure=fig18)], body=True)

fig19 = make_subplots(specs=[[{"secondary_y": True}]])
fig19.add_trace(go.Scatter(x=df19['fecha'], y=df19['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig19.add_trace(go.Scatter(x=df19['fecha'], y=df19['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig19.update_layout(title="Potencial ON CMP 220", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig19.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico19 = dbc.Card(
            [dcc.Graph(id='cmp220', figure=fig19)], body=True)

fig20 = make_subplots(specs=[[{"secondary_y": True}]])
fig20.add_trace(go.Scatter(x=df20['fecha'], y=df20['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig20.add_trace(go.Scatter(x=df20['fecha'], y=df20['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig20.update_layout(title="Potencial ON CMP 221 02AN", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig20.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico20 = dbc.Card(
            [dcc.Graph(id='cmp22102AN', figure=fig20)], body=True)

fig21 = make_subplots(specs=[[{"secondary_y": True}]])
fig21.add_trace(go.Scatter(x=df21['fecha'], y=df21['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig21.add_trace(go.Scatter(x=df21['fecha'], y=df21['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig21.update_layout(title="Potencial ON CMP 236", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig21.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico21 = dbc.Card(
            [dcc.Graph(id='cmp236', figure=fig21)], body=True)

fig22 = make_subplots(specs=[[{"secondary_y": True}]])
fig22.add_trace(go.Scatter(x=df22['fecha'], y=df22['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig22.add_trace(go.Scatter(x=df22['fecha'], y=df22['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig22.update_layout(title="Potencial ON CMP 245", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig22.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico22 = dbc.Card(
            [dcc.Graph(id='cmp245', figure=fig22)], body=True)

fig23 = make_subplots(specs=[[{"secondary_y": True}]])
fig23.add_trace(go.Scatter(x=df23['fecha'], y=df23['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig23.add_trace(go.Scatter(x=df23['fecha'], y=df23['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig23.update_layout(title="Potencial ON CMP 249", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig23.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico23 = dbc.Card(
            [dcc.Graph(id='cmp249', figure=fig23)], body=True)

fig24 = make_subplots(specs=[[{"secondary_y": True}]])
fig24.add_trace(go.Scatter(x=df24['fecha'], y=df24['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig24.add_trace(go.Scatter(x=df24['fecha'], y=df24['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig24.update_layout(title="Potencial ON CMP 259", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig24.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico24 = dbc.Card(
            [dcc.Graph(id='cmp259', figure=fig24)], body=True)

fig25 = make_subplots(specs=[[{"secondary_y": True}]])
fig25.add_trace(go.Scatter(x=df25['fecha'], y=df25['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig25.add_trace(go.Scatter(x=df25['fecha'], y=df25['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig25.update_layout(title="Potencial ON CMP 271", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig25.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico25 = dbc.Card(
            [dcc.Graph(id='cmp271', figure=fig25)], body=True)

fig26 = make_subplots(specs=[[{"secondary_y": True}]])
fig26.add_trace(go.Scatter(x=df26['fecha'], y=df26['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig26.add_trace(go.Scatter(x=df26['fecha'], y=df26['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig26.update_layout(title="Potencial ON CMP 278", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig26.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico26 = dbc.Card(
            [dcc.Graph(id='cmp278', figure=fig26)], body=True)

fig27 = make_subplots(specs=[[{"secondary_y": True}]])
fig27.add_trace(go.Scatter(x=df27['fecha'], y=df27['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig27.add_trace(go.Scatter(x=df27['fecha'], y=df27['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig27.update_layout(title="Potencial ON CMP 284", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig27.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico27 = dbc.Card(
            [dcc.Graph(id='cmp284', figure=fig27)], body=True)

fig28 = make_subplots(specs=[[{"secondary_y": True}]])
fig28.add_trace(go.Scatter(x=df28['fecha'], y=df28['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig28.add_trace(go.Scatter(x=df28['fecha'], y=df28['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig28.update_layout(title="Potencial ON CMP 289", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig28.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico28 = dbc.Card(
            [dcc.Graph(id='cmp289', figure=fig28)], body=True)

fig29 = make_subplots(specs=[[{"secondary_y": True}]])
fig29.add_trace(go.Scatter(x=df29['fecha'], y=df29['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig29.add_trace(go.Scatter(x=df29['fecha'], y=df29['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig29.update_layout(title="Potencial ON CMP 295", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig29.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico29 = dbc.Card(
            [dcc.Graph(id='cmp295', figure=fig29)], body=True)

fig30 = make_subplots(specs=[[{"secondary_y": True}]])
fig30.add_trace(go.Scatter(x=df30['fecha'], y=df30['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig30.add_trace(go.Scatter(x=df30['fecha'], y=df30['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig30.update_layout(title="Potencial ON CMP 300", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig30.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico30 = dbc.Card(
            [dcc.Graph(id='cmp300', figure=fig30)], body=True)

fig31 = make_subplots(specs=[[{"secondary_y": True}]])
fig31.add_trace(go.Scatter(x=df31['fecha'], y=df31['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig31.add_trace(go.Scatter(x=df31['fecha'], y=df31['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig31.update_layout(title="Potencial ON CMP 307", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig31.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico31 = dbc.Card(
            [dcc.Graph(id='cmp307', figure=fig31)], body=True)

fig32 = make_subplots(specs=[[{"secondary_y": True}]])
fig32.add_trace(go.Scatter(x=df32['fecha'], y=df32['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig32.add_trace(go.Scatter(x=df32['fecha'], y=df32['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig32.update_layout(title="Potencial ON CMP 312", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig32.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico32 = dbc.Card(
            [dcc.Graph(id='cmp312', figure=fig32)], body=True)

fig33 = make_subplots(specs=[[{"secondary_y": True}]])
fig33.add_trace(go.Scatter(x=df33['fecha'], y=df33['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig33.add_trace(go.Scatter(x=df33['fecha'], y=df33['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig33.update_layout(title="Potencial ON CMP 318", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig33.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico33 = dbc.Card(
            [dcc.Graph(id='cmp318', figure=fig33)], body=True)

fig34 = make_subplots(specs=[[{"secondary_y": True}]])
fig34.add_trace(go.Scatter(x=df34['fecha'], y=df34['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig34.add_trace(go.Scatter(x=df34['fecha'], y=df34['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig34.update_layout(title="Potencial ON CMP 326", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig34.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico34 = dbc.Card(
            [dcc.Graph(id='cmp326', figure=fig34)], body=True)

fig35 = make_subplots(specs=[[{"secondary_y": True}]])
fig35.add_trace(go.Scatter(x=df35['fecha'], y=df35['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig35.add_trace(go.Scatter(x=df35['fecha'], y=df35['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig35.update_layout(title="Potencial ON CMP 332", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig35.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico35 = dbc.Card(
            [dcc.Graph(id='cmp332', figure=fig35)], body=True)

fig36 = make_subplots(specs=[[{"secondary_y": True}]])
fig36.add_trace(go.Scatter(x=df36['fecha'], y=df36['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig36.add_trace(go.Scatter(x=df36['fecha'], y=df36['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig36.update_layout(title="Potencial ON CMP 337", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig36.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico36 = dbc.Card(
            [dcc.Graph(id='cmp337', figure=fig36)], body=True)

fig37 = make_subplots(specs=[[{"secondary_y": True}]])
fig37.add_trace(go.Scatter(x=df37['fecha'], y=df37['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig37.add_trace(go.Scatter(x=df37['fecha'], y=df37['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig37.update_layout(title="Potencial ON CMP 345", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig37.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico37 = dbc.Card(
            [dcc.Graph(id='cmp345', figure=fig37)], body=True)

fig38 = make_subplots(specs=[[{"secondary_y": True}]])
fig38.add_trace(go.Scatter(x=df38['fecha'], y=df38['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig38.add_trace(go.Scatter(x=df38['fecha'], y=df38['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig38.update_layout(title="Potencial ON CMP 350", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig38.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico38 = dbc.Card(
            [dcc.Graph(id='cmp350', figure=fig38)], body=True)
            
fig39 = make_subplots(specs=[[{"secondary_y": True}]])
fig39.add_trace(go.Scatter(x=df39['fecha'], y=df39['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig39.add_trace(go.Scatter(x=df39['fecha'], y=df39['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig39.update_layout(title="Potencial ON CMP 363", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig39.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico39 = dbc.Card(
            [dcc.Graph(id='cmp363', figure=fig39)], body=True)

fig40 = make_subplots(specs=[[{"secondary_y": True}]])
fig40.add_trace(go.Scatter(x=df40['fecha'], y=df40['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig40.add_trace(go.Scatter(x=df40['fecha'], y=df40['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig40.update_layout(title="Potencial ON CMP 368", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig40.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico40 = dbc.Card(
            [dcc.Graph(id='cmp368', figure=fig40)], body=True)

fig41 = make_subplots(specs=[[{"secondary_y": True}]])
fig41.add_trace(go.Scatter(x=df41['fecha'], y=df41['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig41.add_trace(go.Scatter(x=df41['fecha'], y=df41['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig41.update_layout(title="Potencial ON CMP 375", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig41.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico41 = dbc.Card(
            [dcc.Graph(id='cmp375', figure=fig41)], body=True)

fig42 = make_subplots(specs=[[{"secondary_y": True}]])
fig42.add_trace(go.Scatter(x=df42['fecha'], y=df42['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig42.add_trace(go.Scatter(x=df42['fecha'], y=df42['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig42.update_layout(title="Potencial ON CMP 380", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig42.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico42 = dbc.Card(
            [dcc.Graph(id='cmp380', figure=fig42)], body=True)

fig43 = make_subplots(specs=[[{"secondary_y": True}]])
fig43.add_trace(go.Scatter(x=df43['fecha'], y=df43['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig43.add_trace(go.Scatter(x=df43['fecha'], y=df43['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig43.update_layout(title="Potencial ON CMP 388", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig43.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico43 = dbc.Card(
            [dcc.Graph(id='cmp388', figure=fig43)], body=True)

fig44 = make_subplots(specs=[[{"secondary_y": True}]])
fig44.add_trace(go.Scatter(x=df44['fecha'], y=df44['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig44.add_trace(go.Scatter(x=df44['fecha'], y=df44['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig44.update_layout(title="Potencial ON CMP 389", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig44.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico44 = dbc.Card(
            [dcc.Graph(id='cmp389', figure=fig44)], body=True)

fig45 = make_subplots(specs=[[{"secondary_y": True}]])
fig45.add_trace(go.Scatter(x=df45['fecha'], y=df45['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig45.add_trace(go.Scatter(x=df45['fecha'], y=df45['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig45.update_layout(title="Potencial ON CMP 395", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig45.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico45 = dbc.Card(
            [dcc.Graph(id='cmp395', figure=fig45)], body=True)

fig46 = make_subplots(specs=[[{"secondary_y": True}]])
fig46.add_trace(go.Scatter(x=df46['fecha'], y=df46['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig46.add_trace(go.Scatter(x=df46['fecha'], y=df46['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig46.update_layout(title="Potencial ON CMP 405", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig46.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico46 = dbc.Card(
            [dcc.Graph(id='cmp405', figure=fig46)], body=True)

fig47 = make_subplots(specs=[[{"secondary_y": True}]])
fig47.add_trace(go.Scatter(x=df47['fecha'], y=df47['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', opacity=0.5, showlegend=False, hoverinfo="skip"), row=1, col=1)
fig47.add_trace(go.Scatter(x=df47['fecha'], y=df47['ma10'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON"), row=1, col=1)
fig47.update_layout(title="Potencial ON CMP 412", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig47.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico47 = dbc.Card(
            [dcc.Graph(id='cmp412', figure=fig47)], body=True)
        
tab1_content = dbc.Container(
    [
        html.Br(),
        html.H1("Potenciales ON"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(grafico1, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico2, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico3, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico4, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico5, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico6, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico7, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico8, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico9, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico10, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(grafico11, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(grafico12, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(grafico13, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(grafico14, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(grafico15, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(grafico16, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(grafico17, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(grafico18, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(grafico19, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico20, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico21, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico22, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico23, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico24, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico25, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico26, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico27, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico28, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico29, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico30, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico31, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico32, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico33, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico34, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico35, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico36, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico37, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico38, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico39, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico40, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico41, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico42, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico43, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico44, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico45, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico46, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico47, md=12)              
            ],
            align="top", className='pretty_container'
        ),
        
    ],
    fluid=True,
)

layout = dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="Graficos"),
          
    ]
)