import React from 'react';
import { Eye, Mic2, Search, Repeat, Layout } from 'lucide-react';

const LensSwitcher = () => {
    const lenses = [
        { id: 'pacing', label: 'Pacing Lens', icon: Eye, active: true },
        { id: 'voice', label: 'Voice Lens', icon: Mic2 },
        { id: 'research', label: 'Research Lens', icon: Search },
        { id: 'reframe', label: 'Multi-Reframer', icon: Repeat },
        { id: 'beatboard', label: 'Beat Board', icon: Layout },
    ];

    return (
        <aside className="sidebar">
            <div className="brand mb-8 px-4">
                <h1 className="text-2xl font-black bg-gradient-to-r from-accent-purple to-accent-blue bg-clip-text text-transparent">
                    Annie
                </h1>
            </div>

            <nav className="lens-nav space-y-2">
                {lenses.map((lens) => {
                    const Icon = lens.icon;
                    return (
                        <div
                            key={lens.id}
                            className={`lens-item ${lens.active ? 'active' : ''}`}
                        >
                            <Icon size={20} />
                            <span className="text-sm font-medium">{lens.label}</span>
                        </div>
                    );
                })}
            </nav>

            <div className="mt-auto px-4 pb-4">
                <div className="user-profile flex items-center gap-3 p-2 rounded-lg bg-glass-bg border border-glass-border">
                    <div className="w-8 h-8 rounded-full bg-accent-purple"></div>
                    <div className="text-xs">
                        <p className="font-bold">Aisha M.</p>
                        <p className="text-secondary">Scriptwriter</p>
                    </div>
                </div>
            </div>
        </aside>
    );
};

export default LensSwitcher;
