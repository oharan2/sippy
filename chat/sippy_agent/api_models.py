"""
API models for the Sippy Agent web interface.
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel


class ChatMessage(BaseModel):
    """A single chat message."""

    role: str  # "user" or "assistant"
    content: str
    timestamp: Optional[str] = None


class ChatRequest(BaseModel):
    """Request model for chat endpoint."""

    message: str
    chat_history: Optional[List[ChatMessage]] = None
    show_thinking: Optional[bool] = None
    persona: Optional[str] = None


class ThinkingStep(BaseModel):
    """A single step in the agent's thinking process."""

    step_number: int
    thought: str
    action: str
    action_input: str
    observation: str


class ChatResponse(BaseModel):
    """Response model for chat endpoint."""

    response: str
    thinking_steps: Optional[List[ThinkingStep]] = None
    tools_used: Optional[List[str]] = None
    error: Optional[str] = None


class StreamMessage(BaseModel):
    """WebSocket message for streaming chat."""

    type: str  # "thinking_step", "final_response", "error"
    data: Dict[str, Any]


class AgentStatus(BaseModel):
    """Status information about the agent."""

    available_tools: List[str]
    model_name: str
    endpoint: str
    thinking_enabled: bool
    current_persona: str
    available_personas: List[str]


class PersonaInfo(BaseModel):
    """Information about an available persona."""

    name: str
    description: str
    style_instructions: str


class PersonasResponse(BaseModel):
    """Response listing available personas."""

    personas: List[PersonaInfo]
    current_persona: str


class HealthResponse(BaseModel):
    """Health check response."""

    status: str
    version: str
    agent_ready: bool
