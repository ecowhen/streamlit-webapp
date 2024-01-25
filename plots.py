import numpy as np
import pandas as pd
import plotly.graph_objs as go

def plot_prediction(prediction_df, berlin_now):
    time_axis = prediction_df['time']
    y_biomass = np.asarray(prediction_df['biomass'])
    y_hydropower = np.asarray(prediction_df['hydropower'])
    y_wind = np.asarray(prediction_df['wind'])
    y_solar = np.asarray(prediction_df['solar'])
    y_demand = np.asarray(prediction_df['demand'])
    y_residual = y_demand - (y_biomass + y_hydropower + y_wind + y_solar)
    # y_emissions_factor = 0.875402*(y_residual/y_demand)*1000 #in g/kWh
    # y_emissions_factor[y_emissions_factor < 0] = 0

    color_biomass = (80.988, 178.985, 80.988, 0.8)
    color_hydropower = (166.005, 225.981, 255, 0.8)
    color_wind = (89.9895, 102.995, 255, 0.8)
    color_solar = (255, 242.99, 63.9795, 0.8)
    color_demand = (255, 64, 0, 0.8)
    color_emissions_factor = (255, 64, 255, 0.8)
    color_residual = (116.994, 127.985, 116.994, 0.8)

  
    # create the figure object
    fig1 = go.Figure()
    # add traces to the figure
    fig1.add_trace(go.Scatter(
        x=time_axis, y=y_biomass,
        hoverinfo='y',
        mode='lines',
        line=dict(width=0.5, color=f'rgb{(color_biomass)}'),
        stackgroup='one', # define stack group
        name='Biomass',
        fillcolor=f'rgba{(color_biomass)}',
        hovertemplate='%{y:.2f} MW'
    ))
    fig1.add_trace(go.Scatter(
        x=time_axis, y=y_hydropower,
        hoverinfo='y',
        mode='lines',
        line=dict(width=0.5, color=f'rgb{(color_hydropower)}'),
        stackgroup='one',
        name='Hydropower',
        fillcolor=f'rgba{(color_hydropower)}',
        hovertemplate='%{y:.2f} MW'
    ))
    fig1.add_trace(go.Scatter(
        x=time_axis, y=y_wind,
        hoverinfo='y',
        mode='lines',
        line=dict(width=0.5, color=f'rgb{(color_wind)}'),
        stackgroup='one',
        name='Wind',
        fillcolor=f'rgba{(color_wind)}',
        hovertemplate='%{y:.2f} MW'
    ))
    fig1.add_trace(go.Scatter(
        x=time_axis, y=y_solar,
        hoverinfo='y',
        mode='lines',
        line=dict(width=0.5, color=f'rgb{(color_solar)}'),
        stackgroup='one',
        name='Solar',
        fillcolor=f'rgba{(color_solar)}',
        hovertemplate='%{y:.2f} MW'
    ))
    fig1.add_trace(go.Scatter(
        x=time_axis, y=y_residual,
        hoverinfo='y',
        mode='lines',
        line=dict(width=0.5, color=f'rgb{(color_residual)}'),
        stackgroup='one',
        name='Residual Load',
        fillcolor=f'rgba{(color_residual)}',
        hovertemplate='%{y:.2f} MW'
    ))
    fig1.add_trace(go.Scatter(
        x=time_axis, y=y_demand,
        hoverinfo='y',
        mode='lines',
        line=dict(width=1.25, color=f'rgb{(color_demand)}'),
        name='Demand',
        hovertemplate='%{y:.2f} MW'
    ))
    fig1.add_shape(
        dict(
            type="line",
            x0=berlin_now,
            x1=berlin_now,
            y0=0,
            y1=80000,
            line=dict(color="blue", width=2),
            name="Current Time"
        )
    )
    fig1.add_annotation(valign='top', text="Now", x=berlin_now, y=80000, arrowhead=1, showarrow=True, arrowcolor="blue", ax=-60, ay=0)

    fig1.update_xaxes(showgrid=True, gridwidth=0.2, gridcolor='rgba(0, 0, 0, 0.3)')
    fig1.update_yaxes(showgrid=True, gridwidth=0.2, gridcolor='rgba(0, 0, 0, 0.3)')

    fig1.update_layout(xaxis_title="Time", 
                    yaxis_title="Power [MW]", 
                    title="Electricity Mix Forecast",
                    legend=dict(orientation="h", yanchor="top", y=1.1, xanchor="center", x=0.5),
                    hovermode='x unified'
    )
    return fig1

def plot_renewable_share(prediction_df, berlin_now):
    colorscale = [(0, 'red'), (0.25, 'orange'), (0.5, 'yellow'), (0.75, 'lightgreen'), (1, 'green')]

    fig2 = go.Figure()
    fig2.add_trace(go.Bar(
        x=prediction_df['time'],
        y=prediction_df['re_share'],  
        marker_color=prediction_df['re_share'],
        marker_colorscale=colorscale,
        #hoverinfo='y',
        hovertemplate='%{y:.3}%',
        name='Renewable Share'
    ))

    fig2.add_shape(
        dict(
            type="line",
            x0=berlin_now,
            x1=berlin_now,
            y0=0,
            y1=120,
            line=dict(color="blue", width=2),
            name="Current Time"
        )
    )
    fig2.add_annotation(valign='top', text="Now", x=berlin_now, y=120, arrowhead=1, showarrow=True, arrowcolor="blue", ax=-60, ay=0)

    fig2.update_xaxes(showgrid=True, gridwidth=0.2, gridcolor='rgba(0, 0, 0, 0.3)')
    fig2.update_yaxes(showgrid=True, gridwidth=0.2, gridcolor='rgba(0, 0, 0, 0.3)')

    fig2.update_layout(xaxis_title="Time", 
                       yaxis_title="Renewable Share [%]",
                       title="Electricity Traffic Light Forecast",
                       legend=dict(orientation="h", yanchor="top", y=1.1, xanchor="center", x=0.5),
                       hovermode='x unified'
    )
    
    return fig2