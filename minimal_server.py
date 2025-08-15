#!/usr/bin/env python3
"""
Minimal MCP server entry point for auggie CLI compatibility
"""

import os
import sys
import logging
from pathlib import Path

# Ensure we're in the correct directory
project_dir = Path(__file__).parent
os.chdir(project_dir)
sys.path.insert(0, str(project_dir))

# Set minimal logging for MCP compatibility
os.environ['LOG_LEVEL'] = 'ERROR'

# Disable all logging to stderr to avoid interfering with MCP protocol
logging.getLogger().handlers.clear()
logging.getLogger().addHandler(logging.NullHandler())

# Import and run the server
try:
    from server import run
    if __name__ == "__main__":
        run()
except Exception as e:
    # Log errors to a file instead of stderr to avoid MCP protocol interference
    with open(project_dir / "logs" / "startup_error.log", "a") as f:
        f.write(f"Startup error: {e}\n")
    sys.exit(1)
