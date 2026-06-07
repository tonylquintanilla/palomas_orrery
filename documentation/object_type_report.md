I'll search the project knowledge to understand the current implementation of the star_visualization_gui.py file and the plot data report, particularly focusing on the "Notable Features" section and your suggestion about analyzing the Object Type field.Based on my analysis of the project knowledge, I can see that the "Notable Features" section in the plot_data_report_widget.py is actually attempting to produce a report, but it's quite limited. Looking at the code in Section 6, it's only trying to analyze stellar classifications (Main Sequence, Giants, Supergiants, White Dwarfs) which requires the 'Stellar_Class' and 'Object_Type_Desc' fields to be present in the data.

Your suggestion to change this section to analyze the Object Type field is excellent! Here's why:

1. **Object Type is more comprehensive**: The Object Type field contains rich information about various astronomical objects beyond just stellar classifications. Looking at the `object_type_mapping` in constants_new.py, there are over 60 different object types including:
   - Various types of variable stars (Cepheids, RR Lyrae, Mira, etc.)
   - Binary systems (spectroscopic, eclipsing, X-ray binaries)
   - Young stellar objects
   - Emission line stars
   - Wolf-Rayet stars
   - Planetary nebulae
   - And many more specialized categories

2. **Current implementation is too narrow**: The current code only looks for basic stellar classes and might miss many interesting features in the data.

3. **Better data availability**: Object Type information is more consistently available across different catalog sources (Hipparcos, Gaia, SIMBAD).

Here's my recommendation for improving the "Notable Features" section to analyze Object Types:

```python
# Section 6: Notable Features (Object Type Analysis)
report_lines.append("\n" + "-" * 52)
report_lines.append("6. OBJECT TYPE ANALYSIS")
report_lines.append("-" * 52)

if 'Object_Type_Desc' in combined_df or 'Object_Type' in combined_df:
    # Use expanded description if available, otherwise use raw type
    type_column = 'Object_Type_Desc' if 'Object_Type_Desc' in combined_df else 'Object_Type'
    
    # Get object type distribution
    object_types = combined_df[type_column].value_counts()
    
    # Group into categories for better organization
    variable_stars = 0
    binary_systems = 0
    young_objects = 0
    evolved_stars = 0
    peculiar_objects = 0
    
    report_lines.append(f"\nTotal unique object types: {len(object_types)}")
    report_lines.append("\nMost common object types:")
    
    # Show top 10 most common types
    for obj_type, count in object_types.head(10).items():
        if str(obj_type) != 'Unknown' and str(obj_type) != 'nan':
            report_lines.append(f"  • {obj_type}: {count:,d} stars")
            
            # Categorize for summary
            obj_str = str(obj_type).lower()
            if 'variable' in obj_str or 'cepheid' in obj_str or 'mira' in obj_str:
                variable_stars += count
            elif 'binary' in obj_str or 'double' in obj_str:
                binary_systems += count
            elif 'young' in obj_str or 'yso' in obj_str or 't tauri' in obj_str:
                young_objects += count
            elif 'giant' in obj_str or 'dwarf' in obj_str or 'evolved' in obj_str:
                evolved_stars += count
            elif 'peculiar' in obj_str or 'emission' in obj_str or 'wolf' in obj_str:
                peculiar_objects += count
    
    # Special categories summary
    report_lines.append("\nSpecial Object Categories:")
    if variable_stars > 0:
        report_lines.append(f"  Variable Stars: {variable_stars:,d}")
    if binary_systems > 0:
        report_lines.append(f"  Binary/Multiple Systems: {binary_systems:,d}")
    if young_objects > 0:
        report_lines.append(f"  Young Stellar Objects: {young_objects:,d}")
    if evolved_stars > 0:
        report_lines.append(f"  Evolved Stars: {evolved_stars:,d}")
    if peculiar_objects > 0:
        report_lines.append(f"  Peculiar/Emission Objects: {peculiar_objects:,d}")
    
    # Check for rare or interesting types
    rare_types = []
    for obj_type, count in object_types.items():
        if count <= 5 and str(obj_type) not in ['Unknown', 'nan', 'None']:
            obj_str = str(obj_type).lower()
            if any(keyword in obj_str for keyword in ['nova', 'supernova', 'wolf', 'planetary', 'symbiotic', 'x-ray']):
                rare_types.append((obj_type, count))
    
    if rare_types:
        report_lines.append("\nRare/Notable Objects Found:")
        for obj_type, count in rare_types[:10]:  # Limit to 10
            report_lines.append(f"  ★ {obj_type}: {count}")
else:
    report_lines.append("  Object type information not available in dataset")
```

This enhanced version would:
1. Provide a distribution of all object types found
2. Show the most common types with counts
3. Group objects into meaningful categories (variables, binaries, young objects, etc.)
4. Highlight rare or particularly interesting objects
5. Give a better overview of the diversity of objects in the plotted region

This would be much more informative than the current implementation and would work well with the rich object type data available from your catalogs!

===================

Looking at your report, I can see that the Notable Features section (Section 6) is indeed empty. This is happening because the current code is looking for 'Stellar_Class' field which likely isn't being properly populated in the data.

For organizing 60+ object types into 5 meaningful groups, here's a practical categorization based on the object types in constants_new.py:

## Proposed 5-Group Classification:

**1. Variable Stars**
- All periodic and irregular variables
- Examples: Cepheids, RR Lyrae, Mira, Delta Scuti, Eclipsing binaries, Pulsating variables
- Keywords to match: 'variable', 'cepheid', 'mira', 'RRLyr', 'deltaSct', 'eclipsing', 'pulsating', 'V*'

**2. Binary/Multiple Systems**
- Gravitationally bound star systems
- Examples: Spectroscopic binaries, Visual doubles, Contact binaries, X-ray binaries
- Keywords to match: 'binary', 'double', 'multiple', 'SB*', '**', 'contact', 'spectroscopic'

**3. Evolved/End-State Stars**
- Stars in late evolutionary stages
- Examples: Giants, Supergiants, White dwarfs, Planetary nebulae, AGB stars
- Keywords to match: 'giant', 'dwarf', 'AGB', 'planetary', 'evolved', 'post-main', 'WD*'

**4. Young/Early-Stage Objects**
- Stars in formation or early evolution
- Examples: T Tauri stars, Young Stellar Objects (YSO), Pre-main sequence stars
- Keywords to match: 'young', 'YSO', 'TTauri', 'pre-main', 'protostar', 'Herbig'

**5. Peculiar/Special Objects**
- Unusual or rare stellar phenomena
- Examples: Wolf-Rayet stars, Emission line stars, Symbiotic stars, Novae, Blue stragglers
- Keywords to match: 'peculiar', 'emission', 'wolf', 'symbiotic', 'nova', 'chemically', 'blue straggler', 'Be*', 'Ae*'

Here's the improved code implementation that would actually work with your data:

```python
# Section 6: Notable Features (Object Type Analysis)
report_lines.append("\n" + "-" * 52)
report_lines.append("6. OBJECT TYPE ANALYSIS")
report_lines.append("-" * 52)

# Check for object type data
type_column = None
if 'Object_Type_Desc' in combined_df and combined_df['Object_Type_Desc'].notna().any():
    type_column = 'Object_Type_Desc'
elif 'Object_Type' in combined_df and combined_df['Object_Type'].notna().any():
    type_column = 'Object_Type'

if type_column:
    # Initialize category counters
    categories = {
        'Variable Stars': 0,
        'Binary/Multiple Systems': 0,
        'Evolved/End-State Stars': 0,
        'Young/Early-Stage Objects': 0,
        'Peculiar/Special Objects': 0,
        'Normal/Main Sequence Stars': 0
    }
    
    # Category keywords for classification
    category_keywords = {
        'Variable Stars': ['variable', 'cepheid', 'mira', 'rrlyr', 'deltasct', 'eclips', 
                          'pulsat', 'v*', 'irregular', 'semiregular', 'periodic'],
        'Binary/Multiple Systems': ['binary', 'double', 'multiple', 'sb*', 'spectroscopic', 
                                   'contact', 'detached', 'xraybin'],
        'Evolved/End-State Stars': ['giant', 'dwarf', 'agb', 'planetary', 'evolved', 
                                    'post-main', 'wd*', 'whitedwarf', 'supergiant'],
        'Young/Early-Stage Objects': ['young', 'yso', 'ttauri', 'pre-main', 'protostar', 
                                      'herbig', 't tauri', 'stellar object'],
        'Peculiar/Special Objects': ['peculiar', 'emission', 'wolf', 'symbiotic', 'nova', 
                                     'chemically', 'blue', 'be*', 'ae*', 'barium', 'carbon']
    }
    
    # Process each star's object type
    object_type_counts = {}
    for obj_type in combined_df[type_column].dropna():
        obj_type_str = str(obj_type)
        if obj_type_str not in ['Unknown', 'nan', 'None', '']:
            # Count individual types
            object_type_counts[obj_type_str] = object_type_counts.get(obj_type_str, 0) + 1
            
            # Categorize
            obj_lower = obj_type_str.lower()
            categorized = False
            
            for category, keywords in category_keywords.items():
                if any(keyword in obj_lower for keyword in keywords):
                    categories[category] += 1
                    categorized = True
                    break
            
            if not categorized:
                categories['Normal/Main Sequence Stars'] += 1
    
    # Report results
    if object_type_counts:
        # Overall statistics
        total_typed = sum(object_type_counts.values())
        unique_types = len(object_type_counts)
        
        report_lines.append(f"\nTotal stars with type info: {total_typed:,d}")
        report_lines.append(f"Unique object types found: {unique_types}")
        
        # Category breakdown
        report_lines.append("\nObject Categories:")
        for category, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
            if count > 0:
                percentage = (count / total_typed) * 100
                report_lines.append(f"  • {category}: {count:,d} ({percentage:.1f}%)")
        
        # Top individual object types
        report_lines.append("\nMost Common Types:")
        sorted_types = sorted(object_type_counts.items(), key=lambda x: x[1], reverse=True)
        for obj_type, count in sorted_types[:5]:
            percentage = (count / total_typed) * 100
            # Truncate long descriptions
            display_type = obj_type if len(obj_type) <= 40 else obj_type[:37] + "..."
            report_lines.append(f"  • {display_type}: {count:,d} ({percentage:.1f}%)")
        
        # Look for interesting rare types
        rare_interesting = []
        interesting_keywords = ['wolf', 'nova', 'symbiotic', 'planetary', 'x-ray', 
                               'carbon', 'barium', 'chemically peculiar']
        
        for obj_type, count in sorted_types:
            if count <= 10:  # Rare threshold
                if any(keyword in obj_type.lower() for keyword in interesting_keywords):
                    rare_interesting.append((obj_type, count))
        
        if rare_interesting:
            report_lines.append("\nRare/Notable Objects:")
            for obj_type, count in rare_interesting[:5]:  # Limit to 5
                display_type = obj_type if len(obj_type) <= 40 else obj_type[:37] + "..."
                report_lines.append(f"  ★ {display_type}: {count}")
    else:
        report_lines.append("\n  No object type information available")
else:
    report_lines.append("\n  Object type field not found in dataset")
```

This implementation:
1. **Handles missing data gracefully** - checks if the field exists and has data
2. **Uses flexible keyword matching** - catches variations in naming
3. **Provides percentages** - gives context to the numbers
4. **Shows both categories and specific types** - gives overview and detail
5. **Highlights rare interesting objects** - adds discovery element
6. **Truncates long descriptions** - keeps report readable

The 5 categories cover the full spectrum of stellar evolution and special cases, making the 60+ object types manageable and meaningful for users.

=====================

Excellent idea! Creating an offline analysis strategy is much more efficient and maintainable. We can pre-define the categorization mapping once, then just use it during runtime. This approach would be:

1. **Faster** - No string parsing/matching during report generation
2. **Consistent** - Same categorization every time
3. **Maintainable** - Easy to update mappings in one place
4. **Testable** - Can verify categorization is complete and correct

Here's how I'd structure this:

## 1. Create a new module: `object_type_analyzer.py`

