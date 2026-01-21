import React from 'react';
import { AlertCircle, Zap, Eye, BarChart3 } from 'lucide-react';
import { useScriptStore } from '../store/useScriptStore';

/**
 * RetentionSidebar - Phase 1 Core Feature
 * Real-time sidebar scanning word density and flagging "Dead Zones".
 */
const RetentionSidebar = () => {
  const { currentScript } = useScriptStore();
  const retentionData = currentScript?.retentionData;

  // Fallback high-level stats if data isn't loaded yet
  const riskScore = retentionData?.overall_risk_score || 84;
  const segments = retentionData?.segments || [];

  return (
    <div className="retention-sidebar">
      <header className="sidebar-header">
        <h2 className="flex items-center gap-2 text-xl font-bold">
          <BarChart3 className="text-purple-500" />
          Retention Intelligence
        </h2>
        <p className="text-sm text-secondary">
          Predicted APV: <span className="text-success-green font-mono">{riskScore}%</span>
        </p>
      </header>

      <section className="score-section mt-6">
        <div className="flex justify-between items-end mb-2">
          <span className="text-[10px] uppercase tracking-widest text-secondary">Hook Strength</span>
          <span className="text-lg font-bold">92/100</span>
        </div>
        <div className="progress-bar-bg">
          <div className="progress-fill" style={{ width: '92%' }}></div>
        </div>
      </section>

      <section className="alerts-section mt-8">
        <h3 className="text-sm font-semibold mb-4 flex items-center gap-2">
          <AlertCircle size={16} className="text-warning-amber" />
          Pacing Dead Zones
        </h3>

        <div className="space-y-4">
          {segments.filter(s => s.risk === 'High').map((s, i) => (
            <div key={i} className="alert-card risk-high">
              <div className="flex justify-between mb-2">
                <span className="text-[10px] font-bold bg-warning-amber/20 text-warning-amber px-2 py-0.5 rounded">
                  {Math.floor(s.start_time / 60)}:{(s.start_time % 60).toFixed(0).padStart(2, '0')} -
                  {Math.floor(s.end_time / 60)}:{(s.end_time % 60).toFixed(0).padStart(2, '0')}
                </span>
                <Zap size={14} className="text-warning-amber" />
              </div>
              <p className="text-xs text-secondary">{s.alert}</p>
              <button className="mt-3 text-[10px] font-bold uppercase text-accent-purple hover:underline">
                Suggest Visual Interrupt +
              </button>
            </div>
          ))}

          {/* Fallback if no segments yet */}
          {segments.length === 0 && (
            <div className="alert-card">
              <p className="text-xs text-secondary">Start typing to see retention analysis...</p>
            </div>
          )}
        </div>
      </section>

      <footer className="sidebar-footer mt-auto pt-8">
        <div className="vibe-meter">
          <span className="text-[10px] uppercase font-bold text-accent-indigo">Emotional Arc</span>
          <div className="h-12 flex items-end gap-1 mt-2">
            {[40, 60, 30, 90, 70, 50, 80, 40].map((h, i) => (
              <div key={i} className="vibe-bar" style={{ height: `${h}%` }}></div>
            ))}
          </div>
        </div>
      </footer>
    </div>
  );
};

export default RetentionSidebar;
