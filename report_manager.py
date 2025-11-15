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
    #    self.last_report_file = "last_plot_report.json"
        self.last_report_file = str(self.reports_dir / "last_plot_report.json")
    
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