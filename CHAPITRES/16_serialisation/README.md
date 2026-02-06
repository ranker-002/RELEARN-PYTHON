# =============================================================================
# CHAPITRE 16: SERIALISATION - README
# =============================================================================

# Chapitre 16: Serialisation

## JSON
```python
import json
json.dump(data, f)
json.load(f)
```

## Pickle
```python
import pickle
pickle.dump(obj, f)
pickle.load(f)
```

## CSV
```python
import csv
csv.DictWriter(f, fieldnames).writeheader()
```

## YAML
```python
import yaml
yaml.dump(data, f)
```
