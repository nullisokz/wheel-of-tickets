#!/bin/bash

# Wheel of Tickets - Example Setup Script
# This script sets up the database and initial data for the example

set -e  # Exit on any error

echo "🎡 Setting up Wheel of Tickets Example..."

# Check if PostgreSQL is installed
if ! command -v psql &> /dev/null; then
    echo "❌ PostgreSQL is not installed or not in PATH"
    echo "Please install PostgreSQL and make sure it's running"
    exit 1
fi

# Check if database exists
if psql -lqt | cut -d \| -f 1 | grep -qw swine_sync; then
    echo "⚠️  Database 'swine_sync' already exists"
    read -p "Do you want to recreate it? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "🗑️  Dropping existing database..."
        dropdb swine_sync
    else
        echo "❌ Aborting setup"
        exit 1
    fi
fi

echo "📊 Creating database 'swine_sync'..."
createdb swine_sync

echo "🏗️  Setting up database schema..."
psql -d swine_sync -f ../server/database_files/swine_sync.txt

echo "📋 Loading mock data..."
psql -d swine_sync -f ../server/database_files/mockdata.txt

echo "🔧 Building server..."
cd ../server
dotnet build

echo "🔑 Hashing passwords..."
# Start server in background, hash passwords, then stop it
echo "Starting server temporarily to hash passwords..."
dotnet run &
SERVER_PID=$!

# Wait for server to start
sleep 10

# Hash the passwords
curl -X POST http://localhost:5000/api/password/mockhash/ || echo "Password hashing may have failed, but continuing..."

# Stop the server
kill $SERVER_PID 2>/dev/null || true
wait $SERVER_PID 2>/dev/null || true

echo "📦 Installing client dependencies..."
cd ../client
npm install

echo "✅ Setup complete!"
echo ""
echo "🚀 To start the application:"
echo "1. Start the server:"
echo "   cd server && dotnet run"
echo ""
echo "2. In another terminal, start the client:"
echo "   cd client && npm run dev"
echo ""
echo "3. Open http://localhost:5173/ in your browser"
echo ""
echo "📖 Check example/README.md for detailed usage instructions"