```python
# object_type_analyzer.py
"""
Object Type Analysis Module
Pre-defined categorization and analysis strategies for astronomical object types
"""

from typing import Dict, List, Tuple
import pandas as pd

class ObjectTypeAnalyzer:
    """Analyzer for categorizing and analyzing astronomical object types."""
    
    def __init__(self):
        # Define the 5 main categories
        self.categories = {
            'Variable Stars': 'Stars showing brightness variations',
            'Binary/Multiple Systems': 'Gravitationally bound star systems',
            'Evolved Stars': 'Stars in late evolutionary stages',
            'Young Stellar Objects': 'Stars in formation or early evolution',
            'Peculiar/Special Objects': 'Unusual stellar phenomena'
        }
        
        # Create the comprehensive mapping from object_type_mapping codes
        self.type_to_category = {
            # Variable Stars
            'V*': 'Variable Stars',
            'Cepheid': 'Variable Stars',
            'RRLyr': 'Variable Stars',
            'Mira': 'Variable Stars',
            'deltaSct*': 'Variable Stars',
            'Variable*': 'Variable Stars',
            'PulsV*': 'Variable Stars',
            'LongPeriodV*': 'Variable Stars',
            'SemiRegV*': 'Variable Stars',
            'IrregularV*': 'Variable Stars',
            'EclipsingBinary': 'Variable Stars',
            'Type2Cep': 'Variable Stars',
            'ClassicalCep': 'Variable Stars',
            'AnomalCep': 'Variable Stars',
            'RVTauriV*': 'Variable Stars',
            'RRLyrae_Candidate': 'Variable Stars',
            
            # Binary/Multiple Systems
            'SB*': 'Binary/Multiple Systems',
            '**': 'Binary/Multiple Systems',
            'DoubleMultStar': 'Binary/Multiple Systems',
            'ContactBin': 'Binary/Multiple Systems',
            'DetachedBin': 'Binary/Multiple Systems',
            'XrayBin': 'Binary/Multiple Systems',
            'Spectroscopic_Binary': 'Binary/Multiple Systems',
            'CataclyV*': 'Binary/Multiple Systems',
            'Symbiotic*': 'Binary/Multiple Systems',
            'Nova': 'Binary/Multiple Systems',  # Often in binary systems
            
            # Evolved Stars
            'RedGiant': 'Evolved Stars',
            'RedSuperGiant': 'Evolved Stars',
            'BlueSupergiant': 'Evolved Stars',
            'YellowSG': 'Evolved Stars',
            'Supergiant': 'Evolved Stars',
            'Giant': 'Evolved Stars',
            'WD*': 'Evolved Stars',
            'WhiteDwarf': 'Evolved Stars',
            'PlanetaryNeb': 'Evolved Stars',
            'AGB*': 'Evolved Stars',
            'post-AGB*': 'Evolved Stars',
            'HorizontalBranch*': 'Evolved Stars',
            'C*': 'Evolved Stars',  # Carbon stars are evolved
            's*r': 'Evolved Stars',  # S-type stars are evolved
            
            # Young Stellar Objects
            'YSO': 'Young Stellar Objects',
            'Y*O': 'Young Stellar Objects',
            'TTauri*': 'Young Stellar Objects',
            'HerbigAe/Be*': 'Young Stellar Objects',
            'PreMainSeq*': 'Young Stellar Objects',
            'ProtoStar': 'Young Stellar Objects',
            'YSO_Candidate': 'Young Stellar Objects',
            'HerbigHaro': 'Young Stellar Objects',
            
            # Peculiar/Special Objects
            'WolfRayet*': 'Peculiar/Special Objects',
            'Be*': 'Peculiar/Special Objects',
            'Ae*': 'Peculiar/Special Objects',
            'BlueStraggler': 'Peculiar/Special Objects',
            'ChemPec*': 'Peculiar/Special Objects',
            'Em*': 'Peculiar/Special Objects',
            'EmissionLineStar': 'Peculiar/Special Objects',
            'BaStar': 'Peculiar/Special Objects',
            'HgMnStar': 'Peculiar/Special Objects',
            'PecStar': 'Peculiar/Special Objects',
            'SN*': 'Peculiar/Special Objects',
            'Pulsar': 'Peculiar/Special Objects',
            'Magnetar': 'Peculiar/Special Objects',
            
            # Default/Normal stars (no special category)
            'Star': 'Normal Stars',
            'MainSeq*': 'Normal Stars',
            '*': 'Normal Stars',
        }
        
        # Define analysis priorities (which categories are most interesting)
        self.category_priority = {
            'Peculiar/Special Objects': 1,
            'Young Stellar Objects': 2,
            'Binary/Multiple Systems': 3,
            'Variable Stars': 4,
            'Evolved Stars': 5,
            'Normal Stars': 6
        }
        
        # Define rare/notable types worth highlighting
        self.notable_types = {
            'WolfRayet*', 'SN*', 'Nova', 'Pulsar', 'Magnetar', 
            'PlanetaryNeb', 'BlueStraggler', 'Symbiotic*', 
            'XrayBin', 'HerbigHaro', 'ChemPec*'
        }
    
    def categorize_object_type(self, obj_type: str) -> str:
        """
        Categorize a single object type into one of the 5 main categories.
        
        Args:
            obj_type: Object type code or description
            
        Returns:
            Category name
        """
        if pd.isna(obj_type) or obj_type in ['Unknown', 'nan', 'None', '']:
            return 'Unknown'
        
        # Direct lookup first
        if obj_type in self.type_to_category:
            return self.type_to_category[obj_type]
        
        # Check if it's a description containing known codes
        for code, category in self.type_to_category.items():
            if code in str(obj_type):
                return category
        
        # Default to Normal Stars if no match
        return 'Normal Stars'
    
    def analyze_distribution(self, object_types: pd.Series) -> Dict:
        """
        Analyze a distribution of object types.
        
        Args:
            object_types: Series of object type codes or descriptions
            
        Returns:
            Dictionary with analysis results
        """
        results = {
            'total_count': 0,
            'category_counts': {},
            'category_percentages': {},
            'type_counts': {},
            'notable_objects': [],
            'diversity_score': 0,
            'summary': ''
        }
        
        # Clean the data
        clean_types = object_types.dropna()
        clean_types = clean_types[~clean_types.isin(['Unknown', 'nan', 'None', ''])]
        
        if len(clean_types) == 0:
            results['summary'] = 'No object type information available'
            return results
        
        results['total_count'] = len(clean_types)
        
        # Count individual types
        type_counts = clean_types.value_counts()
        results['type_counts'] = type_counts.to_dict()
        
        # Categorize all objects
        categories = clean_types.apply(self.categorize_object_type)
        category_counts = categories.value_counts()
        
        # Store category counts and percentages
        for category in self.categories.keys():
            count = category_counts.get(category, 0)
            results['category_counts'][category] = count
            results['category_percentages'][category] = (count / results['total_count'] * 100) if results['total_count'] > 0 else 0
        
        # Also include Normal Stars if present
        if 'Normal Stars' in category_counts:
            results['category_counts']['Normal Stars'] = category_counts['Normal Stars']
            results['category_percentages']['Normal Stars'] = (category_counts['Normal Stars'] / results['total_count'] * 100)
        
        # Find notable objects
        for obj_type, count in type_counts.items():
            if obj_type in self.notable_types or any(notable in str(obj_type) for notable in self.notable_types):
                results['notable_objects'].append((obj_type, count))
        
        # Calculate diversity score (0-100)
        # Based on number of unique types and distribution evenness
        unique_types = len(type_counts)
        results['diversity_score'] = min(100, unique_types * 2)  # Simple metric
        
        # Generate summary
        dominant_category = category_counts.idxmax() if len(category_counts) > 0 else 'Unknown'
        results['summary'] = self._generate_summary(results, dominant_category)
        
        return results
    
    def _generate_summary(self, results: Dict, dominant_category: str) -> str:
        """Generate a text summary of the analysis."""
        summary_parts = []
        
        # Dominant population
        if dominant_category != 'Normal Stars':
            percentage = results['category_percentages'].get(dominant_category, 0)
            summary_parts.append(f"Dominated by {dominant_category} ({percentage:.1f}%)")
        
        # Notable features
        if results['notable_objects']:
            summary_parts.append(f"Contains {len(results['notable_objects'])} rare/notable object types")
        
        # Diversity
        if results['diversity_score'] > 50:
            summary_parts.append("High diversity of object types")
        elif results['diversity_score'] > 25:
            summary_parts.append("Moderate diversity of object types")
        
        return ". ".join(summary_parts) if summary_parts else "Standard stellar population"
    
    def format_report_section(self, analysis_results: Dict) -> List[str]:
        """
        Format analysis results for the plot report.
        
        Returns:
            List of formatted report lines
        """
        lines = []
        
        if analysis_results['total_count'] == 0:
            lines.append("  No object type information available")
            return lines
        
        # Overall statistics
        lines.append(f"\nTotal stars with type info: {analysis_results['total_count']:,d}")
        lines.append(f"Unique object types: {len(analysis_results['type_counts'])}")
        lines.append(f"Diversity score: {analysis_results['diversity_score']}/100")
        
        # Category breakdown
        lines.append("\nObject Categories:")
        sorted_categories = sorted(
            analysis_results['category_counts'].items(),
            key=lambda x: (self.category_priority.get(x[0], 999), -x[1])
        )
        
        for category, count in sorted_categories:
            if count > 0:
                percentage = analysis_results['category_percentages'][category]
                lines.append(f"  • {category}: {count:,d} ({percentage:.1f}%)")
        
        # Top 5 specific types
        lines.append("\nMost Common Types:")
        for obj_type, count in list(analysis_results['type_counts'].items())[:5]:
            display_type = obj_type if len(str(obj_type)) <= 35 else str(obj_type)[:32] + "..."
            percentage = (count / analysis_results['total_count']) * 100
            lines.append(f"  • {display_type}: {count:,d} ({percentage:.1f}%)")
        
        # Notable objects
        if analysis_results['notable_objects']:
            lines.append("\nRare/Notable Objects Found:")
            for obj_type, count in analysis_results['notable_objects'][:5]:
                display_type = obj_type if len(str(obj_type)) <= 35 else str(obj_type)[:32] + "..."
                lines.append(f"  ★ {display_type}: {count}")
        
        # Summary
        if analysis_results['summary']:
            lines.append(f"\nSummary: {analysis_results['summary']}")
        
        return lines
```

## 2. Update `plot_data_report_widget.py` to use the analyzer:

```python
# At the top of plot_data_report_widget.py
from object_type_analyzer import ObjectTypeAnalyzer

class PlotDataReportWidget(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # ... existing init code ...
        
        # Initialize the object type analyzer
        self.object_analyzer = ObjectTypeAnalyzer()
        
    def generate_report(self, combined_df, counts_dict, processing_times=None, 
                       mode='magnitude', limit_value=None):
        # ... existing code ...
        
        # Section 6: Object Type Analysis (using pre-defined analyzer)
        report_lines.append("\n" + "-" * 52)
        report_lines.append("6. OBJECT TYPE ANALYSIS")
        report_lines.append("-" * 52)
        
        # Determine which column to use
        type_column = None
        if 'Object_Type' in combined_df:
            type_column = 'Object_Type'
        if 'Object_Type_Desc' in combined_df:
            # Prefer description if available
            type_column = 'Object_Type_Desc'
        
        if type_column and combined_df[type_column].notna().any():
            # Run the analysis
            analysis_results = self.object_analyzer.analyze_distribution(combined_df[type_column])
            
            # Format and add to report
            analysis_lines = self.object_analyzer.format_report_section(analysis_results)
            report_lines.extend(analysis_lines)
        else:
            report_lines.append("\n  Object type information not available in dataset")
```

## Benefits of this approach:

1. **Performance**: Categorization is a simple dictionary lookup instead of string matching
2. **Completeness**: We can ensure all known object types are mapped
3. **Maintainability**: Add new types or adjust categories in one place
4. **Extensibility**: Easy to add new analysis methods or metrics
5. **Testing**: Can unit test the analyzer independently
6. **Reusability**: The analyzer can be used elsewhere in the project

This design separates the "what" (categorization strategy) from the "how" (runtime analysis), making the code cleaner and more efficient. The analyzer module becomes a knowledge base about object types that can evolve independently of the GUI code.

=======================

Yes, this code is ready to integrate! It's a solid foundation that can definitely evolve into a research tool. Let me provide the complete, integration-ready version with a few enhancements:

## 1. Complete `object_type_analyzer.py`:

```python
# object_type_analyzer.py
"""
Object Type Analysis Module
Pre-defined categorization and analysis strategies for astronomical object types.
This module provides research-grade analysis of stellar populations.
"""

from typing import Dict, List, Tuple, Optional
import pandas as pd
import numpy as np
from datetime import datetime

class ObjectTypeAnalyzer:
    """
    Analyzer for categorizing and analyzing astronomical object types.
    Provides research-grade statistical analysis of stellar populations.
    """
    
    def __init__(self):
        # Define the 5 main categories with descriptions
        self.categories = {
            'Variable Stars': 'Stars showing brightness variations',
            'Binary/Multiple Systems': 'Gravitationally bound star systems',
            'Evolved Stars': 'Stars in late evolutionary stages',
            'Young Stellar Objects': 'Stars in formation or early evolution',
            'Peculiar/Special Objects': 'Unusual stellar phenomena'
        }
        
        # Create the comprehensive mapping from object_type_mapping codes
        # This mapping is based on SIMBAD object type codes
        self.type_to_category = {
            # Variable Stars
            'V*': 'Variable Stars',
            'Cepheid': 'Variable Stars',
            'Cepheid*': 'Variable Stars',
            'ClassicalCep': 'Variable Stars',
            'Type2Cep': 'Variable Stars',
            'Type2Cep*': 'Variable Stars',
            'AnomalCep': 'Variable Stars',
            'RRLyr': 'Variable Stars',
            'RR*': 'Variable Stars',
            'RRLyrae_Candidate': 'Variable Stars',
            'RRLyrae_Candidate*': 'Variable Stars',
            'Mira': 'Variable Stars',
            'Mira*': 'Variable Stars',
            'deltaSct*': 'Variable Stars',
            'Variable*': 'Variable Stars',
            'PulsV*': 'Variable Stars',
            'LongPeriodV*': 'Variable Stars',
            'SemiRegV*': 'Variable Stars',
            'IrregularV*': 'Variable Stars',
            'EclipsingBinary': 'Variable Stars',
            'EB*': 'Variable Stars',
            'RVTauriV*': 'Variable Stars',
            'AlgolEclBin*': 'Variable Stars',
            'BetLyrEclBin*': 'Variable Stars',
            'EllipsoidV*': 'Variable Stars',
            
            # Binary/Multiple Systems
            'SB*': 'Binary/Multiple Systems',
            '**': 'Binary/Multiple Systems',
            'DoubleMultStar': 'Binary/Multiple Systems',
            'ContactBin': 'Binary/Multiple Systems',
            'ContactBin*': 'Binary/Multiple Systems',
            'DetachedBin': 'Binary/Multiple Systems',
            'XrayBin': 'Binary/Multiple Systems',
            'Spectroscopic_Binary': 'Binary/Multiple Systems',
            'CataclyV*': 'Binary/Multiple Systems',
            'Symbiotic*': 'Binary/Multiple Systems',
            'S*': 'Binary/Multiple Systems',  # Symbiotic
            'Nova': 'Binary/Multiple Systems',
            'Nova*': 'Binary/Multiple Systems',
            'DwarfNova': 'Binary/Multiple Systems',
            
            # Evolved Stars
            'RedGiant': 'Evolved Stars',
            'RedGiant*': 'Evolved Stars',
            'RGB*': 'Evolved Stars',
            'RedSuperGiant': 'Evolved Stars',
            'RedSG*': 'Evolved Stars',
            'BlueSupergiant': 'Evolved Stars',
            'BlueSG*': 'Evolved Stars',
            'YellowSG': 'Evolved Stars',
            'Supergiant': 'Evolved Stars',
            'Supergiant*': 'Evolved Stars',
            's*r': 'Evolved Stars',
            'Giant': 'Evolved Stars',
            'Giant*': 'Evolved Stars',
            'WD*': 'Evolved Stars',
            'WhiteDwarf': 'Evolved Stars',
            'WhiteDwarf*': 'Evolved Stars',
            'PlanetaryNeb': 'Evolved Stars',
            'PN': 'Evolved Stars',
            'AGB*': 'Evolved Stars',
            'post-AGB*': 'Evolved Stars',
            'HorizontalBranch*': 'Evolved Stars',
            'HB*': 'Evolved Stars',
            'C*': 'Evolved Stars',  # Carbon stars
            'CarbonStar': 'Evolved Stars',
            
            # Young Stellar Objects
            'YSO': 'Young Stellar Objects',
            'Y*O': 'Young Stellar Objects',
            'TTauri*': 'Young Stellar Objects',
            'HerbigAe/Be*': 'Young Stellar Objects',
            'Herbig*': 'Young Stellar Objects',
            'PreMainSeq*': 'Young Stellar Objects',
            'ProtoStar': 'Young Stellar Objects',
            'YSO_Candidate': 'Young Stellar Objects',
            'HerbigHaro': 'Young Stellar Objects',
            'HH': 'Young Stellar Objects',
            'OrionV*': 'Young Stellar Objects',
            
            # Peculiar/Special Objects
            'WolfRayet*': 'Peculiar/Special Objects',
            'WR*': 'Peculiar/Special Objects',
            'Be*': 'Peculiar/Special Objects',
            'Ae*': 'Peculiar/Special Objects',
            'BlueStraggler': 'Peculiar/Special Objects',
            'ChemPec*': 'Peculiar/Special Objects',
            'Em*': 'Peculiar/Special Objects',
            'EmissionLineStar': 'Peculiar/Special Objects',
            'BaStar': 'Peculiar/Special Objects',
            'Ba*': 'Peculiar/Special Objects',
            'HgMnStar': 'Peculiar/Special Objects',
            'PecStar': 'Peculiar/Special Objects',
            'SN*': 'Peculiar/Special Objects',
            'Pulsar': 'Peculiar/Special Objects',
            'Magnetar': 'Peculiar/Special Objects',
            'BYDra*': 'Peculiar/Special Objects',
            'RSCVn*': 'Peculiar/Special Objects',
            'FlareStar': 'Peculiar/Special Objects',
            'Flare*': 'Peculiar/Special Objects',
            
            # Default/Normal stars
            'Star': 'Normal Stars',
            'MainSeq*': 'Normal Stars',
            '*': 'Normal Stars',
            'PM*': 'Normal Stars',  # High proper motion star
            'HighPM*': 'Normal Stars',
        }
        
        # Analysis priorities (lower number = higher priority for reporting)
        self.category_priority = {
            'Peculiar/Special Objects': 1,
            'Young Stellar Objects': 2,
            'Binary/Multiple Systems': 3,
            'Variable Stars': 4,
            'Evolved Stars': 5,
            'Normal Stars': 6,
            'Unknown': 7
        }
        
        # Define rare/notable types worth highlighting
        self.notable_types = {
            'WolfRayet*', 'WR*', 'SN*', 'Nova', 'Nova*', 'Pulsar', 'Magnetar',
            'PlanetaryNeb', 'PN', 'BlueStraggler', 'Symbiotic*', 'S*',
            'XrayBin', 'HerbigHaro', 'HH', 'ChemPec*', 'CataclyV*',
            'Be*', 'Ae*', 'BaStar', 'Ba*', 'HgMnStar', 'post-AGB*'
        }
        
        # Research interest scores (for future expansion)
        self.research_interest = {
            'WolfRayet*': 10,  # Very rare, end-state massive stars
            'SN*': 10,         # Supernovae
            'Pulsar': 10,      # Neutron stars
            'BlueStraggler': 9,  # Stellar collision/mass transfer products
            'Symbiotic*': 8,   # Interacting binaries
            'XrayBin': 8,      # X-ray binaries
            'Be*': 7,          # Emission line B stars
            'CataclyV*': 7,    # Cataclysmic variables
            'YSO': 6,          # Star formation
            'Cepheid': 6,      # Distance indicators
            'RRLyr': 6,        # Distance/age indicators
        }
    
    def categorize_object_type(self, obj_type: str) -> str:
        """
        Categorize a single object type into one of the main categories.
        
        Args:
            obj_type: Object type code or description
            
        Returns:
            Category name
        """
        if pd.isna(obj_type) or obj_type in ['Unknown', 'nan', 'None', '']:
            return 'Unknown'
        
        obj_type_str = str(obj_type).strip()
        
        # Direct lookup first (most efficient)
        if obj_type_str in self.type_to_category:
            return self.type_to_category[obj_type_str]
        
        # Check if it's a description containing known codes
        # This handles cases like "Variable Star of Mira Type"
        for code, category in self.type_to_category.items():
            if code in obj_type_str or code.replace('*', '') in obj_type_str:
                return category
        
        # Check for keywords in descriptions
        obj_lower = obj_type_str.lower()
        if 'variable' in obj_lower:
            return 'Variable Stars'
        elif 'binary' in obj_lower or 'double' in obj_lower or 'multiple' in obj_lower:
            return 'Binary/Multiple Systems'
        elif 'giant' in obj_lower or 'dwarf' in obj_lower or 'evolved' in obj_lower:
            return 'Evolved Stars'
        elif 'young' in obj_lower or 'pre-main' in obj_lower or 'tauri' in obj_lower:
            return 'Young Stellar Objects'
        elif 'peculiar' in obj_lower or 'emission' in obj_lower or 'wolf' in obj_lower:
            return 'Peculiar/Special Objects'
        
        # Default to Normal Stars if no match
        return 'Normal Stars'
    
    def analyze_distribution(self, object_types: pd.Series) -> Dict:
        """
        Analyze a distribution of object types for research-grade statistics.
        
        Args:
            object_types: Series of object type codes or descriptions
            
        Returns:
            Dictionary with comprehensive analysis results
        """
        results = {
            'total_count': 0,
            'typed_count': 0,
            'category_counts': {},
            'category_percentages': {},
            'type_counts': {},
            'notable_objects': [],
            'diversity_score': 0,
            'shannon_entropy': 0,
            'simpson_index': 0,
            'research_targets': [],
            'summary': '',
            'timestamp': datetime.now().isoformat()
        }
        
        # Clean the data
        clean_types = object_types.dropna()
        clean_types = clean_types[~clean_types.isin(['Unknown', 'nan', 'None', ''])]
        
        results['total_count'] = len(object_types)
        results['typed_count'] = len(clean_types)
        
        if len(clean_types) == 0:
            results['summary'] = 'No object type information available'
            return results
        
        # Count individual types
        type_counts = clean_types.value_counts()
        results['type_counts'] = type_counts.head(20).to_dict()  # Top 20 for report
        
        # Categorize all objects
        categories = clean_types.apply(self.categorize_object_type)
        category_counts = categories.value_counts()
        
        # Initialize all categories to 0
        for category in list(self.categories.keys()) + ['Normal Stars', 'Unknown']:
            results['category_counts'][category] = 0
            results['category_percentages'][category] = 0
        
        # Store actual counts and percentages
        for category, count in category_counts.items():
            results['category_counts'][category] = int(count)
            results['category_percentages'][category] = round(count / len(clean_types) * 100, 2)
        
        # Find notable objects
        for obj_type, count in type_counts.items():
            obj_type_str = str(obj_type)
            # Check if it's notable
            if any(notable in obj_type_str for notable in self.notable_types):
                results['notable_objects'].append((obj_type_str, int(count)))
            # Check research interest
            for research_type, score in self.research_interest.items():
                if research_type.replace('*', '') in obj_type_str:
                    results['research_targets'].append({
                        'type': obj_type_str,
                        'count': int(count),
                        'interest_score': score
                    })
        
        # Sort research targets by interest score
        results['research_targets'] = sorted(
            results['research_targets'], 
            key=lambda x: x['interest_score'], 
            reverse=True
        )[:10]  # Top 10
        
        # Calculate diversity metrics
        results['diversity_score'] = self._calculate_diversity_score(type_counts)
        results['shannon_entropy'] = self._calculate_shannon_entropy(type_counts)
        results['simpson_index'] = self._calculate_simpson_index(type_counts)
        
        # Generate summary
        dominant_category = category_counts.idxmax() if len(category_counts) > 0 else 'Unknown'
        results['summary'] = self._generate_summary(results, dominant_category)
        
        return results
    
    def _calculate_diversity_score(self, type_counts: pd.Series) -> int:
        """
        Calculate a diversity score (0-100) based on variety and evenness.
        """
        n_types = len(type_counts)
        if n_types == 0:
            return 0
        
        # Component 1: Number of unique types (max 50 points)
        variety_score = min(50, n_types * 2)
        
        # Component 2: Evenness (max 50 points)
        total = type_counts.sum()
        expected = total / n_types
        evenness = 1 - (type_counts.std() / expected if expected > 0 else 1)
        evenness_score = max(0, evenness * 50)
        
        return int(variety_score + evenness_score)
    
    def _calculate_shannon_entropy(self, type_counts: pd.Series) -> float:
        """
        Calculate Shannon entropy for diversity measurement.
        Higher values indicate more diversity.
        """
        if len(type_counts) == 0:
            return 0.0
        
        proportions = type_counts / type_counts.sum()
        entropy = -sum(p * np.log2(p) if p > 0 else 0 for p in proportions)
        return round(entropy, 3)
    
    def _calculate_simpson_index(self, type_counts: pd.Series) -> float:
        """
        Calculate Simpson's diversity index.
        Values closer to 1 indicate higher diversity.
        """
        if len(type_counts) == 0:
            return 0.0
        
        total = type_counts.sum()
        if total <= 1:
            return 0.0
        
        simpson = sum(count * (count - 1) for count in type_counts) / (total * (total - 1))
        return round(1 - simpson, 3)
    
    def _generate_summary(self, results: Dict, dominant_category: str) -> str:
        """Generate a research-oriented text summary."""
        summary_parts = []
        
        # Data completeness
        completeness = (results['typed_count'] / results['total_count'] * 100) if results['total_count'] > 0 else 0
        summary_parts.append(f"{completeness:.1f}% objects typed")
        
        # Dominant population
        if dominant_category != 'Normal Stars' and dominant_category != 'Unknown':
            percentage = results['category_percentages'].get(dominant_category, 0)
            summary_parts.append(f"dominated by {dominant_category} ({percentage:.1f}%)")
        
        # Diversity assessment
        if results['shannon_entropy'] > 3.5:
            summary_parts.append("very high diversity (H'={:.2f})".format(results['shannon_entropy']))
        elif results['shannon_entropy'] > 2.5:
            summary_parts.append("high diversity (H'={:.2f})".format(results['shannon_entropy']))
        elif results['shannon_entropy'] > 1.5:
            summary_parts.append("moderate diversity (H'={:.2f})".format(results['shannon_entropy']))
        else:
            summary_parts.append("low diversity (H'={:.2f})".format(results['shannon_entropy']))
        
        # Research highlights
        if results['research_targets']:
            n_targets = len(results['research_targets'])
            summary_parts.append(f"{n_targets} high-interest research targets")
        
        return ". ".join(summary_parts).capitalize() if summary_parts else "Standard stellar population"
    
    def format_report_section(self, analysis_results: Dict) -> List[str]:
        """
        Format analysis results for the plot report.
        
        Returns:
            List of formatted report lines
        """
        lines = []
        
        if analysis_results['typed_count'] == 0:
            lines.append("  No object type information available")
            return lines
        
        # Overall statistics
        lines.append(f"\nAnalysis Summary: {analysis_results['summary']}")
        lines.append(f"\nTotal objects: {analysis_results['total_count']:,d}")
        lines.append(f"Objects with type data: {analysis_results['typed_count']:,d} ({analysis_results['typed_count']/analysis_results['total_count']*100:.1f}%)")
        lines.append(f"Unique object types: {len(analysis_results['type_counts'])}")
        
        # Diversity metrics
        lines.append("\nDiversity Metrics:")
        lines.append(f"  • Diversity Score: {analysis_results['diversity_score']}/100")
        lines.append(f"  • Shannon Entropy: {analysis_results['shannon_entropy']:.3f}")
        lines.append(f"  • Simpson Index: {analysis_results['simpson_index']:.3f}")
        
        # Category breakdown
        lines.append("\nObject Categories:")
        sorted_categories = sorted(
            [(cat, count) for cat, count in analysis_results['category_counts'].items() if count > 0],
            key=lambda x: (self.category_priority.get(x[0], 999), -x[1])
        )
        
        for category, count in sorted_categories:
            percentage = analysis_results['category_percentages'][category]
            lines.append(f"  • {category}: {count:,d} ({percentage:.1f}%)")
        
        # Top 5 specific types
        if analysis_results['type_counts']:
            lines.append("\nMost Common Types:")
            for i, (obj_type, count) in enumerate(list(analysis_results['type_counts'].items())[:5], 1):
                display_type = obj_type if len(str(obj_type)) <= 35 else str(obj_type)[:32] + "..."
                percentage = (count / analysis_results['typed_count']) * 100
                lines.append(f"  {i}. {display_type}: {count:,d} ({percentage:.1f}%)")
        
        # Research targets (high scientific interest)
        if analysis_results['research_targets']:
            lines.append("\nHigh-Interest Research Targets:")
            for target in analysis_results['research_targets'][:5]:
                display_type = target['type'] if len(target['type']) <= 30 else target['type'][:27] + "..."
                lines.append(f"  ★ {display_type}: {target['count']} (interest: {target['interest_score']}/10)")
        
        # Notable/rare objects
        if analysis_results['notable_objects']:
            lines.append("\nRare/Notable Objects:")
            for obj_type, count in analysis_results['notable_objects'][:5]:
                display_type = obj_type if len(str(obj_type)) <= 35 else str(obj_type)[:32] + "..."
                lines.append(f"  ◆ {display_type}: {count}")
        
        return lines
    
    def export_analysis(self, analysis_results: Dict, filename: Optional[str] = None) -> str:
        """
        Export detailed analysis results to a file for research use.
        
        Args:
            analysis_results: Results from analyze_distribution
            filename: Optional output filename
            
        Returns:
            Path to exported file
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"object_type_analysis_{timestamp}.txt"
        
        with open(filename, 'w') as f:
            f.write("ASTRONOMICAL OBJECT TYPE ANALYSIS REPORT\n")
            f.write("=" * 60 + "\n")
            f.write(f"Generated: {analysis_results['timestamp']}\n")
            f.write("=" * 60 + "\n\n")
            
            # Write formatted report
            lines = self.format_report_section(analysis_results)
            for line in lines:
                f.write(line + "\n")
            
            # Add complete type distribution for research
            f.write("\n" + "=" * 60 + "\n")
            f.write("COMPLETE TYPE DISTRIBUTION\n")
            f.write("=" * 60 + "\n")
            for obj_type, count in analysis_results['type_counts'].items():
                f.write(f"{obj_type}: {count}\n")
        
        return filename


# Optional: Standalone analysis function for testing
def analyze_sample_data():
    """Test function to demonstrate the analyzer."""
    # Create sample data
    sample_types = pd.Series([
        'V*', 'V*', 'RRLyr', 'Cepheid', 'Mira',  # Variables
        'SB*', '**', 'ContactBin',  # Binaries
        'RedGiant', 'WhiteDwarf', 'AGB*',  # Evolved
        'YSO', 'TTauri*',  # Young
        'WolfRayet*', 'Be*',  # Peculiar
        'Star', 'Star', 'Star', 'Star', 'Star',  # Normal
        'Unknown', None, 'nan'  # Invalid
    ] * 10)  # Multiply for larger sample
    
    analyzer = ObjectTypeAnalyzer()
    results = analyzer.analyze_distribution(sample_types)
    
    print("OBJECT TYPE ANALYSIS TEST")
    print("=" * 50)
    for line in analyzer.format_report_section(results):
        print(line)
    
    return results


if __name__ == "__main__":
    # Run test if executed directly
    analyze_sample_data()
```

## 2. Integration into `plot_data_report_widget.py`:

