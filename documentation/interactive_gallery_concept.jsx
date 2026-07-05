import { useState } from "react";
import { ChevronRight, ArrowLeft, Play, Pause, RotateCcw, Maximize2, Info, Star, Sun, Globe2, Orbit } from "lucide-react";

const PALETTE = {
  void: "#060a12",
  deep: "#0c1220",
  panel: "#111827",
  surface: "#1a2236",
  border: "#2a3452",
  accent: "#6d8cff",
  warm: "#e8a44a",
  text: "#c8cdd8",
  bright: "#eef0f5",
  subtle: "#6b7394",
  success: "#4ade80",
};

const CURATED_CARDS = [
  { id: 1, title: "Halley's Comet Perihelion", subtitle: "1986 close approach", type: "curated", category: "Comets", color: "#4fc3f7" },
  { id: 2, title: "Apophis Close Approach", subtitle: "2029 Earth flyby", type: "curated", category: "Close Approach", color: "#ef5350" },
  { id: 3, title: "Voyager Grand Tour", subtitle: "Jupiter to interstellar", type: "curated", category: "Spacecraft", color: "#ab47bc" },
];

const INTERACTIVE_CARDS = [
  { id: 10, title: "Solar System Explorer", subtitle: "Choose planets, dates, center body", type: "interactive", icon: Sun, color: PALETTE.warm, controls: ["planets", "center", "dates"] },
  { id: 11, title: "Orbital Mechanics Lab", subtitle: "Eccentricity, inclination, periods", type: "interactive", icon: Orbit, color: PALETTE.accent, controls: ["eccentricity", "params"] },
  { id: 12, title: "Stellar Neighborhood", subtitle: "Stars within 100 light-years", type: "interactive", icon: Star, color: "#ffd54f", controls: ["distance", "magnitude"] },
];

const PLANETS = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
const PLANET_COLORS = { Mercury: "#b0b0b0", Venus: "#e8c86a", Earth: "#4a90d9", Mars: "#c1440e", Jupiter: "#c88b3a", Saturn: "#e8d08a", Uranus: "#7cc7c7", Neptune: "#4466cc" };

function GalleryCard({ card, onClick }) {
  const isInteractive = card.type === "interactive";
  const Icon = card.icon;
  return (
    <button onClick={onClick} style={{
      background: PALETTE.surface, border: `1px solid ${PALETTE.border}`,
      borderRadius: 12, padding: 0, cursor: "pointer", textAlign: "left",
      overflow: "hidden", transition: "all 0.25s ease", width: "100%",
      position: "relative",
    }}
    onMouseEnter={e => { e.currentTarget.style.borderColor = card.color; e.currentTarget.style.transform = "translateY(-2px)"; }}
    onMouseLeave={e => { e.currentTarget.style.borderColor = PALETTE.border; e.currentTarget.style.transform = "translateY(0)"; }}
    >
      <div style={{ height: 120, background: `linear-gradient(135deg, ${PALETTE.deep} 0%, ${card.color}22 100%)`,
        display: "flex", alignItems: "center", justifyContent: "center", position: "relative" }}>
        {isInteractive ? (
          <Icon size={40} color={card.color} strokeWidth={1.2} />
        ) : (
          <div style={{ width: 80, height: 80, borderRadius: "50%",
            background: `radial-gradient(circle at 35% 35%, ${card.color}44, ${card.color}11)`,
            border: `1px solid ${card.color}33` }} />
        )}
        {isInteractive && (
          <div style={{ position: "absolute", top: 10, right: 10, background: PALETTE.accent + "22",
            border: `1px solid ${PALETTE.accent}44`, borderRadius: 20, padding: "3px 10px",
            fontSize: 11, color: PALETTE.accent, fontWeight: 500, letterSpacing: 0.5 }}>
            INTERACTIVE
          </div>
        )}
        {!isInteractive && (
          <div style={{ position: "absolute", top: 10, right: 10, background: PALETTE.surface + "cc",
            borderRadius: 20, padding: "3px 10px",
            fontSize: 11, color: PALETTE.subtle, fontWeight: 500 }}>
            {card.category}
          </div>
        )}
      </div>
      <div style={{ padding: "14px 16px 16px" }}>
        <div style={{ color: PALETTE.bright, fontSize: 15, fontWeight: 600, marginBottom: 4 }}>{card.title}</div>
        <div style={{ color: PALETTE.subtle, fontSize: 13 }}>{card.subtitle}</div>
        {isInteractive && (
          <div style={{ display: "flex", alignItems: "center", gap: 6, marginTop: 12,
            color: card.color, fontSize: 13, fontWeight: 500 }}>
            Explore <ChevronRight size={14} />
          </div>
        )}
      </div>
    </button>
  );
}

