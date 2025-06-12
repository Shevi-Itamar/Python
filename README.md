# WIT - Version Control System with Code Analysis Backend

**Author:** Bat-Sheva Itamar  
**Instructor:** Hadasa Avimor  
**Course:** Basic Python Course - Final Project

## 🎯 Project Overview

This project consists of two integrated components:

1. **WIT Client** - A simplified version control system similar to Git, built with Python and Click
2. **Code Analysis Backend** - A FastAPI server that analyzes code quality when `wit push` is executed

The system simulates a basic Continuous Integration (CI) workflow focused on code quality analysis.

## 🏗️ System Architecture

```
┌─────────────────┐    wit push    ┌──────────────────────┐
│   WIT Client    │ ───────────────► │ FastAPI Backend      │
│ (Version Control│                 │ (Code Analysis)      │
│    System)      │                 │                      │
└─────────────────┘                 └──────────────────────┘
        │                                      │
        ▼                                      ▼
┌─────────────────┐                 ┌──────────────────────┐
│  .wit folder    │                 │  Analysis Reports    │
│ (Local Storage) │                 │  & Visual Graphs     │
└─────────────────┘                 └──────────────────────┘
```

## 🔧 WIT Client - Version Control System

### Features
- **Object-Oriented Design** - Built using OOP principles with proper encapsulation
- **CLI Interface** - Powered by Click library for intuitive command-line interaction
- **Git-like Functionality** - Familiar commands for version control operations

### Available Commands

| Command | Description |
|---------|-------------|
| `wit init` | Initialize a new repository (creates `.wit` folder) |
| `wit add <file>` | Stage files for the next commit |
| `wit commit -m "message"` | Create a new commit with staged files |
| `wit log` | Display commit history with hashes, dates, and messages |
| `wit status` | Show current repository status and uncommitted changes |
| `wit checkout <commit_id>` | Revert to a previous commit |
| `wit push` | Send code to analysis server for quality checks |

### Technical Implementation
- **Storage**: Local `.wit` folder containing commit data and metadata
- **Data Structures**: Dictionaries and lists for managing versions and commits
- **File Management**: Tracks file changes and maintains version history

## 🌐 Code Analysis Backend

### Technology Stack
- **Server Framework**: FastAPI
- **Code Analysis**: Python AST (Abstract Syntax Tree)
- **Visualization**: matplotlib
- **Language**: Python

### API Endpoints

#### POST `/analyze`
- **Purpose**: Accepts Python files and returns visual analysis graphs
- **Input**: Python source files
- **Output**: PNG graphs showing code metrics

#### POST `/alerts`
- **Purpose**: Accepts Python files and returns code quality warnings
- **Input**: Python source files  
- **Output**: JSON with detected issues and recommendations

### Code Quality Checks

The system performs automated analysis using AST to detect:

| Issue Type | Threshold | Description |
|------------|-----------|-------------|
| **Function Length** | > 20 lines | Functions that are too long and should be refactored |
| **File Length** | > 200 lines | Files that might benefit from being split |
| **Unused Variables** | N/A | Variables assigned but never referenced |
| **Missing Docstrings** | N/A | Functions without documentation |
| **Non-English Variables** | N/A | Variables using non-ASCII characters (Bonus) |

### Visual Analytics

Generated graphs include:

1. **📊 Histogram** - Distribution of function lengths across codebase
2. **🥧 Pie Chart** - Breakdown of issue types by frequency  
3. **📈 Bar Chart** - Number of issues per analyzed file
4. **📉 Line Graph** - Issue trends over time (Bonus feature)

All graphs are returned as PNG files for easy integration and viewing.

## 📁 Project Structure

```
wit-system/
├── wit-client/
│   ├── wit.py              # Main CLI application
│   ├── models/
│   │   ├── repository.py   # Repository class
│   │   ├── commit.py       # Commit class  
│   │   └── file_manager.py # File management utilities
│   └── requirements.txt
├── analysis-backend/
│   ├── main.py            # FastAPI server
│   ├── analyzers/
│   │   ├── ast_analyzer.py # Code analysis logic
│   │   └── graph_generator.py # Chart creation
│   ├── models/
│   │   └── analysis_models.py # Data models
│   └── requirements.txt
└── README.md
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager

### WIT Client Setup
```bash
cd wit-client
pip install -r requirements.txt
python wit.py init  # Initialize your first repository
```

### Backend Server Setup
```bash
cd analysis-backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

## 💻 Usage Examples

### Basic Version Control Workflow
```bash
# Initialize repository
wit init

# Add files for tracking
wit add main.py
wit add utils.py

# Create commit
wit commit -m "Initial project setup"

# View history
wit log

# Push for analysis
wit push
```

### Expected Analysis Output
When `wit push` is executed, the system will:
1. Send all tracked files to the analysis backend
2. Receive code quality warnings and visual graphs
3. Display results in the terminal
4. Save analysis reports locally

## 🎯 Learning Objectives Achieved

- **Object-Oriented Programming**: Proper use of classes, encapsulation, and abstraction
- **CLI Development**: Building user-friendly command-line interfaces with Click
- **API Development**: Creating RESTful services with FastAPI
- **Code Analysis**: Using AST for static code analysis
- **Data Visualization**: Generating meaningful charts with matplotlib
- **System Integration**: Connecting client and server components

## 🏆 Bonus Features

- **Directory Management**: Handle complex project structures with nested folders
- **Non-English Variable Detection**: Identify variables using Hebrew or other non-ASCII characters
- **Trend Analysis**: Track code quality improvements over time
- **Custom Analysis Rules**: Extensible framework for adding new quality checks

## 📋 Technical Requirements Met

✅ Object-Oriented Programming implementation  
✅ Click-based CLI interface  
✅ Local `.wit` folder for version storage  
✅ File change tracking and version management  
✅ FastAPI backend with proper endpoints  
✅ AST-based code analysis  
✅ matplotlib visualization generation  
✅ Comprehensive error handling  
✅ Clear documentation and examples

## 🔄 System Workflow

1. **Developer writes code** and uses WIT commands for version control
2. **`wit push` triggers** analysis by sending files to backend server
3. **FastAPI server analyzes** code using AST and detects quality issues
4. **Visual graphs are generated** showing code metrics and trends
5. **Results are returned** to the client and displayed to the developer
6. **Developer can review** suggestions and improve code quality

## 📈 Future Enhancements

- Integration with popular IDEs
- Support for additional programming languages
- Advanced security vulnerability detection
- Team collaboration features
- Cloud deployment and scaling

---

**Note**: This project demonstrates a complete software development lifecycle from initial design through implementation, testing, and documentation. It showcases both client-side application development and backend service architecture, providing a solid foundation for understanding modern software engineering practices.
