import json
c = json.load(open(r'data/orbit_paths.json'))
cands = [k for k in c if 'arycenter' in k or k.startswith('Pluto-Charon') or k in ('9_Sun','Pluto-Charon Barycenter_Sun')]
print('barycenter candidate keys:', cands)
for k in cands:
    ks = sorted(c[k].get('data_points', {}))
    print(f"  {k}: {len(ks)} pts, {ks[0] if ks else 'NA'} .. {ks[-1] if ks else 'NA'}")