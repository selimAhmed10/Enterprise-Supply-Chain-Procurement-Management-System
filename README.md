# Enterprise Supply Chain & Procurement Management System

## Document Information

| Attribute | Value |
|-----------|-------|
| **Document Title** | Software Requirements Specification (SRS) |
| **Project Name** | SCM Pro - Enterprise Supply Chain & Procurement Management System |
| **Version** | 1.0 |
| **Date** | July 20, 2026 |
| **Document Type** | Complete System Specification |


## Table of Contents

1. Introduction
2. System Overview
3. User Roles & Responsibilities
4. Redis Usage & Implementation
5. Celery Usage & Implementation
6. Functional Requirements
7. Non-Functional Requirements
8. Database Design
9. File Storage Architecture
10. Technology Stack
11. Project Structure
12. Appendices


## 1. Introduction

### 1.1 Purpose
SCM Pro is a comprehensive web-based ERP system designed to digitize and automate the complete supply chain and procurement lifecycle for organizations of all sizes. The system provides end-to-end management from vendor registration to purchase order fulfillment, ensuring transparency, efficiency, and complete auditability.

### 1.2 Scope
The system manages:

- **Vendor Lifecycle**: Complete management from registration, document verification, approval, to performance tracking and rating
- **Product Catalog & Inventory**: Centralized product management with real-time stock tracking and automated reorder alerts
- **Procurement Process**: End-to-end workflow from requirement creation, bidding, evaluation, to purchase order generation
- **Communication**: Integrated chat system and email with digital signatures for professional communication
- **Analytics & Reporting**: Redis-powered real-time dashboards and comprehensive reports
- **Audit & Security**: Complete audit trail with role-based access control and JWT authentication

### 1.3 Definitions and Acronyms

| Term | Definition |
|------|------------|
| **SCM** | Supply Chain Management |
| **ERP** | Enterprise Resource Planning |
| **RFQ** | Request for Quotation |
| **PO** | Purchase Order |
| **GRN** | Goods Received Note |
| **RBAC** | Role-Based Access Control |
| **JWT** | JSON Web Token |
| **API** | Application Programming Interface |
| **SRS** | Software Requirements Specification |
| **DRF** | Django REST Framework |
| **ZSET** | Redis Sorted Set |
| **Pub/Sub** | Publish-Subscribe |
| **AOF** | Append Only File |
| **RDB** | Redis Database Backup |
| **HLL** | HyperLogLog |
| **UUID** | Universally Unique Identifier |
| **JSON** | JavaScript Object Notation |
| **SMTP** | Simple Mail Transfer Protocol |
| **SSL** | Secure Sockets Layer |
| **TLS** | Transport Layer Security |
| **CSV** | Comma Separated Values |
| **PDF** | Portable Document Format |
| **SKU** | Stock Keeping Unit |
| **NID** | National ID |
| **TIN** | Tax Identification Number |
| **CRUD** | Create, Read, Update, Delete |

### 1.4 Key Users

| Role | Description | Key Responsibilities |
|------|-------------|---------------------|
| **Super Admin** | Highest authority in the system | System oversight, manager management, monitoring, security settings |
| **Senior Manager** | Complete procurement operations | Vendor approval, product management, procurement, bid review, order generation |
| **Junior Manager** | Assist procurement operations | Product creation, inventory viewing, procurement drafting |
| **Vendor** | Participate in procurement | Submit quotations, deliver products, communicate with managers |
| **Guest User** | Public portal access | View procurement posts, apply for vendor registration |



## 2. System Overview

### 2.1 System Description
SCM Pro is a comprehensive web-based ERP system built on modern technologies including Django REST Framework, PostgreSQL, Redis, and Celery. The system follows a modular architecture with clear separation of concerns, enabling easy maintenance and scalability.

**Key System Characteristics:**
- **Web-based**: Accessible from any modern browser
- **Responsive**: Optimized for desktop, tablet, and mobile devices
- **Real-time**: Redis-powered real-time notifications and analytics
- **Scalable**: Horizontal scaling support with load balancing
- **Secure**: JWT authentication with role-based access control
- **Auditable**: Complete audit trail for all business operations

### 2.2 Core Modules (25 Modules)

| # | Module | Description |
|---|--------|-------------|
| 1 | User Management | Authentication, profiles, roles |
| 2 | Manager Management | Create, update, freeze managers |
| 3 | Vendor Management | Registration, approval, rating |
| 4 | Category Management | Product & vendor classification |
| 5 | Product Management | Catalog, SKU, images |
| 6 | Inventory Management | Stock tracking, alerts |
| 7 | Procurement Management | Requirements creation & publishing |
| 8 | Bid Management | Quotations, revisions, selection |
| 9 | Purchase Order Management | Order generation, PDF, email |
| 10 | Delivery Management | Receiving, performance tracking |
| 11 | Inventory Receiving Management | Stock update on delivery |
| 12 | Vendor Performance Management | Rating, ranking, analytics |
| 13 | Communication Management | Chat, email |
| 14 | Report Management | Reports generation, export |
| 15 | Dashboard & Analytics Management | Real-time metrics |
| 16 | Session Management | Authentication, tokens |
| 17 | Security Management | RBAC, JWT |
| 18 | Audit Management | Business action logging |
| 19 | Activity Management | API request logging |
| 20 | Exception Management | Error tracking |
| 21 | File Management | File upload, storage |
| 22 | Email Queue Management | Email processing, retry |
| 23 | Notification Queue Management | Pub/Sub notifications |
| 24 | Celery Task Management | Background tasks |
| 25 | Redis Management | Caching, Pub/Sub, Bitmaps, HyperLogLog |

### 2.3 System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         PRESENTATION LAYER                                  │
│                      React.js Application                                   │
│                    Responsive Web Interface                                 │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ REST API
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         API GATEWAY LAYER                                   │
│                     Django REST Framework                                   │
│                  JWT Authentication & RBAC                                  │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
         ┌──────────────────────────┼──────────────────────────┐
         │                          │                          │
         ▼                          ▼                          ▼
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│   APPLICATION   │      │    CELERY       │      │    REDIS        │
│    LAYER        │      │    WORKERS      │      │    CACHE &      │
│   (Django)      │      │   (Async)       │      │    QUEUE        │
│                 │      │                 │      │                 │
│ • Business      │      │ • Email Worker  │      │ • Cache         │
│   Logic         │      │ • Notification  │      │ • Rate Limiting │
│ • ORM           │      │ • PDF Worker    │      │ • Pub/Sub       │
│ • Validation    │      │ • Report Worker │      │ • Streams       │
│ • Permissions   │      │ • Audit Worker  │      │ • ZSET          │
│ • Serializers   │      │ • Cleanup Worker│      │ • Bitmaps       │
└─────────────────┘      └─────────────────┘      └─────────────────┘
         │                          │                          │
         └──────────────────────────┼──────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           DATA LAYER                                        │
│                    PostgreSQL Database                                      │
│                    Redis (Cache & Analytics)                                │
│                    File Storage (Media Files)                               │
└─────────────────────────────────────────────────────────────────────────────┘
```


## 3. User Roles & Responsibilities

### 3.1 Super Admin (HR Head)

**Dashboard:**
- Organization-wide dashboard with real-time metrics
- Procurement, product, inventory, vendor summaries
- Purchase order & delivery summary
- Category-wise analytics with product stock
- Procurement cost analysis (completed orders)
- Vendor performance (per post)
- User statistics (vendor list, count)
- Manager activities (audit log)
- Monthly and yearly reports (completed orders)

**Manager Management:**
- Create Senior Manager
- Create Junior Manager
- Update Manager Information
- Delete Manager
- Freeze / Unfreeze Manager
- Reset Manager Password
- Search Managers
- Filter Managers
- View Complete Manager Profile
```
Workflow: -- Create Manager → Send Email with Login Info → Manager Logs In 
```

**Can View:**
- All Vendors
- All Vendor Applications
- All Products
- All Inventory
- All Procurement Posts
- All Bids
- All Purchase Orders
- All Deliveries
- Procurement History
- Delivery Performance
- Reports
- Chats
- Emails
- Active Sessions
- Audit Logs
- Activity Logs
- Exception Logs
- Vendor Ratings

**Security & Settings:**
- View Active Sessions
- Force Logout Users
- View Token Blacklist


### 3.2 Senior Manager

**Vendor Management:**
- View Vendor Applications
- Approve Vendor (with confirmation email)
- Reject Vendor (with reason, application removed)
- Freeze/Unfreeze Vendor
- Create/Update/Delete Vendor
- View Vendor Profile (full by ID)
- View Vendor Rating
- Search Vendor
- Filter Vendor by Category
- Filter Vendor by Status

**Product Management:**
- Create Product
- Update Product
- Delete Product
- View Product (full by ID)
- Search Product
- Filter Product
- Upload Product Images
- View Procurement History

**Inventory Management:**
- View Inventory
- Add Stock
- Update Stock
- Search Inventory
- Filter Low Stock
- Filter Sufficient Stock
- Filter Out-of-Stock Products

**Procurement Post Management:**
- Create Procurement Post
- Edit Procurement Post
- Delete Procurement Post
- Publish Procurement Post
- Close Procurement Post
- Search Procurement (save PDF)
- Filter Procurement
- **View vendor performance on the post using Bitmap**

**Option 1 - From Existing Product:**
```
System Loads: Product Name, Category, Description
Manager Enters: Quantity, Required Sample, Attachments, Deadline
```

**Option 2 - Create New Product:**
```
Manager Enters: Complete Product Information
System Creates: Product + Procurement Post simultaneously
```

**Procurement Workflow:**
```
Create Procurement → Publish
    ↓
