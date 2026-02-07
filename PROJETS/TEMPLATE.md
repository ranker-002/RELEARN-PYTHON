# Project: [PROJECT_NAME]

<!-- PROJECT_METADATA -->
<!-- Generated from TEMPLATE.md - Do not edit Manually -->

## 🎯 Learning Objective

Apply [MAIN_CONCEPTS] in a real-world, production-ready project that simulates professional development workflows.

## 📊 Difficulty Level

**LEVEL** | ⏱️ HOURS hours | 🎯 Priority: PRIORITY

## 📚 Prerequisites

- **Required Module**: [MODULE_NUMBER](LINK_TO_MODULE_README)
- Skills required:
  - [SKILL_1]
  - [SKILL_2]
  - [SKILL_3]
- Tools required:
  - [TOOL_1] (installation link)
  - [TOOL_2] (installation link)

---

## 🏗️ Project Architecture

```
[PROJECT_SLUG]/
├── src/
│   ├── __init__.py
│   ├── main.py              # Entry point (CLI/API)
│   ├── models/              # Domain entities
│   │   ├── __init__.py
│   │   └── *.py
│   ├── services/            # Business logic
│   │   ├── __init__.py
│   │   └── *.py
│   └── utils/              # Helper functions
│       ├── __init__.py
│       └── *.py
├── solution/                # Complete solution
│   └── src/
│       ├── main.py
│       ├── models/
│       ├── services/
│       └── utils/
├── data/
│   ├── sample/             # Example data files
│   │   └── *.csv/json/...
│   └── input/              # Input data for testing
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_models.py
│   ├── test_services.py
│   └── test_main.py
├── requirements.txt        # Specific dependencies
├── .env.example           # Environment variables template
└── README.md
```

---

## 📋 Required Features

### Core Features (Mandatory)

#### Feature 1: [FEATURE_NAME]
- **Description**: [CLEAR_DESCRIPTION]
- **Expected Behavior**:
  1. User action triggers...
  2. System processes...
  3. Result is displayed...
- **Constraints**:
  - [CONSTRAINT_1]
  - [CONSTRAINT_2]

#### Feature 2: [FEATURE_NAME]
- **Description**: [CLEAR_DESCRIPTION]
- **Expected Behavior**:
  1. ...
  2. ...
  3. ...
- **Constraints**:
  - ...

### Bonus Features (Optional)

#### Bonus 1: [BONUS_NAME]
- **Description**: [BONUS_DESCRIPTION]
- **Difficulty**: Easy/Medium/Hard
- **Points**: XX points

---

## 💡 Progressive Hints

### 🚦 Level 1 - Discovery

**Goal**: Understand the basic structure

```python
# SKELETON_CODE_HERE
class DataModel:
    def __init__(self, data):
        self.data = data

    def process(self):
        """Process data and return result."""
        # TODO: Implement this
        pass
```

**Hint**: Start by identifying the core entities and their relationships. Draw a simple diagram before coding.

---

### 🚦🚦 Level 2 - Deepening

**Goal**: Implement core functionality

```python
# PARTIAL_IMPLEMENTATION
def validate_input(data: dict) -> bool:
    """
    Validate input data meets requirements.
    
    Args:
        data: Input dictionary to validate
        
    Returns:
        True if valid, False otherwise
    """
    required_fields = ["field1", "field2"]
    for field in required_fields:
        if field not in data or not data[field]:
            return False
    return True
```

**Hint**: Use type hints from the start. They help catch errors early and document your code.

---

### 🚦🚦🚦 Level 3 - Expert

**Goal**: Complete production-ready implementation

```python
# NEAR_COMPLETE_SOLUTION
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class AdvancedProcessor:
    def __init__(self, config: dict):
        self.config = config
        self.cache = {}
    
    def process_with_retry(
        self, 
        data: dict, 
        max_retries: int = 3
    ) -> Optional[dict]:
        """Process with automatic retry on failure."""
        for attempt in range(max_retries):
            try:
                result = self._process(data)
                logger.info(f"Success on attempt {attempt + 1}")
                return result
            except Exception as e:
                logger.warning(f"Attempt {attempt + 1} failed: {e}")
                if attempt == max_retries - 1:
                    raise
        return None
```

**Hint**: Consider edge cases: empty inputs, network timeouts, invalid data formats.

---

## 🎨 Usage Example

### Interactive Mode

```bash
$ python src/main.py
[CLI_OUTPUT_HERE]
```

### Programmatic Usage

```python
from src.models import DataModel
from src.services import Processor

# Initialize
model = DataModel(initial_data)
processor = Processor(config={"option": True})

# Process data
result = processor.run(model)
print(result)
```

### Configuration

```bash
# Set environment variables
export API_KEY="your_key"
export DATABASE_URL="postgresql://..."

# Or create .env file
cp .env.example .env
# Edit .env with your values
```

---

## 🧪 Data Model

### Core Classes

```python
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from enum import Enum

class Status(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass
class ProjectEntity:
    """Main entity for the project."""
    id: str
    name: str
    status: Status = Status.PENDING
    created_at: datetime = None
    metadata: Optional[dict] = None
    
    def is_valid(self) -> bool:
        """Check if entity is valid."""
        return bool(self.id and self.name)
```

---

## ✅ Validation Criteria

- [ ] **CRITERION_1**: [DESCRIPTION]
- [ ] **CRITERION_2**: [DESCRIPTION]
- [ ] **CRITERION_3**: [DESCRIPTION]
- [ ] **CRITERION_4**: [DESCRIPTION]
- [ ] **CRITERION_5**: [DESCRIPTION]

---

## ⚠️ Common Pitfalls

1. **Pitfall**: [DESCRIPTION]
   - **Solution**: [HOW_TO_AVOID]

2. **Pitfall**: [DESCRIPTION]
   - **Solution**: [HOW_TO_AVOID]

---

## 🚀 Installation & Running

### Quick Start

```bash
# 1. Navigate to project
cd [PROJECT_SLUG]

# 2. Install dependencies
uv sync --extra [EXTRA_NAME]

# 3. Run the project
python src/main.py

# 4. Run tests
pytest tests/ -v
```

### Development Mode

```bash
# Install with dev dependencies
uv sync --extra dev

# Run with auto-reload
uv run watchexec -r -e py -- python src/main.py
```

---

## 📖 Resources

### Documentation
- [Official Documentation](https://LINK)
- [API Reference](https://LINK)

### Tutorials
- [Tutorial 1](https://LINK)
- [Tutorial 2](https://LINK)

### Tools
- [Tool 1 Documentation](https://LINK)
- [Tool 2 Documentation](https://LINK)

---

## 🎓 Learning Outcomes

After completing this project, you will be able to:
- [OUTCOME_1]
- [OUTCOME_2]
- [OUTCOME_3]
- [OUTCOME_4]

---

*Difficulty Scale: Beginner → Intermediate → Advanced → Expert*

---

[← Back to module](../README_PROJETS.md)
