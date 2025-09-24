# object_type_analyzer.py
"""
Object Type Analysis and Report Generation Module
Provides comprehensive analysis of astronomical data including object types,
data quality metrics, and full report generation.
"""

from typing import Dict, List, Tuple, Optional, Any
import pandas as pd
import numpy as np
from datetime import datetime

def expand_object_type(ot):
    """
    Expand object type codes to full descriptions.
    This is a utility function used by visualization modules.
    """
    import re
    import pandas as pd
    
    if ot is None or pd.isna(ot):
        return 'Unknown'
    
    ot_codes = re.split(r'[;, ]+', str(ot))
    descriptions = []
    
    # Use the mapping from constants_new that's already imported
    from constants_new import object_type_mapping
    
    for code in ot_codes:
        code = code.strip()
        if code in object_type_mapping:
            desc = object_type_mapping[code]
        else:
            matched = False
            for key in object_type_mapping:
                if key in code:
                    desc = object_type_mapping[key]
                    matched = True
                    break
            if not matched:
                desc = code
        descriptions.append(desc)
    
    return ', '.join(descriptions)

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
        lines.append(f"  - Diversity Score: {analysis_results['diversity_score']}/100")
        lines.append(f"  - Shannon Entropy: {analysis_results['shannon_entropy']:.3f}")
        lines.append(f"  - Simpson Index: {analysis_results['simpson_index']:.3f}")
        
        # Category breakdown
        lines.append("\nObject Categories:")
        sorted_categories = sorted(
            [(cat, count) for cat, count in analysis_results['category_counts'].items() if count > 0],
            key=lambda x: (self.category_priority.get(x[0], 999), -x[1])
        )
        
        for category, count in sorted_categories:
            percentage = analysis_results['category_percentages'][category]
            lines.append(f"  - {category}: {count:,d} ({percentage:.1f}%)")
        
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
                lines.append(f"  - {display_type}: {target['count']} (interest: {target['interest_score']}/10)")
        
        # Notable/rare objects
        if analysis_results['notable_objects']:
            lines.append("\nRare/Notable Objects:")
            for obj_type, count in analysis_results['notable_objects'][:5]:
                display_type = obj_type if len(str(obj_type)) <= 35 else str(obj_type)[:32] + "..."
                lines.append(f"  - {display_type}: {count}")
        
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

    
    def generate_complete_report(self, 
                                combined_df: pd.DataFrame,
                                counts_dict: Dict = None,
                                processing_times: Dict = None,
                                mode: str = 'magnitude',
                                limit_value: float = None) -> Dict[str, Any]:
        """
        Generate a complete report data structure for the plot.
        
        Args:
            combined_df: DataFrame with all star data
            counts_dict: Dictionary with catalog counts
            processing_times: Processing time information
            mode: 'magnitude' or 'distance'
            limit_value: Magnitude or distance limit
            
        Returns:
            Dictionary containing all report sections
        """
        report = {
            'metadata': {
                'mode': mode,
                'limit_value': limit_value,
                'total_stars': len(combined_df),
                'generation_time': datetime.now().isoformat(),
                'generated_by': 'visualization_script'
            },
            'sections': {}
        }
        
        # Section 1: Basic Statistics
        report['sections']['basic_stats'] = self._generate_basic_stats(
            combined_df, counts_dict, mode, limit_value
        )
        
        # Section 2: Data Completeness
        report['sections']['completeness'] = self._generate_completeness_metrics(
            combined_df
        )
        
        # Section 3: Data Quality
        report['sections']['quality'] = self._generate_quality_indicators(
            combined_df
        )
        
        # Section 4: Catalog Coverage
        report['sections']['catalog_coverage'] = self._generate_catalog_coverage(
            combined_df
        )
        
        # Section 5: Processing Diagnostics
        report['sections']['processing'] = processing_times or {'total': 0}
        
        # Section 6: Object Type Analysis
        report['sections']['object_analysis'] = self._generate_object_type_analysis(
            combined_df
        )
        
        # Section 7: Warnings and Recommendations
        report['sections']['warnings'] = self._generate_warnings_and_recommendations(
            combined_df
        )
        
        return report
    
    def _generate_basic_stats(self, df: pd.DataFrame, counts_dict: Dict, 
                              mode: str, limit_value: float) -> Dict:
        """Generate basic statistics section."""
        stats = {
            'total_stars': len(df),
            'mode': mode,
            'limit_value': limit_value,
            'catalog_distribution': {}
        }
        
        if counts_dict:
            stats['catalog_distribution'] = counts_dict
        else:
            # Calculate from dataframe if not provided
            if 'Source_Catalog' in df.columns:
                stats['catalog_distribution'] = df['Source_Catalog'].value_counts().to_dict()
        
        return stats
    
    def _generate_completeness_metrics(self, df: pd.DataFrame) -> Dict:
        """Generate data completeness metrics."""
        metrics = {}
        
        # Temperature completeness
        if 'Temperature' in df.columns:
            temp_valid = df['Temperature'].notna().sum()
            temp_missing = df['Temperature'].isna().sum()
            metrics['temperature'] = {
                'valid': int(temp_valid),
                'missing': int(temp_missing),
                'percentage': round(temp_valid / len(df) * 100, 1) if len(df) > 0 else 0
            }
        
        # Luminosity completeness
        if 'Luminosity' in df.columns:
            lum_valid = df['Luminosity'].notna().sum()
            lum_missing = df['Luminosity'].isna().sum()
            metrics['luminosity'] = {
                'valid': int(lum_valid),
                'missing': int(lum_missing),
                'percentage': round(lum_valid / len(df) * 100, 1) if len(df) > 0 else 0
            }
        
        # Temperature source breakdown
        if 'Temperature_Method' in df.columns:
            methods = df['Temperature_Method'].value_counts().to_dict()
            metrics['temperature_sources'] = {k: int(v) for k, v in methods.items()}
        
        # Plottable stars
        if 'Temperature' in df.columns and 'Luminosity' in df.columns:
            plottable = df['Temperature'].notna() & df['Luminosity'].notna()
            metrics['plottable'] = {
                'count': int(plottable.sum()),
                'percentage': round(plottable.sum() / len(df) * 100, 1) if len(df) > 0 else 0
            }
        
        return metrics
    
    def _generate_quality_indicators(self, df: pd.DataFrame) -> Dict:
        """Generate data quality indicators."""
        indicators = {
            'anomalies': [],
            'statistics': {}
        }
        
        # Check for temperature anomalies
        if 'Temperature' in df.columns:
            temp = df['Temperature'].dropna()
            if len(temp) > 0:
                # Extreme temperatures
                very_hot = (temp > 40000).sum()
                very_cool = (temp < 2000).sum()
                
                if very_hot > 0:
                    indicators['anomalies'].append({
                        'type': 'extreme_temperature',
                        'description': f'{very_hot} stars with T > 40,000 K',
                        'severity': 'info'
                    })
                
                if very_cool > 0:
                    indicators['anomalies'].append({
                        'type': 'extreme_temperature',
                        'description': f'{very_cool} stars with T < 2,000 K',
                        'severity': 'info'
                    })
                
                indicators['statistics']['temperature'] = {
                    'min': float(temp.min()),
                    'max': float(temp.max()),
                    'mean': float(temp.mean()),
                    'median': float(temp.median())
                }
        
        # Check parallax quality if available
        if 'e_Plx' in df.columns and 'Plx' in df.columns:
            parallax_quality = df['e_Plx'] / df['Plx'].abs()
            high_error = (parallax_quality > 0.2).sum()
            if high_error > 0:
                indicators['anomalies'].append({
                    'type': 'parallax_uncertainty',
                    'description': f'{high_error} stars with parallax error > 20%',
                    'severity': 'warning'
                })
        
        return indicators
    
    def _generate_catalog_coverage(self, df: pd.DataFrame) -> Dict:
        """Generate catalog coverage analysis."""
        coverage = {}
        
        if 'Source_Catalog' in df.columns:
            catalog_counts = df['Source_Catalog'].value_counts()
            total = len(df)
            
            coverage['sources'] = {}
            for catalog, count in catalog_counts.items():
                coverage['sources'][catalog] = {
                    'count': int(count),
                    'percentage': round(count / total * 100, 1) if total > 0 else 0
                }
        
        # Add magnitude distribution if available
        if 'Apparent_Magnitude' in df.columns:
            mag = df['Apparent_Magnitude'].dropna()
            if len(mag) > 0:
                coverage['magnitude_stats'] = {
                    'min': float(mag.min()),
                    'max': float(mag.max()),
                    'mean': float(mag.mean())
                }
        
        return coverage
    
    def _generate_object_type_analysis(self, df: pd.DataFrame) -> Dict:
        """Generate object type analysis section."""
        # Look for object type column
        type_column = None
        if 'Object_Type_Desc' in df.columns:
            type_column = 'Object_Type_Desc'
        elif 'Object_Type' in df.columns:
            type_column = 'Object_Type'
        
        if type_column and df[type_column].notna().any():
            # Use existing analyze_distribution method
            return self.analyze_distribution(df[type_column])
        
        return {
            'summary': 'No object type information available',
            'total_count': 0,
            'typed_count': 0,
            'category_counts': {},
            'category_percentages': {},
            'type_counts': {},
            'notable_objects': [],
            'diversity_score': 0
        }
    
    def _generate_warnings_and_recommendations(self, df: pd.DataFrame) -> List[Dict]:
        """Generate warnings and recommendations."""
        warnings = []
        
        # Check data size
        if len(df) < 2:
            warnings.append({
                'level': 'critical',
                'message': f'Only {len(df)} star(s) in dataset - insufficient for meaningful visualization',
                'recommendation': 'Increase magnitude limit or distance range'
            })
        elif len(df) < 10:
            warnings.append({
                'level': 'warning',
                'message': f'Limited dataset with only {len(df)} stars',
                'recommendation': 'Consider expanding search criteria for richer visualization'
            })
        
        # Check completeness
        if 'Temperature' in df.columns:
            temp_complete = df['Temperature'].notna().sum() / len(df) * 100
            if temp_complete < 50:
                warnings.append({
                    'level': 'warning',
                    'message': f'Low temperature completeness ({temp_complete:.1f}%)',
                    'recommendation': 'Many stars lack temperature data'
                })
        
        # Check for catalog bias
        if 'Source_Catalog' in df.columns:
            catalog_counts = df['Source_Catalog'].value_counts()
            if len(catalog_counts) == 1:
                warnings.append({
                    'level': 'info',
                    'message': f'Data from single catalog only ({catalog_counts.index[0]})',
                    'recommendation': 'Results may be biased to catalog selection criteria'
                })
        
        return warnings if warnings else [{'level': 'ok', 'message': 'No warnings - data quality appears good'}]
    
    def format_complete_report(self, report_data: Dict) -> List[str]:
        """
        Format a complete report from report data structure.
        
        Args:
            report_data: Dictionary from generate_complete_report
            
        Returns:
            List of formatted report lines
        """
        lines = []
        
        # Header
        lines.append("=" * 46)
        lines.append("PLOT DATA REPORT")
        lines.append("=" * 46)
        
        metadata = report_data.get('metadata', {})
        lines.append(f"Generated: {metadata.get('generation_time', 'Unknown')}")
        lines.append(f"Plot Mode: {metadata.get('mode', 'Unknown')}")
        
        if metadata.get('mode') == 'magnitude':
            lines.append(f"Limiting Magnitude: {metadata.get('limit_value', 'Unknown')}")
        else:
            lines.append(f"Distance Limit: {metadata.get('limit_value', 'Unknown')} ly")
        
        sections = report_data.get('sections', {})
        
        # Section 1: Basic Statistics
        if 'basic_stats' in sections:
            lines.append("\n" + "-" * 52)
            lines.append("1. BASIC PLOT STATISTICS")
            lines.append("-" * 52)
            stats = sections['basic_stats']
            lines.append(f"Total Stars in Dataset: {stats.get('total_stars', 0)}")
            
            if 'catalog_distribution' in stats:
                lines.append("\nCatalog Distribution:")
                for catalog, count in stats['catalog_distribution'].items():
                    percentage = (count / stats['total_stars'] * 100) if stats['total_stars'] > 0 else 0
                    lines.append(f"  {catalog}: {count} ({percentage:.1f}%)")
        
        # Section 2: Data Completeness
        if 'completeness' in sections:
            lines.append("\n" + "-" * 52)
            lines.append("2. DATA COMPLETENESS METRICS")
            lines.append("-" * 52)
            comp = sections['completeness']
            
            if 'temperature' in comp:
                t = comp['temperature']
                lines.append(f"\nTemperature Data:")
                lines.append(f"  Valid: {t['valid']} ({t['percentage']:.1f}%)")
                lines.append(f"  Missing: {t['missing']}")
            
            if 'luminosity' in comp:
                l = comp['luminosity']
                lines.append(f"\nLuminosity Data:")
                lines.append(f"  Valid: {l['valid']} ({l['percentage']:.1f}%)")
                lines.append(f"  Missing: {l['missing']}")
        
        # Section 6: Object Type Analysis
        if 'object_analysis' in sections:
            lines.append("\n" + "-" * 52)
            lines.append("6. OBJECT TYPE ANALYSIS")
            lines.append("-" * 52)
            analysis = sections['object_analysis']
            lines.extend(self.format_report_section(analysis))
        
        # Section 7: Warnings
        if 'warnings' in sections:
            lines.append("\n" + "-" * 52)
            lines.append("7. WARNINGS AND RECOMMENDATIONS")
            lines.append("-" * 52)
            for warning in sections['warnings']:
                if warning['level'] == 'ok':
                    lines.append(f"\nOK: {warning['message']}")
                else:
                    level = warning['level'].upper()
                    lines.append(f"\n{level}: {warning['message']}")
                    if 'recommendation' in warning:
                        lines.append(f"  -> {warning['recommendation']}")
        
        # Footer
        lines.append("\n" + "=" * 46)
        lines.append("END OF REPORT")
        lines.append("=" * 46)
        
        return lines

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