System checks Product Category
    ↓
Email sent ONLY to vendors in same category
    ↓
Redis PUB/SUB Notification sent to ALL users
    ↓
Procurement appears on everyone's dashboard
```

**Bid Management:**
- View Submitted Bids
- Compare Vendor Quotations
- View Vendor Performance
- Review Bid
- Request Bid Revision
- View Negotiation History
- Select Final Vendor
- Generate Purchase Order
- Search, Filter, Report as per filter

**Redis ZSET Ranking:**
```
Score = Vendor Rating + Delivery Performance - Bid Price

Delivery Performance Calculation:
  Procurement Deadline (from ProcurementPost)
  vs.
  Vendor Delivery Time (from Delivery Table)
```

**Bid Revision Mechanism:**
```
Manager reviews quotation → Revision Requested → Email to Vendor
    ↓
Vendor submits revised quotation → New Bid record created
    ↓
Manager reviews again → Final Vendor selected
```

**Purchase Order Management:**
- Generate Purchase Order
- Generate Purchase Order PDF
- Email Purchase Order
- Track Purchase Order Status
- View Purchase Order History
- Filter, Search and Get Report

**Calculation:** Total Amount = Bid Unit Price × Procurement Quantity

**Purchase Order Workflow:**
```
Manager selects winning bid
    ↓
Purchase Order Created
    ↓
PDF Generated
    ↓
Email sent to Vendor
    ↓
Procurement Status becomes Closed
```

**Delivery Management:**
- Receive Product
- Update Delivery Status
- Store Vendor Delivery Time
- View Delivery History (filter option, search, PDF download)

**Delivery Workflow:**
```
Vendor delivers product
    ↓
Supply Chain Team receives product
    ↓
Status changed to Received
    ↓
Vendor Delivery Time stored (Current Timestamp)
    ↓
Inventory Updated
    ↓
Vendor Performance recalculated
```

**Category Management:**
- Create Category
- Update Category
- Delete Category
- View Category List
- Search Categories
- Filter Categories (save)
- Activate / Deactivate Category


**Session Management:**
- View Active Sessions
- View Logged-in Users
- Monitor User Login History
- View Device Information
- View Browser Information
- View IP Address
- View Session Expiry Time
- Force Logout Users
- Terminate Active Sessions
- Monitor Refresh Token Status
- Monitor Blacklisted Tokens
- Search Sessions
- Filter Sessions
- Session Activity Monitoring

**Exception Log Management:**
- View Exception Logs
- View Validation Errors
- View Database Errors
- View API Errors
- View Authentication Errors
- View Authorization Errors
- View Celery Exceptions
- View Stack Trace
- View Error Messages
- Search Exception Logs
- Filter Exception Logs
- Export Exception Logs
- Monitor Failed Operations

**Celery Task Management:**
- View Celery Task Logs
- Monitor Task Status
- View Running Tasks
- View Completed Tasks
- View Failed Tasks
- View Retried Tasks
- View Queue Information
- View Worker Information
- Monitor Task Execution Time
- Search Task Logs
- Filter Task Logs
- Retry Failed Tasks (Optional)
- Export Task Logs

---

### 3.3 Junior Manager

- Assist Senior Manager in procurement operations
- Create/Update Products
- View Inventory
- Create Procurement Posts (Submit for Approval)
- View Bids & Quotations
- Internal Chat & Email

### 3.4 Vendor

**Registration:**
- Apply for Registration
- Upload Company Information
- Upload NID
- Upload TIN
- Upload Trade License
- Upload Company Logo
- Upload Company Profile PDF
- Select One or Multiple Categories
- Update Registration Information (before approval)

**Workflow:**
```
Register → Upload Documents → Manager Reviews
    ├── Approved → Confirmation Email → Account Activated
    └── Rejected → Rejection Email → Can Apply Again
```

**Dashboard:**
- Company Information
- Registered Categories
- Procurement Posts (Active + Earlier)
- Previous Procurement History
- Previous Bids
- Purchase Orders
- Delivery History
- Vendor Rating
- Notifications (from Redis Pub/Sub)
- Messages

**Bid Management:**
- Submit Quotation
- Upload Sample
- Upload Documents
- Add Comments
- View Bid Status
- Submit Revised Bid
- View Bid History

**Purchase Order:**
- View Purchase Orders
- Download Purchase Order PDF
- View Procurement Details
- View Total Amount
- Track Order Status

**Communication:**
- Chat with Managers
- Receive Emails
- View Notifications (from Redis Pub/Sub)

**Performance:**
- Automatic calculation using:
  - Delivery Performance
  - Previous Ratings
  - Procurement Success Rate

**Delivery Performance Calculation:**
```
Expected Delivery Deadline → Vendor Delivery Time (Delivery table)
    ↓
Delay Calculation → Vendor Rating Updated
```

---

### 3.5 Guest User

**Homepage:**
- View Homepage
- View Procurement Posts
- View Procurement Details
- View Procurement Posts from the Last 30 Days
- Ongoing procurement posts appear first
- Closed procurement posts appear below
- **Website Unique Visitor tracking using HyperLogLog**

**Vendor Registration:**
- Apply for Vendor Registration
- Upload Required Documents
- Select Categories
- Submit Company Information

**Contact:**
- Contact Organization
- View Organization Information
- Send General Inquiry

---

## 4. Redis Usage & Implementation

### 4.1 Caching

| Cache Type | Redis Data Type | Purpose | TTL |
|------------|-----------------|---------|-----|
| Dashboard Statistics | Hash | Real-time dashboard metrics | 5 min |
| Product List | Hash | Quick product catalog access | 15 min |
| Vendor List | Hash | Quick vendor data access | 15 min |
| Procurement Posts | Hash | Quick procurement display | 10 min |
| Reports | String | Cached report data | 30 min |
| Session Data | String | User session cache | 7 days |

### 4.2 Rate Limiting

| Rate Limit | Redis Data Type | Purpose | Limit |
|------------|-----------------|---------|-------|
| Login Attempts | String (INCR) | Prevent brute force | 5 attempts/15min |
| Email Sending | String (INCR) | Prevent email spam | 10 emails/hour |
| Bid Submissions | String (INCR) | Prevent bid spam | 3 bids/24 hours |
| API Abuse | String (INCR) | API protection | 1000 requests/hour |

### 4.3 Pub/Sub (Real-time Notifications - Only for Procurement)

| Channel | Purpose | Trigger | Subscribers |
|---------|---------|---------|-------------|
| **procurement** | **New procurement notification** | **When post is published** | **All users** |

**Notification Flow (Only for Procurement - NO Database Storage):**
```
Procurement Post Published
    ↓
Redis PUBLISH procurement "New procurement posted: {post_id}"
    ↓
All subscribed users receive real-time notification
    ↓
Notification appears on dashboard (in-memory only)
    ↓
NO Database Storage - Just real-time display
```

### 4.4 Streams (Event Processing)

| Stream | Purpose |
|--------|---------|
| procurement_events | Procurement lifecycle events |
| inventory_events | Stock update events |
| audit_events | Audit log events |
| email_queue | Email processing queue |

### 4.5 Sorted Set (ZSET) - Vendor Ranking

```
Score = Vendor Rating + Delivery Performance - Bid Price

