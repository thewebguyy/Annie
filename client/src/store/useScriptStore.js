import { create } from 'zustand';

export const useScriptStore = create((set) => ({
    currentScript: {
        id: null,
        title: 'Untitled Script',
        content: '',
        retentionData: null,
        voiceAudit: null,
    },

    setCurrentScript: (script) => set({ currentScript: script }),

    updateContent: (content) => set((state) => ({
        currentScript: { ...state.currentScript, content }
    })),

    setRetentionData: (data) => set((state) => ({
        currentScript: { ...state.currentScript, retentionData: data }
    })),

    setVoiceAudit: (audit) => set((state) => ({
        currentScript: { ...state.currentScript, voiceAudit: audit }
    })),
}));
