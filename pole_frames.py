"""
pole_frames.py - the matrix that turns coordinates measured about a pole
into the drawing's frame, the ecliptic of J2000.

One function, create_pole_transformation_matrix(ra_deg, dec_deg). It
moved here unchanged from idealized_orbits.py on 2026-10-10 (L-421), so
that code with no Plotly and no Tk -- the Hills cloud's orbit sampler,
hills_cloud_sampler.py, which the gallery may one day run -- can use the
same construction a planet's pole and the galactic tide use, rather than
a second copy of it. idealized_orbits.py imports it from here, so every
existing caller is unchanged.

Key functions:
    create_pole_transformation_matrix() - pole (ICRF RA, Dec) to the
        ecliptic-of-J2000 drawing frame

Consumed by: idealized_orbits.py (create_planet_transformation_matrix),
             solar_visualization_shells.py (the galactic tide, through
             idealized_orbits), hills_cloud_sampler.py

Role: computation
Domain: orrery

Module updated: October 10, 2026 with Anthropic's Claude Opus 5.5
(L-421: moved out of idealized_orbits.py unchanged)
"""
import numpy as np

from constants_new import EARTH_OBLIQUITY_J2000_DEG


def create_pole_transformation_matrix(ra_deg, dec_deg):
    """
    The matrix that turns coordinates measured about a pole into the
    drawing's frame, the ecliptic of J2000.

    The pole is given as ICRF right ascension and declination in degrees
    (equatorial, J2000). Its columns are the basis vectors: x along the
    ascending node of the pole's equator on the ecliptic, z along the
    pole, y completing a right-handed set. So matrix @ [x, y, z] takes a
    point given about the pole into ecliptic coordinates.

    Moved out of create_planet_transformation_matrix on 2026-10-02
    (L-406) unchanged, so that the galactic pole can use it as a planet's
    pole does. Moved out of idealized_orbits.py into this module on
    2026-10-10 (L-421), unchanged.

    Module updated: October 2, 2026 with Anthropic's Claude Opus 5.5
    """
    ra_pole = np.radians(ra_deg)
    dec_pole = np.radians(dec_deg)

    sin_dec = np.sin(dec_pole)
    cos_dec = np.cos(dec_pole)
    sin_ra = np.sin(ra_pole)
    cos_ra = np.cos(ra_pole)

    # The pole vector -- RA/Dec are EQUATORIAL (J2000) coordinates.
    x_pole = cos_dec * cos_ra
    y_pole = cos_dec * sin_ra
    z_pole = sin_dec

    # U3 fix (June 2026): the visualization frame is ECLIPTIC (J2000), but the pole
    # above is in the EQUATORIAL frame. Rotate it into ecliptic by the mean obliquity
    # before building the basis. Omitting this left belts/rings ~23.4 deg off the
    # (ecliptic-native) moon orbits -- caught by Tony's Mode-5 render, not the container test.
    # L-322 Stage D (2026-09-23): the angle Horizons builds its ecliptic of
    # J2000 with, read from constants_new.py. It is the frame's angle, the
    # IAU 1976 value, not Earth's tilt; the label "IAU 2006" that stood
    # here named a standard whose value is 84381.406 arcseconds, not this.
    _OBLIQUITY = np.radians(EARTH_OBLIQUITY_J2000_DEG)
    _ce, _se = np.cos(_OBLIQUITY), np.sin(_OBLIQUITY)
    y_pole, z_pole = (y_pole * _ce + z_pole * _se,
                      -y_pole * _se + z_pole * _ce)

    # Find the ascending node of the pole's equator on the ecliptic
    # This is perpendicular to the pole and in the ecliptic plane
    x_node = -y_pole / np.sqrt(x_pole**2 + y_pole**2)
    y_node = x_pole / np.sqrt(x_pole**2 + y_pole**2)
    z_node = 0

    # Create orthogonal basis vectors
    x_basis = np.array([x_node, y_node, z_node])
    z_basis = np.array([x_pole, y_pole, z_pole])
    y_basis = np.cross(z_basis, x_basis)

    # Construct the transformation matrix
    transform_matrix = np.vstack((x_basis, y_basis, z_basis)).T

    return transform_matrix
