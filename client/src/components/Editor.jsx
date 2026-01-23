import React, { useCallback, useEffect } from 'react';
import { useScriptStore } from '../store/useScriptStore';
import { retentionApi } from '../api';

// Simple debounce without lodash
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

const Editor = () => {
    const { currentScript, updateContent, setRetentionData } = useScriptStore();

    const analyze = useCallback(
        debounce(async (text) => {
            if (!text) return;
            try {
                const { data } = await retentionApi.analyze(text);
                setRetentionData(data.analysis);
            } catch (err) {
                console.error('Failed to analyze script', err);
            }
        }, 1000),
        []
    );

    const handleChange = (e) => {
        const text = e.target.value;
        updateContent(text);
        analyze(text);
    };

    return (
        <main className="editor-canvas">
            <input
                type="text"
                className="script-title-input"
                value={currentScript.title}
                onChange={(e) => updateContent({ ...currentScript, title: e.target.value })}
                placeholder="Untitled Script"
            />
            <textarea
                className="script-textarea"
                value={currentScript.content}
                onChange={handleChange}
                placeholder="Write your script here... Use [Visual: ...] or (B-roll: ...) for patterns."
            />
        </main>
    );
};

export default Editor;
