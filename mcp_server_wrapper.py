#!/usr/bin/env python3
"""
MCP Server Wrapper for auggie compatibility
This wrapper ensures environment variables are properly inherited and the server starts correctly
"""

import os
import sys
from pathlib import Path

# Ensure we're in the correct directory
project_dir = Path(__file__).parent
os.chdir(project_dir)
sys.path.insert(0, str(project_dir))

# Environment variables are inherited automatically from the shell session
# No explicit handling needed - they will be available to the server process

# Set Python path
os.environ['PYTHONPATH'] = str(project_dir)

# Set minimal logging for MCP compatibility
os.environ['LOG_LEVEL'] = 'ERROR'

# Import and run the server
try:
    from server import run
    if __name__ == "__main__":
        run()
except Exception as e:
    # Log errors to a file instead of stderr to avoid MCP protocol interference
    with open(project_dir / "logs" / "wrapper_error.log", "a") as f:
        f.write(f"Wrapper error: {e}\n")
    sys.exit(1)
