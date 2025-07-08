"""
Integration code for using refined orbits in palomas_orrery.py

This shows how to modify the existing orrery code to support both
idealized and refined orbits with minimal changes.
"""

import numpy as np
from typing import Dict, List, Callable, Optional
import json
import os

# Import both orbit systems
try:
    import idealized_orbits
    IDEALIZED_AVAILABLE = True
except ImportError:
    IDEALIZED_AVAILABLE = False
    print("Warning: idealized_orbits.py not found")

try:
    import refined_orbits
    REFINED_AVAILABLE = True
except ImportError:
    REFINED_AVAILABLE = False
    print("Warning: refined_orbits.py not found")


class OrreryConfiguration:
    """Configuration for orbit selection and display options."""
    
    def __init__(self):
        self.use_refined_orbits = True  # Default to refined if available
        self.ephemeris_file = "satellite_ephemerides.json"
        self.show_orbit_comparison = False
        self.refined_orbit_color = 'gold'
        self.idealized_orbit_color = 'silver'
        self.orbit_alpha = 0.6
        
    def load_from_file(self, config_file: str = "orrery_config.json"):
        """Load configuration from JSON file."""
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                config = json.load(f)
                for key, value in config.items():
                    if hasattr(self, key):
                        setattr(self, key, value)


# Global configuration instance
orrery_config = OrreryConfiguration()


def get_orbit_function(object_name: str, primary: str = None) -> Callable:
    """
    Get the appropriate orbit function for an object.
    
    This is the main integration point - it returns either a refined
    or idealized orbit based on configuration and availability.
    """
    
    # Map object names to their primaries if not provided
    object_to_primary = {
        'phobos': 'mars',
        'deimos': 'mars',
        'io': 'jupiter',
        'europa': 'jupiter',
        'ganymede': 'jupiter',
        'callisto': 'jupiter',
        'titan': 'saturn',
        'enceladus': 'saturn',
        'moon': 'earth',
    }
    
    obj_lower = object_name.lower()
    if primary is None and obj_lower in object_to_primary:
        primary = object_to_primary[obj_lower]
    
    # Try refined orbits first if configured
    if orrery_config.use_refined_orbits and REFINED_AVAILABLE:
        try:
            if primary:
                return refined_orbits.create_refined_orbit(object_name, primary)
            else:
                # Try the convenience functions
                func_name = f"create_refined_{obj_lower}_orbit"
                if hasattr(refined_orbits, func_name):
                    return getattr(refined_orbits, func_name)()
        except Exception as e:
            print(f"Could not get refined orbit for {object_name}: {e}")
    
    # Fall back to idealized orbits
    if IDEALIZED_AVAILABLE:
        func_name = f"create_{obj_lower}_orbit"
        if hasattr(idealized_orbits, func_name):
            return getattr(idealized_orbits, func_name)()
    
    # Last resort: simple circular orbit
    print(f"Warning: No orbit function found for {object_name}")
    radius = 10000  # Default 10,000 km
    
    def default_orbit(t):
        t = np.asarray(t)
        return np.array([
            radius * np.cos(t),
            radius * np.sin(t),
            np.zeros_like(t)
        ]).T.squeeze()
    
    return default_orbit


def create_orrery_objects(config: dict) -> Dict[str, Dict]:
    """
    Create orrery objects with appropriate orbit functions.
    
    This replaces/enhances the object creation in palomas_orrery.py
    """
    objects = {}
    
    for obj_name, obj_config in config.items():
        # Get orbit function
        primary = obj_config.get('primary', None)
        orbit_func = get_orbit_function(obj_name, primary)
        
        # Create object entry
        objects[obj_name] = {
            'orbit': orbit_func,
            'color': obj_config.get('color', 'white'),
            'size': obj_config.get('size', 5),
            'primary': primary,
            'show_orbit': obj_config.get('show_orbit', True),
            'orbit_segments': obj_config.get('orbit_segments', 100),
            'is_refined': orrery_config.use_refined_orbits and REFINED_AVAILABLE
        }
        
    return objects


