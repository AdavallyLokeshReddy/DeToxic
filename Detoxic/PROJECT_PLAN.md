# Detoxic - Toxic Comment Classification App
## Complete Implementation Plan

---

## 1. PROJECT OVERVIEW
**Goal:** Build a production-ready application that identifies and classifies toxic comments in real-time, with a professional UI similar to Zomato/Swiggy standards.

**Key Features:**
- Real-time toxicity detection
- Multi-label classification (6 categories)
- User history and analytics dashboard
- Admin moderation panel
- Database storage of all submissions
- Professional, responsive UI

---

## 2. TECHNOLOGY STACK

### 2.1 BACKEND (ML + API)
```
Framework: Flask / FastAPI (FastAPI for async and modern Python)
Language: Python 3.10+
Port: 5000

Key Libraries:
├── fastapi              # Modern API framework
├── uvicorn              # ASGI server
├── sqlalchemy           # ORM for database
├── pydantic             # Data validation
├── scikit-learn         # ML preprocessing
├── transformers         # BERT/DistilBERT models
├── torch                # Deep learning
├── pandas               # Data processing
├── numpy                # Numerical computing
├── python-dotenv        # Environment variables
├── python-multipart     # File uploads
├── cors                 # Cross-origin requests
└── pytest               # Testing
```

### 2.2 DATABASE
```
Primary DB: PostgreSQL (production-grade, ACID compliant)
ORM: SQLAlchemy
Port: 5432

Backup Option: MySQL (good alternative)
```

### 2.3 FRONTEND
```
Framework: React 18+ with TypeScript
Build Tool: Vite (faster than Create React App)
Styling: Tailwind CSS + shadcn/ui components
State Management: Redux Toolkit / Zustand
HTTP Client: Axios / TanStack Query
Port: 3000

Design Inspiration: Zomato, Swiggy (modern, clean, intuitive)
```

### 2.4 ADDITIONAL SERVICES
```
Authentication: JWT (for user login)
File Storage: Local (or AWS S3 for production)
Caching: Redis (optional, for performance)
API Documentation: Swagger/OpenAPI
Deployment: Docker + Docker Compose
```

---

## 3. DATABASE SCHEMA

### Core Tables:

#### users
```sql
- id (PK)
- username (UNIQUE)
- email (UNIQUE)
- password_hash
- full_name
- role (admin, user)
- created_at
- updated_at
```

#### submissions
```sql
- id (PK)
- user_id (FK)
- comment_text (TEXT)
- submission_date
- status (pending, reviewed, approved)
- created_at
```

#### predictions
```sql
- id (PK)
- submission_id (FK)
- toxic (FLOAT 0-1)
- severe_toxic (FLOAT 0-1)
- obscene (FLOAT 0-1)
- threat (FLOAT 0-1)
- insult (FLOAT 0-1)
- identity_hate (FLOAT 0-1)
- predicted_at
```

#### analytics (for user dashboard)
```sql
- id (PK)
- user_id (FK)
- total_submissions
- toxic_count
- clean_count
- last_checked
```

---

## 4. PROJECT STRUCTURE

