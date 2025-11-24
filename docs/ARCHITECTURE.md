# Task Manager CLI - Architecture and Design

## System Overview

The Task Manager CLI is a single-executable command-line application built in C++ with a layered architecture that separates concerns between presentation, business logic, and data persistence.

## Design Patterns

### Layered Architecture
- Clear separation between presentation, business logic, and data
- Each layer depends only on the layer below it
- Easy to test and modify independently

### Repository Pattern (FileStorage)
- Abstract data persistence details
- Easy to swap storage implementations later
- Centralize file I/O error handling

## Data Flow

### Adding a Task
1. User enters command: `task-manager add "Fix bug" high`
2. CLI parses arguments and validates input
3. CLI calls `taskManager.addTask("Fix bug", HIGH)`
4. TaskManager creates Task with unique ID
5. TaskManager adds to in-memory collection
6. TaskManager calls `fileStorage.saveTasks()`
7. FileStorage writes all tasks to file
8. CLI displays success message

### Listing Tasks
1. User enters command: `task-manager list`
2. CLI calls `taskManager.listTasks()`
3. TaskManager returns vector of tasks
4. CLI formats and displays tasks in table format

## Build System

**Build Tool**: GNU Make

**Build Targets**:
- `make` or `make all` - Build the executable
- `make clean` - Remove compiled files
- `make test` - Run tests (if implemented)

**Compiler Flags**:
- `-std=c++17` - Use C++17 standard
- `-Wall -Wextra` - Enable all warnings
- `-O2` - Optimization level 2 for release builds


## Error Handling

- Use return codes for error conditions
- Validate all user inputs before processing
- Handle file I/O errors gracefully
- Provide clear error messages to users
- Never crash on bad input

## Testing Strategy

- Unit tests for TaskManager operations
- File I/O tests for FileStorage
- Integration tests for complete workflows
- Manual testing for CLI interactions

## Performance Considerations

- In-memory operations for fast access
- Batch save operations to minimize I/O
- Simple file format for quick parsing
- Expected capacity: hundreds of tasks (not thousands)

## Security Considerations

- No authentication required (single-user, local)
- Validate file paths to prevent directory traversal
- Handle file permissions appropriately
- No sensitive data stored

## Future Architecture Extensions

- Add abstraction layer for different storage backends
- Implement observer pattern for UI updates
- Add command pattern for undo/redo functionality
- Consider SQLite for better query capabilities
