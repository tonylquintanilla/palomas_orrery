import numpy as np
import math
import plotly.graph_objs as go
from planet_visualization_utilities import (create_sphere_points, SOLAR_RADIUS_AU, CORE_AU, RADIATIVE_ZONE_AU, CHROMOSPHERE_RADII,
                                            INNER_CORONA_RADII, OUTER_CORONA_RADII, TERMINATION_SHOCK_AU, HELIOPAUSE_RADII,
                                            INNER_LIMIT_OORT_CLOUD_AU, INNER_OORT_CLOUD_AU, OUTER_OORT_CLOUD_AU, GRAVITATIONAL_INFLUENCE_AU)
from constants_new import (
    # Sun information texts
    gravitational_influence_info_hover,
    outer_oort_info_hover,
    inner_oort_info_hover,
    inner_limit_oort_info_hover,
    solar_wind_info_hover,
    termination_shock_info_hover,
    outer_corona_info_hover,
    inner_corona_info_hover,
    chromosphere_info_hover,
    photosphere_info_hover,
    radiative_zone_info_hover,
    core_info_hover
)


#####################################
# Sun Visualization Functions
#####################################

# Individual Sun shell creation functions

def create_sun_gravitational_shell():
    """Creates the Sun's gravitational influence shell."""
    x, y, z = create_sphere_points(GRAVITATIONAL_INFLUENCE_AU, n_points=40)
    
    text_array = [gravitational_influence_info_hover for _ in range(len(x))]
    customdata_array = ["Sun's Gravitational Influence" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=1.0,
                color='rgb(102, 187, 106)', 
                opacity=0.2
            ),
            name='Sun\'s Gravitational Influence',
            text=text_array,             
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces

def create_sun_outer_oort_shell():
    """Creates the Sun's outer Oort cloud shell."""
    x, y, z = create_sphere_points(OUTER_OORT_CLOUD_AU, n_points=40)
    
    text_array = [outer_oort_info_hover for _ in range(len(x))]
    customdata_array = ["Outer Oort Cloud" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=1.0,
                color='white',
                opacity=0.2
            ),
            name='Outer Oort Cloud',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces

def create_sun_inner_oort_shell():
    """Creates the Sun's inner Oort cloud shell."""
    x, y, z = create_sphere_points(INNER_OORT_CLOUD_AU, n_points=40)
    
    text_array = [inner_oort_info_hover for _ in range(len(x))]
    customdata_array = ["Inner Oort Cloud" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=1.0,
                color='white',
                opacity=0.3
            ),
            name='Inner Oort Cloud',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces

def create_sun_inner_oort_limit_shell():
    """Creates the inner limit of the Sun's Oort cloud shell."""
    x, y, z = create_sphere_points(INNER_LIMIT_OORT_CLOUD_AU, n_points=40)
    
    text_array = [inner_limit_oort_info_hover for _ in range(len(x))]
    customdata_array = ["Inner Limit of Oort Cloud" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=1.0,
                color='white',
                opacity=0.3
            ),
            name='Inner Limit of Oort Cloud',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces

def create_sun_heliopause_shell():
    """Creates the Sun's heliopause shell."""
    x, y, z = create_sphere_points(HELIOPAUSE_RADII * SOLAR_RADIUS_AU, n_points=40)
    
    text_array = [solar_wind_info_hover for _ in range(len(x))]
    customdata_array = ["Solar Wind Heliopause" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=0.5,
                color='rgb(135, 206, 250)',
                opacity=0.2
            ),
            name='Solar Wind Heliopause',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces

def create_sun_termination_shock_shell():
    """Creates the Sun's termination shock shell."""
    x, y, z = create_sphere_points(TERMINATION_SHOCK_AU, n_points=40)
    
    text_array = [termination_shock_info_hover for _ in range(len(x))]
    customdata_array = ["Solar Wind Termination Shock" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=0.5,
                color='rgb(240, 244, 255)',
                opacity=0.2
            ),
            name='Solar Wind Termination Shock',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces

def create_sun_outer_corona_shell():
    """Creates the Sun's outer corona shell."""
    x, y, z = create_sphere_points(OUTER_CORONA_RADII * SOLAR_RADIUS_AU, n_points=50)
    
    text_array = [outer_corona_info_hover for _ in range(len(x))]
    customdata_array = ["Sun: Outer Corona" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=0.75,
                color='rgb(25, 25, 112)',
                opacity=0.3
            ),
            name='Sun: Outer Corona',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces

def create_sun_inner_corona_shell():
    """Creates the Sun's inner corona shell."""
    x, y, z = create_sphere_points(INNER_CORONA_RADII * SOLAR_RADIUS_AU, n_points=60)
    
    text_array = [inner_corona_info_hover for _ in range(len(x))]
    customdata_array = ["Sun: Inner Corona" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=1,
                color='rgb(0, 0, 255)',
                opacity=0.09
            ),
            name='Sun: Inner Corona',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces

def create_sun_chromosphere_shell():
    """Creates the Sun's chromosphere shell."""
    x, y, z = create_sphere_points(CHROMOSPHERE_RADII * SOLAR_RADIUS_AU, n_points=60)
    
    text_array = [chromosphere_info_hover for _ in range(len(x))]
    customdata_array = ["Sun: Chromosphere" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=1.25,
                color='rgb(30, 144, 255)',
                opacity=0.10
            ),
            name='Sun: Chromosphere',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces

def create_sun_photosphere_shell():
    """Creates the Sun's photosphere shell."""
    x, y, z = create_sphere_points(SOLAR_RADIUS_AU, n_points=60)
    
    text_array = [photosphere_info_hover for _ in range(len(x))]
    customdata_array = ["Sun: Photosphere" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=7.0,
                color='rgb(255, 244, 214)',
                opacity=1.0
            ),
            name='Sun: Photosphere',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces

def create_sun_radiative_shell():
    """Creates the Sun's radiative zone shell."""
    x, y, z = create_sphere_points(RADIATIVE_ZONE_AU, n_points=60)
    
    text_array = [radiative_zone_info_hover for _ in range(len(x))]
    customdata_array = ["Sun: Radiative Zone" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=7,
                color='rgb(30, 144, 255)',
                opacity=1.0
            ),
            name='Sun: Radiative Zone',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces

def create_sun_core_shell():
    """Creates the Sun's core shell."""
    x, y, z = create_sphere_points(CORE_AU, n_points=60)
    
    text_array = [core_info_hover for _ in range(len(x))]
    customdata_array = ["Sun: Core" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=10,
                color='rgb(70, 130, 180)',
                opacity=1.0
            ),
            name='Sun: Core',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces