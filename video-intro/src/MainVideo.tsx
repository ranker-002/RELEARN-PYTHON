import { useCurrentFrame, useVideoConfig, AbsoluteFill, interpolate, spring, Easing } from "remotion";

const COLORS = {
  bg: "#000000",
  text: "#ffffff",
  muted: "#6b7280",
  primary: "#0ea5e9",
  secondary: "#8b5cf6",
  accent: "#f43f5e",
  success: "#22c55e",
  codeBg: "#0a0a0a",
  codeBorder: "#1a1a1a",
};

const easeOutExpo = Easing.bezier(0, 0, 0, 1);
const easeOutQuart = Easing.bezier(0.165, 0.84, 0.44, 1);
const easeInOutExpo = Easing.bezier(0.16, 1, 0.3, 1);

const formatNumber = (num: number) => new Intl.NumberFormat("en-US").format(num);

const SectionContainer: React.FC<{
  children: React.ReactNode;
  frame: number;
  start: number;
  end: number;
  fadeThroughBlack?: boolean;
}> = ({ children, frame, start, end, fadeThroughBlack = false }) => {
  const progress = Math.max(0, Math.min(1, (frame - start) / 60));
  const fadeOutStart = end - 60;
  const fadeOutProgress = Math.max(0, Math.min(1, (frame - fadeOutStart) / 60));

  const opacity = fadeThroughBlack
    ? progress > 0 && progress < 0.1
      ? (progress - 0) / 0.1
      : fadeOutProgress > 0 && fadeOutProgress < 0.1
      ? 1 - fadeOutProgress / 0.1
      : progress >= 0.1 && fadeOutProgress <= 0.9
      ? 1
      : 0
    : interpolate(progress, [0, 0.1], [0, 1], { easing: easeOutExpo }) *
      (1 - interpolate(fadeOutProgress, [0, 0.1], [0, 1], { easing: easeOutExpo }));

  const scale = 1 - fadeOutProgress * 0.02;

  return (
    <AbsoluteFill style={{ opacity, transform: `scale(${scale})` }}>
      {children}
    </AbsoluteFill>
  );
};

const CodeBlock: React.FC<{ lines: string[]; highlightLines?: number[] }> = ({ lines, highlightLines = [] }) => (
  <div
    style={{
      background: COLORS.codeBg,
      border: `1px solid ${COLORS.codeBorder}`,
      borderRadius: 12,
      overflow: "hidden",
      fontFamily: "SF Mono, Menlo, Monaco, monospace",
      fontSize: 13,
      lineHeight: 1.6,
    }}
  >
    <div
      style={{
        background: "#0d0d0d",
        padding: "8px 12px",
        display: "flex",
        alignItems: "center",
        gap: 8,
        borderBottom: `1px solid ${COLORS.codeBorder}`,
      }}
    >
      <div style={{ display: "flex", gap: 6 }}>
        {["#ff5f57", "#febc2e", "#28c840"].map((color, i) => (
          <div key={i} style={{ width: 10, height: 10, borderRadius: "50%", background: color }} />
        ))}
      </div>
    </div>
    <div style={{ padding: 16 }}>
      {lines.map((line, i) => {
        const isHighlighted = highlightLines.includes(i);
        return (
          <div
            key={i}
            style={{
              padding: "2px 8px",
              margin: "0 -8px",
              background: isHighlighted ? "rgba(14, 165, 233, 0.15)" : "transparent",
              borderRadius: 4,
              color: isHighlighted ? COLORS.text : COLORS.muted,
            }}
          >
            <span style={{ color: COLORS.secondary, userSelect: "none", marginRight: 8 }}>{(i + 1).toString().padStart(2, "0")}</span>
            {line}
          </div>
        );
      })}
    </div>
  </div>
);

const BigStat: React.FC<{ number: string; label: string; frame: number; delay: number }> = ({ number, label, frame, delay }) => {
  const progress = Math.max(0, Math.min(1, (frame - delay) / 40));
  const animatedNumber = interpolate(progress, [0, 1], [0, parseInt(number.replace(/,/g, ""))]);
  const displayNumber = formatNumber(Math.round(animatedNumber));

  return (
    <div style={{ textAlign: "center" }}>
      <div style={{ fontSize: 56, fontWeight: 700, color: COLORS.text, letterSpacing: "-0.03em" }}>{number.includes(",") ? displayNumber : number}</div>
      <div style={{ fontSize: 14, color: COLORS.muted, marginTop: 4 }}>{label}</div>
    </div>
  );
};

const ModuleBar: React.FC<{
  name: string;
  chapters: string;
  progress: number;
  index: number;
  total: number;
  frame: number;
  accentColor: string;
}> = ({ name, chapters, progress, index, total, frame, accentColor }) => {
  const delay = 20 + index * 12;
  const itemProgress = Math.max(0, Math.min(1, (frame - delay) / 25));
  const opacity = interpolate(itemProgress, [0, 0.2], [0, 1]);
  const x = interpolate(itemProgress, [0, 1], [30, 0]);
  const barWidth = interpolate(itemProgress, [0, 0.6, 1], [0, 0, progress]);

  return (
    <div style={{ display: "flex", alignItems: "center", gap: 20, opacity, transform: `translateX(${x}px)`, marginBottom: index < total - 1 ? 12 : 0 }}>
      <div style={{ width: 48, height: 48, borderRadius: 10, background: accentColor, display: "flex", alignItems: "center", justifyContent: "center", flexShrink: 0 }}>
        <span style={{ fontSize: 20 }}>{(index + 1).toString().padStart(2, "0")}</span>
      </div>
      <div style={{ flex: 1 }}>
        <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 8 }}>
          <span style={{ fontSize: 18, fontWeight: 500, color: COLORS.text }}>{name}</span>
          <span style={{ fontSize: 14, color: COLORS.muted }}>{chapters}</span>
        </div>
        <div style={{ height: 4, background: "rgba(255,255,255,0.1)", borderRadius: 2, overflow: "hidden" }}>
          <div style={{ width: `${barWidth}%`, height: "100%", background: accentColor, borderRadius: 2 }} />
        </div>
      </div>
    </div>
  );
};

const ProjectCard: React.FC<{
  name: string;
  category: string;
  difficulty: string;
  icon: string;
  color: string;
  frame: number;
  delay: number;
}> = ({ name, category, difficulty, icon, color, frame, delay }) => {
  const progress = Math.max(0, Math.min(1, (frame - delay) / 30));
  const opacity = interpolate(progress, [0, 0.2], [0, 1]);
  const y = interpolate(progress, [0, 1], [15, 0]);

  return (
    <div style={{ opacity, transform: `translateY(${y}px)` }}>
      <div
        style={{
          background: "rgba(255, 255, 255, 0.02)",
          border: "1px solid rgba(255, 255, 255, 0.06)",
          borderRadius: 16,
          padding: 20,
        }}
      >
        <div style={{ display: "flex", alignItems: "center", gap: 14 }}>
          <div style={{ width: 44, height: 44, borderRadius: 10, background: "rgba(255, 255, 255, 0.04)", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 22 }}>{icon}</div>
          <div>
            <div style={{ fontSize: 16, fontWeight: 500, color: COLORS.text }}>{name}</div>
            <div style={{ fontSize: 12, color: COLORS.muted, marginTop: 2 }}>{category}</div>
          </div>
        </div>
        <div style={{ marginTop: 16, display: "flex", alignItems: "center", gap: 10 }}>
          <div style={{ flex: 1, height: 3, background: "rgba(255,255,255,0.05)", borderRadius: 2 }}>
            <div
              style={{
                width: `${difficulty === "Débutant" ? 25 : difficulty === "Intermédiaire" ? 50 : difficulty === "Avancé" ? 75 : 100}%`,
                height: "100%",
                background: color,
                borderRadius: 2,
              }}
            />
          </div>
          <span style={{ fontSize: 11, fontWeight: 500, color: color, minWidth: 65 }}>{difficulty}</span>
        </div>
      </div>
    </div>
  );
};

export const MainVideo: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  return (
    <AbsoluteFill style={{ backgroundColor: COLORS.bg }}>
      <IntroSection frame={frame} fps={fps} />
      <InstallSection frame={frame} fps={fps} />
      <StructureSection frame={frame} fps={fps} />
      <ModulesSection frame={frame} fps={fps} />
      <ProjectsSection frame={frame} fps={fps} />
      <UsageSection frame={frame} fps={fps} />
      <FinalSection frame={frame} fps={fps} />
    </AbsoluteFill>
  );
};

const IntroSection: React.FC<{ frame: number; fps: number }> = ({ frame, fps }) => {
  const titleProgress = Math.min(1, frame / 50);
  const codeProgress = Math.max(0, Math.min(1, (frame - 40) / 40));

  const titleScale = 0.95 + 0.05 * interpolate(titleProgress, [0, 1], [0, 1], { easing: easeOutQuart });
  const titleOpacity = interpolate(titleProgress, [0, 0.15], [0, 1]);
  const codeY = interpolate(codeProgress, [0, 1], [40, 0]);
  const codeOpacity = interpolate(codeProgress, [0, 0.2, 0.9, 1], [0, 0, 1, 0]);

  if (frame > 180) return null;

  return (
    <AbsoluteFill style={{ padding: "10% 8%", display: "flex", flexDirection: "column", alignItems: "center" }}>
      <div style={{ transform: `scale(${titleScale})`, opacity: titleOpacity, textAlign: "center" }}>
        <div style={{ display: "flex", alignItems: "center", justifyContent: "center", gap: 28, marginBottom: 32 }}>
          <div style={{ width: 80, height: 80, borderRadius: 20, background: "linear-gradient(135deg, #3776ab, #ffd43b)", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 38 }}>
            🐍
          </div>
          <div style={{ textAlign: "left" }}>
            <div style={{ fontSize: 56, fontWeight: 700, color: COLORS.text, letterSpacing: "-0.025em", lineHeight: 1 }}>Python</div>
            <div style={{ fontSize: 36, fontWeight: 500, background: "linear-gradient(90deg, #0ea5e9, #8b5cf6)", WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent", letterSpacing: "-0.02em" }}>Mastery</div>
          </div>
        </div>

        <div style={{ fontSize: 22, color: COLORS.muted, fontWeight: 400 }}>De Débutant à Expert en Intelligence Artificielle</div>
      </div>

      <div style={{ marginTop: 60, opacity: codeOpacity, transform: `translateY(${codeY}px)` }}>
        <CodeBlock
          lines={[
            "git clone https://github.com/ranker/RELEARN-PYTHON.git",
            "cd RELEARN-PYTHON",
            "./install.sh",
          ]}
          highlightLines={[0, 1, 2]}
        />
      </div>

      <div style={{ position: "absolute", bottom: 60, opacity: codeOpacity, fontSize: 14, color: COLORS.muted }}>
        Créé par <span style={{ color: COLORS.text }}>Ranker</span>
      </div>
    </AbsoluteFill>
  );
};

const InstallSection: React.FC<{ frame: number; fps: number }> = ({ frame, fps }) => {
  if (frame < 180 || frame > 360) return null;

  const steps = [
    { num: "01", title: "Cloner le repository", code: "git clone https://github.com/ranker/RELEARN-PYTHON.git" },
    { num: "02", title: "Installer uv", code: "curl -LsSf https://astral.sh/uv/install.sh | sh" },
    { num: "03", title: "Exécuter l'installateur", code: "./install.sh" },
    { num: "04", title: "Commencer à apprendre", code: "cd MODULES/01_core_fondations/01_premiers_pas/" },
  ];

  return (
    <SectionContainer frame={frame} start={180} end={360} fadeThroughBlack>
      <AbsoluteFill style={{ padding: "8% 10%", display: "flex", flexDirection: "column", alignItems: "center" }}>
        <div style={{ fontSize: 32, fontWeight: 600, color: COLORS.text, marginBottom: 60, letterSpacing: "-0.025em" }}>Installation</div>

        <div style={{ display: "grid", gridTemplateColumns: "repeat(2, 1fr)", gap: 16, width: "100%", maxWidth: 900 }}>
          {steps.map((step, i) => {
            const progress = Math.max(0, Math.min(1, (frame - 200 - i * 20) / 30));
            return (
              <div key={i} style={{ opacity: progress, transform: `translateY(${interpolate(progress, [0, 1], [20, 0])})` }}>
                <div style={{ background: "rgba(255, 255, 255, 0.02)", border: "1px solid rgba(255, 255, 255, 0.06)", borderRadius: 16, padding: 24, height: "100%" }}>
                  <div style={{ display: "flex", alignItems: "center", gap: 14, marginBottom: 16 }}>
                    <div style={{ width: 40, height: 40, borderRadius: 10, background: "linear-gradient(135deg, #0ea5e9, #8b5cf6)", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 14, fontWeight: 600, color: "#000" }}>{step.num}</div>
                    <span style={{ fontSize: 18, fontWeight: 500, color: COLORS.text }}>{step.title}</span>
                  </div>
                  <div style={{ fontFamily: "SF Mono, Menlo, Monaco, monospace", fontSize: 12, background: "rgba(0, 0, 0, 0.4)", borderRadius: 8, padding: "12px 16px", color: COLORS.success }}>{step.code}</div>
                </div>
              </div>
            );
          })}
        </div>

        <div style={{ marginTop: 48, fontSize: 14, color: COLORS.muted, background: "rgba(255, 255, 255, 0.02)", borderRadius: 8, padding: "12px 24px" }}>
          <span style={{ color: COLORS.primary }}>uv sync</span> --extra [core | web | automation | data | ai]
        </div>
      </AbsoluteFill>
    </SectionContainer>
  );
};

const StructureSection: React.FC<{ frame: number; fps: number }> = ({ frame, fps }) => {
  if (frame < 360 || frame > 480) return null;

  const structures = [
    { name: "MODULES/", desc: "26 chapitres progressifs", icon: "📚", items: ["01_core_fondations", "02_fonctions_poo", "03_robustesse_fichiers", "04_concepts_avances", "05_domaines_specifies"] },
    { name: "PROJETS/", desc: "14 projets concrets", icon: "🛠️", items: ["core_fondations", "data_science", "machine_learning", "web_scraping", "deep_learning"] },
    { name: "relearn_python", desc: "package utilitaire", icon: "📦", items: ["__init__.py", "utils.py", "validators.py"] },
  ];

  return (
    <SectionContainer frame={frame} start={360} end={480} fadeThroughBlack>
      <AbsoluteFill style={{ padding: "8% 10%", display: "flex", flexDirection: "column", alignItems: "center" }}>
        <div style={{ fontSize: 32, fontWeight: 600, color: COLORS.text, marginBottom: 60, letterSpacing: "-0.025em" }}>Structure du projet</div>

        <div style={{ display: "flex", gap: 20, width: "100%", maxWidth: 1000 }}>
          {structures.map((s, i) => {
            const progress = Math.max(0, Math.min(1, (frame - 380 - i * 25) / 35));
            return (
              <div key={i} style={{ flex: 1, opacity: progress, transform: `translateY(${interpolate(progress, [0, 1], [30, 0])})` }}>
                <div style={{ background: "rgba(255, 255, 255, 0.02)", border: "1px solid rgba(255, 255, 255, 0.06)", borderRadius: 16, padding: 24, height: "100%" }}>
                  <div style={{ display: "flex", alignItems: "center", gap: 14, marginBottom: 20 }}>
                    <div style={{ width: 44, height: 44, borderRadius: 10, background: "linear-gradient(135deg, rgba(14, 165, 233, 0.2), rgba(139, 92, 246, 0.2))", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 22 }}>{s.icon}</div>
                    <div>
                      <div style={{ fontSize: 18, fontWeight: 600, color: COLORS.text }}>{s.name}</div>
                      <div style={{ fontSize: 13, color: COLORS.muted, marginTop: 2 }}>{s.desc}</div>
                    </div>
                  </div>
                  <div style={{ fontFamily: "SF Mono, Menlo, Monaco, monospace", fontSize: 11, background: "rgba(0, 0, 0, 0.3)", borderRadius: 8, padding: 14, color: COLORS.muted }}>
                    {s.items.map((item, j) => (
                      <div key={j} style={{ padding: "3px 0" }}>{item}</div>
                    ))}
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </AbsoluteFill>
    </SectionContainer>
  );
};

const ModulesSection: React.FC<{ frame: number; fps: number }> = ({ frame, fps }) => {
  if (frame < 480 || frame > 600) return null;

  const modules = [
    { name: "Fondations Core", chapters: "7 chapitres • Variables, boucles, fonctions", color: "#0ea5e9" },
    { name: "Fonctions & POO", chapters: "6 chapitres • Classes, héritage, polymorphisme", color: "#8b5cf6" },
    { name: "Robustesse & Fichiers", chapters: "3 chapitres • Exceptions, I/O, sérialisation", color: "#22c55e" },
    { name: "Concepts Avancés", chapters: "3 chapitres • Décorateurs, async, type hints", color: "#f43f5e" },
    { name: "Domaines Spécialisés", chapters: "7 chapitres • ML, DL, web, automation", color: "#f59e0b" },
  ];

  return (
    <SectionContainer frame={frame} start={480} end={600} fadeThroughBlack>
      <AbsoluteFill style={{ padding: "8% 10%", display: "flex", flexDirection: "column", alignItems: "center" }}>
        <div style={{ fontSize: 32, fontWeight: 600, color: COLORS.text, marginBottom: 60, letterSpacing: "-0.025em" }}>Un parcours complet</div>

        <div style={{ width: "100%", maxWidth: 700 }}>
          {modules.map((m, i) => (
            <ModuleBar key={i} name={m.name} chapters={m.chapters} progress={100 - i * 18} index={i} total={modules.length} frame={frame} accentColor={m.color} />
          ))}
        </div>
      </AbsoluteFill>
    </SectionContainer>
  );
};

const ProjectsSection: React.FC<{ frame: number; fps: number }> = ({ frame, fps }) => {
  if (frame < 600 || frame > 720) return null;

  const projects = [
    { name: "CLI Calculator", category: "Core", difficulty: "Débutant", icon: "🔢", color: COLORS.success },
    { name: "Task Manager", category: "Core", difficulty: "Intermédiaire", icon: "📋", color: "#f59e0b" },
    { name: "Banking System", category: "POO", difficulty: "Intermédiaire", icon: "🏦", color: "#f59e0b" },
    { name: "Web Scraper", category: "Automation", difficulty: "Avancé", icon: "🕸️", color: COLORS.accent },
    { name: "ML Predictor", category: "Machine Learning", difficulty: "Expert", icon: "🤖", color: "#ef4444" },
    { name: "Image Classifier", category: "Deep Learning", difficulty: "Expert", icon: "🧠", color: "#ef4444" },
  ];

  return (
    <SectionContainer frame={frame} start={600} end={720} fadeThroughBlack>
      <AbsoluteFill style={{ padding: "8% 10%", display: "flex", flexDirection: "column", alignItems: "center" }}>
        <div style={{ fontSize: 32, fontWeight: 600, color: COLORS.text, marginBottom: 12, letterSpacing: "-0.025em" }}>Projets concrets</div>
        <div style={{ fontSize: 16, color: COLORS.muted, marginBottom: 48 }}>Pour construire votre portfolio</div>

        <div style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: 14, width: "100%", maxWidth: 850 }}>
          {projects.map((p, i) => (
            <ProjectCard key={i} name={p.name} category={p.category} difficulty={p.difficulty} icon={p.icon} color={p.color} frame={frame} delay={620 + i * 12} />
          ))}
        </div>
      </AbsoluteFill>
    </SectionContainer>
  );
};

const UsageSection: React.FC<{ frame: number; fps: number }> = ({ frame, fps }) => {
  if (frame < 720 || frame > 840) return null;

  const commands = [
    { title: "Exécuter un exercice", code: "uv run python exercices.py" },
    { title: "Voir la solution", code: "uv run python solutions.py" },
    { title: "Lancer les tests", code: "just test" },
    { title: "Formatter le code", code: "just format" },
  ];

  return (
    <SectionContainer frame={frame} start={720} end={840} fadeThroughBlack>
      <AbsoluteFill style={{ padding: "8% 10%", display: "flex", flexDirection: "column", alignItems: "center" }}>
        <div style={{ fontSize: 32, fontWeight: 600, color: COLORS.text, marginBottom: 48, letterSpacing: "-0.025em" }}>Utilisation simple</div>

        <div style={{ display: "flex", gap: 48, alignItems: "flex-start" }}>
          <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
            {commands.map((cmd, i) => {
              const progress = Math.max(0, Math.min(1, (frame - 740 - i * 15) / 25));
              return (
                <div key={i} style={{ opacity: progress, transform: `translateX(${interpolate(progress, [0, 1], [20, 0])})` }}>
                  <div style={{ background: "rgba(255, 255, 255, 0.02)", border: "1px solid rgba(255, 255, 255, 0.06)", borderRadius: 10, padding: "14px 24px", minWidth: 260 }}>
                    <span style={{ fontSize: 15, fontWeight: 500, color: COLORS.text }}>{cmd.title}</span>
                  </div>
                </div>
              );
            })}
          </div>

          <div style={{ width: 380 }}>
            <CodeBlock lines={[commands[0].code, "", `💡 ${commands[0].title.toLowerCase().replace("un", "")}`]} highlightLines={[0]} />
          </div>
        </div>
      </AbsoluteFill>
    </SectionContainer>
  );
};

const FinalSection: React.FC<{ frame: number; fps: number }> = ({ frame, fps }) => {
  if (frame < 840) return null;

  const progress = Math.max(0, Math.min(1, (frame - 840) / 50));
  const opacity = interpolate(progress, [0, 0.15], [0, 1]);
  const y = interpolate(progress, [0, 1], [20, 0]);

  return (
    <AbsoluteFill style={{ padding: "8% 10%", display: "flex", flexDirection: "column", alignItems: "center", opacity }}>
      <div style={{ display: "flex", alignItems: "center", gap: 24, marginBottom: 40, transform: `translateY(${y}px})` }}>
        <div style={{ width: 72, height: 72, borderRadius: 18, background: "linear-gradient(135deg, #3776ab, #ffd43b)", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 36 }}>🐍</div>
        <div>
          <div style={{ fontSize: 32, fontWeight: 700, color: COLORS.text, letterSpacing: "-0.025em" }}>Python Mastery</div>
          <div style={{ fontSize: 16, color: COLORS.muted, marginTop: 4 }}>Par Ranker</div>
        </div>
      </div>

      <div style={{ fontSize: 40, fontWeight: 700, color: COLORS.text, textAlign: "center", marginBottom: 16, transform: `translateY(${y}px})`, letterSpacing: "-0.025em" }}>
        Commencez votre voyage
      </div>
      <div style={{ fontSize: 18, color: COLORS.muted, textAlign: "center", marginBottom: 48, transform: `translateY(${y}px})` }}>
        De débutant à expert en IA, étape par étape
      </div>

      <div style={{ display: "flex", gap: 24, marginBottom: 48, transform: `translateY(${y}px})` }}>
        <BigStat number="26" label="Chapitres" frame={frame} delay={880} />
        <BigStat number="14" label="Projets" frame={frame} delay={900} />
        <BigStat number="5" label="Modules" frame={frame} delay={920} />
      </div>

      <div
        style={{
          padding: "16px 36px",
          background: "linear-gradient(90deg, #0ea5e9, #8b5cf6)",
          borderRadius: 10,
          fontSize: 16,
          fontWeight: 500,
          color: "#ffffff",
          transform: `translateY(${y}px})`,
        }}
      >
        ⭐ Star sur GitHub
      </div>

      <div style={{ position: "absolute", bottom: 40, fontSize: 13, color: COLORS.muted, opacity }}>
        github.com/ranker/relearn-python
      </div>
    </AbsoluteFill>
  );
};
