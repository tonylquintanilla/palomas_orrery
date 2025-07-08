"""
refined_orbits.py - Refined satellite orbits using JPL Horizons ephemeris data

This module works alongside idealized_orbits.py to provide more accurate
satellite positions by applying corrections based on actual ephemeris data.
"""

import numpy as np
import json
import os
from scipy.spatial.transform import Rotation
from typing import Callable, Dict, Optional, Tuple
from datetime import datetime

# Import idealized orbits module
IDEALIZED_ORBITS_AVAILABLE = False
ORBITAL_PARAMS = None

try:
    import idealized_orbits
    
    # Check if the module has orbital parameters
    if hasattr(idealized_orbits, 'planetary_params'):
        ORBITAL_PARAMS = idealized_orbits.planetary_params
        IDEALIZED_ORBITS_AVAILABLE = True
        print(f"Loaded orbital parameters for {len(ORBITAL_PARAMS)} objects")
    else:
        print("Warning: idealized_orbits.py found but no orbital parameters")
        
except ImportError:
    print("Warning: idealized_orbits.py not found. Using built-in approximations.")


class RefinedOrbitSystem:
    """System for creating refined satellite orbits using ephemeris data."""
    
    def __init__(self, ephemeris_file: str = "satellite_ephemerides.json"):
        """Initialize with ephemeris database."""
        self.ephemeris_file = ephemeris_file
        self.ephemeris_data = self._load_ephemeris_data()
        self._orbit_cache = {}  # Cache refined orbits
        
    def _load_ephemeris_data(self) -> Dict:
        """Load ephemeris data from JSON file."""
        if os.path.exists(self.ephemeris_file):
            with open(self.ephemeris_file, 'r') as f:
                return json.load(f)
        else:
            print(f"Warning: {self.ephemeris_file} not found. Using idealized orbits only.")
            return {"satellites": {}}
    
    def get_orbit_function(self, satellite: str, primary: str) -> Callable:
        """
        Get refined orbit function for a satellite.
        Falls back to idealized orbit if no ephemeris data available.
        """
        cache_key = f"{primary}_{satellite}".lower()
        
        # Check cache first
        if cache_key in self._orbit_cache:
            return self._orbit_cache[cache_key]
        
        # Try to create refined orbit
        if cache_key in self.ephemeris_data.get("satellites", {}):
            refined_func = self._create_refined_orbit(satellite, primary)
            self._orbit_cache[cache_key] = refined_func
            return refined_func
        
        # Fall back to idealized orbit
        idealized_func = self._get_idealized_orbit(satellite, primary)
        if idealized_func:
            print(f"Using idealized orbit for {satellite} (no ephemeris data)")
            self._orbit_cache[cache_key] = idealized_func
            return idealized_func
        
        # Last resort: simple circular orbit
        print(f"Warning: No orbit data for {satellite}. Using default circular orbit.")
        default_func = self._create_default_orbit(satellite, primary)
        self._orbit_cache[cache_key] = default_func
        return default_func
    
    def _create_refined_orbit(self, satellite: str, primary: str) -> Callable:
        """Create refined orbit by comparing actual vs idealized orbit normals."""
        sat_key = f"{primary}_{satellite}".lower()
        
        # First, we MUST have an idealized orbit to refine
        idealized = self._get_idealized_orbit(satellite, primary)
        if not idealized:
            print(f"Warning: No idealized orbit found for {satellite}. Cannot create refined orbit.")
            return self._create_default_orbit(satellite, primary)
        
        # Try to get actual orbit positions from the main program's orbit cache
        correction = None
        try:
            # Check if we're in special fetch mode and have temp cache
            from palomas_orrery import special_fetch_var, temp_cache
            
            orbit_key = f"{satellite}_{primary}"
            
            # Try temp cache first if in special mode
            if special_fetch_var.get() == 1 and temp_cache and orbit_key in temp_cache:
                print(f"Found actual orbit data in temp cache for {satellite}")
                actual_orbit_data = temp_cache[orbit_key]
            else:
                # Try main cache
                import orbit_data_manager
                orbit_paths = orbit_data_manager.load_orbit_paths()
                
                if orbit_key in orbit_paths:
                    print(f"Found cached actual orbit data for {satellite}")
                    actual_orbit_data = orbit_paths[orbit_key]
                else:
                    actual_orbit_data = None
            
            if actual_orbit_data:
                # Extract positions (they should be in AU already)
                actual_x = np.array(actual_orbit_data['x'])
                actual_y = np.array(actual_orbit_data['y'])
                actual_z = np.array(actual_orbit_data['z'])
                
                # Sample enough points to calculate normal vector reliably
                num_points = min(len(actual_x), 100)
                if num_points >= 3:
                    # Take evenly spaced points
                    indices = np.linspace(0, len(actual_x)-1, num_points, dtype=int)
                    actual_positions = np.column_stack((
                        actual_x[indices],
                        actual_y[indices],
                        actual_z[indices]
                    ))
                    
                    # Calculate actual orbit normal from positions
                    r1 = actual_positions[0]
                    r2 = actual_positions[num_points//4]  # ~90 degrees
                    r3 = actual_positions[num_points//2]  # ~180 degrees
                    
                    v1 = r2 - r1
                    v2 = r3 - r1
                    n_actual = np.cross(v1, v2)
                    n_actual = n_actual / np.linalg.norm(n_actual)
                    
                    print(f"Calculated actual orbit normal: [{n_actual[0]:.4f}, {n_actual[1]:.4f}, {n_actual[2]:.4f}]")
                    
                    # Calculate idealized orbit normal
                    t_sample = np.linspace(0, 2*np.pi, 100)
                    ideal_positions = np.array([idealized(t) for t in t_sample])
                    
                    # Make sure ideal positions are in AU
                    if np.max(np.abs(ideal_positions)) > 10:  # Likely in km
                        ideal_positions = ideal_positions / 149597870.7
                    
                    r1_ideal = ideal_positions[0]
                    r2_ideal = ideal_positions[25]  # 90 degrees
                    r3_ideal = ideal_positions[50]  # 180 degrees
                    
                    v1_ideal = r2_ideal - r1_ideal
                    v2_ideal = r3_ideal - r1_ideal
                    n_ideal = np.cross(v1_ideal, v2_ideal)
                    n_ideal = n_ideal / np.linalg.norm(n_ideal)
                    
                    print(f"Calculated ideal orbit normal: [{n_ideal[0]:.4f}, {n_ideal[1]:.4f}, {n_ideal[2]:.4f}]")
                    
                    # Calculate rotation to align ideal normal with actual normal
                    axis = np.cross(n_ideal, n_actual)
                    if np.linalg.norm(axis) > 1e-10:  # If normals aren't already aligned
                        axis = axis / np.linalg.norm(axis)
                        angle = np.arccos(np.clip(np.dot(n_ideal, n_actual), -1, 1))
                        
                        # Create rotation
                        correction = Rotation.from_rotvec(angle * axis)
                        print(f"Refined orbit for {satellite}: applying {np.degrees(angle):.2f}° correction")
                    else:
                        print(f"Refined orbit for {satellite}: normals already aligned")
                else:
                    print(f"Not enough actual orbit points for {satellite}")
            else:
                print(f"No actual orbit data found for {satellite}")
                
        except Exception as e:
            print(f"Could not load actual orbit data for {satellite}: {e}")
            import traceback
            traceback.print_exc()
        
        def refined_orbit(t):
            """Refined orbit function that applies correction to idealized orbit."""
            # Get position from idealized orbit
            pos = idealized(t)
            
            # Apply correction if available
            if correction is not None:
                if isinstance(pos, np.ndarray) and pos.ndim == 2:
                    # Multiple positions
                    pos = np.array([correction.apply(p) for p in pos])
                else:
                    # Single position
                    pos = correction.apply(pos)
            
            return pos
        
        return refined_orbit
    
    def _get_idealized_orbit(self, satellite: str, primary: str) -> Optional[Callable]:
        """Get idealized orbit function if available."""
        if not IDEALIZED_ORBITS_AVAILABLE or not ORBITAL_PARAMS:
            return None
        
        # Check if we have orbital parameters for this satellite
        if satellite not in ORBITAL_PARAMS:
            return None
            
        params = ORBITAL_PARAMS[satellite]
        
        # For Mars satellites, use time-varying elements with special transformation
        if primary.lower() == 'mars' and hasattr(idealized_orbits, 'calculate_mars_satellite_elements'):
            def mars_satellite_orbit(t):
                """Generate Mars satellite orbit with proper transformations."""
                # Get current date for time-varying elements
                current_date = datetime.now()
                elements = idealized_orbits.calculate_mars_satellite_elements(current_date, satellite)
                
                a = elements['a']  # Already in AU
                e = elements['e']
                i = np.radians(elements['i'])
                omega = np.radians(elements['omega'])
                Omega = np.radians(elements['Omega'])
                
                # Handle both scalar and array inputs
                t_array = np.atleast_1d(t)
                scalar_input = np.isscalar(t)
                
                # Calculate radius for each point
                r = a * (1 - e**2) / (1 + e * np.cos(t_array))
                
                # Convert to Cartesian in orbital plane
                x_orbit = r * np.cos(t_array)
                y_orbit = r * np.sin(t_array)
                z_orbit = np.zeros_like(t_array)
                
                # Apply orbital element rotations
                if hasattr(idealized_orbits, 'rotate_points'):
                    # 1. Longitude of ascending node
                    x1, y1, z1 = idealized_orbits.rotate_points(x_orbit, y_orbit, z_orbit, Omega, 'z')
                    # 2. Inclination
                    x2, y2, z2 = idealized_orbits.rotate_points(x1, y1, z1, i, 'x')
                    # 3. Argument of periapsis
                    x3, y3, z3 = idealized_orbits.rotate_points(x2, y2, z2, omega, 'z')
                    
                    # 4. Apply Mars equatorial to ecliptic transformation (Y-axis rotation by Mars tilt)
                    mars_tilt = np.radians(25.19)
                    x_final, y_final, z_final = idealized_orbits.rotate_points(x3, y3, z3, mars_tilt, 'y')
                    
                    # Return in AU (no conversion needed)
                    if scalar_input:
                        return np.array([x_final[0], y_final[0], z_final[0]])
                    else:
                        return np.column_stack((x_final, y_final, z_final))
                else:
                    # Fallback without the Mars transformation
                    if scalar_input:
                        return np.array([x_orbit[0], y_orbit[0], z_orbit[0]])
                    else:
                        return np.column_stack((x_orbit, y_orbit, z_orbit))
            
            return mars_satellite_orbit
        
        # For Saturn's Phoebe, use special handling for Laplace plane reference
        elif primary.lower() == 'saturn' and satellite.lower() == 'phoebe':
            def phoebe_orbit(t):
                """Generate Phoebe's orbit with Laplace plane transformation."""
                a = params.get('a', 0.08655)  # Semi-major axis in AU
                e = params.get('e', 0.1635)
                i = np.radians(params.get('i', 175.986))  # Retrograde inclination
                omega = np.radians(params.get('omega', 240.3))
                Omega = np.radians(params.get('Omega', 192.7))
                
                # Handle both scalar and array inputs
                t_array = np.atleast_1d(t)
                scalar_input = np.isscalar(t)
                
                # Calculate radius for each point
                r = a * (1 - e**2) / (1 + e * np.cos(t_array))
                
                # Convert to Cartesian in orbital plane
                x_orbit = r * np.cos(t_array)
                y_orbit = r * np.sin(t_array)
                z_orbit = np.zeros_like(t_array)
                
                # Apply orbital element rotations
                if hasattr(idealized_orbits, 'rotate_points'):
                    # Standard rotation sequence
                    x1, y1, z1 = idealized_orbits.rotate_points(x_orbit, y_orbit, z_orbit, Omega, 'z')
                    x2, y2, z2 = idealized_orbits.rotate_points(x1, y1, z1, i, 'x')
                    x3, y3, z3 = idealized_orbits.rotate_points(x2, y2, z2, omega, 'z')
                    
                    # Transform from Laplace plane to ecliptic
                    laplace_tilt = np.radians(15.0)
                    saturn_orbit_inc = np.radians(2.485)
                    saturn_orbit_node = np.radians(113.665)
                    
                    x4, y4, z4 = idealized_orbits.rotate_points(x3, y3, z3, -laplace_tilt, 'x')
                    x5, y5, z5 = idealized_orbits.rotate_points(x4, y4, z4, -saturn_orbit_node, 'z')
                    x_final, y_final, z_final = idealized_orbits.rotate_points(x5, y5, z5, -saturn_orbit_inc, 'x')
                    
                    if scalar_input:
                        return np.array([x_final[0], y_final[0], z_final[0]])
                    else:
                        return np.column_stack((x_final, y_final, z_final))
                else:
                    # Fallback without transformation
                    if scalar_input:
                        return np.array([x_orbit[0], y_orbit[0], z_orbit[0]])
                    else:
                        return np.column_stack((x_orbit, y_orbit, z_orbit))
            
            return phoebe_orbit
        
        else:
            # Generic satellite orbit (all parameters in AU)
            a = params.get('a', 0.1)  # Semi-major axis already in AU
            e = params.get('e', 0)
            i = np.radians(params.get('i', 0))
            omega = np.radians(params.get('omega', 0))
            Omega = np.radians(params.get('Omega', 0))
            
            def generic_orbit(t):
                """Generate generic satellite orbit."""
                # Handle both scalar and array inputs
                t_array = np.atleast_1d(t)
                scalar_input = np.isscalar(t)
                
                # Solve Kepler's equation
                M = t_array  # Mean anomaly
                E = M.copy()
                for _ in range(10):
                    E = M + e * np.sin(E)
                
                # True anomaly
                nu = 2 * np.arctan2(np.sqrt(1 + e) * np.sin(E/2), 
                                  np.sqrt(1 - e) * np.cos(E/2))
                
                # Radius in AU
                r = a * (1 - e * np.cos(E))
                
                # Position in orbital plane (AU)
                x_orbital = r * np.cos(nu)
                y_orbital = r * np.sin(nu)
                z_orbital = np.zeros_like(t_array)
                
                # Apply rotations using idealized_orbits functions if available
                if hasattr(idealized_orbits, 'rotate_points'):
                    # Standard rotation sequence
                    x1, y1, z1 = idealized_orbits.rotate_points(x_orbital, y_orbital, z_orbital, Omega, 'z')
                    x2, y2, z2 = idealized_orbits.rotate_points(x1, y1, z1, i, 'x')
                    x3, y3, z3 = idealized_orbits.rotate_points(x2, y2, z2, omega, 'z')
                    
                    # Check if this satellite needs special planet-specific transformation
                    if hasattr(idealized_orbits, 'planet_tilts') and primary in idealized_orbits.planet_tilts:
                        tilt = np.radians(idealized_orbits.planet_tilts[primary])
                        # Apply the same transformation idealized orbits uses
                        if primary.lower() == 'pluto':
                            # Pluto uses a complex transformation
                            x4, y4, z4 = idealized_orbits.rotate_points(x3, y3, z3, tilt, 'x')
                            x5, y5, z5 = idealized_orbits.rotate_points(x4, y4, z4, tilt, 'y')
                            z_angle = np.radians(-105)
                            x_final, y_final, z_final = idealized_orbits.rotate_points(x5, y5, z5, z_angle, 'z')
                        else:
                            # Other planets use simple X-axis tilt
                            x_final, y_final, z_final = idealized_orbits.rotate_points(x3, y3, z3, tilt, 'x')
                    else:
                        x_final, y_final, z_final = x3, y3, z3
                    
                    # Return in AU
                    if scalar_input:
                        return np.array([x_final[0], y_final[0], z_final[0]])
                    else:
                        return np.column_stack((x_final, y_final, z_final))
                else:
                    # Fallback: simple rotation matrices
                    positions = np.column_stack((x_orbital, y_orbital, z_orbital))
                    
                    # Apply rotations
                    r_node = Rotation.from_euler('z', Omega)
                    r_inc = Rotation.from_euler('x', i)
                    r_peri = Rotation.from_euler('z', omega)
                    
                    positions = r_node.apply(positions)
                    positions = r_inc.apply(positions)
                    positions = r_peri.apply(positions)
                    
                    # Return in AU
                    if scalar_input:
                        return positions[0]
                    else:
                        return positions
            
            return generic_orbit
    
    def _create_default_orbit(self, satellite: str, primary: str) -> Callable:
        """Create simple default orbit when no data available."""
        # Default radii for common satellites (in AU)
        default_radii_km = {
            ("phobos", "mars"): 9377,
            ("deimos", "mars"): 23463,
            ("io", "jupiter"): 421800,
            ("europa", "jupiter"): 671100,
            ("ganymede", "jupiter"): 1070400,
            ("callisto", "jupiter"): 1882700,
        }
        
        key = (satellite.lower(), primary.lower())
        radius_km = default_radii_km.get(key, 10000)  # Default 10,000 km
        radius_au = radius_km / 149597870.7  # Convert to AU
        
        def default_orbit(t):
            """Simple circular orbit in AU."""
            t = np.asarray(t)
            return np.array([
                radius_au * np.cos(t),
                radius_au * np.sin(t),
                np.zeros_like(t)
            ]).T.squeeze()
        
        return default_orbit
    
    def _calculate_normal(self, positions: np.ndarray) -> np.ndarray:
        """Calculate orbit normal from positions."""
        # Use first three non-collinear points
        r1, r2, r3 = positions[0], positions[1], positions[2]
        v1 = r2 - r1
        v2 = r3 - r1
        n = np.cross(v1, v2)
        return n / np.linalg.norm(n)


# Singleton instance for easy access
_refined_system = None

def get_refined_system(ephemeris_file: str = "satellite_ephemerides.json") -> RefinedOrbitSystem:
    """Get or create the refined orbit system."""
    global _refined_system
    if _refined_system is None:
        _refined_system = RefinedOrbitSystem(ephemeris_file)
    return _refined_system


# Convenience functions that match the pattern of idealized_orbits.py
def create_refined_phobos_orbit():
    """Create refined Phobos orbit function."""
    system = get_refined_system()
    return system.get_orbit_function("Phobos", "Mars")


def create_refined_deimos_orbit():
    """Create refined Deimos orbit function."""
    system = get_refined_system()
    return system.get_orbit_function("Deimos", "Mars")


def create_refined_moon_orbit():
    """Create refined Moon orbit function."""
    system = get_refined_system()
    return system.get_orbit_function("Moon", "Earth")


def create_refined_io_orbit():
    """Create refined Io orbit function."""
    system = get_refined_system()
    return system.get_orbit_function("Io", "Jupiter")


def create_refined_europa_orbit():
    """Create refined Europa orbit function."""
    system = get_refined_system()
    return system.get_orbit_function("Europa", "Jupiter")


def create_refined_ganymede_orbit():
    """Create refined Ganymede orbit function."""
    system = get_refined_system()
    return system.get_orbit_function("Ganymede", "Jupiter")


def create_refined_callisto_orbit():
    """Create refined Callisto orbit function."""
    system = get_refined_system()
    return system.get_orbit_function("Callisto", "Jupiter")


# Generic function for any satellite
def create_refined_orbit(satellite: str, primary: str) -> Callable:
    """Create refined orbit for any satellite."""
    system = get_refined_system()
    return system.get_orbit_function(satellite, primary)


# Validation and reporting
def validate_all_orbits():
    """Validate all available refined orbits."""
    system = get_refined_system()
    
    print("Refined Orbits Status Report")
    print("=" * 60)
    
    satellites = [
        ("Phobos", "Mars"),
        ("Deimos", "Mars"),
        ("Moon", "Earth"),
        ("Io", "Jupiter"),
        ("Europa", "Jupiter"),
        ("Ganymede", "Jupiter"),
        ("Callisto", "Jupiter"),
    ]
    
    for satellite, primary in satellites:
        key = f"{primary}_{satellite}".lower()
        has_ephemeris = key in system.ephemeris_data.get("satellites", {})
        has_idealized = satellite in ORBITAL_PARAMS if ORBITAL_PARAMS else False
        
        if has_ephemeris and has_idealized:
            status = "✓ Refined"
        elif has_idealized:
            status = "○ Idealized only"
        else:
            status = "✗ Default only"
        
        orbit_func = system.get_orbit_function(satellite, primary)
        test_pos = orbit_func(0)
        radius = np.linalg.norm(test_pos)
        
        # Check if it's returning km or AU
        if radius < 100:  # Likely in AU
            radius_km = radius * 149597870.7  # Convert to km
            print(f"{satellite:<12} ({primary:<8}): {status}  r = {radius:.6f} AU ({radius_km:,.0f} km)")
        else:
            radius_au = radius / 149597870.7  # Convert to AU
            print(f"{satellite:<12} ({primary:<8}): {status}  r = {radius:,.0f} km ({radius_au:.6f} AU)")
    
    print("=" * 60)
    print("✓ = Refined (idealized + correction), ○ = Idealized only, ✗ = Default circular")


if __name__ == "__main__":
    # Example usage
    print("Creating refined orbit functions...")
    
    # Get refined Phobos orbit
    phobos_orbit = create_refined_phobos_orbit()
    
    # Test it
    print("\nPhobos position at t=0:", phobos_orbit(0))
    print("Phobos position at t=π:", phobos_orbit(np.pi))
    
    # Validate all orbits
    print("\n")
    validate_all_orbits()