def plot_objects_enhanced(objects: Dict, t: float, ax, show_orbits: bool = True, 
                         show_comparison: bool = False):
    """
    Enhanced version of plot_objects that can show orbit comparisons.
    """
    import matplotlib.pyplot as plt
    
    for name, obj in objects.items():
        # Get current position
        pos = obj['orbit'](t)
        
        # Plot object
        ax.scatter(pos[0], pos[1], pos[2], 
                  color=obj['color'], 
                  s=obj['size']**2,
                  label=name.title())
        
        # Plot orbit trail if requested
        if show_orbits and obj.get('show_orbit', True):
            t_orbit = np.linspace(0, 2*np.pi, obj.get('orbit_segments', 100))
            orbit_positions = np.array([obj['orbit'](t) for t in t_orbit])
            
            # Choose color based on orbit type
            orbit_color = (orrery_config.refined_orbit_color 
                          if obj.get('is_refined', False) 
                          else orrery_config.idealized_orbit_color)
            
            ax.plot(orbit_positions[:, 0], 
                   orbit_positions[:, 1], 
                   orbit_positions[:, 2],
                   color=orbit_color,
                   alpha=orrery_config.orbit_alpha,
                   linewidth=1)
        
        # Show comparison orbits if requested
        if (show_comparison and orrery_config.show_orbit_comparison 
            and IDEALIZED_AVAILABLE and obj.get('is_refined', False)):
            
            # Get idealized orbit for comparison
            try:
                func_name = f"create_{name.lower()}_orbit"
                if hasattr(idealized_orbits, func_name):
                    idealized_func = getattr(idealized_orbits, func_name)()
                    orbit_positions = np.array([idealized_func(t) for t in t_orbit])
                    
                    ax.plot(orbit_positions[:, 0], 
                           orbit_positions[:, 1], 
                           orbit_positions[:, 2],
                           color=orrery_config.idealized_orbit_color,
                           alpha=orrery_config.orbit_alpha * 0.5,
                           linewidth=1,
                           linestyle='--')
            except:
                pass


def animate_objects_enhanced(objects: Dict, duration: float = 10.0, fps: int = 30,
                           show_comparison: bool = False):
    """
    Enhanced animation function that supports orbit comparisons.
    """
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation
    from mpl_toolkits.mplot3d import Axes3D
    
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Set up the plot
    ax.set_xlabel('X (km)')
    ax.set_ylabel('Y (km)')
    ax.set_zlabel('Z (km)')
    ax.set_title('Solar System Orrery - Enhanced')
    
    # Calculate axis limits
    max_radius = 0
    for obj in objects.values():
        test_positions = np.array([obj['orbit'](t) for t in np.linspace(0, 2*np.pi, 50)])
        max_radius = max(max_radius, np.max(np.abs(test_positions)))
    
    ax.set_xlim([-max_radius, max_radius])
    ax.set_ylim([-max_radius, max_radius])
    ax.set_zlim([-max_radius/10, max_radius/10])  # Compressed Z axis
    
    # Animation update function
    def update(frame):
        ax.clear()
        
        # Reconfigure axes
        ax.set_xlabel('X (km)')
        ax.set_ylabel('Y (km)')
        ax.set_zlabel('Z (km)')
        ax.set_xlim([-max_radius, max_radius])
        ax.set_ylim([-max_radius, max_radius])
        ax.set_zlim([-max_radius/10, max_radius/10])
        
        # Calculate time
        t = frame / (fps * duration) * 2 * np.pi
        
        # Plot objects
        plot_objects_enhanced(objects, t, ax, show_orbits=True, 
                            show_comparison=show_comparison)
        
        # Add time display
        ax.text2D(0.05, 0.95, f'Time: {t/(2*np.pi)*100:.1f}%', 
                 transform=ax.transAxes)
        
        # Add orbit type indicator
        orbit_type = "Refined" if orrery_config.use_refined_orbits else "Idealized"
        ax.text2D(0.05, 0.90, f'Orbits: {orbit_type}', 
                 transform=ax.transAxes, color='gold' if orrery_config.use_refined_orbits else 'silver')
        
        # Add legend
        if frame == 0:
            ax.legend(loc='upper right')
    
    # Create animation
    n_frames = int(duration * fps)
    anim = FuncAnimation(fig, update, frames=n_frames, interval=1000/fps, blit=False)
    
    return fig, anim