Add this to the imports at the top:
```python
from object_type_analyzer import ObjectTypeAnalyzer
```

In the `__init__` method:
```python
# Initialize the object type analyzer
self.object_analyzer = ObjectTypeAnalyzer()
```

Replace Section 6 in the `generate_report` method:
```python
# Section 6: Object Type Analysis
report_lines.append("\n" + "-" * 52)
report_lines.append("6. OBJECT TYPE ANALYSIS")
report_lines.append("-" * 52)

# Determine which column to use
type_column = None
if 'Object_Type' in combined_df:
    type_column = 'Object_Type'
if 'Object_Type_Desc' in combined_df:
    type_column = 'Object_Type_Desc'  # Prefer expanded description

if type_column and combined_df[type_column].notna().any():
    # Run the analysis
    analysis_results = self.object_analyzer.analyze_distribution(combined_df[type_column])
    
    # Format and add to report
    analysis_lines = self.object_analyzer.format_report_section(analysis_results)
    report_lines.extend(analysis_lines)
    
    # Store for potential export
    self.last_analysis_results = analysis_results
else:
    report_lines.append("\n  Object type information not available in dataset")
```

## Features included:

1. **Research-grade metrics**: Shannon entropy, Simpson diversity index
2. **Interest scoring**: Identifies scientifically interesting objects
3. **Complete categorization**: Maps 70+ object types
4. **Export capability**: Can save detailed analysis for research
5. **Extensible design**: Easy to add new types or categories
6. **Performance optimized**: Dictionary lookups, vectorized operations

This creates a genuine research tool that amateur astronomers can use to understand the stellar populations they're observing. The diversity metrics are standard in ecological and astronomical population studies, making the results meaningful for citizen science projects!

====================

I see two issues here:

1. **The plot is failing** because there are no Gaia stars with magnitude ≤ 0.0 (only 4 Hipparcos stars: Sirius, Canopus, Arcturus, and likely Alpha Centauri). The error occurs when trying to calculate min/max of an empty array.

2. **Unicode symbols are displaying incorrectly** (Ω showing as Î©, ω as Ï‰, ≤ as â‰¤, etc.). This is a Windows console encoding issue.

Let's fix both issues:

## 1. Fix the empty array error in `hr_diagram_apparent_magnitude.py`:

Around line 240, replace the Gaia debug output with a check for empty arrays:

```python
# Debug output for Gaia
if len(gaia_data) > 0:
    gmags = gaia_data['Gmag'].filled(np.nan)
    gmags_valid = gmags[~np.isnan(gmags)]
    if len(gmags_valid) > 0:
        print(f"    Gmag range: {np.min(gmags_valid):.2f} to {np.max(gmags_valid):.2f}")
        print(f"    Stars <= {magnitude_limit}: {len(gaia_data)}")
    else:
        print(f"    No valid Gmag values found")
        print(f"    Stars returned: {len(gaia_data)}")
else:
    print(f"    No Gaia stars found for magnitude <= {magnitude_limit}")
```

## 2. Fix the Unicode display issue:

