# ⏱️ LatencyWatch

[![PyPI version](https://badge.fury.io/py/latencywatch.svg)](https://pypi.org/project/latencywatch/0.2.0)
[![PyPI Downloads](https://img.shields.io/pypi/dm/latencywatch.svg?label=PyPI%20downloads)](
https://pypi.org/project/latencywatch/)

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**LatencyWatch** is a lightweight Python profiler for tracing nested function call latencies using `sys.setprofile`. It tracks execution time for every function call — including self-time (excluding children) — and presents a hierarchical report of where time was spent.

---

## 🚀 Installation

Install the package directly from PyPI:

```sh
pip install latencywatch
```
---

## 🔍 Features

- ✅ **Zero Configuration** - Start profiling with just a decorator
- 📊 **Hierarchical Reports** - View nested call stacks with timing information
- ⚡ **Low Overhead** - Minimal impact on application performance
- 🧵 **Thread-Safe** - Built-in thread-local storage for multi-threaded apps
- 🎯 **Flexible Filtering** - Include/exclude specific functions or modules
- 📈 **Performance Insights** - Separate self-time vs total time measurements
- 🔍 **Root-Only Mode** - Focus on top-level function calls for high-level analysis

---

## 🧪 Basic Usage

### Simple Profiling

```python
from latency_watch import LatencyWatch
import time

@LatencyWatch.watch
def process_data():
    def prepare():
        time.sleep(0.05)
    prepare()
    time.sleep(0.1)

process_data()
print(LatencyWatch.get_last_report(threshold_ms=1))
```

### Advanced Configuration

```python
from latency_watch import LatencyWatch, TraceConfig
import time

# Configure profiling options
TraceConfig.set(
    include_names=["my_module"],  # Only profile functions from my_module
    exclude_names=["test_"],      # Exclude test functions
    max_depth=3,                 # Limit call stack depth
    min_duration_ms=5,           # Only show calls taking >5ms
    root_only=False              # Show full call stack
)

def example():
    time.sleep(0.1)
    another_function()

def another_function():
    time.sleep(0.05)

# Profile with current configuration
LatencyWatch.watch(example)()
print(LatencyWatch.get_last_report())
```

---

## 📋 API Reference

### `@LatencyWatch.watch`
Decorator to trace function execution time.

### `LatencyWatch.get_last_report(threshold_ms=0, as_dict=False)`
Get the profiling report from the last execution.
- `threshold_ms`: Minimum duration (in ms) to include in report
- `as_dict`: Return structured dictionary instead of formatted string

### `LatencyWatch.reset()`
Clear all recorded profiling data.

### `TraceConfig.set(**kwargs)`
Configure profiling behavior:
- `include_names`: List of function/module name patterns to include
- `exclude_names`: List of function/module name patterns to exclude
- `max_depth`: Maximum call stack depth to track
- `min_duration_ms`: Minimum duration to include in reports (ms)
- `root_only`: Only track direct children of the root function

---

## 🧪 Testing

Run the test suite:

```bash
python -m pytest tests/
```

Or use the test runner:

```bash
python tests/run_all_tests.py
```

---

## 📦 Project Structure

```
latencywatch/
├── latencywatch/
│   ├── __init__.py
│   ├── profiler.py
│   └── trace_config.py
├── tests/
│   ├── test_basic_hierarchy.py
│   ├── test_include_exclude.py
│   ├── test_max_depth.py
│   ├── test_min_duration.py
│   ├── test_root_only.py
│   └── run_all_tests.py
├── README.md
├── setup.py
├── pyproject.toml
└── LICENSE
```

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📄 Changelog

### 0.2.0
- Added advanced filtering with include/exclude patterns
- Implemented max depth limiting
- Added root-only profiling mode
- Improved test coverage and documentation
- Added thread-safety improvements

### 0.1.0
- Initial release
- Basic function profiling
- Simple hierarchical reports
- Thread-local storage support