Example:
Vendor A: Rating 4.5 + Delivery 4.0 - Price 2.0 = 6.5
Vendor B: Rating 3.0 + Delivery 3.5 - Price 1.5 = 5.0
Vendor C: Rating 4.0 + Delivery 4.5 - Price 3.0 = 5.5
```

### 4.6 Hashes - Frequently Accessed Objects

| Hash Key | Purpose |
|----------|---------|
| vendor:{id} | Vendor profile cache |
| product:{id} | Product details cache |
| dashboard:stats | Dashboard statistics cache |

### 4.7 Sets

| Set Key | Purpose |
|---------|---------|
| vendor:categories:{category_id} | Vendors in category |
| online:users | Currently online users |
| active:sessions | Active session IDs |

### 4.8 Bitmaps - Analytics (Vendor Performance per Post)

| Bitmap Key | Purpose | Bit Assignment |
|------------|---------|----------------|
| **post:{post_id}:vendor:performance** | **Vendor performance per post** | **Each bit represents a vendor** |

**Vendor Performance Bitmap Example:**
```
post:123:vendor:performance
  - Bit 0: Vendor A (Delivered On-Time) → Set to 1
  - Bit 1: Vendor B (Delivered Late) → Set to 0
  - Bit 2: Vendor C (Delivered On-Time) → Set to 1
  - Bit 3: Vendor D (Not Delivered) → Set to 0

BITCOUNT post:123:vendor:performance → Returns 2
```

**Manager View:** Senior Manager can see performance of all vendors on a specific procurement post using Bitmap analytics.

### 4.9 HyperLogLog - Visitor Analytics (Unique Visitors)

| HLL Key | Purpose | Accuracy |
|---------|---------|----------|
| **website:visitors:today** | **Unique visitors today** | **~97%** |
| website:visitors:month | Unique visitors this month | ~97% |

**HyperLogLog Operations:**
```
PFADD website:visitors:today "user_123" "user_456"
PFCOUNT website:visitors:today → Returns unique visitor count
```

### 4.10 AOF Persistence

- Ensures Redis data durability
- Every write operation logged
- Enables point-in-time recovery

### 4.11 RDB Snapshot Backup

- Periodic Redis snapshots (every 5 minutes)
- Disaster recovery backup
- Faster restart time

---

## 5. Celery Usage & Implementation

### 5.1 Celery Workers

| Worker | Tasks | Priority |
|--------|-------|----------|
| **Email Worker** | Approval/Rejection/Bid/PO emails | High |
| **Notification Worker** | Pub/Sub notifications (procurement only) | High |
| **PDF Worker** | PO PDF, Reports | Medium |
| **Report Worker** | Excel & Large reports | Medium |
| **Audit Worker** | Audit & Activity logs | Low |
| **Cleanup Worker** | Sessions, Tokens, Temp files | Low |
| **Reminder Worker** | Deadline reminders | Low |

### 5.2 Task Definitions

**Email Worker Tasks:**
```python
@shared_task
def send_vendor_approval_email(vendor_id):
    # Send approval email to vendor

@shared_task
def send_bid_revision_email(bid_id):
    # Send revision request email

@shared_task
def send_purchase_order_email(order_id):
    # Send PO with PDF attachment
```

**Notification Worker Tasks:**
```python
@shared_task
def send_procurement_notification(post_id):
    # PUB/SUB notification for new procurement
    redis.publish('procurement', f'New procurement posted: {post_id}')
```

**PDF Worker Tasks:**
```python
@shared_task
def generate_purchase_order_pdf(order_id):
    # Generate PO PDF

@shared_task
def generate_report_pdf(report_id):
    # Generate report PDF
```

**Cleanup Worker Tasks:**
```python
@shared_task
def cleanup_expired_sessions():
    # Delete expired sessions

@shared_task
def cleanup_blacklisted_tokens():
    # Delete blacklisted tokens

@shared_task
def cleanup_temp_files():
    # Delete temporary files