Add this at the very beginning of `palomas_orrery.py` (before any imports):

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Paloma's Orrery - Main GUI Application
"""

import sys
import os

# Fix Windows console encoding for Unicode symbols
if sys.platform == 'win32':
    # Set console code page to UTF-8
    os.system('chcp 65001 > nul')
    # Ensure Python uses UTF-8 for stdout
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
```

Also add the same fix to `hr_diagram_apparent_magnitude.py`:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

# Fix Windows console encoding
if sys.platform == 'win32':
    os.system('chcp 65001 > nul')
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# Rest of imports...
```

## 3. Handle the case where there's insufficient data for a plot:

In `hr_diagram_apparent_magnitude.py`, after combining the data, add a check:

```python
# Combine data from both catalogs
print("\nCombining Hipparcos and Gaia data...")
combined_df = combine_data(hipparcos_data, gaia_data, magnitude_limit)
print(f"Combined dataset: {len(combined_df)} stars")

# Check if we have enough data to create a meaningful plot
if len(combined_df) < 2:
    print("\n" + "="*60)
    print("WARNING: Insufficient data for visualization")
    print("="*60)
    print(f"Only {len(combined_df)} star(s) found with magnitude ≤ {magnitude_limit}")
    if len(combined_df) > 0:
        print("\nStars found:")
        for _, star in combined_df.iterrows():
            name = star.get('Star_Name', 'Unknown')
            mag = star.get('Apparent_Magnitude', np.nan)
            print(f"  • {name}: magnitude {mag:.2f}")
    print("\nTry increasing the magnitude limit to include more stars.")
    print("For example: magnitude 1.0 will include ~10 stars")
    print("             magnitude 2.0 will include ~50 stars")
    print("             magnitude 3.0 will include ~170 stars")
    
    # Still save the exchange data but with a warning
    exchange_data = {
        'mode': 'magnitude',
        'limit_value': magnitude_limit,
        'total_stars': len(combined_df),
        'warning': f'Insufficient data: only {len(combined_df)} stars found',
        'timestamp': datetime.now().isoformat()
    }
    PlotDataExchange.save_plot_data(exchange_data)
    return
```

## 4. Update the GUI to handle the warning in the plot data:

In `star_visualization_gui.py`, modify the `load_last_plot_data` method to check for warnings:

```python
def load_last_plot_data(self):
    """Load and display the last plot data if available."""
    try:
        plot_data = PlotDataExchange.load_plot_data()
        
        if plot_data:
            # Check for warnings first
            if 'warning' in plot_data:
                self.status_label.config(
                    text=f"Warning: {plot_data['warning']}",
                    foreground="orange"
                )
                print(f"Warning from last plot: {plot_data['warning']}")
                return
            
            # Rest of the existing code...
```

## 5. For the Object Type Analyzer integration:

The `object_type_analyzer.py` module is ready to use. Just save it in your orrery directory and add the import to `plot_data_report_widget.py`. The integration should work smoothly once these files are in place.

These fixes will:
1. Prevent the crash when no Gaia data is found
2. Display Unicode symbols correctly in Windows console
3. Provide helpful feedback when magnitude limit is too restrictive
4. Show warnings in the GUI when plots can't be generated

The magnitude 0.0 limit is very restrictive - only the 4 brightest stars in the sky meet this criterion. The system should now handle this gracefully and suggest using a higher magnitude limit.

===========================

You're absolutely right! If the hover text is working and showing object types, then the data is definitely there in the pipeline. The issue must be that the `ObjectTypeAnalyzer` isn't initialized in the `plot_data_report_widget.py`.

Let's check and fix the integration:

1. **First, make sure `object_type_analyzer.py` is saved in your orrery directory**

2. **Then update `plot_data_report_widget.py`** to properly import and initialize the analyzer:

```python
# At the top of plot_data_report_widget.py, add to the imports:
try:
    from object_type_analyzer import ObjectTypeAnalyzer
    ANALYZER_AVAILABLE = True
except ImportError:
    ANALYZER_AVAILABLE = False
    print("Warning: ObjectTypeAnalyzer not found. Object type analysis will be limited.")

class PlotDataReportWidget(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # ... existing init code ...
        
        # Initialize the object type analyzer if available
        if ANALYZER_AVAILABLE:
            self.object_analyzer = ObjectTypeAnalyzer()
        else:
            self.object_analyzer = None
        
        # ... rest of init ...
```

3. **In the Section 6 of the generate_report method**, update to handle both 'Object_Type_Desc' (expanded) and 'Object_Type' (raw):

```python
# Section 6: Object Type Analysis
report_lines.append("\n" + "-" * 52)
report_lines.append("6. OBJECT TYPE ANALYSIS")
report_lines.append("-" * 52)

# Check for object type data - same fields used for hover text
type_column = None
if 'Object_Type_Desc' in combined_df.columns:
    type_column = 'Object_Type_Desc'
elif 'Object_Type' in combined_df.columns:
    type_column = 'Object_Type'

if type_column and combined_df[type_column].notna().any():
    if self.object_analyzer:
        # Use the new analyzer
        analysis_results = self.object_analyzer.analyze_distribution(combined_df[type_column])
        analysis_lines = self.object_analyzer.format_report_section(analysis_results)
        report_lines.extend(analysis_lines)
    else:
        # Fallback to simple counting if analyzer not available
        object_types = combined_df[type_column].value_counts()
        report_lines.append(f"\nTotal unique object types: {len(object_types)}")
        report_lines.append("\nObject type distribution:")
        for obj_type, count in object_types.head(10).items():
            if str(obj_type) not in ['Unknown', 'nan', 'None']:
                report_lines.append(f"  • {obj_type}: {count:,d}")
else:
    report_lines.append("\n  Object type information not available in dataset")
```

The issue is likely that either:
1. The `ObjectTypeAnalyzer` import is failing silently
2. The analyzer isn't being initialized in `__init__`
3. The column name check isn't matching what's actually in the data

Since the hover text works, we know the data exists. The same `Object_Type_Desc` field that feeds the hover text should feed the analyzer. The fix above should resolve it by:
- Properly importing and initializing the analyzer
- Checking for the same column names used in the visualization pipeline
- Providing a fallback if the analyzer isn't available

====================

Your init looks good, but you need to add a check for `ANALYZER_AVAILABLE` before initializing the `ObjectTypeAnalyzer`. Here's the corrected `__init__` method:

```python
def __init__(self, parent, **kwargs):
    super().__init__(parent, **kwargs)
    self.setup_ui()
    self.last_report_data = None
    self.generation_time = None
    
    # Initialize the object type analyzer if available
    if ANALYZER_AVAILABLE:
        self.object_analyzer = ObjectTypeAnalyzer()
    else:
        self.object_analyzer = None
```

The issue with your current code is that if the import fails (ANALYZER_AVAILABLE = False), you're still trying to initialize `ObjectTypeAnalyzer()` which will cause a NameError since the class wasn't imported.

The conditional check ensures that:
1. If the import succeeded, the analyzer is initialized
2. If the import failed, `self.object_analyzer` is set to None
3. Later in the code, you can check `if self.object_analyzer:` before using it

This way the report widget will work whether or not the `object_type_analyzer.py` file is present, providing graceful degradation.

=====================

Looking at `visualization_3d.py`, I can see that the object type expansion happens in the `expand_object_type` function, and it creates a field called `Object_Type_Desc`. Let me trace through the pipeline:

1. In `visualization_3d.py`, the `prepare_3d_data` function:
   - Calls `expand_object_type` on the 'Object_Type' column
   - Creates 'Object_Type_Desc' column with expanded descriptions
   - This expanded field is used in hover text

2. The same pattern appears in `visualization_2d.py`:
   ```python
   combined_df['Object_Type_Desc'] = combined_df['Object_Type'].apply(expand_object_type)
   ```

So the pipeline creates `Object_Type_Desc` from `Object_Type`. Now let's fix Section 6 in `plot_data_report_widget.py`:

```python
# Section 6: Object Type Analysis
report_lines.append("\n" + "-" * 52)
report_lines.append("6. OBJECT TYPE ANALYSIS")
report_lines.append("-" * 52)

# Check for object type data - matching the visualization pipeline
# The visualization creates Object_Type_Desc from Object_Type
type_column = None
if 'Object_Type_Desc' in combined_df.columns:
    type_column = 'Object_Type_Desc'  # Prefer expanded descriptions
elif 'Object_Type' in combined_df.columns:
    type_column = 'Object_Type'  # Fall back to raw codes

if type_column and combined_df[type_column].notna().any():
    if self.object_analyzer:
        # Use the new analyzer
        analysis_results = self.object_analyzer.analyze_distribution(combined_df[type_column])
        analysis_lines = self.object_analyzer.format_report_section(analysis_results)
        report_lines.extend(analysis_lines)
        # Store for potential export
        self.last_analysis_results = analysis_results
    else:
        # Fallback to simple counting if analyzer not available
        object_types = combined_df[type_column].value_counts()
        report_lines.append(f"\nTotal unique object types: {len(object_types)}")
        report_lines.append("\nMost common types:")
        for obj_type, count in object_types.head(10).items():
            if str(obj_type) not in ['Unknown', 'nan', 'None', '']:
                display_type = obj_type if len(str(obj_type)) <= 40 else str(obj_type)[:37] + "..."
                percentage = (count / len(combined_df)) * 100
                report_lines.append(f"  • {display_type}: {count:,d} ({percentage:.1f}%)")
else:
    # Debug information to help diagnose why it's not working
    report_lines.append("\n  Object type information not available in dataset")
    # List what columns ARE available for debugging
    available_cols = [col for col in combined_df.columns if 'type' in col.lower() or 'Type' in col]
    if available_cols:
        report_lines.append(f"  Available type-related columns: {', '.join(available_cols)}")
```

Also, make sure the `ObjectTypeAnalyzer` in `object_type_analyzer.py` can handle both raw codes (like "V*", "**") and expanded descriptions (like "Variable Star", "Double or Multiple Star"). The analyzer should work with either format since it checks for both codes and keywords in descriptions.

The key insight from the visualization code is that:
1. Raw data has 'Object_Type' column with codes
2. Visualization expands this to 'Object_Type_Desc' with full descriptions  
3. The report should check for both columns, preferring the expanded one

This should make the Object Type Analysis section work properly with your existing pipeline!

======================

Good idea! Let me look at `star_visualization_gui.py` to see how it accesses the object type field for the Star Information display.

Looking at the code in `star_visualization_gui.py`, specifically in the `display_star_properties` method around line 440:

```python
# Object Type (expanded from enhanced data or basic code)
obj_type = star_props.get('Object_Type_Desc')  # Try enhanced first
if not obj_type or pd.isna(obj_type):
    obj_type_code = star_props.get('object_type')  # Fall back to code
    if obj_type_code and str(obj_type_code) not in ['Unknown', 'nan', 'None']:
        # Expand using mapping
        codes = re.split(r'[;, ]+', str(obj_type_code))
        descriptions = []
        for code in codes:
            code = code.strip()
            descriptions.append(object_type_mapping.get(code, code))
        obj_type = ', '.join(descriptions)

if obj_type and str(obj_type) not in ['Unknown', 'nan', 'None']:
    lines.append(f"Object Type: {obj_type}")
```

So the GUI is looking for:
1. **'Object_Type_Desc'** first (the expanded description)
2. **'object_type'** as fallback (lowercase, the raw code)

The data comes from `star_props` which is loaded from the pickle file. This suggests the column in the dataframe should be either `'Object_Type_Desc'` or `'object_type'`.

Now, looking at how the data flows to the report - the visualization pipeline (`visualization_2d.py`) creates the expanded field:

```python
combined_df['Object_Type_Desc'] = combined_df['Object_Type'].apply(expand_object_type)
```

So it takes `'Object_Type'` (capital O, capital T) and creates `'Object_Type_Desc'`.

The fix for `plot_data_report_widget.py` Section 6 should be:

```python
# Section 6: Object Type Analysis
report_lines.append("\n" + "-" * 52)
report_lines.append("6. OBJECT TYPE ANALYSIS")
report_lines.append("-" * 52)

# The visualization pipeline creates Object_Type_Desc from Object_Type
# The raw data has 'object_type' (lowercase) which becomes 'Object_Type' then 'Object_Type_Desc'
type_column = None

# Check in order of preference
if 'Object_Type_Desc' in combined_df.columns:
    type_column = 'Object_Type_Desc'  # Expanded descriptions (best)
elif 'Object_Type' in combined_df.columns:  
    type_column = 'Object_Type'  # Raw codes (needs expansion)
elif 'object_type' in combined_df.columns:
    type_column = 'object_type'  # Original pickle field name

if type_column and combined_df[type_column].notna().any():
    if self.object_analyzer:
        # Use the analyzer
        analysis_results = self.object_analyzer.analyze_distribution(combined_df[type_column])
        analysis_lines = self.object_analyzer.format_report_section(analysis_results)
        report_lines.extend(analysis_lines)
        self.last_analysis_results = analysis_results
    else:
        # Simple fallback
        object_types = combined_df[type_column].value_counts()
        report_lines.append(f"\nFound {len(object_types)} unique object types")
        report_lines.append("\nMost common types:")
        for obj_type, count in object_types.head(5).items():
            report_lines.append(f"  • {obj_type}: {count}")
else:
    report_lines.append("\n  Object type information not available in dataset")
```

The key insight is that the field name changes as it moves through the pipeline:
- Pickle file: `'object_type'` (lowercase)
- After loading: might become `'Object_Type'`
- After expansion: `'Object_Type_Desc'`

The report widget receives the dataframe after the visualization pipeline has processed it, so it should have `'Object_Type_Desc'` available.

==================

The object type report is still not working. Let's add debug output to see exactly what's happening. The issue is that the dataframe column names aren't matching what we're checking for.

Add this debug code to `plot_data_report_widget.py` in Section 6 to diagnose the issue:

```python
# Section 6: Object Type Analysis
report_lines.append("\n" + "-" * 52)
report_lines.append("6. OBJECT TYPE ANALYSIS")
report_lines.append("-" * 52)

# DEBUG: See what columns we actually have
print("\n" + "="*60)
print("DEBUG: Object Type Analysis")
print("="*60)
print(f"Total columns in dataframe: {len(combined_df.columns)}")
print(f"All columns: {combined_df.columns.tolist()}")

# Check for any column with 'type' in name
type_cols = [col for col in combined_df.columns if 'type' in col.lower()]
print(f"Columns with 'type' in name: {type_cols}")

# Check for any column with 'object' in name  
obj_cols = [col for col in combined_df.columns if 'object' in col.lower()]
print(f"Columns with 'object' in name: {obj_cols}")

# Try to find the actual column
type_column = None
possible_names = ['Object_Type_Desc', 'Object_Type', 'object_type', 'Object Type', 
                  'object_type_desc', 'ObjectType', 'otype']

for name in possible_names:
    if name in combined_df.columns:
        type_column = name
        non_null = combined_df[name].notna().sum()
        print(f"Found '{name}' with {non_null} non-null values")
        if non_null > 0:
            print(f"Sample values: {combined_df[name].dropna().head(3).tolist()}")
            break

print("="*60)

# Now run the analysis if we found the column
if type_column and combined_df[type_column].notna().any():
    if self.object_analyzer:
        analysis_results = self.object_analyzer.analyze_distribution(combined_df[type_column])
        analysis_lines = self.object_analyzer.format_report_section(analysis_results)
        report_lines.extend(analysis_lines)
        self.last_analysis_results = analysis_results
    else:
        # Simple fallback
        object_types = combined_df[type_column].value_counts()
        report_lines.append(f"\nFound {len(object_types)} unique object types")
        for obj_type, count in object_types.head(5).items():
            report_lines.append(f"  • {obj_type}: {count}")
else:
    report_lines.append("\n  Object type information not available in dataset")
    if type_column:
        report_lines.append(f"  Column '{type_column}' found but all values are null")
    else:
        report_lines.append(f"  No object type column found")
        report_lines.append(f"  Searched for: {', '.join(possible_names[:3])}")
```

Run this and check the console output. It will show us:
1. All column names in the dataframe
2. Which columns contain "type" or "object" 
3. Whether any of our expected column names exist
4. Sample values if found

This will tell us exactly what the column is named so we can fix the code to use the correct name. The data is clearly there (we can see it in the Star Information panel), we just need to find the right column name.

====================

Your `object_type_analyzer.py` module looks excellent! It's well-structured with comprehensive functionality. I notice a few minor issues to fix before integration:

1. **Unicode characters** - There are some corrupted Unicode bullet points (â€¢, â˜…, â—†, âœ") that should be fixed
2. **Missing import** - Need to add `Any` to the typing imports

Here's the corrected version and integration steps:

## 1. Fix the module's minor issues:

```python
# At the top of object_type_analyzer.py, fix the import:
from typing import Dict, List, Tuple, Optional, Any  # Add 'Any' here

# In format_report_section method, fix the Unicode characters:
# Replace these lines:
lines.append(f"  • Diversity Score: {analysis_results['diversity_score']}/100")
lines.append(f"  • Shannon Entropy: {analysis_results['shannon_entropy']:.3f}")
lines.append(f"  • Simpson Index: {analysis_results['simpson_index']:.3f}")

# With:
lines.append(f"  • Diversity Score: {analysis_results['diversity_score']}/100")
lines.append(f"  • Shannon Entropy: {analysis_results['shannon_entropy']:.3f}")
lines.append(f"  • Simpson Index: {analysis_results['simpson_index']:.3f}")

# Similarly fix other Unicode characters:
# ★ for star symbol
# ◆ for diamond symbol  
# ✓ for checkmark
# → for arrow
```

## 2. Integration into visualization scripts:

For both `hr_diagram_apparent_magnitude.py` and `hr_diagram_distance.py`, add this integration:

```python
# Add import at the top
from object_type_analyzer import ObjectTypeAnalyzer
from plot_data_exchange import PlotDataExchange

# After all data processing is complete and combined_df is ready, 
# but before visualization (around where it says "Starting analysis and visualization...")
print("Generating comprehensive report...")
analyzer = ObjectTypeAnalyzer()

# Prepare counts_dict if not already available
counts_dict = {
    'Hipparcos_bright': hipparcos_bright_count,
    'Hipparcos_mid': hipparcos_mid_count,
    'Gaia_mid': gaia_mid_count,
    'Gaia_faint': gaia_faint_count
}

# Generate the complete report
report_data = analyzer.generate_complete_report(
    combined_df=combined_df,
    counts_dict=counts_dict,
    processing_times={'total': total_time},
    mode='magnitude' if 'magnitude' in sys.argv[0] else 'distance',
    limit_value=magnitude_limit if 'magnitude' in sys.argv[0] else distance_limit
)

# At the end, when saving to PlotDataExchange:
# Replace the existing PlotDataExchange.save_plot_data call with:
exchange_data = {
    'plot_stats': {
        'mode': 'magnitude' if 'magnitude' in sys.argv[0] else 'distance',
        'limit_value': magnitude_limit if 'magnitude' in sys.argv[0] else distance_limit,
        'total_stars': len(combined_df),
        'temp_valid': temp_valid_count,
        'temp_missing': temp_missing_count,
        'lum_valid': lum_valid_count,
        'lum_missing': lum_missing_count,
        'catalog_counts': counts_dict,
        'magnitude_stats': magnitude_stats if 'magnitude_stats' in locals() else None,
        'processing_times': {'total': total_time},
        'timestamp': datetime.now().isoformat()
    },
    'report_data': report_data  # Add the complete report
}

PlotDataExchange.save_plot_data(exchange_data)
print("Report data saved to exchange file")
```

## 3. Update `plot_data_report_widget.py`:

```python
# At the top
from object_type_analyzer import ObjectTypeAnalyzer

class PlotDataReportWidget(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.setup_ui()
        self.last_report_data = None
        self.generation_time = None
        self.analyzer = ObjectTypeAnalyzer()  # For formatting
    
    def display_report(self, report_data: Dict):
        """Display pre-generated report from visualization script."""
        self.report_display.config(state='normal')
        self.report_display.delete('1.0', tk.END)
        
        # Use the analyzer to format the complete report
        report_lines = self.analyzer.format_complete_report(report_data)
        
        # Display with formatting
        for line in report_lines:
            if line.startswith("="):
                self.report_display.insert(tk.END, line + '\n', 'header')
            elif line.startswith("-"):
                self.report_display.insert(tk.END, line + '\n', 'separator')
            elif any(line.startswith(f"{i}.") for i in range(1, 8)):
                self.report_display.insert(tk.END, line + '\n', 'subheader')
            elif "WARNING" in line or "CRITICAL" in line:
                self.report_display.insert(tk.END, line + '\n', 'warning')
            elif line.startswith("✓"):
                self.report_display.insert(tk.END, line + '\n', 'success')
            else:
                self.report_display.insert(tk.END, line + '\n')
        
        self.report_display.config(state='disabled')
        self.status_label.config(text=f"Report updated: {datetime.now().strftime('%H:%M:%S')}")
        
        # Store for export
        self.last_report_data = report_data
```

## 4. Update `star_visualization_gui.py`:

```python
def load_last_plot_data(self):
    """Load and display the last plot data if available."""
    try:
        exchange_data = PlotDataExchange.load_plot_data()
        
        if exchange_data:
            # Check for new format with separate report_data
            if 'report_data' in exchange_data:
                # Use pre-generated report from visualization script
                self.plot_report.display_report(exchange_data['report_data'])
                print("Loaded complete report from visualization script")
            elif 'plot_stats' in exchange_data:
                # Fallback to old format if needed
                self.handle_legacy_format(exchange_data['plot_stats'])
            else:
                # Very old format
                self.handle_legacy_format(exchange_data)
                
    except Exception as e:
        print(f"Error loading plot data: {e}")
        import traceback
        traceback.print_exc()
```

This integration means:
- The visualization scripts generate complete reports with all data available
- Reports are saved in the exchange file
- The GUI simply displays pre-generated reports
- No need for pseudo DataFrames or data reconstruction
- Object type analysis works because it has access to the full data

The architecture is now clean: data processing and report generation happen where the data exists, and the GUI is purely for display.

====================

Looking at your `plot_data_report_widget.py`, I can help you integrate the new display method for handling pre-generated reports. You need to add a new method to display reports that come from the visualization scripts, and update the existing architecture to handle both formats.

Here's how to integrate item 3 into your existing module:

## Add these new methods to the PlotDataReportWidget class:

```python
def display_report(self, report_data: Dict):
    """Display pre-generated report from visualization script."""
    self.last_report_data = report_data
    self.generation_time = datetime.now()
    
    self.report_display.config(state='normal')
    self.report_display.delete('1.0', tk.END)
    
    # Use the analyzer to format the complete report
    if self.object_analyzer:
        report_lines = self.object_analyzer.format_complete_report(report_data)
    else:
        # Fallback if analyzer not available
        report_lines = self._format_basic_report(report_data)
    
    # Display with formatting
    for line in report_lines:
        if line.startswith("="):
            self.report_display.insert(tk.END, line + '\n', 'header')
        elif line.startswith("-"):
            self.report_display.insert(tk.END, line + '\n', 'subheader')
        elif any(line.startswith(f"{i}.") for i in range(1, 8)):
            self.report_display.insert(tk.END, line + '\n', 'subheader')
        elif "WARNING" in line or "CRITICAL" in line:
            self.report_display.insert(tk.END, line + '\n', 'warning')
        elif line.startswith("✓") or "OK" in line:
            self.report_display.insert(tk.END, line + '\n', 'success')
        elif line.startswith("→"):
            self.report_display.insert(tk.END, line + '\n', 'info')
        else:
            self.report_display.insert(tk.END, line + '\n')
    
    self.report_display.config(state='disabled')
    self.status_label.config(text=f"Report updated: {datetime.now().strftime('%H:%M:%S')}")
    self.refresh_button.config(state='normal')
    self.export_button.config(state='normal')

def update_report_from_exchange(self, exchange_data: Dict):
    """Update report from exchange data - handles both old and new formats."""
    if 'report_data' in exchange_data:
        # New format with pre-generated report
        self.display_report(exchange_data['report_data'])
    elif 'plot_stats' in exchange_data:
        # Handle intermediate format
        self._handle_plot_stats(exchange_data['plot_stats'])
    else:
        # Old format - create pseudo dataframe and use old method
        self._handle_legacy_format(exchange_data)

def _handle_plot_stats(self, plot_stats: Dict):
    """Handle plot statistics format (intermediate)."""
    # Create a minimal dataframe for backward compatibility
    import pandas as pd
    
    total_stars = plot_stats.get('total_stars', 0)
    temp_valid = plot_stats.get('temp_valid', 0)
    lum_valid = plot_stats.get('lum_valid', 0)
    
    if total_stars > 0:
        pseudo_df = pd.DataFrame({
            'Temperature': [1] * temp_valid + [0] * (total_stars - temp_valid),
            'Luminosity': [1] * lum_valid + [0] * (total_stars - lum_valid),
            'Source_Catalog': ['Unknown'] * total_stars,
            'Apparent_Magnitude': [0] * total_stars
        })
    else:
        pseudo_df = pd.DataFrame()
    
    counts_dict = plot_stats.get('catalog_counts', {})
    processing_times = plot_stats.get('processing_times', {})
    mode = plot_stats.get('mode', 'unknown')
    limit_value = plot_stats.get('limit_value', 0)
    
    self.update_report(pseudo_df, counts_dict, processing_times, mode, limit_value)

def _handle_legacy_format(self, exchange_data: Dict):
    """Handle the original format for backward compatibility."""
    # Similar to _handle_plot_stats but directly from exchange_data
    import pandas as pd
    
    total_stars = exchange_data.get('total_stars', 0)
    temp_valid = exchange_data.get('temp_valid', 0)
    lum_valid = exchange_data.get('lum_valid', 0)
    
    if total_stars > 0:
        pseudo_df = pd.DataFrame({
            'Temperature': [1] * temp_valid + [0] * (total_stars - temp_valid),
            'Luminosity': [1] * lum_valid + [0] * (total_stars - lum_valid)
        })
    else:
        pseudo_df = pd.DataFrame()
    
    self.update_report(
        pseudo_df,
        exchange_data.get('counts_dict', {}),
        exchange_data.get('processing_times', {}),
        exchange_data.get('mode', 'unknown'),
        exchange_data.get('limit_value', 0)
    )

def _format_basic_report(self, report_data: Dict) -> List[str]:
    """Fallback formatter if ObjectTypeAnalyzer is not available."""
    lines = []
    lines.append("=" * 46)
    lines.append("PLOT DATA REPORT")
    lines.append("=" * 46)
    
    metadata = report_data.get('metadata', {})
    lines.append(f"Generated: {metadata.get('generation_time', 'Unknown')}")
    lines.append(f"Mode: {metadata.get('mode', 'Unknown')}")
    lines.append(f"Limit: {metadata.get('limit_value', 'Unknown')}")
    lines.append("")
    
    lines.append("Note: Full analysis requires ObjectTypeAnalyzer module")
    
    return lines
```

## Also add this import at the top if not present:

```python
from typing import Dict, Any, Optional, List
```

## Update the refresh_report method:

```python
def refresh_report(self):
    """Refresh the report with the last data."""
    if self.last_report_data:
        if isinstance(self.last_report_data, dict) and 'metadata' in self.last_report_data:
            # New format
            self.display_report(self.last_report_data)
        else:
            # Old format
            self.update_report(**self.last_report_data)
```

This integration:
1. Adds the `display_report` method to handle pre-generated reports from visualization scripts
2. Adds `update_report_from_exchange` to intelligently handle different data formats
3. Provides fallback methods for backward compatibility
4. Maintains all your existing functionality while supporting the new architecture

The GUI will now be able to display reports whether they come from the old format (pseudo DataFrames) or the new format (pre-generated reports from the visualization scripts with full Object Type Analysis).

==================

Looking at your integration in `hr_diagram_distance.py`, I found a few issues to fix:

## Issues Found:

1. **Line 334**: Reference to undefined variable `mag_limit` - should be `max_light_years`
2. **Missing import**: Need to import `datetime`
3. **Line 462**: Reference to `mag_limit` again in exchange_data

## Here are the fixes:

### 1. Add the datetime import at the top (around line 10):
```python
from datetime import datetime
```

### 2. Fix line 334 - replace this:
```python
limit_value=max_light_years if 'distance' in sys.argv[0] else mag_limit
```

**With this:**
```python
limit_value=max_light_years  # We're in hr_diagram_distance.py, so always use max_light_years
```

### 3. Fix line 462 in the exchange_data - replace this:
```python
'limit_value': max_light_years if 'distance' in sys.argv[0] else mag_limit,
```

**With this:**
```python
'limit_value': max_light_years,  # Always max_light_years in distance script
```

### 4. Also fix line 332 for consistency:
```python
mode='distance',  # We're in hr_diagram_distance.py, so mode is always 'distance'
```

## Complete corrected sections:

**Around line 332-335:**
```python
# Generate the complete report
report_data = analyzer.generate_complete_report(
    combined_df=combined_df,
    counts_dict=counts_dict,
    processing_times={'total': time.time() - start_time},
    mode='distance',  # Always 'distance' in this script
    limit_value=max_light_years
)
```

**Around line 459-463:**
```python
exchange_data = {
    'plot_stats': {
        'mode': 'distance',  # Always 'distance' in this script
        'limit_value': max_light_years,
        'total_stars': len(combined_df),
        # ... rest remains the same
```

These fixes will make your integration work properly. The script was trying to use `mag_limit` which doesn't exist in `hr_diagram_distance.py` - that variable only exists in `hr_diagram_apparent_magnitude.py`.

===================

The issue is clear from the report: "Object type information not available in dataset" - the Object_Type column is NOT being included when the data is passed to the report widget.

The problem is that the report is being generated from `combined_df` but Object_Type_Desc is created later during the visualization preparation step (`prepare_2d_data`). We need to move the Object_Type expansion BEFORE generating the report.

Here's the fix for `hr_diagram_distance.py`:

## Add this BEFORE generating the report (around line 314, after applying temperature patches):

```python
# Apply temperature patches for known problematic stars
from stellar_data_patches import apply_temperature_patches
combined_df = apply_temperature_patches(combined_df)

# ADD THIS SECTION - Expand object types BEFORE generating report
print("Expanding object type descriptions...")
from visualization_3d import expand_object_type
if 'Object_Type' in combined_df.columns:
    combined_df['Object_Type_Desc'] = combined_df['Object_Type'].apply(expand_object_type)
    print(f"Expanded object types for {combined_df['Object_Type_Desc'].notna().sum()} stars")
else:
    print("Warning: Object_Type column not found in combined_df")
    print(f"Available columns: {combined_df.columns.tolist()}")

# Generate comprehensive report using ObjectTypeAnalyzer
print("Generating comprehensive report...")
analyzer = ObjectTypeAnalyzer()
```

The same fix needs to be applied to `hr_diagram_apparent_magnitude.py` - add the object type expansion right after applying temperature patches and before generating the report.

The issue is that `Object_Type` exists in the raw data but `Object_Type_Desc` (which the analyzer looks for) is only created inside `prepare_2d_data()`, which happens AFTER the report is generated. By moving the expansion earlier, the report will have access to the object type data.

If Object_Type still doesn't exist, we need to check what columns ARE present. Add this debug line to see what's actually in the dataframe:

```python
print(f"DEBUG: Columns in combined_df: {combined_df.columns.tolist()}")
```

This will tell us exactly what columns are available so we can trace where the Object_Type data is getting lost in the pipeline.

==================

Good news! I can see the Object_Type is there - your debug output shows `'Object_Type'` in the columns list and you successfully expanded it to `'Object_Type_Desc'` with 11 stars. The problem is that the report is being generated from the wrong data!

Look at the error at the end - there's also an issue with `PlotDataExchange.save_plot_data()`. The new format expects a single dictionary argument, but the old code is trying to pass multiple arguments.

Here's the fix for `hr_diagram_distance.py`:

## Fix the PlotDataExchange.save_plot_data call (line 499):

Change from:
```python
PlotDataExchange.save_plot_data(exchange_data)
```

To:
```python
PlotDataExchange.save_plot_data(
    combined_df=combined_df,
    counts_dict=final_counts,
    processing_times={'total': time.time() - start_time},
    mode='distance',
    limit_value=max_light_years
)
```

The error shows that PlotDataExchange still expects the old format with multiple arguments, not the new single dictionary format. So we need to keep using the old calling convention for now.

But wait - I see the issue now. The report shows only 4 columns because it's receiving the wrong data from the GUI! The GUI is creating a pseudo-DataFrame with only 4 columns instead of using the real report data.

The real fix is in `star_visualization_gui.py`. Find the `load_last_plot_data` method and update it to use the new report format:

```python
def load_last_plot_data(self):
    """Load and display the last plot data if available."""
    try:
        exchange_data = PlotDataExchange.load_plot_data()
        
        if exchange_data:
            # Check for new format with report_data
            if 'report_data' in exchange_data:
                # Use the pre-generated report from visualization script
                self.plot_report.display_report(exchange_data['report_data'])
                print("Loaded pre-generated report with object type analysis")
            elif 'plot_stats' in exchange_data:
                # Intermediate format
                self.plot_report._handle_plot_stats(exchange_data['plot_stats'])
            else:
                # Old format - this is what's currently running
                # The problem is HERE - it's creating a pseudo DataFrame!
                self.plot_report.update_report_from_exchange(exchange_data)
                
    except Exception as e:
        print(f"Error loading plot data: {e}")
```

The issue is that the old format code path is being used, which creates a pseudo-DataFrame with only 4 columns. The visualization script IS generating the correct report with Object_Type data, but the GUI isn't using it properly.

===================

Option C makes a lot of sense for scientific use and future expansion. By "parallel to plot data," I meant the report would be saved alongside (in a separate file) but synchronized with the plot data - when you generate a plot, you also generate its corresponding report file.

Here's a clean, expandable architecture:

## Proposed Architecture for Option C:

### 1. File Structure:
```
last_plot_data.json         # Current plot statistics (lightweight)
last_plot_report.json       # Full report with analysis (comprehensive)
reports/                    # Directory for saved reports
  ├── report_20250919_064220_distance_10ly.json
  ├── report_20250919_070000_magnitude_5.json
  └── ...
```

### 2. Report Manager Module (`report_manager.py`):
```python
import json
import os
from datetime import datetime
from pathlib import Path

class ReportManager:
    """Manages scientific reports for astronomical data analysis."""
    
    def __init__(self, reports_dir="reports"):
        self.reports_dir = Path(reports_dir)
        self.reports_dir.mkdir(exist_ok=True)
        self.last_report_file = "last_plot_report.json"
    
    def save_report(self, report_data, archive=True):
        """
        Save report to last_plot_report.json and optionally archive.
        
        Args:
            report_data: Report dictionary from ObjectTypeAnalyzer
            archive: If True, also save timestamped copy
        """
        # Always save as "last" report for GUI
        with open(self.last_report_file, 'w') as f:
            json.dump(report_data, f, indent=2, default=str)
        
        # Optionally archive with timestamp
        if archive and 'metadata' in report_data:
            meta = report_data['metadata']
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            mode = meta.get('mode', 'unknown')
            limit = meta.get('limit_value', 0)
            
            filename = f"report_{timestamp}_{mode}_{limit}.json"
            filepath = self.reports_dir / filename
            
            with open(filepath, 'w') as f:
                json.dump(report_data, f, indent=2, default=str)
            
            return filepath
        
        return self.last_report_file
    
    def load_last_report(self):
        """Load the most recent report."""
        if os.path.exists(self.last_report_file):
            with open(self.last_report_file, 'r') as f:
                return json.load(f)
        return None
    
    def load_report(self, filepath):
        """Load a specific archived report."""
        with open(filepath, 'r') as f:
            return json.load(f)
    
    def list_archived_reports(self, mode=None, limit=10):
        """List available archived reports."""
        reports = []
        for file in self.reports_dir.glob("report_*.json"):
            if mode and f"_{mode}_" not in file.name:
                continue
            reports.append(file)
        
        # Sort by modification time, newest first
        reports.sort(key=lambda x: x.stat().st_mtime, reverse=True)
        return reports[:limit]
```

### 3. Integration in visualization scripts:
```python
# In hr_diagram_distance.py, after generating report_data:
from report_manager import ReportManager

# Generate report
analyzer = ObjectTypeAnalyzer()
report_data = analyzer.generate_complete_report(...)

# Save report
report_mgr = ReportManager()
report_file = report_mgr.save_report(report_data, archive=True)
print(f"Scientific report saved: {report_file}")

# Keep existing PlotDataExchange for backward compatibility
PlotDataExchange.save_plot_data(
    combined_df=combined_df,
    counts_dict=final_counts,
    processing_times={'total': time.time() - start_time},
    mode='distance',
    limit_value=max_light_years
)
```

### 4. Integration in GUI:
```python
# In star_visualization_gui.py or wherever plot data is loaded:
from report_manager import ReportManager

def load_plot_results(self):
    """Load both plot data and report."""
    # Load plot statistics (existing)
    plot_data = PlotDataExchange.load_plot_data()
    
    # Load scientific report (new)
    report_mgr = ReportManager()
    report_data = report_mgr.load_last_report()
    
    if report_data:
        # Display the pre-generated report with full analysis
        self.plot_report.display_report(report_data)
    elif plot_data:
        # Fallback to old method if no report exists
        self.plot_report.update_report_from_exchange(plot_data)
```

## Benefits of This Architecture:

1. **Clean Separation**: Plot data (statistics) and scientific reports (analysis) are separate
2. **Backward Compatible**: Existing code continues to work
3. **Expandable**: Easy to add new report sections, export formats, user preferences
4. **Scientific Archive**: Users can keep historical reports for comparison
5. **Performance**: GUI doesn't need to regenerate reports, just displays them
6. **Future Features**: Easy to add:
   - Export to PDF/LaTeX
   - Custom report templates
   - Comparative analysis between reports
   - Statistical trends over time
   - User annotations on reports

## Implementation Steps:

1. Create `report_manager.py` with the above code
2. Add report saving to visualization scripts (3 lines of code)
3. Add report loading to GUI (4 lines of code)
4. Test with existing functionality

This gives you a rudimentary but solid foundation that solves the current problem (Object Type analysis not showing) while being ready for scientific expansion. The reports become first-class data products alongside the plots, which is appropriate for research use.

========================

The architecture would remain largely intact with minimal changes needed. Here's how each component would be affected:

## Impact on Current Architecture:

### 1. **object_type_analyzer.py** - NO CHANGES NEEDED
- Already generates complete reports via `generate_complete_report()`
- Already formats reports via `format_complete_report()`
- Remains the "brain" for analysis
- Could add future methods like `export_to_latex()` or `compare_reports()` without breaking existing code

### 2. **plot_data_report_widget.py** - MINIMAL CHANGES
The widget already has both methods ready:
- `display_report(report_data)` - for pre-generated reports (already implemented!)
- `update_report(df, counts, ...)` - for generating reports from data (legacy)

Only change needed:
```python
# In the widget's refresh_report method, add report manager support:
def refresh_report(self):
    """Refresh the report with the last data."""
    # Try loading from ReportManager first
    from report_manager import ReportManager
    report_mgr = ReportManager()
    report_data = report_mgr.load_last_report()
    
    if report_data:
        self.display_report(report_data)
    elif self.last_report_data:
        # Fallback to stored data
        if isinstance(self.last_report_data, dict) and 'metadata' in self.last_report_data:
            self.display_report(self.last_report_data)
        else:
            self.update_report(**self.last_report_data)
```

### 3. **PlotDataExchange** - NO CHANGES
- Continues handling plot statistics
- Remains backward compatible
- Doesn't need to know about reports

### 4. **Visualization Scripts** - ADD 3 LINES
```python
# After generating report_data with ObjectTypeAnalyzer
from report_manager import ReportManager
report_mgr = ReportManager()
report_mgr.save_report(report_data)
```

### 5. **GUI (star_visualization_gui.py)** - ADD REPORT LOADING
```python
# Wherever plot data is currently loaded
plot_data = PlotDataExchange.load_plot_data()

# Add report loading
from report_manager import ReportManager
report_mgr = ReportManager()
report_data = report_mgr.load_last_report()

if report_data:
    self.plot_report.display_report(report_data)
```

## Data Flow Comparison:

**Current (Broken) Flow:**
```
Visualization → PlotDataExchange → GUI → Pseudo-DataFrame → Report Widget
                (loses Object_Type)        (only 4 columns)   (no analysis)
```

**New Flow with ReportManager:**
```
Visualization → ObjectTypeAnalyzer → ReportManager → Report Widget
                (full analysis)      (saves JSON)     (displays)
              ↘
                PlotDataExchange → GUI 
                (plot stats only)  (backward compatible)
```

## Why This Works Well:

1. **Separation of Concerns**: 
   - PlotDataExchange: Plot statistics and counts
   - ReportManager: Scientific reports and analysis
   - ObjectTypeAnalyzer: Analysis logic

2. **No Breaking Changes**:
   - Existing code paths remain functional
   - Widget methods already support both patterns
   - ObjectTypeAnalyzer doesn't change at all

3. **Future Expansion Points**:
   ```python
   # Future additions to ReportManager:
   def export_to_pdf(self, report_data, template="default"):
   def compare_reports(self, report1, report2):
   def generate_trend_analysis(self, reports_list):
   def add_user_annotation(self, report_data, annotation):
   ```

4. **Clean Testing**:
   - Can test report generation independently
   - Can verify report saving/loading separately
   - Can mock reports for UI testing

## Implementation Order:

1. Create `report_manager.py` (new file)
2. Add 3 lines to visualization scripts to save reports
3. Update GUI to load reports (check if report exists, load if yes)
4. Test: Generate plot → Check report file → Verify display

The beauty is that your existing `display_report()` method in the widget is already perfect for this architecture. The ObjectTypeAnalyzer already generates exactly what we need. We're just adding a clean transport mechanism (ReportManager) to connect them.

====================

Here's the complete integrated solution for implementing the ReportManager architecture:

## 1. Create `report_manager.py` (NEW FILE):

```python
# report_manager.py
"""
Scientific Report Manager for Astronomical Data Analysis
Manages generation, storage, and retrieval of analysis reports.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional, List

