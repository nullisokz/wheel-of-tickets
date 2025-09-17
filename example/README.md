# Wheel of Tickets - Complete Example

This example demonstrates the full functionality of the Wheel of Tickets system, from setup to ticket creation and management.

## Quick Start

1. **Prerequisites Setup**
   ```bash
   # Install PostgreSQL and create database
   createdb swine_sync
   
   # Install .NET 8.0 SDK
   # Install Node.js (version 18+)
   ```

2. **Database Setup**
   ```bash
   # Navigate to the example directory
   cd example
   
   # Run the setup script
   ./setup.sh
   ```

3. **Start the Application**
   ```bash
   # Terminal 1: Start the backend
   cd ../server
   dotnet run
   
   # Terminal 2: Start the frontend
   cd ../client
   npm install
   npm run dev
   ```

4. **Open the Application**
   - Navigate to: http://localhost:5173/
   - Use example credentials below

## Example Workflow

### 1. Login as Different Users

**Super Admin:**
- Email: `super_gris@mail.com`
- Password: `kung`
- Can manage companies and admin users

**Admin (Tech Solutions):**
- Email: `grune@grymt.se` 
- Password: `hejhej`
- Can manage products, categories, and support agents

**Customer Agent:**
- Email: `tryne@hotmail.com`
- Password: `asd123`
- Can respond to and manage tickets

### 2. Create a Ticket (Customer View)

1. Navigate to: http://localhost:5173/tech-solutions
2. Fill out the ticket form:
   - **Product:** Select "Premium Piglet Starter Feed"
   - **Category:** Select "Technical Support"
   - **Email:** Enter your email address
   - **Message:** "Having issues with the feed quality"
   - **Description:** "The recent batch seems to have quality issues"
3. Submit the ticket
4. Check your email for the chat link

### 3. Manage Tickets (Customer Agent View)

1. Login as Customer Agent: `tryne@hotmail.com` / `asd123`
2. Navigate to Customer Service dashboard
3. View unassigned tickets
4. Assign tickets to yourself
5. Respond to customer messages
6. Change ticket status when resolved

### 4. Admin Management

1. Login as Admin: `grune@grymt.se` / `hejhej`
2. Manage products and categories
3. Add new support agents
4. View ticket analytics

## Example Data

The system comes pre-loaded with:

### Companies
- **Tech Solutions** - IT services company
- **Eco Enterprises** - Eco-friendly products
- **Swine Sync** - CRM software company

### Products (Tech Solutions)
- Premium Piglet Starter Feed ($150)
- Organic Swine Feed ($180)
- Swine Health Supplement ($90)

### Categories
- Technical Support
- Billing Issues
- Product Information
- General Inquiry

## API Examples

### Create a Ticket via API
```bash
curl -X POST http://localhost:5000/api/tickets \
  -H "Content-Type: application/json" \
  -d '{
    "productId": 1,
    "categoryId": 1,
    "message": "Need help with setup",
    "email": "customer@example.com",
    "description": "Having trouble with initial configuration"
  }'
```

### Get Ticket Information
```bash
curl http://localhost:5000/api/tickets/{slug}
```

### List Companies
```bash
curl http://localhost:5000/api/companies?active=true
```

## Testing the Email Feature

1. The system sends emails when tickets are created
2. Check the MailService.cs configuration for email settings
3. For testing, you can use the test email: `pig.swinesync@gmail.com`
4. Emails contain direct links to chat with customer agents

## Mobile View

1. Open http://localhost:5173/tech-solutions
2. Resize browser to mobile view (or use device tools)
3. Test ticket creation on mobile interface
4. The interface is responsive and optimized for mobile

## Troubleshooting

### Database Connection Issues
- Check PostgreSQL is running
- Verify database name and credentials in `server/Program.cs`
- Ensure database schema is created with `database_files/swine_sync.txt`

### Email Not Working
- Check email credentials in `server/MailService.cs`
- Verify SMTP settings for Gmail
- Check firewall settings for SMTP port 587

### Frontend Issues
- Ensure Node.js version 18+
- Clear npm cache: `npm cache clean --force`
- Delete node_modules and reinstall: `rm -rf node_modules && npm install`

## Next Steps

After running this example, you can:
1. Create your own company
2. Add custom products and categories
3. Customize the email templates
4. Modify the UI styling
5. Add additional user roles
6. Integrate with external systems

For more details, see the main README.md in the project root.