```

### 5.3 Celery Beat Schedule

| Task | Frequency | Time | Queue |
|------|-----------|------|-------|
| Daily Inventory Report | Daily | 8:00 AM | report_queue |
| Weekly Procurement Report | Weekly (Monday) | 9:00 AM | report_queue |
| Monthly Vendor Performance | Monthly (1st) | 10:00 AM | report_queue |
| Session Cleanup | Daily | 2:00 AM | cleanup_queue |
| Token Cleanup | Daily | 2:30 AM | cleanup_queue |
| Log Archiving | Daily | 3:00 AM | cleanup_queue |
| Database Backup | Daily | 1:00 AM | backup_queue |

### 5.4 Task Monitoring

- **Flower Dashboard**: Real-time task monitoring
- **Task Status**: Pending, Running, Success, Failed, Retry
- **Retry Mechanism**: Auto-retry on failure
- **Queue Management**: Priority queues


## 6. Functional Requirements

### 6.1 User Management

| Feature | Description |
|---------|-------------|
| User Registration | Self-registration with email and phone number |
| User Login | JWT authentication with access and refresh tokens |
| User Logout | Token blacklisting and session termination |
| Change Password | Secure password update with validation |
| Profile Management | Update user information, email, phone |
| User Search | Search users by name, email, role |
| User Filtering | Filter users by role, status, date |
| Freeze/Unfreeze | Admin freeze/unfreeze user accounts |
| Activate/Deactivate | Super Admin activate/deactivate users |
| User Details View | Complete user profile view by ID |
| Save PDF | Export user list,Profile as PDF |

### 6.2 Manager Management

| Feature | Description |
|---------|-------------|
| Create Senior Manager | Super Admin creates senior manager |
| Create Junior Manager | Super Admin creates junior manager |
| Update Manager | Update manager information |
| Delete Manager | Remove manager account |
| Freeze Manager | Temporarily suspend manager |
| Unfreeze Manager | Reactivate frozen manager |
| View Details | Complete manager profile |
| Search Manager | Search by name, email, role |
| Filter Manager | Filter by role, status |
| Save PDF | Export manager list,Profile as PDF |
| Activity Monitoring | View manager activities (audit log) |

### 6.3 Vendor Management

| Feature | Description |
|---------|-------------|
| Vendor Registration | Complete registration with documents |
| Vendor Approval | Senior Manager approve vendor |
| Vendor Rejection | Senior Manager reject vendor with reason |
| Vendor Creation | Senior Manager create vendor manually |
| Vendor Update | Update vendor information |
| Vendor Delete | Delete vendor (with validation) |
| Vendor Freeze | Temporarily suspend vendor |
| Vendor Unfreeze | Reactivate frozen vendor |
| Category Assignment | Assign one or multiple categories |
| Rating Management | Automatic rating calculation |
| Profile Management | Complete vendor profile |
| Document Verification | NID, TIN, Trade License verification |
| Performance Tracking | Delivery performance tracking |
| Procurement History | View procurement history |
| Delivery History | View delivery history |
| Search Vendor | Search by name, email, company |
| Filter Vendor | Filter by category, status, rating |
| Save PDF | Export vendor list,Profile as PDF |

### 6.4 Category Management

| Feature | Description |
|---------|-------------|
| Create Category | Senior Manager creates category |
| Update Category | Update category information |
| Delete Category | Delete category |
| Category List | View all categories |
| Search Category | Search categories by name |
| Activate/Deactivate | Enable/disable categories |


### 6.5 Product Management

| Feature | Description |
|---------|-------------|
| Create Product | New product creation |
| Update Product | Edit product information |
| Delete Product | Remove product |
| Product Details | Complete product view by ID |
| Image Management | Upload product images |
| Category Management | Assign to category |
| Product Search | Search products by name, SKU |
| Product Filter | Filter by category, status |
| SKU Generation | Auto-generate unique SKU |

### 6.6 Inventory Management

| Feature | Description |
|---------|-------------|
| Stock Addition | Add stock to products |
| Stock Update | Update stock quantities |
| Stock Adjustment | Manual stock adjustments |
| Inventory View | Complete inventory view |
| Inventory Search | Search by product |
| Inventory Filter | Filter by stock level |
| Save PDF | Export inventory as PDF |
| Save Excel | Export inventory as Excel |
| Low Stock Monitoring | Filter low stock products |
| Out of Stock Monitoring | Filter out-of-stock products |

### 6.7 Procurement Management

| Feature | Description |
|---------|-------------|
| Create Post | New procurement requirement |
| Edit Post | Edit draft procurement |
| Delete Post | Remove procurement |
| Draft | Save as draft |
| Approval | Submit for approval |
| Publish | Publish procurement |
| Close | Close procurement |
| Cancel | Cancel procurement |
| Search | Search procurement posts |
| Filter | Filter by status, category, date |
| Save PDF | Export procurement as PDF |
| History | View procurement history |
| **View Performance** | **Vendor performance per post using Bitmap** |

### 6.8 Bid Management

| Feature | Description |
|---------|-------------|
| Bid Submission | Vendor submits quotation |
| Bid Revision Request | Manager requests revision |
| Bid Resubmission | Vendor submits revised bid |
| Bid Comparison | Compare vendor quotations |
| Bid Ranking | Vendor ranking (Redis ZSET) |
| Bid Review | Manager reviews bids |
| Bid Negotiation | Complete negotiation history |
| Bid History | View bid history |
| Bid Analytics | Bid analytics |
| Final Vendor Selection | Select final vendor |

### 6.9 Purchase Order Management

| Feature | Description |
|---------|-------------|
| Purchase Order Creation | Auto-generated from selected bid |
| Purchase Order Generation | Generate purchase order |
| Purchase Order PDF Generation | Create PDF |
| Purchase Order Emailing | Send to vendor |
| Purchase Order Status Tracking | Track order status |
| Purchase Order Search | Search purchase orders |
| Purchase Order Filter | Filter by status, vendor |
| Purchase Order History | View order history |

### 6.10 Delivery Management

| Feature | Description |
|---------|-------------|
| Delivery Creation | Delivery record creation |
| Product Receiving | Receive products |
| Delivery Status Update | Update delivery status |
| Stock Update | Auto-update inventory |
| Vendor Delivery Time Tracking | Track delivery time |
| Delivery History | View delivery history |
| Delivery Performance Analysis | Analyze performance |
| Delay Calculation | Calculate delay |
| On-Time Delivery Calculation | Calculate on-time delivery |
| Search/Filter | Search and filter deliveries |
| Save PDF | Export delivery as PDF |

### 6.11 Vendor Performance Management

| Feature | Description |
|---------|-------------|
| Delivery Performance Calculation | Calculate delivery performance |
| Vendor Rating Calculation | Automatic rating update |
| Vendor Ranking | Vendor ranking (Redis ZSET) |
| Procurement Success Rate | Calculate success rate |
| **Bitmap Tracking** | **Performance per post using Bitmap** |
| Performance Analytics | Analyze vendor performance |

### 6.12 Communication Management

**Chat:**
- Send Message
- Receive Message
- File Sharing
- Message History
- Search Messages
- Filter Messages
- Save Messages

**Email:**
- Send Email (Manager to Vendor only)
- Receive Email (Vendor)
- CC Support
- BCC Support
- Attachment Management
- Email Templates (using manager name and position)
- Email History
- Email Tracking
- Email Status Monitoring

**Notification (Only via Pub/Sub):**
- **New Procurement Posted → PUB/SUB notification**
- Real-time delivery
- **NO Database Storage**

### 6.13 Dashboard & Analytics

| Feature | Redis Usage |
|---------|-------------|
| Procurement Analytics | Cached in Redis |
| Inventory Analytics | Cached in Redis |
| Vendor Analytics | ZSET ranking |
| Product Analytics | Cached in Redis |
| Delivery Analytics | Cached in Redis |
| Purchase Analytics | Cached in Redis |
| Cost Analytics | Cached in Redis |
| **User Analytics** | **HyperLogLog for unique visitors** |
| **Performance Analytics** | **Bitmap for vendor performance per post** |

### 6.14 Session Management

| Feature | Description |
|---------|-------------|
| Session Creation | Create on login |
| Session Tracking | Track active sessions |
| Active Sessions | View active sessions |
| Session Expiry | Automatic expiry |
| Session Termination | Terminate sessions |
| Device Tracking | Track device information |
| Browser Tracking | Track browser information |
| IP Tracking | Track IP address |
| Force Logout | Admin force logout |
| Refresh Token Rotation | Rotate refresh tokens |
| Token Blacklist | Blacklist tokens |
| Token Revocation | Revoke tokens |

### 6.15 Security Management

| Feature | Description |
|---------|-------------|
| JWT Authentication | Access/Refresh tokens |
| Access Token Management | Access token lifecycle |
| Refresh Token Management | Refresh token lifecycle |
| Token Blacklisting | Blacklist compromised tokens |
| Role Based Access Control | RBAC implementation |
| Object Level Permission | Fine-grained permissions |
| Password Security | Secure password handling |
| Rate Limiting | Redis protection |

### 6.16 Audit Management

| Feature | Description |
|---------|-------------|
| Create Audit Log | Create audit logs |
| User Action Audit | Track all user actions |
| Time Store | Store timestamp |
| CRUD Audit | Create/Update/Delete tracking |
| Approval Audit | Approve/Reject tracking |
| Freeze Audit | Freeze/Unfreeze tracking |
| Value Tracking | Previous/New value tracking |
| Login Audit | Login attempts |
| Data Change Tracking | Track all changes |
| Audit Search | Search audits |
| Audit Filtering | Filter audits |
| Save | Export audit logs |

### 6.17 Activity Management

| Feature | Description |
|---------|-------------|
| Request Logging | Log all API requests |
| Response Logging | Log all responses |
| API Monitoring | Monitor API endpoints |
| Endpoint Monitoring | Specific endpoint monitoring |
| Success Tracking | Track success status |
| Failure Tracking | Track failure status |
| Execution Time Monitoring | Track performance |
| User Activity Tracking | Track user actions |
| Activity Analytics | Analyze user activity |

### 6.18 Exception Management

| Feature | Description |
|---------|-------------|
| Exception Logging | Log all exceptions |
| Validation Error Tracking | Track validation errors |
| Database Error Tracking | Track database errors |
| API Error Tracking | Track API errors |
| Celery Error Tracking | Track Celery errors |
| System Error Tracking | Track system errors |
| Stack Trace Storage | Store full stack trace |
| Error Monitoring | Monitor errors |
| Error Analytics | Analyze errors |

### 6.19 File Management

| Feature | Description |
|---------|-------------|
| File Upload | Upload files |
| File Download | Download files |
| File Delete | Delete files |
| Image Upload | Upload images |
| Document Upload | Upload documents |
| PDF Upload | Upload PDFs |
| File Validation | Validate file type, size |
| File Storage | Store files in media folder |
| File History | Track file history |

### 6.20 Email Queue Management

| Feature | Description |
|---------|-------------|
| Email Queue Creation | Create email queue entries |
| Email Processing | Process emails async |
| Email Retry | Retry failed emails |
| Failed Email Handling | Handle failed emails |
| Bulk Email Processing | Process bulk emails |
| Email Delivery Tracking | Track email delivery |

### 6.21 Notification Queue Management (Only for Procurement)

| Feature | Description |
|---------|-------------|
| Notification Queue | Queue for procurement notifications |
| Real-Time Notification Processing | Process in real-time |
| Pub/Sub Notification Processing | Pub/Sub delivery |
| Notification Retry | Retry failed notifications |
| Notification Delivery Tracking | Track delivery |

### 6.22 Celery Task Management

| Feature | Description |
|---------|-------------|
| Task Creation | Create background tasks |
| Task Execution | Execute tasks asynchronously |
| Task Monitoring | Monitor task status |
| Task Retry | Retry failed tasks |
| Task Scheduling | Schedule periodic tasks |
| Task History | View task history |
| Queue Management | Manage task queues |
| Worker Management | Manage workers |
| Worker Scaling | Scale workers |
| Worker Monitoring | Monitor worker health |
| Celery Beat Scheduling | Celery Beat scheduling |
| Celery Chains | Sequential tasks |
| Celery Groups | Parallel tasks |
| Celery Chords | Tasks with callback |

### 6.23 Redis Management

| Feature | Redis Usage |
|---------|-------------|
| Cache Management | Dashboard, Products, Vendors |
| Session Cache | Session data cache |
| Dashboard Cache | Dashboard data cache |
| API Cache | API response cache |
| Rate Limiting | Login, Email, Bid, API |
| Pub/Sub | Real-time notifications |
| Streams | Event processing |
| Hash Management | Hash operations |
| Set Management | Set operations |
| ZSET Management | Vendor ranking |
| Bitmap Analytics | Vendor performance tracking per post |
| HyperLogLog Analytics | Unique visitor tracking |
| AOF Persistence | Redis durability |
| RDB Snapshot Backup | Redis backup |

---

## 7. Non-Functional Requirements

### 7.1 Performance

| Requirement | Target |
|-------------|--------|
| Dashboard Load Time | < 500ms (Redis cached) |
| API Response Time (Average) | < 200ms |
| API Response Time (Peak) | < 1s |
| CSV Import (10,000 rows) | < 30s (Celery) |
| Bulk Email (500 vendors) | < 5s (Celery) |
| Page Load Time | < 2s |
| Search Query | < 300ms |
| Report Generation | < 3s |
| **Redis Pub/Sub Notification** | **< 100ms** |
| **Bitmap Operation** | **< 10ms** |
| **HyperLogLog Operation** | **< 5ms** |

### 7.2 Security

| Requirement | Implementation |
|-------------|----------------|
| Authentication | JWT with Access/Refresh tokens ,Blacklisting|
| Token Expiry | Access: 15 min, Refresh: 7 days |
| Password Hashing |  bcrypt |
| Data at Rest | Database encryption |
| Data in Transit | SSL/TLS (HTTPS) |
| Role-Based Access | RBAC middleware |
| Object-Level Permissions | DRF permissions |
| Token Blacklisting | Immediate on logout |
| Rate Limiting | Redis protection |
| XSS Protection | Django built-in |
| SQL Injection | ORM parameterization |
| CSRF Protection | Django CSRF tokens |

### 7.3 Reliability

| Requirement | Target |
|-------------|--------|
| System Availability | 99.9% uptime |
| Data Backup | Daily |
| Recovery Point Objective | < 15 minutes |
| Recovery Time Objective | < 4 hours |
| Data Integrity | Automatic checks |
| Transaction Rollback | Yes |

### 7.4 Scalability

| Requirement | Target |
|-------------|--------|
| Concurrent Users | 1,000+ |
| Daily Transactions | 10,000+ |
| Vendors | 5,000+ |
| Products | 20,000+ |
| Records per Table | 1,000,000+ |
| Horizontal Scaling | Supported |
| Load Balancing | Supported |

---

## 8. Database Design

### 8.1 Table List (17 Tables)

| # | Table | Purpose |
|---|-------|---------|
| 1 | User | Authentication & roles |
| 2 | Category | Product & vendor classification |
| 3 | VendorExtra | Vendor information |
| 4 | Product | Product catalog |
| 5 | Inventory | Stock management |
| 6 | ProcurementPost | Procurement requirements |
| 7 | Bid | Vendor quotations with history |
| 8 | PurchaseOrder | Order generation |
| 9 | Delivery | Goods receipt tracking |
| 10 | ChatMessage | Vendor-Manager communication |
| 11 | EmailLog | Email history |
| 12 | BaseLog | Common audit fields |
| 13 | UserSession | Session & token management |
| 14 | AuditLog | Business operations history |
| 15 | ActivityLog | API request tracking |
| 16 | ExceptionLog | Error tracking |
| 17 | CeleryTaskLog | Background task monitoring |


### 8.2 Table Structures

#### User Table
| Field | Type | Description |
|-------|------|-------------|
| id | SERIAL | Primary key |
| first_name | VARCHAR(150) | User's first name |
| last_name | VARCHAR(150) | User's last name |
| email | VARCHAR(254) | Unique email |
| phone | VARCHAR(15) | Unique phone |
| password | VARCHAR(128) | Hashed password |
| role | VARCHAR(20) | Super Admin, Senior Manager, Junior Manager, Vendor |
| is_active | BOOLEAN | Active status |
| is_frozen | BOOLEAN | Frozen status |
| last_login | TIMESTAMP | Last login |
| created_at | TIMESTAMP | Creation time |
| updated_at | TIMESTAMP | Update time |

#### Category Table
| Field | Type | Description |
|-------|------|-------------|
| id | SERIAL | Primary key |
| name | VARCHAR(100) | Category name (Unique) |
| description | TEXT | Category description |
| is_active | BOOLEAN | Active status |
| created_at | TIMESTAMP | Creation time |
| updated_at | TIMESTAMP | Update time |

#### VendorExtra Table
| Field | Type | Description |
|-------|------|-------------|
| id | SERIAL | Primary key |
| user_id | INTEGER | User reference (Unique) |
| category_id | INTEGER | Primary category |
| company_name | VARCHAR(255) | Company name |
| owner_name | VARCHAR(255) | Owner name |
| email | VARCHAR(254) | Business email |
| phone | VARCHAR(15) | Business phone |
| address | TEXT | Business address |
| nid_number | VARCHAR(50) | National ID |
| tin_number | VARCHAR(50) | TIN number |
| trade_license_number | VARCHAR(100) | Trade license |
| company_logo | VARCHAR(255) | Logo path |
| nid_photo | VARCHAR(255) | NID photo path |
| tin_photo | VARCHAR(255) | TIN photo path |
| trade_license_photo | VARCHAR(255) | License photo path |
| company_profile_pdf | VARCHAR(255) | Company PDF path |
| rating | DECIMAL(3,2) | Rating (1-5) |
| status | VARCHAR(20) | Pending, Approved, Rejected, Frozen |
| created_at | TIMESTAMP | Creation time |
| updated_at | TIMESTAMP | Update time |

#### Product Table
| Field | Type | Description |
|-------|------|-------------|
| id | SERIAL | Primary key |
| category_id | INTEGER | Product category |
| name | VARCHAR(255) | Product name |
| description | TEXT | Product description |
| sku | VARCHAR(50) | Unique SKU |
| unit | VARCHAR(20) | Measurement unit |
| image | VARCHAR(255) | Product image path |
| specification | TEXT | Product specs |
| is_active | BOOLEAN | Active status |
| created_by | INTEGER | Who created |
| created_at | TIMESTAMP | Creation time |
| updated_at | TIMESTAMP | Update time |

#### Inventory Table
| Field | Type | Description |
|-------|------|-------------|
| id | SERIAL | Primary key |
| product_id | INTEGER | Product reference (Unique) |
| quantity | INTEGER | Current stock |
| minimum_quantity | INTEGER | Reorder level |
| maximum_quantity | INTEGER | Maximum stock |
| last_updated_by | INTEGER | Who updated |
| created_at | TIMESTAMP | Creation time |
| updated_at | TIMESTAMP | Update time |

#### ProcurementPost Table
| Field | Type | Description |
|-------|------|-------------|
| id | SERIAL | Primary key |
| product_id | INTEGER | Product reference |
| created_by | INTEGER | Who created |
| title | VARCHAR(255) | Post title |
| description | TEXT | Description |
| quantity | INTEGER | Required quantity |
| expected_unit_price | DECIMAL(12,2) | Expected price |
| required_sample | BOOLEAN | Sample required? |
| attachment | VARCHAR(255) | Attachment path |
| deadline | TIMESTAMP | Submission deadline |
| status | VARCHAR(20) | Draft, Pending Approval, Live, Closed, Completed, Cancelled |
| created_at | TIMESTAMP | Creation time |
| updated_at | TIMESTAMP | Update time |

#### Bid Table
| Field | Type | Description |
|-------|------|-------------|
| id | SERIAL | Primary key |
| post_id | INTEGER | Post reference |
| vendor_id | INTEGER | Vendor reference |
| previous_bid_id | INTEGER | Previous bid version |
| reviewed_by | INTEGER | Who reviewed |
| reviewed_at | TIMESTAMP | Review timestamp |
| review_round | INTEGER | Round number |
| unit_price | DECIMAL(12,2) | Quoted price |
| sample | VARCHAR(255) | Sample path |
| attachment | VARCHAR(255) | Attachment path |
| description | TEXT | Quotation description |
| manager_review | TEXT | Review notes |
| status | VARCHAR(20) | Submitted, Revision Requested, Selected, Rejected |
| is_resubmission | BOOLEAN | Is resubmission? |
| created_at | TIMESTAMP | Submission time |
| updated_at | TIMESTAMP | Update time |

#### PurchaseOrder Table
| Field | Type | Description |
|-------|------|-------------|
| id | SERIAL | Primary key |
| post_id | INTEGER | Post reference |
| bid_id | INTEGER | Selected bid |
| vendor_id | INTEGER | Vendor reference |
| quantity | INTEGER | Order quantity |
| unit_price | DECIMAL(12,2) | Unit price |
| total_amount | DECIMAL(12,2) | Total amount |
| status | VARCHAR(20) | Pending, Completed, Cancelled |
| created_by | INTEGER | Who created |
| created_at | TIMESTAMP | Creation time |
| updated_at | TIMESTAMP | Update time |

#### Delivery Table
| Field | Type | Description |
|-------|------|-------------|
| id | SERIAL | Primary key |
| order_id | INTEGER | Order reference |
| vendor_delivery_time | TIMESTAMP | Actual delivery time |
| status | VARCHAR(20) | Pending, Received |
| received_by | INTEGER | Who received |
| remarks | TEXT | Delivery remarks |
| created_at | TIMESTAMP | Creation time |
| updated_at | TIMESTAMP | Update time |

#### BaseLog Table (Common Fields)
| Field | Type | Description |
|-------|------|-------------|
| id | SERIAL | Primary key |
| created_by | INTEGER | Who created |
| updated_by | INTEGER | Who updated |
| created_at | TIMESTAMP | Creation time |
| updated_at | TIMESTAMP | Update time |

#### UserSession Table
| Field | Type | Description |
|-------|------|-------------|
| id | SERIAL | Primary key |
| base_log_id | INTEGER | Common fields reference |
| user_id | INTEGER | User reference |
| access_token | TEXT | JWT access token |
| refresh_token | TEXT | JWT refresh token |
| device | VARCHAR(100) | Device information |
| browser | VARCHAR(100) | Browser information |
| ip_address | VARCHAR(45) | IP address |
| expires_at | TIMESTAMP | Token expiry |
| is_active | BOOLEAN | Active session |
| is_blacklisted | BOOLEAN | Blacklisted token |
| blacklisted_at | TIMESTAMP | Blacklist timestamp |
| blacklist_reason | VARCHAR(100) | Reason |

#### AuditLog Table
| Field | Type | Description |
|-------|------|-------------|
| id | SERIAL | Primary key |
| base_log_id | INTEGER | Common fields reference |
| module | VARCHAR(50) | Module name |
| record_id | INTEGER | Record ID |
| action | VARCHAR(20) | CREATE, UPDATE, DELETE, APPROVE, REJECT, FREEZE |
| old_value | JSON | Previous values |
| new_value | JSON | New values |
| status | VARCHAR(10) | SUCCESS, FAILED |
| ip_address | VARCHAR(45) | IP address |

#### ActivityLog Table
| Field | Type | Description |
|-------|------|-------------|
| id | SERIAL | Primary key |
| base_log_id | INTEGER | Common fields reference |
| endpoint | VARCHAR(255) | API endpoint |
| http_method | VARCHAR(10) | GET, POST, PUT, DELETE, PATCH |
| request_data | JSON | Request payload |
| response_code | INTEGER | HTTP status |
| status | VARCHAR(10) | SUCCESS, FAILED |
| execution_time | INTEGER | Response time (ms) |
| ip_address | VARCHAR(45) | IP address |

#### ExceptionLog Table
| Field | Type | Description |
|-------|------|-------------|
| id | SERIAL | Primary key |
| base_log_id | INTEGER | Common fields reference |
| module | VARCHAR(50) | Module name |
| api | VARCHAR(255) | API endpoint |
| exception_type | VARCHAR(100) | Error type |
| error_message | TEXT | Error description |
| stack_trace | TEXT | Stack trace |
| request_payload | JSON | Request data |

#### CeleryTaskLog Table
| Field | Type | Description |
|-------|------|-------------|
| id | SERIAL | Primary key |
| base_log_id | INTEGER | Common fields reference |
| task_id | VARCHAR(255) | Celery task ID |
| task_name | VARCHAR(255) | Task name |
| queue | VARCHAR(50) | Queue name |
| worker | VARCHAR(100) | Worker name |
| status | VARCHAR(20) | Pending, Running, Success, Failed, Retry |
| retry_count | INTEGER | Number of retries |
| error_message | TEXT | Error if failed |
| started_at | TIMESTAMP | Start time |
| finished_at | TIMESTAMP | Finish time |

### 8.3 Key Relationships

```
User (1) ── VendorExtra (1:1)
User (1) ── Product (1:N)
User (1) ── ProcurementPost (1:N)
User (1) ── Bid (1:N)
User (1) ── PurchaseOrder (1:N)
User (1) ── Delivery (1:N)
User (1) ── ChatMessage (1:N)
User (1) ── EmailLog (1:N)
User (1) ── BaseLog (1:N)
User (1) ── UserSession (1:N)

