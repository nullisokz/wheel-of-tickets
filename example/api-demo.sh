#!/bin/bash

# Wheel of Tickets - API Demo Script
# This script demonstrates the API endpoints with example data

set -e

API_BASE="http://localhost:5000/api"

echo "🎫 Wheel of Tickets API Demo"
echo "=============================="
echo ""

echo "📋 1. Listing Companies..."
echo "GET $API_BASE/companies?active=true"
curl -s "$API_BASE/companies?active=true" | jq '.' || echo "Response received (jq not available for formatting)"
echo ""
echo ""

echo "🛍️  2. Listing Products for Tech Solutions (company ID 2)..."
echo "GET $API_BASE/products/customer-ticket?companyId=2"
curl -s "$API_BASE/products/customer-ticket?companyId=2" | jq '.' || echo "Response received"
echo ""
echo ""

echo "🏷️  3. Listing Categories for Tech Solutions..."
echo "GET $API_BASE/tickets/categories?companyId=2"
curl -s "$API_BASE/tickets/categories?companyId=2" | jq '.' || echo "Response received"
echo ""
echo ""

echo "🎫 4. Creating a Demo Ticket..."
TICKET_DATA='{
    "productId": 1,
    "categoryId": 1,
    "message": "Demo ticket created via API",
    "email": "demo@example.com",
    "description": "This is a demonstration ticket created through the API example script"
}'

echo "POST $API_BASE/tickets"
echo "Data: $TICKET_DATA"
TICKET_RESPONSE=$(curl -s -X POST "$API_BASE/tickets" \
    -H "Content-Type: application/json" \
    -d "$TICKET_DATA")

echo "Response: $TICKET_RESPONSE"
echo ""

# Extract slug from response if possible
if echo "$TICKET_RESPONSE" | grep -q "customer"; then
    SLUG=$(echo "$TICKET_RESPONSE" | sed -n 's/.*customer\/\([^\/]*\)\/.*/\1/p')
    if [ ! -z "$SLUG" ]; then
        echo "✅ Ticket created successfully!"
        echo "🔗 Chat URL: $TICKET_RESPONSE"
        echo "🆔 Ticket Slug: $SLUG"
        echo ""
        
        echo "📖 5. Retrieving the created ticket..."
        echo "GET $API_BASE/tickets/$SLUG"
        curl -s "$API_BASE/tickets/$SLUG" | jq '.' || echo "Response received"
        echo ""
    fi
else
    echo "⚠️  Ticket creation may have failed. Response: $TICKET_RESPONSE"
fi

echo ""
echo "🎉 Demo completed!"
echo ""
echo "💡 To test interactively:"
echo "   - Open http://localhost:5173/tech-solutions"
echo "   - Create a ticket through the web interface"
echo "   - Login as customer agent to respond to tickets"
echo ""
echo "📚 See example/README.md for more detailed examples"