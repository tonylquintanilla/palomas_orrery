To properly test the apsidal markers and dates, here are some things to check:

Enable ideal orbit markers - Make sure the checkbox/option for showing ideal apsidal markers is enabled in your GUI
Check the date range - Your current date is 2025-08-10, and Mercury's last perihelion was 2024-03-27. The next perihelion should be approximately:

2024-03-27 + 87.97 days ≈ 2024-06-23
2024-06-23 + 87.97 days ≈ 2024-09-19
2024-09-19 + 87.97 days ≈ 2024-12-16
2024-12-16 + 87.97 days ≈ 2025-03-14
2025-03-14 + 87.97 days ≈ 2025-06-10
2025-06-10 + 87.97 days ≈ 2025-09-06 (this should be visible in your current plot!)


Test with different objects:

Earth: Has TP=2460677.413 (2025-01-03), period=365.25 days
Mars: Has TP=2460587.648 (2024-10-05), period=686.98 days   # this works
3I/ATLAS: Hyperbolic orbit (e=6.14), should only show perihelion


Check hover text - Hover over the apsidal markers to see if dates and distances are displayed correctly
Visual verification:

Perihelion markers should appear at the closest point to the Sun
Aphelion markers should appear at the farthest point (for elliptical orbits only)
Markers should be colored squares matching the object's color



Run the visualization and let me know if you see:

The apsidal markers appearing at the correct positions
Hover text showing dates and distances
Any error messages in the console

If there are issues, we can debug them specifically.

# Comprehensive Testing Protocol for Apsidal Markers and Dates

## Overview
This protocol ensures complete validation of apsidal marker visualization and date calculations across all implementations in Paloma's Orrery.

## 1. Test Categories

### 1.1 Orbit Type Coverage
Test each orbit type to verify correct handling:

#### Elliptical Orbits (e < 1)
- **Planets**: Mercury (e=0.206), Mars (e=0.093)
- **Asteroids**: Ceres (e=0.076), Vesta (e=0.089)
- **Comets**: Halley (e=0.968), Churyumov-Gerasimenko (e=0.641)
- **Satellites**: Moon (e=0.055), Phobos (e=0.015)

#### Near-Parabolic Orbits (e ≈ 1)
- **Comets**: C/2025_K1 (e=1.000251), Ikeya-Seki (e=0.99992)

#### Hyperbolic Orbits (e > 1)
- **Interstellar**: 3I/ATLAS (e=6.141), Oumuamua (e=1.201)

### 1.2 Marker Type Tests

#### Ideal Apsidal Markers
- Verify markers appear at correct orbital positions
- Check marker colors match object color scheme
- Validate hover text shows correct distances
- Confirm terminology (perihelion/aphelion vs perigee/apogee)

#### Actual Apsidal Markers
- Verify JPL Horizons positions are fetched correctly
- Check white square markers appear at actual positions
- Validate distance calculations from fetched positions
- Confirm date strings match expected format

## 2. Functional Test Cases

### Test Case 2.1: Elliptical Orbit Date Calculation
**Setup**: Select Earth, date 2025-01-10
**Expected Results**:
- Perihelion marker at correct position (near January 3, 2025)
- Aphelion marker opposite side of orbit
- Hover text shows "Perihelion: 2025-01-03" and "Aphelion: 2025-07-04"
- Distances: perihelion ~0.983 AU, aphelion ~1.017 AU

### Test Case 2.2: Satellite Terminology
**Setup**: Select Moon as satellite of Earth
**Expected Results**:
- Markers labeled "Perigee" and "Apogee" (not perihelion/aphelion)
- Distances shown in Earth radii or km (not AU)
- Dates calculated based on lunar month (~27.3 days)

### Test Case 2.3: Hyperbolic Orbit Handling
**Setup**: Select 3I/ATLAS, date 2025-07-10
**Expected Results**:
- Only perihelion marker shown (no aphelion for hyperbolic)
- Hover text shows "Approaching perihelion" or estimated date
- No aphelion marker or date displayed

### Test Case 2.4: Dual Marker Comparison
**Setup**: Select Mars with both ideal and actual markers enabled
**Expected Results**:
- Colored square-open markers at ideal positions
- White square-open markers at actual JPL positions
- Small positional differences visible (perturbation effects)
- Both sets have correct hover information

## 3. Date Calculation Validation

### Test Case 3.1: Forward Prediction
**Setup**: Select object before perihelion passage
**Verification Steps**:
1. Check calculated perihelion date is in future
2. Verify date matches known ephemeris data
3. Confirm mean anomaly calculation is correct
4. Validate Kepler's equation solver convergence

### Test Case 3.2: Historical Dates
**Setup**: Select comet with known perihelion dates
**Verification Steps**:
1. Compare calculated dates with historical records
2. Verify TP (Time of Perihelion) parameter usage
3. Check orbital period calculations

### Test Case 3.3: Edge Cases
- Objects at exact perihelion (true anomaly = 0)
- Objects at exact aphelion (true anomaly = π)
- High eccentricity orbits (e > 0.95)
- Circular orbits (e ≈ 0)

## 4. Visualization Consistency Tests

### Test Case 4.1: Main Plot vs Orbital Parameter Viz
**Setup**: Open both visualizations for same object
**Expected Results**:
- Identical apsidal dates shown in both views
- Same marker positions (accounting for projection)
- Consistent color schemes
- Matching hover text information

### Test Case 4.2: Animation Continuity
**Setup**: Animate object through full orbit
**Expected Results**:
- Markers remain at fixed orbital positions
- Dates update correctly as time progresses
- No flickering or position jumps
- Smooth transitions at apsidal points

