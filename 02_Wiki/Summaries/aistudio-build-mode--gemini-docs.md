---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/aistudio-build-mode.md
source_url: https://ai.google.dev/gemini-api/docs/aistudio-build-mode
title: "Gemini API — AI Studio Build Mode"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# AI Studio Build Mode

Source is in German (crawler localization).

## Overview

Build Mode in Google AI Studio enables rapid app creation ("vibe coding") via natural language prompts. Supports full-stack runtimes with server-side logic, secure secret management, and npm package support.

## Starting Options

- **From a prompt**: Describe what you want to build in the input field. Add AI Chips for specific features (image generation, Google Maps data). Voice-to-text available.
- **"Lucky" button**: Gemini generates a creative project idea prompt.
- **Remix from Gallery**: Open a project from App Gallery → "Copy App".

## What Gets Created

A complete full-stack application:
- **Client-side**: Web frontend (default: React)
- **Server-side**: Node.js runtime for secure API calls, database connections, npm packages

View generated code in the **Code** tab of the preview panel.

## Antigravity Agent

The core AI engine in Build Mode (from Google Antigravity). Features:
- **Context awareness**: Remembers previous prompts and file states
- **Multi-file management**: Handles dependencies between multiple files
- **Verified execution**: Reviews code updates to reduce hallucinations

## Full-Stack Features

- **npm packages**: Agent auto-identifies and installs required packages
- **Secret management**: API keys stored securely in Settings menu (server-side only, not exposed client-side)
- **Multiplayer**: Real-time collaborative experiences; server manages state and connections
- **Firebase integration**: Auto-provisioned — Firestore database (persistent storage) + Firebase Authentication (login flows including Google Sign-In)

## Iteration

- Continue refining via chat in Build Mode
- Edit code directly in the Code editor
- Deploy: one-click to public URL, or export code to develop locally

## Use Cases

- Testing Gemini features (Nano Banana image gen, Live API, etc.) without manual setup
- Rapid app prototyping
- Full-stack application development with AI assistance
