// Type definitions for the autonomous agent

type AgentStatus = 'idle' | 'running' | 'error';

type Action = {
    name: string;
    params: Record<string, any>;
};
