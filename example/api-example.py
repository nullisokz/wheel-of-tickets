#!/usr/bin/env python3
"""
Wheel of Tickets - Python API Example

This script demonstrates how to interact with the Wheel of Tickets API using Python.
Make sure the server is running before executing this script.

Requirements:
    pip install requests

Usage:
    python api-example.py
"""

import requests
import json
import time
from datetime import datetime

# Configuration
API_BASE = "http://localhost:5000/api"
COMPANY_ID = 2  # Tech Solutions


def make_request(method, endpoint, data=None):
    """Make an API request and handle errors"""
    url = f"{API_BASE}{endpoint}"
    
    try:
        if method.upper() == "GET":
            response = requests.get(url, timeout=10)
        elif method.upper() == "POST":
            response = requests.post(url, json=data, timeout=10)
        else:
            raise ValueError(f"Unsupported method: {method}")
        
        print(f"📡 {method} {endpoint}")
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            try:
                return response.json()
            except:
                return response.text
        else:
            print(f"❌ Error: {response.text}")
            return None
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection error. Make sure the server is running on localhost:5000")
        return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None


def demo_companies():
    """Demonstrate company listing"""
    print("=" * 50)
    print("📋 LISTING COMPANIES")
    print("=" * 50)
    
    companies = make_request("GET", "/companies?active=true")
    if companies:
        print(f"Found {len(companies)} companies:")
        for company in companies:
            print(f"  - {company['name']} ({company['domain']})")
    print()


def demo_products():
    """Demonstrate product listing"""
    print("=" * 50)
    print("🛍️  LISTING PRODUCTS")
    print("=" * 50)
    
    products = make_request("GET", f"/products/customer-ticket?companyId={COMPANY_ID}")
    if products:
        print(f"Found {len(products)} products for company {COMPANY_ID}:")
        for product in products:
            print(f"  - {product['name']} (${product.get('price', 'N/A')})")
    print()


def demo_categories():
    """Demonstrate category listing"""
    print("=" * 50)
    print("🏷️  LISTING CATEGORIES")
    print("=" * 50)
    
    categories = make_request("GET", f"/tickets/categories?companyId={COMPANY_ID}")
    if categories:
        print(f"Found {len(categories)} categories for company {COMPANY_ID}:")
        for category in categories:
            print(f"  - {category['name']}")
    print()


def demo_create_ticket():
    """Demonstrate ticket creation"""
    print("=" * 50)
    print("🎫 CREATING TICKET")
    print("=" * 50)
    
    # Create ticket data
    ticket_data = {
        "productId": 1,
        "categoryId": 1,
        "message": f"Python API demo ticket created at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "email": "python-demo@example.com",
        "description": "This ticket was created using the Python API example script"
    }
    
    print("Creating ticket with data:")
    print(json.dumps(ticket_data, indent=2))
    print()
    
    response = make_request("POST", "/tickets", ticket_data)
    if response:
        print(f"✅ Ticket created successfully!")
        print(f"🔗 Response: {response}")
        
        # Try to extract slug from response
        if "customer/" in str(response):
            try:
                slug = str(response).split("customer/")[1].split("/")[0]
                print(f"🆔 Ticket slug: {slug}")
                return slug
            except:
                print("Could not extract slug from response")
    print()
    return None


def demo_get_ticket(slug):
    """Demonstrate getting ticket details"""
    if not slug:
        print("⚠️  No slug provided, skipping ticket retrieval")
        return
        
    print("=" * 50)
    print("📖 RETRIEVING TICKET")
    print("=" * 50)
    
    ticket = make_request("GET", f"/tickets/{slug}")
    if ticket:
        print("Ticket details:")
        print(json.dumps(ticket, indent=2))
    print()


def main():
    """Run the demo"""
    print("🎡 Wheel of Tickets - Python API Demo")
    print("=" * 50)
    print()
    
    # Test server connectivity
    print("Testing server connectivity...")
    companies = make_request("GET", "/companies?active=true")
    if not companies:
        print("❌ Cannot connect to server. Please make sure:")
        print("   1. The server is running (cd server && dotnet run)")
        print("   2. The server is accessible at http://localhost:5000")
        return
    
    print("✅ Server is accessible!")
    print()
    
    # Run demos
    demo_companies()
    demo_products()
    demo_categories()
    
    # Create and retrieve ticket
    slug = demo_create_ticket()
    if slug:
        time.sleep(1)  # Brief pause
        demo_get_ticket(slug)
    
    print("🎉 Python API demo completed!")
    print()
    print("💡 Next steps:")
    print("   - Try the web interface at http://localhost:5173/tech-solutions")
    print("   - Check the example/README.md for more detailed examples")
    print("   - Explore other API endpoints in the main README.md")


if __name__ == "__main__":
    main()