```
Detoxic/
├── Backend/
│   ├── App/
│   │   ├── main.py                 # FastAPI app entry
│   │   ├── config.py               # Configuration
│   │   ├── requirements.txt         # Dependencies
│   │   ├── .env.example             # Environment template
│   │   │
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── user.py              # User model
│   │   │   ├── submission.py        # Submission model
│   │   │   └── prediction.py        # Prediction model
│   │   │
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── user.py              # User Pydantic schemas
│   │   │   ├── submission.py        # Submission schemas
│   │   │   └── prediction.py        # Prediction schemas
│   │   │
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py              # Login/register endpoints
│   │   │   ├── predict.py           # Prediction endpoints
│   │   │   ├── submissions.py       # Submission CRUD
│   │   │   ├── analytics.py         # Dashboard data
│   │   │   └── admin.py             # Admin endpoints
│   │   │
│   │   ├── ml_model/
│   │   │   ├── __init__.py
│   │   │   ├── predictor.py         # Model loading & inference
│   │   │   ├── preprocessor.py      # Text preprocessing
│   │   │   └── train.py             # Model training script
│   │   │
│   │   ├── database/
│   │   │   ├── __init__.py
│   │   │   ├── connection.py        # DB connection
│   │   │   └── crud.py              # Database operations
│   │   │
│   │   ├── auth/
│   │   │   ├── __init__.py
│   │   │   ├── security.py          # JWT, password hashing
│   │   │   └── dependencies.py      # Auth middleware
│   │   │
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   └── helpers.py           # Utility functions
│   │   │
│   │   └── tests/
│   │       ├── __init__.py
│   │       └── test_api.py
│   │
│   └── docker/
│       ├── Dockerfile               # Backend container
│       └── .dockerignore
│
├── Frontend/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.ts
│   ├── tsconfig.json
│   ├── tailwind.config.js
│   │
│   ├── src/
│   │   ├── main.tsx
│   │   ├── App.tsx
│   │   ├── index.css
│   │   │
│   │   ├── pages/
│   │   │   ├── Login.tsx
│   │   │   ├── Register.tsx
│   │   │   ├── Dashboard.tsx
│   │   │   ├── AnalyticsPage.tsx
│   │   │   └── AdminPanel.tsx
│   │   │
│   │   ├── components/
│   │   │   ├── Navbar.tsx
│   │   │   ├── CommentInput.tsx     # Main input component
│   │   │   ├── ResultCard.tsx       # Prediction results
│   │   │   ├── HistoryList.tsx
│   │   │   ├── StatsCard.tsx
│   │   │   └── LoadingSpinner.tsx
│   │   │
│   │   ├── services/
│   │   │   ├── api.ts              # API calls
│   │   │   └── auth.ts             # Auth service
│   │   │
│   │   ├── store/
│   │   │   ├── userStore.ts        # User state
│   │   │   └── submissionStore.ts  # Submission state
│   │   │
│   │   ├── hooks/
│   │   │   ├── useAuth.ts
│   │   │   ├── usePredict.ts
│   │   │   └── useFetch.ts
│   │   │
│   │   └── utils/
│   │       ├── constants.ts
│   │       └── helpers.ts
│   │
│   └── docker/
│       ├── Dockerfile             # Frontend container
│       └── .dockerignore
│
├── Dataset/
│   └── Detoxic.csv/
│       ├── train.csv
│       ├── test.csv
│       ├── test_labels.csv
│       └── sample_submission.csv
│
├── docker-compose.yml             # Orchestrate all services
├── .gitignore
├── PROJECT_PLAN.md                # This file
└── README.md
```

---

## 5. KEY API ENDPOINTS
### Authentication
```
POST   /api/auth/register           # User registration
POST   /api/auth/login              # User login
POST   /api/auth/logout             # User logout
POST   /api/auth/refresh            # Refresh JWT token
```

### Predictions
```
POST   /api/predict                 # Analyze comment (core feature)
GET    /api/predictions/{id}        # Get specific prediction
```

### Submissions
```
GET    /api/submissions             # User's history
GET    /api/submissions/{id}        # Get single submission
DELETE /api/submissions/{id}        # Delete submission
```

### Analytics & Dashboard
```
GET    /api/analytics/stats         # User stats
GET    /api/analytics/history       # Submission history
GET    /api/analytics/trends        # Trend data
```

### Admin (Protected)
```
GET    /api/admin/submissions       # All submissions
POST   /api/admin/review/{id}       # Review submission
GET    /api/admin/stats             # System stats
```

---

## 6. FRONTEND UI COMPONENTS (Zomato/Swiggy Style)

### Page: Landing/Dashboard
- Header with Logo + Navigation
- Hero Section: "Detect Toxic Comments in Real-Time"
- Main Comment Input Box (large, prominent)
- Recent Submissions Card
- Statistics Cards (Total analyzed, toxic detected, etc.)
- Footer

### Page: Comment Analysis
- Input Box (top)
- Real-time Character Counter
- Submit Button (prominent CTA)
- Results Panel:
  - Overall Toxicity Score (large percentage/gauge)
  - Category Breakdown (6 bars/cards)
  - Color coding (red=high toxicity, green=clean)
  - Action buttons (Save, Share, Report)

### Page: Dashboard/History
- Filter options (by date, by toxicity level)
- Table/Card view toggle
- Each submission shows:
  - Comment preview
  - Toxicity score
  - Categories detected
  - Timestamp
  - Actions (view full, delete)

### Page: User Profile/Analytics
- Statistics dashboard:
  - Total submissions
  - Toxic vs Clean comments
  - Category breakdown charts
  - Trends over time
  - Monthly activity

### Page: Admin Panel
- Moderation queue
- Bulk submission review
- System statistics
- User management (if needed)

---

## 7. ML MODEL DETAILS

### Model Options (Ranked by Performance):

#### Option 1: DistilBERT (RECOMMENDED)
- **Size:** 268MB
- **Speed:** Fast inference (~100ms)
- **Accuracy:** ~95%
- **Memory:** Low (good for production)
- **Training:** Pre-trained on toxic comments dataset