function ExhibitView({ card, onBack }) {
  const [selectedPlanets, setSelectedPlanets] = useState(["Earth", "Mars", "Jupiter"]);
  const [center, setCenter] = useState("Sun");
  const [year, setYear] = useState(2026);
  const [showInfo, setShowInfo] = useState(false);
  const [loading, setLoading] = useState(false);

  const togglePlanet = (p) => {
    setSelectedPlanets(prev => prev.includes(p) ? prev.filter(x => x !== p) : [...prev, p]);
    setLoading(true);
    setTimeout(() => setLoading(false), 800);
  };

  return (
    <div style={{ minHeight: "100vh", background: PALETTE.void }}>
      {/* Top bar */}
      <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between",
        padding: "12px 20px", background: PALETTE.deep, borderBottom: `1px solid ${PALETTE.border}` }}>
        <button onClick={onBack} style={{ display: "flex", alignItems: "center", gap: 8,
          background: "none", border: "none", color: PALETTE.text, cursor: "pointer", fontSize: 14 }}>
          <ArrowLeft size={16} /> Gallery
        </button>
        <div style={{ fontSize: 15, fontWeight: 600, color: PALETTE.bright }}>{card.title}</div>
        <button onClick={() => setShowInfo(!showInfo)} style={{ background: showInfo ? PALETTE.accent + "22" : "none",
          border: `1px solid ${showInfo ? PALETTE.accent : PALETTE.border}`, borderRadius: 8,
          padding: "6px 8px", cursor: "pointer", color: showInfo ? PALETTE.accent : PALETTE.subtle }}>
          <Info size={16} />
        </button>
      </div>

      <div style={{ display: "flex", flexDirection: "column", height: "calc(100vh - 49px)" }}>
        {/* Visualization area */}
        <div style={{ flex: 1, position: "relative", overflow: "hidden",
          background: `radial-gradient(ellipse at 50% 50%, ${PALETTE.deep} 0%, ${PALETTE.void} 70%)` }}>
          {/* Grid lines to suggest 3D space */}
          <svg width="100%" height="100%" style={{ position: "absolute", top: 0, left: 0, opacity: 0.15 }}>
            {Array.from({ length: 12 }).map((_, i) => (
              <line key={`h${i}`} x1="0" y1={`${(i + 1) * 8.33}%`} x2="100%" y2={`${(i + 1) * 8.33}%`}
                stroke={PALETTE.accent} strokeWidth="0.5" />
            ))}
            {Array.from({ length: 16 }).map((_, i) => (
              <line key={`v${i}`} x1={`${(i + 1) * 6.25}%`} y1="0" x2={`${(i + 1) * 6.25}%`} y2="100%"
                stroke={PALETTE.accent} strokeWidth="0.5" />
            ))}
          </svg>

          {/* Mock orbits */}
          <div style={{ position: "absolute", top: "50%", left: "50%", transform: "translate(-50%, -50%)" }}>
            {/* Sun */}
            <div style={{ position: "absolute", width: 16, height: 16, borderRadius: "50%",
              background: PALETTE.warm, boxShadow: `0 0 20px ${PALETTE.warm}88`,
              top: -8, left: -8 }} />
            {selectedPlanets.map((p, i) => {
              const r = 50 + i * 45;
              const angle = (Date.now() / 1000 + i * 2.1) % (Math.PI * 2);
              return (
                <g key={p}>
                  <div style={{ position: "absolute", width: r * 2, height: r * 2,
                    border: `1px solid ${PLANET_COLORS[p]}33`, borderRadius: "50%",
                    top: -r, left: -r }} />
                  <div style={{ position: "absolute",
                    width: p === "Jupiter" ? 12 : p === "Saturn" ? 10 : 7,
                    height: p === "Jupiter" ? 12 : p === "Saturn" ? 10 : 7,
                    borderRadius: "50%", background: PLANET_COLORS[p],
                    boxShadow: `0 0 8px ${PLANET_COLORS[p]}66`,
                    top: Math.sin(angle + i * 1.3) * r - 4,
                    left: Math.cos(angle + i * 1.3) * r - 4,
                    transition: "all 0.3s ease" }}>
                    <div style={{ position: "absolute", top: -18, left: "50%", transform: "translateX(-50%)",
                      fontSize: 10, color: PLANET_COLORS[p], whiteSpace: "nowrap", fontWeight: 500 }}>{p}</div>
                  </div>
                </g>
              );
            })}
          </div>

          {/* Loading indicator */}
          {loading && (
            <div style={{ position: "absolute", top: 12, left: "50%", transform: "translateX(-50%)",
              background: PALETTE.panel + "ee", border: `1px solid ${PALETTE.border}`,
              borderRadius: 8, padding: "6px 16px", fontSize: 12, color: PALETTE.accent }}>
              Assembling scene...
            </div>
          )}

          {/* Info panel */}
          {showInfo && (
            <div style={{ position: "absolute", top: 12, right: 12, width: 240,
              background: PALETTE.panel + "f0", border: `1px solid ${PALETTE.border}`,
              borderRadius: 12, padding: 16, backdropFilter: "blur(8px)" }}>
              <div style={{ fontSize: 14, fontWeight: 600, color: PALETTE.bright, marginBottom: 8 }}>
                About This Exhibit
              </div>
              <div style={{ fontSize: 12, color: PALETTE.text, lineHeight: 1.6 }}>
                Explore the solar system with real orbital data from JPL Horizons.
                Select planets, choose a center body, and set a date to see
                accurate positions. All data is pre-cached — no live queries.
              </div>
              <div style={{ marginTop: 12, fontSize: 11, color: PALETTE.subtle }}>
                Data: JPL Horizons via astroquery
              </div>
            </div>
          )}

          {/* Toolbar */}
          <div style={{ position: "absolute", bottom: 12, right: 12, display: "flex", gap: 6 }}>
            {[RotateCcw, Maximize2].map((Icon, i) => (
              <button key={i} style={{ background: PALETTE.panel + "cc", border: `1px solid ${PALETTE.border}`,
                borderRadius: 8, padding: 8, cursor: "pointer", color: PALETTE.subtle }}>
                <Icon size={16} />
              </button>
            ))}
          </div>
        </div>

        {/* Control panel */}
        <div style={{ background: PALETTE.panel, borderTop: `1px solid ${PALETTE.border}`,
          padding: "14px 20px" }}>
          {/* Planet toggles */}
          <div style={{ marginBottom: 12 }}>
            <div style={{ fontSize: 11, color: PALETTE.subtle, fontWeight: 600, letterSpacing: 1,
              marginBottom: 8, textTransform: "uppercase" }}>Objects</div>
            <div style={{ display: "flex", flexWrap: "wrap", gap: 6 }}>
              {PLANETS.map(p => {
                const active = selectedPlanets.includes(p);
                return (
                  <button key={p} onClick={() => togglePlanet(p)} style={{
                    background: active ? PLANET_COLORS[p] + "22" : PALETTE.surface,
                    border: `1px solid ${active ? PLANET_COLORS[p] : PALETTE.border}`,
                    borderRadius: 20, padding: "5px 12px", cursor: "pointer",
                    color: active ? PLANET_COLORS[p] : PALETTE.subtle,
                    fontSize: 12, fontWeight: active ? 600 : 400,
                    transition: "all 0.15s ease",
                  }}>{p}</button>
                );
              })}
            </div>
          </div>

          {/* Center + Date row */}
          <div style={{ display: "flex", gap: 16, alignItems: "flex-end" }}>
            <div style={{ flex: 1 }}>
              <div style={{ fontSize: 11, color: PALETTE.subtle, fontWeight: 600, letterSpacing: 1,
                marginBottom: 6, textTransform: "uppercase" }}>Center</div>
              <div style={{ display: "flex", gap: 6 }}>
                {["Sun", "Earth", "Mars"].map(c => (
                  <button key={c} onClick={() => { setCenter(c); setLoading(true); setTimeout(() => setLoading(false), 600); }}
                    style={{ background: center === c ? PALETTE.accent + "22" : PALETTE.surface,
                      border: `1px solid ${center === c ? PALETTE.accent : PALETTE.border}`,
                      borderRadius: 8, padding: "5px 12px", cursor: "pointer",
                      color: center === c ? PALETTE.accent : PALETTE.subtle,
                      fontSize: 12, fontWeight: center === c ? 600 : 400 }}>{c}</button>
                ))}
              </div>
            </div>
            <div style={{ flex: 1 }}>
              <div style={{ fontSize: 11, color: PALETTE.subtle, fontWeight: 600, letterSpacing: 1,
                marginBottom: 6, textTransform: "uppercase" }}>Epoch</div>
              <input type="range" min={2000} max={2040} value={year}
                onChange={e => { setYear(+e.target.value); setLoading(true); setTimeout(() => setLoading(false), 500); }}
                style={{ width: "100%", accentColor: PALETTE.accent }} />
              <div style={{ fontSize: 12, color: PALETTE.bright, textAlign: "center", marginTop: 2 }}>
                {year}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default function InteractiveGalleryConcept() {
  const [view, setView] = useState("gallery");
  const [selectedCard, setSelectedCard] = useState(null);

  if (view === "exhibit" && selectedCard) {
    return <ExhibitView card={selectedCard} onBack={() => { setView("gallery"); setSelectedCard(null); }} />;
  }

  return (
    <div style={{ minHeight: "100vh", background: PALETTE.void, color: PALETTE.text,
      fontFamily: "'Inter', system-ui, -apple-system, sans-serif" }}>

      {/* Hero */}
      <div style={{ padding: "48px 24px 40px", textAlign: "center",
        background: `linear-gradient(180deg, ${PALETTE.deep} 0%, ${PALETTE.void} 100%)` }}>
        <div style={{ fontSize: 11, color: PALETTE.accent, fontWeight: 600, letterSpacing: 2,
          textTransform: "uppercase", marginBottom: 12 }}>Paloma's Orrery</div>
        <h1 style={{ fontSize: 28, fontWeight: 700, color: PALETTE.bright, margin: "0 0 12px",
          lineHeight: 1.2 }}>Interactive Gallery</h1>
        <p style={{ fontSize: 14, color: PALETTE.subtle, maxWidth: 420, margin: "0 auto", lineHeight: 1.6 }}>
          Explore the solar system, stars, and Earth's climate with real scientific data.
          View curated exhibits or dive into hands-on interactive exploration.
        </p>
      </div>

      {/* Narrative banner */}
      <div style={{ margin: "0 20px 32px", padding: "16px 20px",
        background: `linear-gradient(135deg, ${PALETTE.warm}11, ${PALETTE.accent}08)`,
        border: `1px solid ${PALETTE.warm}22`, borderRadius: 12 }}>
        <div style={{ fontSize: 13, color: PALETTE.warm, fontWeight: 600, marginBottom: 4 }}>
          The Orrery as Museum
        </div>
        <div style={{ fontSize: 13, color: PALETTE.text, lineHeight: 1.6 }}>
          Like a science museum exhibit, the gallery invites you to explore at your own pace.
          Pre-curated scenes are the permanent collection — beautiful, ready to view.
          Interactive exhibits let you change what's plotted and discover for yourself.
        </div>
      </div>

      {/* Curated Collection */}
      <div style={{ padding: "0 20px 32px" }}>
        <div style={{ display: "flex", alignItems: "baseline", justifyContent: "space-between", marginBottom: 16 }}>
          <h2 style={{ fontSize: 16, fontWeight: 600, color: PALETTE.bright, margin: 0 }}>
            Curated Collection
          </h2>
          <span style={{ fontSize: 12, color: PALETTE.subtle }}>Pre-rendered • Instant load</span>
        </div>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(200px, 1fr))", gap: 12 }}>
          {CURATED_CARDS.map(card => (
            <GalleryCard key={card.id} card={card} onClick={() => {}} />
          ))}
        </div>
      </div>

      {/* Interactive Exhibits */}
      <div style={{ padding: "0 20px 48px" }}>
        <div style={{ display: "flex", alignItems: "baseline", justifyContent: "space-between", marginBottom: 6 }}>
          <h2 style={{ fontSize: 16, fontWeight: 600, color: PALETTE.bright, margin: 0 }}>
            Interactive Exhibits
          </h2>
          <span style={{ fontSize: 12, color: PALETTE.accent }}>Powered by Pyodide</span>
        </div>
        <p style={{ fontSize: 12, color: PALETTE.subtle, margin: "0 0 16px", lineHeight: 1.5 }}>
          Choose parameters and see the results in real time. First visit loads the computation engine (~10s).
        </p>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(200px, 1fr))", gap: 12 }}>
          {INTERACTIVE_CARDS.map(card => (
            <GalleryCard key={card.id} card={card} onClick={() => { setSelectedCard(card); setView("exhibit"); }} />
          ))}
        </div>
      </div>

      {/* Footer */}
      <div style={{ padding: "20px 20px 32px", borderTop: `1px solid ${PALETTE.border}`,
        textAlign: "center" }}>
        <div style={{ fontSize: 12, color: PALETTE.subtle, lineHeight: 1.8 }}>
          Data: JPL Horizons • ESA Gaia • Copernicus CDS • NOAA
        </div>
        <div style={{ fontSize: 11, color: PALETTE.subtle + "88", marginTop: 4 }}>
          Paloma's Orrery © 2025-2026 Tony Quintanilla
        </div>
      </div>

      {/* Inspirations bar */}
      <div style={{ padding: "16px 20px 24px", background: PALETTE.deep }}>
        <div style={{ fontSize: 11, color: PALETTE.subtle, fontWeight: 600, letterSpacing: 1,
          textTransform: "uppercase", marginBottom: 10 }}>Design Inspirations</div>
        <div style={{ display: "flex", flexWrap: "wrap", gap: 8 }}>
          {[
            { name: "NASA Eyes", note: "3D solar system, real data, browser-native" },
            { name: "Exploratorium", note: "\"You play with exhibits, not look at them\"" },
            { name: "teamLab", note: "Art + science + immersion" },
            { name: "ViewSpace", note: "STScI interactive astronomy" },
          ].map(ref => (
            <div key={ref.name} style={{ background: PALETTE.surface, border: `1px solid ${PALETTE.border}`,
              borderRadius: 8, padding: "8px 12px", flex: "1 1 160px" }}>
              <div style={{ fontSize: 12, color: PALETTE.bright, fontWeight: 600 }}>{ref.name}</div>
              <div style={{ fontSize: 11, color: PALETTE.subtle, marginTop: 2 }}>{ref.note}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
