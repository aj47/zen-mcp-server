#!/bin/bash
# Setup script for Auggie CLI integration

set -e

echo "🚀 Setting up Zen MCP Server for Auggie CLI"
echo "============================================"

# Get the absolute path of the current directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "📁 Project directory: $SCRIPT_DIR"

# Create auggie-config.json from template
if [ ! -f "$SCRIPT_DIR/auggie-config.json" ]; then
    echo "📝 Creating auggie-config.json..."
    sed "s|/path/to/zen-mcp-server|$SCRIPT_DIR|g" "$SCRIPT_DIR/auggie-config.example.json" > "$SCRIPT_DIR/auggie-config.json"
    echo "✅ Created auggie-config.json with correct paths"
else
    echo "⚠️  auggie-config.json already exists, skipping..."
fi

# Create .env from template if it doesn't exist
if [ ! -f "$SCRIPT_DIR/.env" ]; then
    echo "📝 Creating .env file from template..."
    cp "$SCRIPT_DIR/.env.example" "$SCRIPT_DIR/.env"
    echo "✅ Created .env file"
    echo "⚠️  IMPORTANT: Edit .env file and add your API keys!"
else
    echo "⚠️  .env file already exists, skipping..."
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Edit .env file and add your API keys:"
echo "   nano $SCRIPT_DIR/.env"
echo ""
echo "2. Use with Auggie CLI:"
echo "   auggie --mcp-config $SCRIPT_DIR/auggie-config.json"
echo ""
echo "📖 For detailed instructions, see: AUGGIE_SETUP_FINAL.md"