# Modified version of the main plotting function for palomas_orrery.py
def plot_palomas_orrery(date_time=None, show_orbits=True, use_refined=None):
    """
    Main plotting function that integrates with palomas_orrery.py
    
    Parameters:
    -----------
    date_time : datetime, optional
        Time to display (default: now)
    show_orbits : bool
        Whether to show orbit trails
    use_refined : bool, optional
        Override the default orbit type (None = use config)
    """
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    from datetime import datetime
    
    # Override configuration if specified
    if use_refined is not None:
        original = orrery_config.use_refined_orbits
        orrery_config.use_refined_orbits = use_refined
    
    # Define objects (this would come from palomas_orrery.py config)
    orrery_objects = {
        'mars': {
            'primary': 'sun',
            'color': 'red',
            'size': 6
        },
        'phobos': {
            'primary': 'mars',
            'color': 'gray',
            'size': 3
        },
        'deimos': {
            'primary': 'mars',
            'color': 'lightgray',
            'size': 2
        }
    }
    
    # Create objects with appropriate orbits
    objects = create_orrery_objects(orrery_objects)
    
    # Create plot
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Calculate time parameter (simplified - would need proper conversion)
    if date_time is None:
        date_time = datetime.now()
    t = 0  # Would calculate from date_time
    
    # Plot objects
    plot_objects_enhanced(objects, t, ax, show_orbits=show_orbits,
                         show_comparison=orrery_config.show_orbit_comparison)
    
    # Configure plot
    ax.set_xlabel('X (km)')
    ax.set_ylabel('Y (km)')
    ax.set_zlabel('Z (km)')
    
    orbit_type = "Refined" if orrery_config.use_refined_orbits else "Idealized"
    ax.set_title(f"Paloma's Orrery - {orbit_type} Orbits\n{date_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    plt.legend()
    plt.show()
    
    # Restore configuration if overridden
    if use_refined is not None:
        orrery_config.use_refined_orbits = original
    
    return fig, ax


# Validation function to check orbit accuracy
def validate_orbit_accuracy():
    """Compare refined vs idealized orbits for all available objects."""
    if not (REFINED_AVAILABLE and IDEALIZED_AVAILABLE):
        print("Both orbit systems needed for comparison")
        return
    
    objects = ['phobos', 'deimos', 'io', 'europa', 'ganymede', 'callisto']
    
    print("Orbit Comparison Report")
    print("=" * 70)
    print(f"{'Object':<12} {'Idealized R (km)':<18} {'Refined R (km)':<18} {'Difference':<12}")
    print("-" * 70)
    
    for obj in objects:
        try:
            # Get both orbit types
            ideal_func = getattr(idealized_orbits, f"create_{obj}_orbit", None)
            refined_func = getattr(refined_orbits, f"create_refined_{obj}_orbit", None)
            
            if ideal_func and refined_func:
                ideal_orbit = ideal_func()
                refined_orbit = refined_func()
                
                # Compare at t=0
                ideal_pos = ideal_orbit(0)
                refined_pos = refined_orbit(0)
                
                ideal_r = np.linalg.norm(ideal_pos)
                refined_r = np.linalg.norm(refined_pos)
                diff = refined_r - ideal_r
                
                print(f"{obj.title():<12} {ideal_r:<18.1f} {refined_r:<18.1f} {diff:<+12.1f}")
        except Exception as e:
            print(f"{obj.title():<12} Error: {e}")
    
    print("=" * 70)


if __name__ == "__main__":
    # Example usage
    print("Orrery Integration Module")
    print("-" * 40)
    
    # Validate orbit accuracy
    validate_orbit_accuracy()
    
    # Example: Create Mars system with refined orbits
    print("\nCreating Mars system...")
    mars_system = {
        'phobos': get_orbit_function('phobos', 'mars'),
        'deimos': get_orbit_function('deimos', 'mars')
    }
    
    for name, orbit_func in mars_system.items():
        pos = orbit_func(0)
        print(f"{name}: {pos}, r = {np.linalg.norm(pos):.1f} km")
