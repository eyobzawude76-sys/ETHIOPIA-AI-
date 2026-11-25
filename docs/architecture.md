# ETHIOPIA AI — Initial Architecture

## Goal

Build an open-source AI assistant that initially supports Afaan Oromoo and Afaan Amharic, with a modular path toward AI agents and robotics research.

## High-level components

1. **Android app** — the user-facing chat interface.
2. **Assistant backend** — manages conversations and coordinates model requests.
3. **Model runtime** — runs a selected open-source language model. The first prototype will evaluate device capability before choosing on-device or server inference.
4. **Language resources** — prompts, evaluation examples, and language-specific tests for Afaan Oromoo and Afaan Amharic.
5. **Memory (later phase)** — optional, user-controlled storage with clear privacy controls.
6. **Agents and tools (later phase)** — narrowly scoped capabilities added after the basic assistant is reliable.
7. **Robotics integration (future research)** — separate, safety-reviewed interfaces; not part of the first prototype.

## Initial development principles

- Start with a small, testable assistant.
- Do not commit model weights, API keys, passwords, or private user data.
- Keep secrets in environment variables and out of Git.
- Evaluate language quality with human-reviewed examples before claiming fluency.
- Make memory opt-in and provide a way to inspect and delete stored data.
- Add features in small commits and test each change.

## First milestone

Create a minimal chat prototype and compare suitable open-source models against the target Android device's RAM, storage, and performance. The model choice is intentionally deferred until device constraints are known.
