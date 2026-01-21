import React, { useState } from 'react';
import { AlertCircle, Zap, Eye, BarChart3 } from 'lucide-react';

/**
 * RetentionSidebar - Phase 1 Core Feature
 * Real-time sidebar scanning word density and flagging "Dead Zones".
 */
const RetentionSidebar = ({ scriptData }) => {
  const [activeLens, setActiveLens] = useState('retention');

  return (
    <div className="retention-sidebar">
      <header className="sidebar-header">
        <h2 className="flex items-center gap-2 text-xl font-bold">
          <BarChart3 className="text-purple-500" />
          Retention Intelligence
        </h2>
        <p className="text-sm text-gray-400">Predicted APV: <span className="text-green-400 font-mono">84%</span></p>
      </header>

      <section className="score-section mt-6">
        <div className="flex justify-between items-end mb-2">
          <span className="text-xs uppercase tracking-widest text-gray-500">Hook Strength</span>
          <span className="text-lg font-bold text-white">92/100</span>
        </div>
        <div className="progress-bar-bg h-2 w-full bg-gray-800 rounded-full overflow-hidden">
          <div className="progress-fill h-full bg-gradient-to-r from-purple-500 to-blue-500 w-[92%]"></div>
        </div>
      </section>

      <section className="alerts-section mt-8">
        <h3 className="text-sm font-semibold mb-4 flex items-center gap-2">
          <AlertCircle size={16} className="text-amber-400" />
          Pacing Dead Zones
        </h3>
        
        <div className="space-y-4">
          <div className="alert-card p-4 bg-gray-900/50 border border-gray-800 rounded-lg hover:border-amber-500/50 transition-all cursor-pointer">
            <div className="flex justify-between mb-2">
              <span className="text-[10px] font-bold bg-amber-500/20 text-amber-500 px-2 py-0.5 rounded">00:45 - 01:12</span>
              <Zap size={14} className="text-amber-500" />
            </div>
            <p className="text-xs text-gray-300">Monologue too long (27s). Viewers likely to drop off here.</p>
            <button className="mt-3 text-[10px] font-bold uppercase text-purple-400 hover:text-purple-300 transition-colors">
              Suggest Visual Interrupt +
            </button>
          </div>

          <div className="alert-card p-4 bg-gray-900/50 border border-gray-800 rounded-lg opacity-60">
            <div className="flex justify-between mb-2">
              <span className="text-[10px] font-bold bg-green-500/20 text-green-500 px-2 py-0.5 rounded">02:30 - 02:45</span>
              <Eye size={14} className="text-green-500" />
            </div>
            <p className="text-xs text-gray-300">Strong B-roll sequence. Optimal retention predicted.</p>
          </div>
        </div>
      </section>

      <footer className="sidebar-footer mt-auto pt-8">
        <div className="vibe-meter p-4 rounded-xl bg-gradient-to-br from-indigo-900/40 to-purple-900/40 border border-indigo-500/30">
          <span className="text-[10px] uppercase font-bold text-indigo-300">Emotional Arc</span>
          <div className="h-12 flex items-end gap-1 mt-2">
             {[40, 60, 30, 90, 70, 50, 80, 40].map((h, i) => (
               <div key={i} className="flex-1 bg-indigo-500/50 rounded-t-sm" style={{height: `${h}%`}}></div>
             ))}
          </div>
        </div>
      </footer>
    </div>
  );
};

export default RetentionSidebar;