## 5. Data Source Integration

### Test Case 5.1: KNOWN_ORBITAL_PERIODS Usage
**Verification**:
- Confirm all period lookups use constants_new.py
- Verify no duplicate PER parameters remain
- Check fallback to Kepler's third law works
- Test unknown objects use calculated periods

### Test Case 5.2: JPL Horizons Fetching
**Verification**:
- Test fetch_positions_for_apsidal_dates function
- Verify caching mechanism works
- Check error handling for unavailable dates
- Validate coordinate transformations

## 6. Error Handling Tests

### Test Case 6.1: Missing Data
- Object without orbital parameters
- No current position available
- Missing orbital period data
- Invalid eccentricity values

### Test Case 6.2: Numerical Stability
- Near-zero eccentricity
- Eccentricity very close to 1
- Large semi-major axes
- Retrograde orbits (i > 90°)

## 7. Performance Tests

### Test Case 7.1: Multiple Objects
**Setup**: Display 10+ objects with apsidal markers
**Metrics**:
- Frame rate remains above 30 FPS
- Marker generation < 100ms per object
- Memory usage stable
- No UI lag

### Test Case 7.2: Date Range Queries
**Setup**: Large date ranges for actual markers
**Metrics**:
- JPL queries complete < 2 seconds
- Caching reduces subsequent queries
- Batch fetching works correctly

## 8. Regression Tests

### Critical Paths to Verify:
1. `calculate_apsidal_dates()` → accurate date computation
2. `calculate_true_anomaly_from_position()` → correct angle
3. `true_to_eccentric_anomaly()` → proper conversion
4. `add_perihelion_marker()` → correct visualization
5. `fetch_positions_for_apsidal_dates()` → accurate positions

## 9. User Experience Tests

### Test Case 9.1: Hover Information
- Text is readable and well-formatted
- Information is accurate and relevant
- Units are appropriate (AU, km, days)
- Dates use consistent format (YYYY-MM-DD)

### Test Case 9.2: Visual Clarity
- Markers are distinguishable from orbit lines
- Ideal vs actual markers clearly different
- Colors provide good contrast
- Size appropriate for visibility

## 10. Known Issues to Address

### Issue 1: PER Parameter Redundancy
- **Location**: `idealized_orbits.py` planetary_params
- **Fix**: Remove PER, use KNOWN_ORBITAL_PERIODS exclusively
- **Impact**: Code duplication, maintenance burden

### Issue 2: Hyperbolic Date Estimation
- **Location**: `calculate_apsidal_dates()` line with "days_estimate = 30 * (1 - current_theta/np.pi)"
- **Issue**: Oversimplified velocity estimation
- **Fix**: Implement proper hyperbolic orbit mechanics

### Issue 3: Satellite Distance Units
- **Location**: `add_actual_apsidal_markers()`
- **Issue**: Always shows distances in AU, even for satellites
- **Fix**: Add unit conversion for satellites (show in km or planetary radii)

### Issue 4: Missing Error Context
- **Location**: Multiple try/except blocks
- **Issue**: Generic error messages without context
- **Fix**: Add specific error messages with object names and parameters

### Issue 5: Coordinate Frame Assumptions
- **Location**: `calculate_true_anomaly_from_position()`
- **Issue**: Assumes ecliptic frame, may fail for satellites
- **Fix**: Add frame transformation handling

## 11. Test Execution Checklist

### Pre-Test Setup
- [ ] Clear cache to test fresh data fetching
- [ ] Verify test date (2025-08-10) is set
- [ ] Check all required modules imported
- [ ] Confirm JPL Horizons connectivity

### During Testing
- [ ] Document any unexpected behaviors
- [ ] Screenshot anomalies for debugging
- [ ] Note performance metrics
- [ ] Track error messages

### Post-Test Validation
- [ ] Compare results with ephemeris tables
- [ ] Verify consistency across modules
- [ ] Check log files for warnings
- [ ] Update test results documentation

## 12. Automated Test Script Template

```python
def test_apsidal_markers():
    """Automated test suite for apsidal markers."""
    
    test_objects = [
        {'name': 'Earth', 'expected_peri': '2025-01-03', 'e': 0.0167},
        {'name': 'Mars', 'expected_peri': '2024-10-05', 'e': 0.0934},
        {'name': 'Halley', 'expected_peri': '2061-07-28', 'e': 0.968},
        {'name': '3I/ATLAS', 'expected_peri': '2025-10-29', 'e': 6.141}
    ]
    
    for obj in test_objects:
        # Test date calculation
        peri_date, apo_date = calculate_apsidal_dates(...)
        assert peri_date.strftime('%Y-%m-%d') == obj['expected_peri']
        
        # Test marker generation
        fig = go.Figure()
        add_perihelion_marker(fig, ...)
        assert len(fig.data) > 0
        
        # Test hover text
        hover_text = fig.data[-1].hovertemplate
        assert obj['name'] in hover_text
        assert 'Perihelion' in hover_text or 'Periapsis' in hover_text
    
    print("All tests passed!")
```

## 13. Success Criteria

The apsidal marker system is considered fully functional when:
1. All test cases pass without errors
2. Dates match JPL Horizons data within 1 day
3. Visual markers appear at correct positions
4. Performance meets specified metrics
5. No regression in existing functionality
6. User experience is intuitive and informative

## 14. Maintenance Schedule

- **Daily**: Automated regression tests
- **Weekly**: Manual visual inspection
- **Monthly**: Performance benchmarking
- **Quarterly**: Full test suite execution
- **Annually**: Update ephemeris data validation

---

*This testing protocol should be executed before any major release and after significant changes to orbital calculation or visualization code.*