#### Option 2: RoBERTa
- **Size:** 498MB
- **Speed:** Medium (~150ms)
- **Accuracy:** ~97%
- **Memory:** Medium
- **Training:** Better general NLP performance

#### Option 3: XLNet
- **Size:** 736MB
- **Speed:** Slow (~300ms)
- **Accuracy:** ~98%
- **Memory:** High
- **Training:** Best accuracy but resource-heavy

### Recommendation: Use DistilBERT for initial deployment, optimize with RoBERTa later

### Model Pipeline:
```
Text Input 
    ↓
Preprocessing (lowercase, special char handling)
    ↓
Tokenization (BERT tokenizer)
    ↓
Model Inference (DistilBERT)
    ↓
Post-processing (sigmoid for probabilities)
    ↓
Results (6 probability scores 0-1)
```

---

## 8. IMPLEMENTATION STEPS

### Phase 1: Foundation (Week 1)
- [ ] Setup project structure
- [ ] Configure PostgreSQL database
- [ ] Create database models (SQLAlchemy)
- [ ] Setup FastAPI with basic routes
- [ ] Implement user authentication (JWT)
- [ ] Setup React frontend scaffold
- [ ] Configure Tailwind CSS

### Phase 2: Core ML Feature (Week 2)
- [ ] Load and test DistilBERT model
- [ ] Create prediction endpoint
- [ ] Build text preprocessing pipeline
- [ ] Implement caching for repeated predictions
- [ ] Build comment input component (frontend)
- [ ] Create results display component

### Phase 3: Data Persistence (Week 3)
- [ ] Implement submission save/retrieve
- [ ] Create prediction storage
- [ ] Build user history page
- [ ] Add filtering and sorting
- [ ] Implement delete functionality
- [ ] Add pagination

### Phase 4: Analytics & Dashboard (Week 4)
- [ ] Create statistics calculations
- [ ] Build analytics endpoints
- [ ] Design dashboard UI
- [ ] Implement charts (Chart.js or Recharts)
- [ ] Add trend analysis
- [ ] Build admin panel basics

### Phase 5: UI/UX Polish (Week 5)
- [ ] Design refinement (Zomato/Swiggy style)
- [ ] Responsive mobile design
- [ ] Animation and transitions
- [ ] Error handling UI
- [ ] Loading states
- [ ] Accessibility improvements

### Phase 6: Testing & Optimization (Week 6)
- [ ] API testing (pytest)
- [ ] Frontend testing (Jest/Vitest)
- [ ] Performance optimization
- [ ] Database query optimization
- [ ] Caching strategy
- [ ] Load testing

### Phase 7: Deployment (Week 7)
- [ ] Docker setup (backend + frontend)
- [ ] Docker Compose configuration
- [ ] Environment variables setup
- [ ] Database migrations
- [ ] CI/CD pipeline
- [ ] Deployment to server (AWS/Heroku/DigitalOcean)

---

## 9. TECH STACK COMPARISON TABLE

| Component | Technology | Why? |
|-----------|-----------|------|
| Backend | FastAPI | Modern, fast, async, great for ML |
| Frontend | React + TypeScript | Type-safe, component-reusable |
| Database | PostgreSQL | ACID compliance, JSON support, scalable |
| Styling | Tailwind CSS | Utility-first, responsive, professional |
| ML Model | DistilBERT | Fast, accurate, lightweight |
| Auth | JWT + bcrypt | Secure, stateless, industry standard |
| API Doc | Swagger | Auto-generated, interactive |
| Containerization | Docker | Consistent environment, easy deployment |

---

## 10. ENVIRONMENT SETUP CHECKLIST

```bash
Backend:
- [ ] Python 3.10+ installed
- [ ] PostgreSQL installed and running
- [ ] Virtual environment created
- [ ] All dependencies installed

Frontend:
- [ ] Node.js 18+ installed
- [ ] npm/yarn installed
- [ ] All dependencies installed

Local Development:
- [ ] Docker installed (optional but recommended)
- [ ] Git configured
- [ ] .env files created
- [ ] API keys ready (if needed)
```

---

## 11. SUCCESS METRICS

- **Performance:** Model inference < 200ms
- **Accuracy:** > 90% precision on toxic detection
- **UI/UX:** Page load < 2 seconds
- **Uptime:** 99% availability
- **User Experience:** Similar to Zomato/Swiggy dashboard

---

## 12. NEXT STEPS

1. ✅ You're reading this plan
2. → Let's start with **Phase 1: Foundation**
3. Setup database schema and backend structure
4. Create frontend scaffold
5. Build API endpoints one by one
6. Integrate ML model
7. Polish and deploy

**Ready to start implementing?** Let me know which phase to begin with!
