import axios from 'axios';

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL,
});

// Add token to requests if available
api.interceptors.request.use((config) => {
    const token = localStorage.getItem('token');
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});

export const retentionApi = {
    analyze: (text) => api.post('/retention/analyze', { script_text: text }),
};

export const voiceApi = {
    audit: (text, personaId) => api.post('/voice/audit', { script_text: text, persona_id: personaId }),
    clone: (personaId, texts) => api.post('/voice/clone', { persona_id: personaId, texts }),
};

export const hookApi = {
    analyze: (text) => api.post('/hooks/analyze', { script_text: text }),
    generate: (hook, platform) => api.post('/hooks/generate', { base_hook: hook, platform }),
};

export default api;