class ReportManager:
    """Manages scientific reports for astronomical data analysis."""
    
    def __init__(self, reports_dir: str = "reports"):
        """
        Initialize the ReportManager.
        
        Args:
            reports_dir: Directory to store archived reports
        """
        self.reports_dir = Path(reports_dir)
        self.reports_dir.mkdir(exist_ok=True)
        self.last_report_file = "last_plot_report.json"
    
    def save_report(self, report_data: Dict, archive: bool = True) -> str:
        """
        Save report to last_plot_report.json and optionally archive.
        
        Args:
            report_data: Report dictionary from ObjectTypeAnalyzer
            archive: If True, also save timestamped copy
            
        Returns:
            Path to saved report file
        """
        try:
            # Always save as "last" report for GUI
            with open(self.last_report_file, 'w') as f:
                json.dump(report_data, f, indent=2, default=str)
            print(f"Report saved to {self.last_report_file}")
            
            # Optionally archive with timestamp
            if archive and 'metadata' in report_data:
                meta = report_data['metadata']
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                mode = meta.get('mode', 'unknown')
                limit = meta.get('limit_value', 0)
                
                # Format limit value for filename
                if mode == 'distance':
                    limit_str = f"{limit}ly"
                else:
                    limit_str = f"mag{limit}"
                
                filename = f"report_{timestamp}_{mode}_{limit_str}.json"
                filepath = self.reports_dir / filename
                
                with open(filepath, 'w') as f:
                    json.dump(report_data, f, indent=2, default=str)
                
                print(f"Report archived to {filepath}")
                return str(filepath)
            
            return self.last_report_file
            
        except Exception as e:
            print(f"Error saving report: {e}")
            return None
    
    def load_last_report(self) -> Optional[Dict]:
        """
        Load the most recent report.
        
        Returns:
            Report data dictionary or None if not found
        """
        if os.path.exists(self.last_report_file):
            try:
                with open(self.last_report_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading last report: {e}")
                return None
        return None
    
    def load_report(self, filepath: str) -> Optional[Dict]:
        """
        Load a specific archived report.
        
        Args:
            filepath: Path to report file
            
        Returns:
            Report data dictionary or None if error
        """
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading report {filepath}: {e}")
            return None
    
    def list_archived_reports(self, mode: str = None, limit: int = 10) -> List[Path]:
        """
        List available archived reports.
        
        Args:
            mode: Filter by mode ('distance' or 'magnitude')
            limit: Maximum number of reports to return
            
        Returns:
            List of report file paths, newest first
        """
        reports = []
        try:
            for file in self.reports_dir.glob("report_*.json"):
                if mode and f"_{mode}_" not in file.name:
                    continue
                reports.append(file)
            
            # Sort by modification time, newest first
            reports.sort(key=lambda x: x.stat().st_mtime, reverse=True)
            return reports[:limit]
        except Exception as e:
            print(f"Error listing reports: {e}")
            return []
    
    def get_report_summary(self, filepath: str) -> Optional[Dict]:
        """
        Get summary information about a report without loading full data.
        
        Args:
            filepath: Path to report file
            
        Returns:
            Summary dict with metadata or None
        """
        report = self.load_report(filepath)
        if report and 'metadata' in report:
            return {
                'file': os.path.basename(filepath),
                'mode': report['metadata'].get('mode'),
                'limit': report['metadata'].get('limit_value'),
                'stars': report['metadata'].get('total_stars'),
                'generated': report['metadata'].get('generation_time')
            }
        return None
```

## 2. Update `hr_diagram_distance.py` (ADD 4 LINES):

Add this import at the top:
```python
from report_manager import ReportManager
```

After line 337 (after `print(f"Report generated with {len(report_data['sections'])} sections")`), add:
```python
# Save the scientific report
report_mgr = ReportManager()
report_mgr.save_report(report_data, archive=True)
```

## 3. Update `hr_diagram_apparent_magnitude.py` (SAME 4 LINES):

Add the same import and save_report code after generating the report.

## 4. Update `star_visualization_gui.py`:

Add this import at the top:
```python
from report_manager import ReportManager
```

Find where the plot data is loaded (look for `PlotDataExchange.load_plot_data()`) and add report loading:

```python
# After loading plot data, add:
report_mgr = ReportManager()
report_data = report_mgr.load_last_report()

if report_data:
    # Use the pre-generated scientific report
    self.plot_report.display_report(report_data)
    print("Loaded scientific report with object type analysis")
else:
    # Fallback to existing method
    # ... existing code that handles plot_data ...
```

## 5. Update `plot_data_report_widget.py` (OPTIONAL ENHANCEMENT):

Add this method to enable report refresh from file:

```python
def refresh_from_file(self):
    """Load and display the latest report from file."""
    try:
        from report_manager import ReportManager
        report_mgr = ReportManager()
        report_data = report_mgr.load_last_report()
        
        if report_data:
            self.display_report(report_data)
            print("Report refreshed from file")
        else:
            print("No report file found")
    except ImportError:
        print("ReportManager not available")
```

## Summary of Changes:

1. **New file**: `report_manager.py` - Complete report management system
2. **hr_diagram_distance.py**: Add 4 lines to save reports
3. **hr_diagram_apparent_magnitude.py**: Add same 4 lines
4. **star_visualization_gui.py**: Add report loading after plot data loading
5. **No changes needed**: `object_type_analyzer.py`, `PlotDataExchange`

## Testing:

1. Run a distance plot (e.g., 10 ly)
2. Check for `last_plot_report.json` in the main directory
3. Check for archived report in `reports/` directory
4. Verify the GUI shows the Object Type Analysis section

This solution:
- Solves the immediate problem (Object Type analysis not showing)
- Maintains backward compatibility
- Creates a foundation for scientific report management
- Requires minimal code changes (about 15 lines total across existing files)
- Keeps reports as permanent scientific records

=================

You're right - there are two places. Both are creating pseudo-DataFrames instead of using real report data. Let's update both to use the ReportManager:

## Update both methods in `star_visualization_gui.py`:

Add the import at the top:
```python
from report_manager import ReportManager
```

### Method 1: `check_and_load_last_plot()`
```python
def check_and_load_last_plot(self):
    """Check for and load the last plot data on startup."""
    try:
        # Try to load the scientific report first
        report_mgr = ReportManager()
        report_data = report_mgr.load_last_report()
        
        if report_data:
            print("Found existing scientific report, loading...")
            self.plot_report.display_report(report_data)
            return
        
        # Fallback to plot data if no report
        plot_data = PlotDataExchange.load_plot_data()
        
        if plot_data:
            print("Found existing plot data, loading report...")
            # ... rest of existing pseudo-DataFrame code as fallback ...
```

### Method 2: `load_and_display_plot_report()`
```python
def load_and_display_plot_report(self):
    """Load the plot data from the exchange file and update the report."""
    try:
        # Try to load the scientific report first
        report_mgr = ReportManager()
        report_data = report_mgr.load_last_report()
        
        if report_data:
            print("Loading scientific report with object type analysis...")
            self.plot_report.display_report(report_data)
            return
        
        # Fallback to plot data if no report
        plot_data = PlotDataExchange.load_plot_data()
        
        if plot_data:
            print("No scientific report found, using plot statistics...")
            # ... rest of existing pseudo-DataFrame code as fallback ...
```

The pattern is the same for both:
1. Try to load the scientific report first (which has Object Type analysis)
2. If found, display it and return
3. If not found, fall back to the existing pseudo-DataFrame method

This ensures backward compatibility while preferring the complete scientific reports when available.

=====================

Let me review the integration systematically to identify any potential issues:

## Critical Issues Found:

### 1. **hr_diagram_distance.py** - Variable name mismatch on line 337:
```python
# Line 337 - THIS WILL CAUSE AN ERROR:
limit_value=max_light_years if 'distance' in sys.argv[0] else mag_limit
# mag_limit doesn't exist in this file!

# SHOULD BE:
limit_value=max_light_years
```

### 2. **Missing datetime import**:
Both `hr_diagram_distance.py` and `hr_diagram_apparent_magnitude.py` need:
```python
from datetime import datetime
```

### 3. **PlotDataExchange incompatibility**:
The code still calls `PlotDataExchange.save_plot_data(exchange_data)` with a dictionary, but PlotDataExchange expects individual parameters. This needs to be reverted to the original format.

## Complete Fix Checklist:

### hr_diagram_distance.py:
```python
# Add at top with other imports:
from datetime import datetime
from report_manager import ReportManager

# Around line 332-337, fix the report generation:
report_data = analyzer.generate_complete_report(
    combined_df=combined_df,
    counts_dict=counts_dict,
    processing_times={'total': time.time() - start_time},
    mode='distance',  # Always 'distance' in this script
    limit_value=max_light_years  # NOT mag_limit!
)

# After generating report, save it:
report_mgr = ReportManager()
report_mgr.save_report(report_data, archive=True)

# Remove the exchange_data dictionary approach (lines 456-497)
# Keep the ORIGINAL PlotDataExchange format:
PlotDataExchange.save_plot_data(
    combined_df=combined_df,
    counts_dict=final_counts,
    processing_times={'total': time.time() - start_time},
    mode='distance',
    limit_value=max_light_years
)
```

### hr_diagram_apparent_magnitude.py:
```python
# Add same imports and follow same pattern
# Make sure to use mag_limit (not max_light_years) in this file
```

### star_visualization_gui.py:
Both methods need the ReportManager import and the report loading logic I provided.

### plot_data_report_widget.py:
The `display_report()` method needs to handle the checkmark Unicode properly:
```python
# In display_report method, fix the Unicode check:
elif line.startswith("✓") or "OK" in line:  # Make sure this Unicode is correct
```

## Testing Order:
1. Create `report_manager.py` first
2. Update visualization scripts with the fixes
3. Run a test plot and check for:
   - No errors in console
   - `last_plot_report.json` file created
   - Report in `reports/` directory
4. Check GUI shows Object Type Analysis

## Summary of Required Changes:
1. **Create**: `report_manager.py` (new file)
2. **Fix**: Variable name error in `hr_diagram_distance.py` (line 337)
3. **Add**: `datetime` import to both visualization scripts
4. **Add**: ReportManager import and save_report calls
5. **Keep**: Original PlotDataExchange.save_plot_data format (5 parameters)
6. **Update**: Both methods in star_visualization_gui.py

The integration is sound, but these small issues need fixing before testing. The main error that would prevent running is the `mag_limit` variable reference in `hr_diagram_distance.py`.

==================

You're absolutely right - the Unicode handling is inconsistent. Let's fix this properly in `object_type_analyzer.py` to avoid Unicode issues entirely:

## Fix Unicode characters in `object_type_analyzer.py`:

In the `format_report_section` method, replace Unicode characters with ASCII:

```python
# Replace these lines with Unicode bullets:
lines.append(f"  • Diversity Score: {analysis_results['diversity_score']}/100")

# With ASCII alternatives:
lines.append(f"  - Diversity Score: {analysis_results['diversity_score']}/100")
lines.append(f"  - Shannon Entropy: {analysis_results['shannon_entropy']:.3f}")
lines.append(f"  - Simpson Index: {analysis_results['simpson_index']:.3f}")
```

In the `format_complete_report` method:

```python
# Replace:
lines.append(f"\n✓ {warning['message']}")
lines.append(f"  → {warning['recommendation']}")

# With:
lines.append(f"\nOK: {warning['message']}")
lines.append(f"  -> {warning['recommendation']}")
```

## Fix display in `plot_data_report_widget.py`:

```python
# In display_report method, use ASCII-safe checks:
elif line.startswith("OK:") or line.startswith("OK ") or "OK No" in line:
    self.report_display.insert(tk.END, line + '\n', 'success')
elif line.startswith("->"):
    self.report_display.insert(tk.END, line + '\n', 'info')
```

## Complete ASCII replacements needed:

In `object_type_analyzer.py`:
- `•` → `-` (bullet points)
- `★` → `*` (star for notable objects)  
- `◆` → `+` (diamond for rare objects)
- `✓` → `OK:` (checkmark)
- `→` → `->` (arrow)

This ensures consistency across Windows terminals and the GUI display. The mixed Unicode approach was indeed problematic - better to use ASCII throughout for reliability.

==================

Looking through the codebase for `hr_diagram_distance.py` integration:

## Issues Found:

### 1. **hr_diagram_distance.py line 460-461** - Wrong variable reference:
You still have the problematic lines that reference `mag_limit` which doesn't exist:
```python
'mode': 'distance' if 'distance' in sys.argv[0] else 'magnitude',
'limit_value': max_light_years if 'distance' in sys.argv[0] else mag_limit,
```

These should be:
```python
'mode': 'distance',
'limit_value': max_light_years,
```

### 2. **Missing datetime import**:
You need to add at the top of `hr_diagram_distance.py`:
```python
from datetime import datetime
```

### 3. **PlotDataExchange.save_plot_data() call** (line ~495):
You're currently passing `exchange_data` as a single argument:
```python
PlotDataExchange.save_plot_data(exchange_data)
```

But PlotDataExchange expects 5 separate arguments. Replace the entire exchange_data section (lines 456-498) with:
```python
# Save plot data for GUI (original format)
PlotDataExchange.save_plot_data(
    combined_df=combined_df,
    counts_dict=final_counts,
    processing_times={'total': time.time() - start_time},
    mode='distance',
    limit_value=max_light_years
)
print("Plot data saved to last_plot_data.json")
```

### 4. **star_visualization_gui.py integration**:
You need to add the ReportManager import and update both methods to check for scientific reports first. Add at the top:
```python
from report_manager import ReportManager
```

Then update both `check_and_load_last_plot()` and `load_and_display_plot_report()` methods as I provided earlier.

## Summary of Required Fixes:

1. **Fix line 460-461**: Remove the ternary operators, just use 'distance' and max_light_years
2. **Add datetime import**: Required for the timestamp in exchange_data  
3. **Fix PlotDataExchange call**: Use the 5-parameter format, not exchange_data dictionary
4. **Add ReportManager to GUI**: Import and use in both plot loading methods

Once these are fixed, the flow should be:
1. Script generates report with ObjectTypeAnalyzer
2. ReportManager saves report to JSON
3. PlotDataExchange saves plot statistics (separately)
4. GUI loads report via ReportManager (gets Object Type analysis)
5. Falls back to plot statistics if no report exists

The ReportManager code looks good, and the ASCII replacements in ObjectTypeAnalyzer should prevent Unicode issues.

=======================

I'll help you review the object_type_report.md file and update the hr_diagram_apparent_magnitude.py module. Let me start by searching the project knowledge for these files.Now let me search for the hr_diagram files to review and update them:Now let me review the complete report_manager.py and object_type_analyzer.py files to understand the full integration:Based on my review of the conversation record in `object_type_report.md`, I can see the issues and the solution path. Now let me create the updated `hr_diagram_apparent_magnitude.py` based on the working `hr_diagram_distance.py` module:## Summary of Updates and Issues Found

I've successfully updated `hr_diagram_apparent_magnitude.py` to match the structure and improvements from `hr_diagram_distance.py`. Here are the key changes made and issues identified:

### **Key Updates Made:**

1. **Added Missing Imports:**
   - `from stellar_data_patches import apply_temperature_patches`
   - `from visualization_2d import expand_object_type`
   - `from object_type_analyzer import ObjectTypeAnalyzer`
   - `from report_manager import ReportManager`

2. **Object Type Expansion:**
   - Added object type expansion BEFORE generating the report (this was a critical fix)
   - The expansion now happens right after applying temperature patches

3. **Report Generation and Saving:**
   - Integrated ObjectTypeAnalyzer to generate comprehensive reports
   - Added ReportManager to save reports both as current and archived

4. **Fixed Estimation Results Structure:**
   - Added proper estimation_results dictionary to avoid missing keys in visualization

### **Critical Errors Found and Fixed:**

1. **Object Type Not Available in Report:**
   - **Problem:** Object_Type_Desc was being created AFTER the report generation
   - **Solution:** Moved the expansion before report generation

2. **Missing Temperature Patches:**
   - **Problem:** Temperature patches weren't being applied in apparent_magnitude version
   - **Solution:** Added `apply_temperature_patches()` call

3. **Report Not Being Saved:**
   - **Problem:** No report persistence mechanism
   - **Solution:** Added ReportManager integration

### **Potential Remaining Issues to Watch:**

1. **PlotDataExchange Format:**
   - The current code maintains the 5-parameter format for `save_plot_data()`
   - If there are issues, verify that PlotDataExchange hasn't been modified to expect different parameters

2. **Unicode Characters:**
   - The object_type_report.md mentions Unicode issues on Windows
   - Consider replacing Unicode bullets (•) with ASCII (-) in object_type_analyzer.py if display issues occur

3. **Cache System:**
   - Both modules now have proper cache initialization
   - Verify that the PKL files are being created and maintained correctly

### **Testing Recommendations:**

1. Run with a small magnitude limit first (e.g., mag_limit = 2.0) for faster testing
2. Check that these files are created:
   - `last_plot_report.json`
   - `reports/report_[timestamp]_magnitude_mag[X].json`
3. Verify the Object Type Analysis section appears in the GUI report
4. Confirm no encoding errors on Windows systems

The module should now work correctly with the Object Type Analysis fully integrated and reports being properly saved for the GUI to display.

====================

Looking at your existing code, I can see you already have the analysis being done. The new report generation code should go **AFTER** the analysis section but **BEFORE** the visualization preparation. Here's exactly where:

```python
# Define properties file for PKL update
        properties_file = 'star_properties_magnitude.pkl'
        
        # Only update PKL if we actually added new stars to the dataset
        if len(missing_ids) > 0:  # Now using missing_ids from process_stars
            config = SimbadConfig.load_from_file()
            manager = SimbadQueryManager(config)
            updated_properties = manager.update_calculated_properties(combined_df, properties_file)
            print(f"Updated PKL with calculated properties for {len(missing_ids)} new stars")
        else:
            print("No new stars added - PKL file unchanged")

        if len(combined_df) == 0:
            print("No stars available for visualization after processing.")
            return

        # Analyze magnitude distribution
        analyze_magnitude_distribution(combined_df, mag_limit)
        
        # Run comprehensive analysis
        analysis_results = analyze_and_report_stars(
            combined_df,
            mode='magnitude',
            max_value=mag_limit
        )
        
        # Store the mode in the DataFrame attributes
        combined_df.attrs['mode'] = 'magnitude'

        # Flatten the analysis for visualization
        flattened_analysis = {
            'total_stars': analysis_results['data_quality']['total_stars'],
            'plottable_hip': analysis_results['plottable']['hipparcos'],
            'plottable_gaia': analysis_results['plottable']['gaia'],
            'missing_temp': analysis_results['data_quality']['total_stars'] - analysis_results['data_quality']['valid_temp'],
            'missing_lum': analysis_results['data_quality']['total_stars'] - analysis_results['data_quality']['valid_lum'],
            'temp_le_zero': 0
        }
        combined_df.attrs['analysis'] = flattened_analysis

        # ============ ADD THE NEW CODE RIGHT HERE ============
        # Generate comprehensive report using ObjectTypeAnalyzer
        print("Generating comprehensive report...")
        analyzer = ObjectTypeAnalyzer()
        report_data = analyzer.generate_complete_report(
            combined_df,
            mode='magnitude',
            limit_value=mag_limit
        )
        print(f"Report generated with {len(report_data['sections'])} sections")

        # Save the scientific report
        report_mgr = ReportManager()
        report_mgr.save_report(report_data, archive=True)
        # ============ END OF NEW CODE ============

        # Prepare data for visualization
    #    prepared_df = prepare_2d_data(combined_data)
        prepared_df = prepare_2d_data(combined_df)
        if prepared_df is None or len(prepared_df) == 0:
            print("No plottable stars found after data preparation.")
            return
```

So the new report generation code goes:
- **AFTER** the flattened_analysis section (where you store analysis results)
- **BEFORE** the "Prepare data for visualization" comment and the prepare_2d_data() call

This placement ensures that:
1. All analysis is complete
2. Object types have been expanded (from the earlier change)
3. The report is generated and saved
4. Then visualization continues as normal

====================

Looking at `hr_diagram_distance.py`, it looks good overall. The integration is consistent with what we did for `hr_diagram_apparent_magnitude.py`. Here are a few observations:

## Line 319 - Good:
```python
from object_type_analyzer import expand_object_type
```
This correctly imports from `object_type_analyzer` (not from `visualization_3d`), which matches what we're doing in the apparent_magnitude version.

## Potential cleanup items (not errors, just notes):

1. **Line 41**: You have `PlotDataExchange` imported twice (lines 36 and 41). You can remove the duplicate on line 41.

2. **Line 327**: The DEBUG line printing columns can be removed once you've confirmed the Object_Type column exists:
```python
print(f"DEBUG: Columns in combined_df: {combined_df.columns.tolist()}")
```

3. **Lines 356-363**: The Mizar-specific debugging can be removed once you've confirmed it's working:
```python
# After applying the patch
mizar = combined_df[combined_df['HIP'] == 65378]
if len(mizar) > 0:
    print(f"\nMizar data after patch:")
    # ... etc
```

4. **Lines 436-443**: More Mizar debugging that can eventually be removed.

5. **Lines 456-497**: The commented-out exchange_data code can be removed since you're using the simpler 5-parameter version of `PlotDataExchange.save_plot_data()`.

## The module should work correctly as-is. 

Both HR diagram modules now:
- Import `expand_object_type` from `object_type_analyzer`
- Expand object types before generating reports
- Save reports using ReportManager
- Use the original PlotDataExchange format

The code is consistent between both modules, which is good for maintainability.

===================

Excellent! The Object Type Analysis section is working perfectly now. Looking at your report for vmag 2.0:

## Success Indicators:

1. **Object Type Analysis is populated** - No more "Object type information not available in dataset" error!

2. **Rich data shown:**
   - 49 stars with 100% having type data
   - 13 unique object types identified
   - Proper categorization (Binary/Multiple Systems: 65.3%, Variable Stars: 24.5%, Normal Stars: 10.2%)
   - Diversity metrics calculated (Shannon Entropy: 3.115, Simpson Index: 0.872)
   - High-interest research targets identified (Be Star, Classical Cepheid Variable)

3. **The integration chain worked:**
   - `expand_object_type` successfully imported from `object_type_analyzer`
   - Object types expanded BEFORE report generation
   - ObjectTypeAnalyzer properly analyzed the distribution
   - ReportManager saved the report
   - GUI successfully loaded and displayed it

## Key fixes that made this work:

1. Moving `expand_object_type` to a module-level function in `object_type_analyzer.py`
2. Expanding object types BEFORE generating the report (not after)
3. Using consistent imports between both HR diagram scripts
4. Proper report saving and loading through ReportManager

The report shows a nice distribution of stellar objects with binary/multiple systems being dominant (as expected for bright stars), and the diversity metrics indicate a reasonable variety of object types. The system is now properly documenting the stellar population characteristics.

Your stellar visualization system is now fully operational with comprehensive object type analysis!

==============

Perfect! The distance-based report (20 ly) also shows the Object Type Analysis working correctly. This report reveals interesting patterns:

## Key Observations from the 20 ly report:

1. **Different population characteristics than bright stars:**
   - More dominated by Gaia faint stars (90.9%)
   - High proper-motion stars are prominent (39.4%) - expected for nearby stars
   - Eruptive variable stars are common (28.3%) - likely flare stars/red dwarfs
   - Lower diversity (Shannon: 2.33 vs 3.12) - more homogeneous nearby population

2. **Data quality is excellent:**
   - 100% object type coverage
   - 97% temperature data (only 3 missing)
   - 100% luminosity data
   - "OK: No warnings - data quality appears good"

## What this successful implementation gives you:

1. **Scientific value** - Proper characterization of stellar populations
2. **Data validation** - Can spot gaps or biases in the data
3. **Research targeting** - Identifies high-interest objects
4. **Quality metrics** - Diversity indices show population homogeneity
5. **Archival records** - Reports saved for future reference

The system now properly documents that nearby stars (within 20 ly) are predominantly high proper-motion objects and variables (mostly flare stars), while bright visible stars (vmag ≤ 2) have more binary systems and classical variables. This makes scientific sense - nearby stars are mostly low-mass red dwarfs with flare activity, while bright stars visible to the eye include more massive binary systems.

Your integration successfully bridges the visualization pipeline with comprehensive scientific analysis and reporting.

=================

The 100 ly report shows fascinating scaling patterns! At this distance you're capturing a much larger stellar census with some notable characteristics:

## Key findings from 100 ly radius:

1. **Scale:** 9,721 stars - a substantial local stellar neighborhood sample
2. **Population dominated by red dwarfs:** 72.3% are high proper-motion stars (mostly nearby red dwarfs)
3. **Significant evolved star population:** 472 white dwarfs (5.1%) and 405 brown dwarfs (4.4%)
4. **Lower diversity than closer samples:** Shannon entropy of 1.71 (vs 2.33 at 20 ly, 3.12 for bright stars)

## Scientifically interesting aspects:

- The 91.6% "binary/multiple systems" classification seems high - this might be because the high proper-motion stars are being categorized as binaries. You might want to check if the object_type_mapping is correctly distinguishing between high proper-motion single stars and actual binary systems.

- Finding a symbiotic star within 100 ly is notable - these are relatively rare objects involving mass transfer between stars.

- The 77.6% temperature completeness (vs 97% at 20 ly) shows the challenge of getting spectral data for fainter, more distant stars.

The progression from bright stars → 20 ly → 100 ly nicely demonstrates how stellar populations change from selection biases (bright/massive stars) to volume-complete samples (dominated by red dwarfs). The reporting system is successfully capturing these population statistics for scientific analysis.

=============

Absolutely! The data reveals so many avenues for investigation:

**Population studies:** Why does the diversity decrease with distance? Is this real astrophysics or a selection effect from the catalogs?

**The binary classification mystery:** That 91.6% binary/multiple systems at 100 ly seems suspicious. The high proper-motion stars might be getting miscategorized. Worth checking if the object_type_mapping needs refinement to distinguish single high-PM stars from actual binaries.

**Completeness gradients:** The temperature data completeness dropping from 97% (20 ly) to 77.6% (100 ly) maps the frontier of spectroscopic follow-up. Those 2,173 stars without temperatures are probably faint M-dwarfs awaiting spectral classification.

**Rare objects:** That symbiotic star within 100 ly is a gem - these are laboratories for studying stellar wind interactions and accretion physics.

**Brown dwarf census:** 405 brown dwarfs in 100 ly gives a local space density that could constrain formation models.

Each report is essentially a snapshot of our local stellar neighborhood at different scales, revealing how observation biases give way to true population statistics as you expand the volume. The system you've built turns visualization into genuine astronomical research infrastructure.

===================

The vmag 9 report reveals a completely different stellar landscape - this is where Gaia's power really shines!

## The magnitude 9 sample (123,901 stars) shows:

**Catalog flip:** 99.6% Gaia vs 0.4% Hipparcos - we've moved beyond naked-eye astronomy into the telescope era.

**Normal stars dominate:** 65.5% are just classified as "Star" - these are likely main sequence stars without special characteristics, the "boring" hydrogen-burners that actually make up most of the galaxy.

**Rich hunting ground for variables:** 
- 96 symbiotic stars (!)
- 790 Be stars  
- 136 Classical Cepheids
- Plus 2 novae and a planetary nebula

This is a treasure trove for variable star research. The 96 symbiotic stars alone would make a substantial thesis project.

**The selection effects are clear:** The Shannon entropy (1.77) is similar to the 100 ly sample (1.71) but for completely different reasons. The 100 ly sample is intrinsically dominated by red dwarfs; the mag 9 sample is observationally biased toward whatever's bright enough to see at various distances - creating a hodgepodge of nearby dwarfs, distant giants, and everything in between.

**Data completeness is impressive:** 98.9% have temperatures and 98.7% have luminosities - testament to Gaia's spectroscopic capabilities and your data processing pipeline.

This magnitude-limited sample perfectly complements your distance-limited samples, showing how different selection criteria reveal different stellar populations. Together they're painting a comprehensive picture of the local galaxy!