Category (1) ── VendorExtra (1:N)
Category (1) ── Product (1:N)

Product (1) ── Inventory (1:1)
Product (1) ── ProcurementPost (1:N)

ProcurementPost (1) ── Bid (1:N)
ProcurementPost (1) ── PurchaseOrder (1:1)

Bid (1) ── PurchaseOrder (1:1)
Bid (1) ── Bid (Self) (1:N)

PurchaseOrder (1) ── Delivery (1:1)

BaseLog (1) ── UserSession (1:1)
BaseLog (1) ── AuditLog (1:1)
BaseLog (1) ── ActivityLog (1:1)
BaseLog (1) ── ExceptionLog (1:1)
BaseLog (1) ── CeleryTaskLog (1:1)
```


## 9. File Storage Architecture

### 9.1 Storage Strategy

Files stored in organized folder structure, only file paths stored in PostgreSQL database. No BLOB data in database.

### 9.2 Directory Structure

```
Project Root/
├── media/
│   ├── vendors/
│   │   ├── {vendor_id}/
│   │   │   ├── logo/
│   │   │   ├── nid/
│   │   │   ├── tin/
│   │   │   ├── trade_license/
│   │   │   └── profile/
│   ├── products/
│   │   ├── {product_id}/
│   │   │   └── images/
│   ├── procurement/
│   │   ├── {post_id}/
│   │   │   ├── attachments/
│   │   │   └── samples/
│   ├── bids/
│   │   ├── {bid_id}/
│   │   │   ├── samples/
│   │   │   └── documents/
│   ├── purchase_orders/
│   │   ├── {order_id}/
│   ├── chat/
│   │   ├── {chat_id}/
│   │   │   └── attachments/
│   └── temp/
│       └── {session_id}/
```

### 9.3 File Storage Mapping

| File Type | Storage Location | Database Field |
|-----------|------------------|----------------|
| Vendor Logo | media/vendors/{id}/logo/ | company_logo |
| NID Photo | media/vendors/{id}/nid/ | nid_photo |
| TIN Photo | media/vendors/{id}/tin/ | tin_photo |
| Trade License | media/vendors/{id}/trade_license/ | trade_license_photo |
| Company Profile | media/vendors/{id}/profile/ | company_profile_pdf |
| Product Image | media/products/{id}/images/ | image |
| Procurement Attachment | media/procurement/{id}/attachments/ | attachment |
| Bid Sample | media/bids/{id}/samples/ | sample |
| Bid Document | media/bids/{id}/documents/ | attachment |
| PO PDF | media/purchase_orders/{id}/ | pdf |
| Chat Attachment | media/chat/{id}/attachments/ | attachment |
| Email Attachment | media/email/{id}/ | attachment |

### 9.4 File Naming Convention

**Format:** `{type}_{timestamp}.{extension}`

**Examples:**
```
logo_20260716_103045.jpg
nid_20260716_103045.jpg
profile_20260716_103045.pdf
po_20260716_103045.pdf
```

### 9.5 File Validation Rules

| Validation | Description |
|------------|-------------|
| File Type | Only allowed file types |
| File Size | Must be within max size |
| File Name | No special characters, spaces |
| File Content | Virus scan required |
| Image Dimensions | Min/Max dimensions check |
| PDF Validation | Valid PDF structure |

**Allowed Extensions:**
```
image: jpg, jpeg, png, gif, bmp
document: pdf, doc, docx, xls, xlsx, csv
```

**Max File Sizes:**
```
image: 5MB
document: 10MB
pdf: 10MB
csv: 10MB
```

---

## 10. Technology Stack

### 10.1 Backend

| Component | Technology | |
|-----------|------------|---------|
| Framework | Django REST Framework | 
| Language | Python | 
| Database | PostgreSQL |
| Cache & Queue | Redis |
| Task Queue | Celery | 
| Real-time | Django Channels |
| Authentication | JWT (Simple JWT) |
| API Documentation | PostMan | 

### 10.2 Frontend

| Component | Technology |
|-----------|------------|
| Framework | React.js | |
| UI Library | Ant Design |
| Charts | Chart.js / Recharts |
| HTTP Client | Axios | - |

### 10.3 DevOps

| Component | Technology | 
|-----------|------------|
| Server OS | Ubuntu | 
| Web Server | Nginx + Gunicorn |
| Container | Docker & Docker Compose |
| CI/CD | GitLab CI | 
| Monitoring | Prometheus + Grafana |

## 11. Project Structure

### 11.1 Two Services Structure ( Backend( service-1),FrontEnd(service-2) )

```
~/scm/scm_project/
│
├── backend/                                    #  SERVICE 1: BACKEND (Django API)
│   ├── apps/                                   # All Django Apps
│   │   ├── accounts/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py                       # User Model
│   │   │   ├── serializers.py
│   │   │   ├── views.py                        # Login, Register, Profile
│   │   │   ├── urls.py
│   │   │   ├── permissions.py
│   │   │   └── utils.py
│   │   ├── managers/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py                       # Manager Profile
│   │   │   ├── serializers.py
│   │   │   ├── views.py                        # CRUD, Freeze Managers
│   │   │   ├── urls.py
│   │   │   └── permissions.py
│   │   ├── vendors/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py                       # VendorExtra (NID, TIN, License)
│   │   │   ├── serializers.py
│   │   │   ├── views.py                        # CRUD, Approve, Reject
│   │   │   ├── urls.py
│   │   │   ├── permissions.py
│   │   │   ├── signals.py
│   │   │   └── file_upload.py                  # Logo, NID, TIN, License
│   │   ├── categories/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py                       # Category
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   └── permissions.py
│   │   ├── products/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py                       # Product (SKU, Category)
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   ├── permissions.py
│   │   │   └── file_upload.py                  # Product Images
│   │   ├── inventory/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py                       # Inventory (Stock, Min, Max)
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   └── permissions.py
│   │   ├── procurement/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py                       # ProcurementPost
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   ├── permissions.py
│   │   │   ├── signals.py                      # Email + Redis Pub/Sub
│   │   │   └── file_upload.py                  # Attachments
│   │   ├── bids/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py                       # Bid (Unit Price, Status)
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   ├── permissions.py
│   │   │   ├── redis_service.py                # ZSET Ranking
│   │   │   └── file_upload.py                  # Samples, Documents
│   │   ├── orders/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py                       # PurchaseOrder
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   ├── permissions.py
│   │   │   ├── signals.py                      # Auto-close Procurement
│   │   │   ├── file_upload.py
│   │   │   └── pdf_generator.py                # PO PDF
│   │   ├── deliveries/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py                       # Delivery
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   ├── permissions.py
│   │   │   ├── signals.py                      # Auto-update Inventory
│   │   │   └── utils.py
│   │   ├── chat/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py                       # ChatMessage
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   ├── permissions.py
│   │   │   ├── consumers.py                    # WebSocket
│   │   │   ├── routing.py
│   │   │   └── file_upload.py
│   │   ├── emails/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py                       # EmailLog
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   ├── permissions.py
│   │   │   ├── tasks.py                        # Celery Email
│   │   │   └── templates.py                    # Email Templates
│   │   ├── sessions/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py                       # UserSession (Tokens, Blacklist)
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   ├── permissions.py
│   │   │   └── middleware.py
│   │   └── logging/
│   │       ├── __init__.py
│   │       ├── admin.py
│   │       ├── apps.py
│   │       ├── models.py                       # AuditLog, ActivityLog, ExceptionLog
│   │       ├── serializers.py
│   │       ├── views.py                        # View, Filter, Export Logs
│   │       ├── urls.py
│   │       ├── permissions.py
│   │       ├── middleware.py                   # Auto-log API Requests
│   │       └── handlers.py                     # Exception Handlers
│   │
│   ├── core/                                   # Shared Core Utilities
│   │   ├── __init__.py
│   │   ├── constants.py                        # Global Constants
│   │   ├── exceptions.py                       # Custom Exceptions
│   │   ├── validators.py                       # Validators
│   │   ├── pagination.py                       # Custom Pagination
│   │   ├── permissions.py                      # Global Permissions
│   │   ├── middleware.py                       # Global Middleware
│   │   ├── redis_client.py                     # Redis Connection
│   │   ├── email_service.py                    # Email Service
│   │   ├── pdf_export.py                       # PDF/Excel/CSV Export
│   │   ├── file_upload.py                      # File Upload Handler
│   │   └── utils.py                            # Common Utilities
│   │
│   ├── scm_pro/                                # Django Project Config
│   │   ├── __init__.py
│   │   ├── settings.py                         #  API ONLY
│   │   ├── urls.py                             #  ONLY API Endpoints
│   │   ├── wsgi.py
│   │   ├── asgi.py
│   │   ├── celery.py
│   │   └── celery_beat.py
│   │
│   ├── media/                                  # User Uploaded Files
│   │   ├── vendors/
│   │   │   └── {vendor_id}/
│   │   │       ├── logo/
│   │   │       ├── nid/
│   │   │       ├── tin/
│   │   │       ├── trade_license/
│   │   │       └── profile/
│   │   ├── products/
│   │   │   └── {product_id}/
│   │   │       └── images/
│   │   ├── procurement/
│   │   │   └── {post_id}/
│   │   │       ├── attachments/
│   │   │       └── samples/
│   │   ├── bids/
│   │   │   └── {bid_id}/
│   │   │       ├── samples/
│   │   │       └── documents/
│   │   ├── purchase_orders/
│   │   │   └── {order_id}/
│   │   ├── chat/
│   │   │   └── {chat_id}/
│   │   │       └── attachments/
│   │   └── temp/
│   │       └── {session_id}/
│   │
│   ├── tests/                                  # Test Files
│   │   ├── __init__.py
│   │   ├── test_accounts.py
│   │   ├── test_vendors.py
│   │   ├── test_products.py
│   │   ├── test_procurement.py
│   │   ├── test_bids.py
│   │   ├── test_orders.py
│   │   ├── test_deliveries.py
│   │   └── test_logging.py
│   │
│   ├── fixtures/                               # Initial Data
│   │   ├── categories.json
│   │   ├── users.json
│   │   └── vendors.json
│   │
│   ├── logs/                                   # Application Logs
│   │   ├── app.log
│   │   ├── celery.log
│   │   ├── django.log
│   │   ├── audit.log
│   │   └── exception.log
│   │
│   ├── scripts/                                # Backend Scripts
│   │   ├── backup.py
│   │   ├── cleanup.py
│   │   ├── seed.py
│   │   └── migration_helper.py
│   │
│   ├── manage.py                               # Django Management
│   ├── requirements.txt                        # Python Dependencies
│   ├── .env                                    # Backend Environment Variables
│   ├── .env.example                            # Environment Template
│   ├── Dockerfile                              # Backend Docker Image
│   ├── entrypoint.sh                           # Docker Entrypoint
│   └── setup.sh                                # Setup Script
│
│
│
│
│
├── frontend/                                   #  SERVICE 2: FRONTEND (React)
│   ├── public/
│   │   ├── index.html
│   │   ├── favicon.ico
│   │   ├── manifest.json
│   │   └── robots.txt
│   │
│   ├── src/
│   │   ├── api/                                # API Integration
│   │   │   ├── index.js                        # Axios Config
│   │   │   ├── endpoints.js                    # API Endpoints
│   │   │   ├── auth.js
│   │   │   ├── vendors.js
│   │   │   ├── products.js
│   │   │   ├── procurement.js
│   │   │   ├── bids.js
│   │   │   ├── orders.js
│   │   │   └── deliveries.js
│   │   │
│   │   ├── components/                         # UI Components
│   │   │   ├── common/
│   │   │   │   ├── Header.js
│   │   │   │   ├── Sidebar.js
│   │   │   │   ├── Footer.js
│   │   │   │   ├── Loading.js
│   │   │   │   ├── Modal.js
│   │   │   │   ├── Alert.js
│   │   │   │   ├── Card.js
│   │   │   │   ├── Table.js
│   │   │   │   ├── Pagination.js
│   │   │   │   ├── SearchBar.js
│   │   │   │   ├── FilterBar.js
│   │   │   │   ├── ExportButtons.js
│   │   │   │   └── FileUpload.js
│   │   │   ├── auth/
│   │   │   │   ├── Login.js
│   │   │   │   ├── Register.js
│   │   │   │   ├── ForgotPassword.js
│   │   │   │   └── ResetPassword.js
│   │   │   ├── dashboard/
│   │   │   │   ├── Dashboard.js
│   │   │   │   ├── SummaryCards.js
│   │   │   │   ├── ProcurementChart.js
│   │   │   │   ├── VendorChart.js
│   │   │   │   └── ActivityFeed.js
│   │   │   ├── vendors/
│   │   │   │   ├── VendorList.js
│   │   │   │   ├── VendorDetail.js
│   │   │   │   ├── VendorCreate.js
│   │   │   │   ├── VendorEdit.js
│   │   │   │   ├── VendorApproval.js
│   │   │   │   └── VendorPerformance.js
│   │   │   ├── products/
│   │   │   │   ├── ProductList.js
│   │   │   │   ├── ProductDetail.js
│   │   │   │   ├── ProductCreate.js
│   │   │   │   └── ProductEdit.js
│   │   │   ├── inventory/
│   │   │   │   ├── InventoryList.js
│   │   │   │   ├── InventoryDetail.js
│   │   │   │   └── StockUpdate.js
│   │   │   ├── procurement/
│   │   │   │   ├── ProcurementList.js
│   │   │   │   ├── ProcurementDetail.js
│   │   │   │   ├── ProcurementCreate.js
│   │   │   │   ├── ProcurementEdit.js
│   │   │   │   └── ProcurementPerformance.js
│   │   │   ├── bids/
│   │   │   │   ├── BidList.js
│   │   │   │   ├── BidDetail.js
│   │   │   │   ├── BidSubmit.js
│   │   │   │   ├── BidRevision.js
│   │   │   │   └── BidComparison.js
│   │   │   ├── orders/
│   │   │   │   ├── OrderList.js
│   │   │   │   ├── OrderDetail.js
│   │   │   │   └── OrderPDF.js
│   │   │   ├── deliveries/
│   │   │   │   ├── DeliveryList.js
│   │   │   │   ├── DeliveryDetail.js
│   │   │   │   └── DeliveryReceive.js
│   │   │   ├── chat/
│   │   │   │   ├── ChatList.js
│   │   │   │   ├── ChatRoom.js
│   │   │   │   └── MessageInput.js
│   │   │   ├── logs/
│   │   │   │   ├── LogList.js
│   │   │   │   ├── AuditLog.js
│   │   │   │   ├── ActivityLog.js
│   │   │   │   └── ExceptionLog.js
│   │   │   └── managers/
│   │   │       ├── ManagerList.js
│   │   │       ├── ManagerCreate.js
│   │   │       └── ManagerEdit.js
│   │   │
│   │   ├── pages/                              # Pages
│   │   │   ├── HomePage.js
│   │   │   ├── LoginPage.js
│   │   │   ├── DashboardPage.js
│   │   │   ├── VendorPage.js
│   │   │   ├── ProductPage.js
│   │   │   ├── InventoryPage.js
│   │   │   ├── ProcurementPage.js
│   │   │   ├── BidPage.js
│   │   │   ├── OrderPage.js
│   │   │   ├── DeliveryPage.js
│   │   │   ├── ChatPage.js
│   │   │   └── SettingsPage.js
│   │   │
│   │   ├── layouts/                             # Layouts
│   │   │   ├── MainLayout.js
│   │   │   ├── AuthLayout.js
│   │   │   └── GuestLayout.js
│   │   │
│   │   ├── store/                               # Redux State Management
│   │   │   ├── index.js
│   │   │   └── slices/
│   │   │       ├── authSlice.js
│   │   │       ├── vendorSlice.js
│   │   │       ├── productSlice.js
│   │   │       ├── procurementSlice.js
│   │   │       ├── bidSlice.js
│   │   │       ├── orderSlice.js
│   │   │       └── deliverySlice.js
│   │   │
│   │   ├── hooks/                               # Custom Hooks
│   │   │   ├── useAuth.js
│   │   │   ├── useApi.js
│   │   │   ├── useWebSocket.js
│   │   │   ├── useExport.js
│   │   │   └── useFilter.js
│   │   │
│   │   ├── utils/                               # Utilities
│   │   │   ├── helpers.js
│   │   │   ├── validators.js
│   │   │   ├── formatters.js
│   │   │   ├── constants.js
│   │   │   ├── websocket.js
│   │   │   └── export.js
│   │   │
│   │   ├── styles/                              # Global Styles
│   │   │   ├── global.css
│   │   │   ├── variables.css
│   │   │   └── theme.js
│   │   │
│   │   ├── routes/                              # Routing
│   │   │   ├── index.js
│   │   │   ├── private.js
│   │   │   └── public.js
│   │   │
│   │   ├── App.js
│   │   ├── App.css
│   │   └── index.js
│   │
│   ├── package.json
│   ├── package-lock.json
│   ├── .env                                     # Frontend Environment Variables
│   ├── Dockerfile                               # Frontend Docker Image
│   └── README.md
│
├── docs/                                        #Documentation (Shared)
│   ├── SRS/
│   │   └── SCM_Pro_SRS.pdf
│   ├── API/
│   │   └── api_documentation.md
│   └── Database/
│       └── er_diagram.png
│
├── scripts/                                     #  Utility Scripts (Shared)
│   ├── backup.sh
│   ├── deploy.sh
│   └── setup.sh
│
├── docker-compose.yml                           #  Both Services Together
├── .gitignore                                   # Git Ignore
├── README.md                                    # Project Documentation
└── venv/                                        # Python Virtual Environment
```

---

## 12. Appendices

### Appendix A: Redis Implementation Summary

| Feature | Redis Data Type | Key Format | Purpose |
|---------|-----------------|------------|---------|
| Dashboard Cache | Hash | dashboard:{user_id} | Real-time metrics |
| Vendor Ranking | ZSET | vendor:ranking | Score = Rating + Delivery - Price |
| **Vendor Performance** | **Bitmap** | **post:{post_id}:vendor:perf** | **Track vendor performance per post** |
| **Unique Visitors** | **HyperLogLog** | **website:visitors:today** | **Count unique visitors** |
| Procurement Notification | Pub/Sub | procurement | Real-time post notifications |
| Rate Limiting | String (INCR) | rate:login:{ip}:{date} | Prevent abuse |
| Session Cache | String | session:{session_id} | User session cache |
| Event Processing | Stream | procurement:events | Event logging |

### Appendix B: Celery Implementation Summary

| Worker | Task Type | Priority |
|--------|-----------|----------|
| Email Worker | Send emails (Approval, Rejection, PO) | High |
| Notification Worker | PUB/SUB notifications | High |
| PDF Worker | Generate PDFs (PO, Reports) | Medium |
| Report Worker | Generate reports | Medium |
| Audit Worker | Log audit activities | Low |
| Cleanup Worker | Clean sessions/tokens | Low |

### Appendix C: Notification Flow (Only Procurement - No Database Storage)

```
Procurement Post Published
    ↓
