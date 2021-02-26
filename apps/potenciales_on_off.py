import dash_bootstrap_components as dbc
import dash_core_components as dcc
import plotly.graph_objs as go
import dash_html_components as html
import pandas as pd
from plotly.subplots import make_subplots
import pathlib

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

df = pd.read_csv(DATA_PATH.joinpath("potenciales_on_off.csv"))
df1 = df.loc[df['cmp'] == "CMP 006"]
df2 = df.loc[df['cmp'] == "CMP 010"]
df3 = df.loc[df['cmp'] == "CMP 017"]
df4 = df.loc[df['cmp'] == "CMP 021"]
df5 = df.loc[df['cmp'] == "CMP 034"]
df6 = df.loc[df['cmp'] == "CMP 043"]
df7 = df.loc[df['cmp'] == "CMP 056"]
df8 = df.loc[df['cmp'] == "CMP 071"]
df9 = df.loc[df['cmp'] == "CMP 084"]
df10 = df.loc[df['cmp'] == "CMP 090"]
df11 = df.loc[df['cmp'] == "CMP 101"]
df12 = df.loc[df['cmp'] == "CMP 105"]
df13 = df.loc[df['cmp'] == "CMP 122"]
df14 = df.loc[df['cmp'] == "CMP 143"]
df15 = df.loc[df['cmp'] == "CMP 153"]
df16 = df.loc[df['cmp'] == "CMP 173"]
df17 = df.loc[df['cmp'] == "CMP 184"]
df18 = df.loc[df['cmp'] == "CMP 203"]
df19 = df.loc[df['cmp'] == "CMP 220"]
df20 = df.loc[df['cmp'] == "CMP 221 02AN"]
df21 = df.loc[df['cmp'] == "CMP 236"]
df22 = df.loc[df['cmp'] == "CMP 245"]
df23 = df.loc[df['cmp'] == "CMP 249"]
df24 = df.loc[df['cmp'] == "CMP 259"]
df25 = df.loc[df['cmp'] == "CMP 271"]
df26 = df.loc[df['cmp'] == "CMP 278"]
df27 = df.loc[df['cmp'] == "CMP 284"]
df28 = df.loc[df['cmp'] == "CMP 289"]
df29 = df.loc[df['cmp'] == "CMP 295"]
df30 = df.loc[df['cmp'] == "CMP 300"]
df31 = df.loc[df['cmp'] == "CMP 307"]
df32 = df.loc[df['cmp'] == "CMP 312"]
df33 = df.loc[df['cmp'] == "CMP 318"]
df34 = df.loc[df['cmp'] == "CMP 326"]
df35 = df.loc[df['cmp'] == "CMP 332"]
df36 = df.loc[df['cmp'] == "CMP 337"]
df37 = df.loc[df['cmp'] == "CMP 345"]
df38 = df.loc[df['cmp'] == "CMP 350"]
df39 = df.loc[df['cmp'] == "CMP 363"]
df40 = df.loc[df['cmp'] == "CMP 368"]
df41 = df.loc[df['cmp'] == "CMP 375"]
df42 = df.loc[df['cmp'] == "CMP 380"]
df43 = df.loc[df['cmp'] == "CMP 388"]
df44 = df.loc[df['cmp'] == "CMP 389"]
df45 = df.loc[df['cmp'] == "CMP 395"]
df46 = df.loc[df['cmp'] == "CMP 405"]
df47 = df.loc[df['cmp'] == "CMP 412"]






