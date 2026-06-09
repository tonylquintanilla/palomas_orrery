"""
measure_animation_html.py - Measure frame payload in a saved Plotly animation HTML.

Reports, for each animation HTML export: total file size, number of figure
traces, number of frames, traces carried per frame, total serialized frames
payload, and the largest per-frame traces by name. Run it on a BASELINE export
(pre-patch) and a PATCHED export of the same animation to quantify the 21/51
Phase 1 frame-fence fix. Pure stdlib; works on Windows, macOS, and Linux.

Usage:
    python measure_animation_html.py baseline.html patched.html
    python measure_animation_html.py some_animation.html

Key functions:
    extract_figure_and_frames() - locate the Plotly.newPlot / Plotly.addFrames
                                  JSON in the saved HTML and parse both
    report() - print the measurement block for one file

Consumed by: ANIMATION_TEST_PROTOCOL (Mode-5 animation testing)

Module updated: June 2026 with Anthropic's Claude Fable 5
"""

import json
import os
import sys


def _raw_decode_at(html, start):
    """Decode one JSON value beginning at html[start]."""
    decoder = json.JSONDecoder()
    obj, _end = decoder.raw_decode(html[start:])
    return obj


def extract_figure_and_frames(html):
    """Return (data_list, frames_list, frames_json_bytes) from a saved
    Plotly HTML. Saved structure (verified against plotly write_html output):
        Plotly.newPlot("<id>", [DATA], {LAYOUT}, {CONFIG})
            .then(function(){ Plotly.addFrames('<id>', [FRAMES]); ... })
    The last Plotly.newPlot in the file is the figure (earlier hits are
    inside the bundled plotly.js library source).
    """
    i = html.rfind('Plotly.newPlot')
    if i < 0:
        raise ValueError('No Plotly.newPlot call found - is this a saved plot?')
    # First '[' after the div-id string argument opens the data array
    data_start = html.find('[', html.find(',', i))
    data = _raw_decode_at(html, data_start)

    frames = []
    frames_bytes = 0
    j = html.find('Plotly.addFrames', i)
    if j >= 0:
        frames_start = html.find('[', html.find(',', j))
        decoder = json.JSONDecoder()
        frames, end = decoder.raw_decode(html[frames_start:])
        frames_bytes = end  # length of the serialized frames JSON in the file
    return data, frames, frames_bytes


def _trace_name(trace, idx):
    return trace.get('name') or '(unnamed trace %d)' % idx


def report(path):
    size = os.path.getsize(path)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    data, frames, frames_bytes = extract_figure_and_frames(html)

    print('=' * 70)
    print(path)
    print('-' * 70)
    print('Total file size:        %.2f MB' % (size / 1e6))
    print('Figure traces:          %d' % len(data))
    print('Frames:                 %d' % len(frames))
    if frames:
        per_frame_traces = [len(fr.get('data', [])) for fr in frames]
        print('Traces per frame:       %d (min) / %d (max)'
              % (min(per_frame_traces), max(per_frame_traces)))
        print('Frames payload (JSON):  %.2f MB (%.1f%% of file)'
              % (frames_bytes / 1e6, 100.0 * frames_bytes / size))
        print('Average per frame:      %.1f KB' % (frames_bytes / len(frames) / 1e3))

        # Which figure traces are carried in frames (by the traces index list)?
        carried = set()
        for fr in frames:
            for t in fr.get('traces', []):
                carried.add(t)
        names_carried = [_trace_name(data[t], t) for t in sorted(carried)
                         if t < len(data)]
        print('Traces carried in frames (%d): %s'
              % (len(names_carried), ', '.join(names_carried[:12])
                 + (' ...' if len(names_carried) > 12 else '')))

        # Largest per-frame traces by serialized size (first frame as sample)
        sample = frames[0].get('data', [])
        sized = sorted(((len(json.dumps(tr)), k) for k, tr in enumerate(sample)),
                       reverse=True)[:5]
        print('Largest traces inside frame 0:')
        for nbytes, k in sized:
            tlist = frames[0].get('traces', [])
            abs_idx = tlist[k] if k < len(tlist) else None
            nm = (_trace_name(data[abs_idx], abs_idx)
                  if abs_idx is not None and abs_idx < len(data)
                  else '(frame slot %d)' % k)
            print('    %8.1f KB  %s' % (nbytes / 1e3, nm))
    else:
        print('No frames found (static plot?)')
    print()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    for p in sys.argv[1:]:
        report(p)