Celery Task: send_procurement_notification.delay(post_id)
    ↓
Redis PUBLISH procurement "New procurement posted: {post_id}"
    ↓
All subscribed users receive real-time notification
    ↓
Notification appears on dashboard (in-memory only)
    ↓
NO Database Storage - Just real-time display
```

### Appendix D: Core Management Modules Summary

| # | Module | Description |
|---|--------|-------------|
| 1 | User Management | Authentication, profiles, roles |
| 2 | Manager Management | Create, update, freeze managers |
| 3 | Vendor Management | Registration, approval, rating |
| 4 | Category Management | Product & vendor classification |
| 5 | Product Management | Catalog, SKU, images |
| 6 | Inventory Management | Stock tracking, alerts |
| 7 | Procurement Management | Requirements creation & publishing |
| 8 | Bid Management | Quotations, revisions, selection |
| 9 | Purchase Order Management | Order generation, PDF, email |
| 10 | Delivery Management | Receiving, performance tracking |
| 11 | Inventory Receiving Management | Stock update on delivery |
| 12 | Vendor Performance Management | Rating, ranking, analytics |
| 13 | Communication Management | Chat, email |
| 14 | Report Management | Reports generation, export |
| 15 | Dashboard & Analytics Management | Real-time metrics |
| 16 | Session Management | Authentication, tokens |
| 17 | Security Management | RBAC, JWT |
| 18 | Audit Management | Business action logging |
| 19 | Activity Management | API request logging |
| 20 | Exception Management | Error tracking |
| 21 | File Management | File upload, storage |
| 22 | Email Queue Management | Email processing, retry |
| 23 | Notification Queue Management | Pub/Sub notifications |
| 24 | Celery Task Management | Background tasks |
| 25 | Redis Management | Caching, Pub/Sub, Bitmaps, HyperLogLog |