fig1 = make_subplots(specs=[[{"secondary_y": True}]])
fig1.add_trace(go.Scatter(x=df1['fecha'], y=df1['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-OFF"), row=1, col=1)

fig1.update_layout(title="Potencial ON-OFF CMP 006", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig1.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico1 = dbc.Card(
            [dcc.Graph(id='cmp006', figure=fig1)], body=True)

fig2 = make_subplots(specs=[[{"secondary_y": True}]])
fig2.add_trace(go.Scatter(x=df2['fecha'], y=df2['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-OFF"), row=1, col=1)

fig2.update_layout(title="Potencial ON-OFF CMP 010", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig2.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico2 = dbc.Card(
            [dcc.Graph(id='cmp010', figure=fig2)], body=True)

fig3 = make_subplots(specs=[[{"secondary_y": True}]])
fig3.add_trace(go.Scatter(x=df3['fecha'], y=df3['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-OFF"), row=1, col=1)

fig3.update_layout(title="Potencial ON-OFF CMP 017", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig3.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico3 = dbc.Card(
            [dcc.Graph(id='cmp017', figure=fig3)], body=True)

fig4 = make_subplots(specs=[[{"secondary_y": True}]])
fig4.add_trace(go.Scatter(x=df4['fecha'], y=df4['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-OFF"), row=1, col=1)

fig4.update_layout(title="Potencial ON-OFF CMP 021", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig4.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico4 = dbc.Card(
            [dcc.Graph(id='cmp021', figure=fig4)], body=True)

fig5 = make_subplots(specs=[[{"secondary_y": True}]])
fig5.add_trace(go.Scatter(x=df5['fecha'], y=df5['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-OFF"), row=1, col=1)

fig5.update_layout(title="Potencial ON-OFF CMP 034", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig5.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico5 = dbc.Card(
            [dcc.Graph(id='cmp034', figure=fig5)], body=True)

fig6 = make_subplots(specs=[[{"secondary_y": True}]])
fig6.add_trace(go.Scatter(x=df6['fecha'], y=df6['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-OFF"), row=1, col=1)

fig6.update_layout(title="Potencial ON-OFF CMP 043", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig6.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico6 = dbc.Card(
            [dcc.Graph(id='cmp043', figure=fig6)], body=True)

fig7 = make_subplots(specs=[[{"secondary_y": True}]])
fig7.add_trace(go.Scatter(x=df7['fecha'], y=df7['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-OFF"), row=1, col=1)

fig7.update_layout(title="Potencial ON-OFF CMP 056", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig7.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico7 = dbc.Card(
            [dcc.Graph(id='cmp056', figure=fig7)], body=True)

fig8 = make_subplots(specs=[[{"secondary_y": True}]])
fig8.add_trace(go.Scatter(x=df8['fecha'], y=df8['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-OFF"), row=1, col=1)

fig8.update_layout(title="Potencial ON-OFF CMP 071", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig8.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico8 = dbc.Card(
            [dcc.Graph(id='cmp071', figure=fig8)], body=True)

fig9 = make_subplots(specs=[[{"secondary_y": True}]])
fig9.add_trace(go.Scatter(x=df9['fecha'], y=df9['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-OFF"), row=1, col=1)

fig9.update_layout(title="Potencial ON-OFF CMP 084", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig9.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico9 = dbc.Card(
            [dcc.Graph(id='cmp084', figure=fig9)], body=True)

fig10 = make_subplots(specs=[[{"secondary_y": True}]])
fig10.add_trace(go.Scatter(x=df10['fecha'], y=df10['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-OFF"), row=1, col=1)

fig10.update_layout(title="Potencial ON-OFF CMP 090", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig10.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico10 = dbc.Card(
            [dcc.Graph(id='cmp090', figure=fig10)], body=True)

fig11 = make_subplots(specs=[[{"secondary_y": True}]])
fig11.add_trace(go.Scatter(x=df11['fecha'], y=df11['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-OFF"), row=1, col=1)

fig11.update_layout(title="Potencial ON-OFF CMP 101", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig11.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico11 = dbc.Card(
            [dcc.Graph(id='cmp101', figure=fig11)], body=True)

fig12 = make_subplots(specs=[[{"secondary_y": True}]])
fig12.add_trace(go.Scatter(x=df12['fecha'], y=df12['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-OFF"), row=1, col=1)

fig12.update_layout(title="Potencial ON-OFF CMP 105", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig12.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico12 = dbc.Card(
            [dcc.Graph(id='cmp105', figure=fig12)], body=True)

fig13 = make_subplots(specs=[[{"secondary_y": True}]])
fig13.add_trace(go.Scatter(x=df13['fecha'], y=df13['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-OFF"), row=1, col=1)

fig13.update_layout(title="Potencial ON-OFF CMP 122", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig13.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico13 = dbc.Card(
            [dcc.Graph(id='cmp122', figure=fig13)], body=True)

fig14 = make_subplots(specs=[[{"secondary_y": True}]])
fig14.add_trace(go.Scatter(x=df14['fecha'], y=df14['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-OFF"), row=1, col=1)

fig14.update_layout(title="Potencial ON-OFF CMP 143", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig14.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico14 = dbc.Card(
            [dcc.Graph(id='cmp143', figure=fig14)], body=True)

fig15 = make_subplots(specs=[[{"secondary_y": True}]])
fig15.add_trace(go.Scatter(x=df15['fecha'], y=df15['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-OFF"), row=1, col=1)

fig15.update_layout(title="Potencial ON-OFF CMP 153", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig15.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico15 = dbc.Card(
            [dcc.Graph(id='cmp153', figure=fig15)], body=True)

fig16 = make_subplots(specs=[[{"secondary_y": True}]])
fig16.add_trace(go.Scatter(x=df16['fecha'], y=df16['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-OFF"), row=1, col=1)

fig16.update_layout(title="Potencial ON-OFF CMP 173", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig16.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico16 = dbc.Card(
            [dcc.Graph(id='cmp173', figure=fig16)], body=True)

fig17 = make_subplots(specs=[[{"secondary_y": True}]])
fig17.add_trace(go.Scatter(x=df17['fecha'], y=df17['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-OFF"), row=1, col=1)

fig17.update_layout(title="Potencial ON-OFF CMP 184", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig17.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico17 = dbc.Card(
            [dcc.Graph(id='cmp184', figure=fig17)], body=True)

fig18 = make_subplots(specs=[[{"secondary_y": True}]])
fig18.add_trace(go.Scatter(x=df18['fecha'], y=df18['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig18.update_layout(title="Potencial ON CMP 203", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig18.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico18 = dbc.Card(
            [dcc.Graph(id='cmp220', figure=fig18)], body=True)

fig19 = make_subplots(specs=[[{"secondary_y": True}]])
fig19.add_trace(go.Scatter(x=df19['fecha'], y=df19['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig19.update_layout(title="Potencial ON CMP 220", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig19.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico19 = dbc.Card(
            [dcc.Graph(id='cmp22102AN', figure=fig19)], body=True)

fig20 = make_subplots(specs=[[{"secondary_y": True}]])
fig20.add_trace(go.Scatter(x=df20['fecha'], y=df20['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig20.update_layout(title="Potencial ON CMP 221 02AN", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig20.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico20 = dbc.Card(
            [dcc.Graph(id='cmp236', figure=fig20)], body=True)

fig21 = make_subplots(specs=[[{"secondary_y": True}]])
fig21.add_trace(go.Scatter(x=df21['fecha'], y=df21['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig21.update_layout(title="Potencial ON CMP 236", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig21.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico21 = dbc.Card(
            [dcc.Graph(id='cmp245', figure=fig21)], body=True)

fig22 = make_subplots(specs=[[{"secondary_y": True}]])
fig22.add_trace(go.Scatter(x=df22['fecha'], y=df22['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig22.update_layout(title="Potencial ON CMP 245", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig22.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico22 = dbc.Card(
            [dcc.Graph(id='cmp249', figure=fig22)], body=True)

fig23 = make_subplots(specs=[[{"secondary_y": True}]])
fig23.add_trace(go.Scatter(x=df23['fecha'], y=df23['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig23.update_layout(title="Potencial ON CMP 249", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig23.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico23 = dbc.Card(
            [dcc.Graph(id='cmp259', figure=fig23)], body=True)

fig24 = make_subplots(specs=[[{"secondary_y": True}]])
fig24.add_trace(go.Scatter(x=df24['fecha'], y=df24['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig24.update_layout(title="Potencial ON CMP 259", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig24.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico24 = dbc.Card(
            [dcc.Graph(id='cmp271', figure=fig24)], body=True)

fig25 = make_subplots(specs=[[{"secondary_y": True}]])
fig25.add_trace(go.Scatter(x=df25['fecha'], y=df25['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig25.update_layout(title="Potencial ON CMP 271", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig25.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico25 = dbc.Card(
            [dcc.Graph(id='cmp278', figure=fig25)], body=True)

fig26 = make_subplots(specs=[[{"secondary_y": True}]])
fig26.add_trace(go.Scatter(x=df26['fecha'], y=df26['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig26.update_layout(title="Potencial ON CMP 278", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig26.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico26 = dbc.Card(
            [dcc.Graph(id='cmp284', figure=fig26)], body=True)

fig27 = make_subplots(specs=[[{"secondary_y": True}]])
fig27.add_trace(go.Scatter(x=df27['fecha'], y=df27['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig27.update_layout(title="Potencial ON CMP 284", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig27.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico27 = dbc.Card(
            [dcc.Graph(id='cmp289', figure=fig27)], body=True)

fig28 = make_subplots(specs=[[{"secondary_y": True}]])
fig28.add_trace(go.Scatter(x=df28['fecha'], y=df28['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig28.update_layout(title="Potencial ON CMP 289", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig28.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico28 = dbc.Card(
            [dcc.Graph(id='cmp295', figure=fig28)], body=True)

fig29 = make_subplots(specs=[[{"secondary_y": True}]])
fig29.add_trace(go.Scatter(x=df29['fecha'], y=df29['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig29.update_layout(title="Potencial ON CMP 295", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig29.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico29 = dbc.Card(
            [dcc.Graph(id='cmp300', figure=fig29)], body=True)

fig30 = make_subplots(specs=[[{"secondary_y": True}]])
fig30.add_trace(go.Scatter(x=df30['fecha'], y=df30['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig30.update_layout(title="Potencial ON CMP 300", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig30.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico30 = dbc.Card(
            [dcc.Graph(id='cmp307', figure=fig30)], body=True)

fig31 = make_subplots(specs=[[{"secondary_y": True}]])
fig31.add_trace(go.Scatter(x=df31['fecha'], y=df31['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig31.update_layout(title="Potencial ON CMP 307", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig31.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico31 = dbc.Card(
            [dcc.Graph(id='cmp312', figure=fig31)], body=True)

fig32 = make_subplots(specs=[[{"secondary_y": True}]])
fig32.add_trace(go.Scatter(x=df32['fecha'], y=df32['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig32.update_layout(title="Potencial ON CMP 312", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig32.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico32 = dbc.Card(
            [dcc.Graph(id='cmp318', figure=fig32)], body=True)

fig33 = make_subplots(specs=[[{"secondary_y": True}]])
fig33.add_trace(go.Scatter(x=df33['fecha'], y=df33['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig33.update_layout(title="Potencial ON CMP 318", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig33.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico33 = dbc.Card(
            [dcc.Graph(id='cmp326', figure=fig33)], body=True)

fig34 = make_subplots(specs=[[{"secondary_y": True}]])
fig34.add_trace(go.Scatter(x=df34['fecha'], y=df34['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig34.update_layout(title="Potencial ON CMP 326", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig34.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico34 = dbc.Card(
            [dcc.Graph(id='cmp332', figure=fig34)], body=True)

fig35 = make_subplots(specs=[[{"secondary_y": True}]])
fig35.add_trace(go.Scatter(x=df35['fecha'], y=df35['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig35.update_layout(title="Potencial ON CMP 332", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig35.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico35 = dbc.Card(
            [dcc.Graph(id='cmp337', figure=fig35)], body=True)

fig36 = make_subplots(specs=[[{"secondary_y": True}]])
fig36.add_trace(go.Scatter(x=df36['fecha'], y=df36['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig36.update_layout(title="Potencial ON CMP 337", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig36.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico36 = dbc.Card(
            [dcc.Graph(id='cmp350', figure=fig36)], body=True)

fig37 = make_subplots(specs=[[{"secondary_y": True}]])
fig37.add_trace(go.Scatter(x=df37['fecha'], y=df37['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig37.update_layout(title="Potencial ON CMP 345", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig37.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico37 = dbc.Card(
            [dcc.Graph(id='cmp363', figure=fig37)], body=True)

fig38 = make_subplots(specs=[[{"secondary_y": True}]])
fig38.add_trace(go.Scatter(x=df38['fecha'], y=df38['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig38.update_layout(title="Potencial ON CMP 350", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig38.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico38 = dbc.Card(
            [dcc.Graph(id='cmp368', figure=fig38)], body=True)
            
fig39 = make_subplots(specs=[[{"secondary_y": True}]])
fig39.add_trace(go.Scatter(x=df39['fecha'], y=df39['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig39.update_layout(title="Potencial ON CMP 363", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig39.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico39 = dbc.Card(
            [dcc.Graph(id='cmp375', figure=fig39)], body=True)

fig40 = make_subplots(specs=[[{"secondary_y": True}]])
fig40.add_trace(go.Scatter(x=df40['fecha'], y=df40['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig40.update_layout(title="Potencial ON CMP 368", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig40.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico40 = dbc.Card(
            [dcc.Graph(id='cmp380', figure=fig40)], body=True)

fig41 = make_subplots(specs=[[{"secondary_y": True}]])
fig41.add_trace(go.Scatter(x=df41['fecha'], y=df41['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig41.update_layout(title="Potencial ON CMP 375", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig41.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico41 = dbc.Card(
            [dcc.Graph(id='cmp388', figure=fig41)], body=True)

fig42 = make_subplots(specs=[[{"secondary_y": True}]])
fig42.add_trace(go.Scatter(x=df42['fecha'], y=df42['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig42.update_layout(title="Potencial ON CMP 380", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig42.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico42 = dbc.Card(
            [dcc.Graph(id='cmp380', figure=fig42)], body=True)

fig43 = make_subplots(specs=[[{"secondary_y": True}]])
fig43.add_trace(go.Scatter(x=df43['fecha'], y=df43['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig43.update_layout(title="Potencial ON CMP 388", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig43.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico43 = dbc.Card(
            [dcc.Graph(id='cmp388', figure=fig43)], body=True)

fig44 = make_subplots(specs=[[{"secondary_y": True}]])
fig44.add_trace(go.Scatter(x=df44['fecha'], y=df44['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig44.update_layout(title="Potencial ON CMP 389", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig44.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico44 = dbc.Card(
            [dcc.Graph(id='cmp389', figure=fig44)], body=True)

fig45 = make_subplots(specs=[[{"secondary_y": True}]])
fig45.add_trace(go.Scatter(x=df45['fecha'], y=df45['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig45.update_layout(title="Potencial ON CMP 395", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig45.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico45 = dbc.Card(
            [dcc.Graph(id='cmp395', figure=fig45)], body=True)

fig46 = make_subplots(specs=[[{"secondary_y": True}]])
fig46.add_trace(go.Scatter(x=df46['fecha'], y=df46['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig46.update_layout(title="Potencial ON CMP 405", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig46.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico46 = dbc.Card(
            [dcc.Graph(id='cmp405', figure=fig46)], body=True)

fig47 = make_subplots(specs=[[{"secondary_y": True}]])
fig47.add_trace(go.Scatter(x=df47['fecha'], y=df47['potencial'], mode="lines", marker_color='rgba(229, 45, 35, 1)', name="Potencial ON-FF"), row=1, col=1)

fig47.update_layout(title="Potencial ON CMP 412", coloraxis=dict(colorscale='Bluered_r'), xaxis_title="Fecha [mm/dd/yyyy]", showlegend=True)
fig47.update_yaxes(title_text="Potencial [V]", secondary_y=False, autorange="reversed", row=1, col=1, tickformat=".2f")

grafico47 = dbc.Card(
            [dcc.Graph(id='cmp412', figure=fig47)], body=True)


        
tab1_content = dbc.Container(
    [
        html.Hr(),
        html.H1("Potenciales ON-OFF"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(grafico1, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.531 [V]"),
                                                dbc.ListGroupItem("IR: 793.223 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.690 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)              
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico2, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.521 [V]"),
                                                dbc.ListGroupItem("IR: 631.318 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.700 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico3, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -0.490 [V]"),
                                                dbc.ListGroupItem("IR: 64.384 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.450 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico4, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.213 [V]"),
                                                dbc.ListGroupItem("IR: 644.669 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.660 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico5, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.417 [V]"),
                                                dbc.ListGroupItem("IR: 629.870 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.820 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico6, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.260 [V]"),
                                                dbc.ListGroupItem("IR: 612.961 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.800 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico7, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.369 [V]"),
                                                dbc.ListGroupItem("IR: 516.747 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.960 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico8, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.104 [V]"),
                                                dbc.ListGroupItem("IR: 548.908 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.480 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico9, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.306 [V]"),
                                                dbc.ListGroupItem("IR: 476.696 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -1.070 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico10, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.422 [V]"),
                                                dbc.ListGroupItem("IR: 526.390 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -1.230 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico11, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.120 [V]"),
                                                dbc.ListGroupItem("IR: 493.402 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.740 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico12, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.147 [V]"),
                                                dbc.ListGroupItem("IR: 516.240 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.690 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico13, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.531 [V]"),
                                                dbc.ListGroupItem("IR: 793.22 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.690 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico14, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.242 [V]"),
                                                dbc.ListGroupItem("IR: 479.515 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.915 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico15, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.408 [V]"),
                                                dbc.ListGroupItem("IR: 556.125 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.870 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico16, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.432 [V]"),
                                                dbc.ListGroupItem("IR: 554.607 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.840 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico17, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.419 [V]"),
                                                dbc.ListGroupItem("IR: 583.511 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.810 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico18, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.072 [V]"),
                                                dbc.ListGroupItem("IR: 331.850 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.770 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico19, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.072 [V]"),
                                                dbc.ListGroupItem("IR: 331.850 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.770 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico20, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.183 [V]"),
                                                dbc.ListGroupItem("IR: 409.969 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.760 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico21, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.312 [V]"),
                                                dbc.ListGroupItem("IR: 517.158 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.800 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico22, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.425 [V]"),
                                                dbc.ListGroupItem("IR: 528.743 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.810 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico23, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.421 [V]"),
                                                dbc.ListGroupItem("IR: 381.991 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.905 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico24, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.449 [V]"),
                                                dbc.ListGroupItem("IR: 498.401 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.960 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico25, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.415 [V]"),
                                                dbc.ListGroupItem("IR: 475.049 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -1.040 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico26, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -0.911 [V]"),
                                                dbc.ListGroupItem("IR: 444.577 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.500 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico27, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.349 [V]"),
                                                dbc.ListGroupItem("IR: 437.502 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.940 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico28, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.305 [V]"),
                                                dbc.ListGroupItem("IR: 373.360 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.900 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico29, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.121 [V]"),
                                                dbc.ListGroupItem("IR: 316.426 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.750 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico30, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -0.937 [V]"),
                                                dbc.ListGroupItem("IR: 259.492 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.610 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico31, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.058 [V]"),
                                                dbc.ListGroupItem("IR: 242.426 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.900 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico32, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.284 [V]"),
                                                dbc.ListGroupItem("IR: 372.733 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.840 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico33, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -0.949 [V]"),
                                                dbc.ListGroupItem("IR: 193.740 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -1.130 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico34, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.051 [V]"),
                                                dbc.ListGroupItem("IR: 338.087 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.750 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico35, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.025 [V]"),
                                                dbc.ListGroupItem("IR: 278.583 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.770 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico36, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.071 [V]"),
                                                dbc.ListGroupItem("IR: 323.825 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.710 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico37, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -0.926 [V]"),
                                                dbc.ListGroupItem("IR: 188.004 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.750 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico38, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.060 [V]"),
                                                dbc.ListGroupItem("IR: 270.082 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.750 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico39, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.060 [V]"),
                                                dbc.ListGroupItem("IR: 270.082 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.750 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico40, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.067 [V]"),
                                                dbc.ListGroupItem("IR: 226.955 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.920 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico41, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -0.961 [V]"),
                                                dbc.ListGroupItem("IR: 176.127 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.800 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico42, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -0.984 [V]"),
                                                dbc.ListGroupItem("IR: 225.872 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.735 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico43, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.006 [V]"),
                                                dbc.ListGroupItem("IR: 266.574 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.700 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico44, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.305 [V]"),
                                                dbc.ListGroupItem("IR: 373.360 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.900 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico45, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.001 [V]"),
                                                dbc.ListGroupItem("IR: 227.888 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.750 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico46, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -0.898 [V]"),
                                                dbc.ListGroupItem("IR: 307.092 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.510 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
            ],
            align="top", className='pretty_container'
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(grafico47, md=9),
                dbc.Col(dbc.Card(
                            dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem("ON: -1.169 [V]"),
                                                dbc.ListGroupItem("IR: 310.689 [mV]"),
                                                dbc.ListGroupItem("Instant OFF: -0.870 [V]"),
                                            ],
                                            flush=True,
                                            ),
                                            style={"width": "18rem"},
                                            ), md=2)                     
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