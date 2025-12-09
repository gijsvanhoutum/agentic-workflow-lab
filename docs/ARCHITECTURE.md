# Task Manager CLI - Architecture and Design

## System Overview

The Task Manager CLI is a single-executable command-line application with a layered architecture that separates concerns between presentation, business logic, and data persistence. We are building the application for demo, do not overcomplicate it.

## Design Patterns

### Layered Architecture
- Clear separation between presentation, business logic, and data
- Each layer depends only on the layer below it
- Easy to test and modify independently

### Repository Pattern 
- Abstract data persistence details
- Easy to swap storage implementations later
	- In-memory repository used for tests and imported usage
	- File-backed repository used when running the CLI script (JSON `tasks.json`)

## Security Considerations
- No authentication required (single-user, local)

## Tests
- add unit tests
 - Use `pytest` with auto-discovery in devcontainer