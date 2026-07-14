# Framework Design

## Architecture

The framework follows the Page Object Model (POM) design pattern to improve maintainability and code reusability.

---

## Components

### Pages

Contains all page objects.

Examples:

- Login Page
- Dashboard Page
- Project Page

---

### Tests

Contains:

- Web Tests
- API Tests
- Integration Tests

---

### Utils

Contains reusable utilities such as:

- API Client
- Browser Factory
- Configuration Reader
- Helper Functions

---

### Config

Stores:

- Environment URLs
- BrowserStack Configuration
- Test Environment Details

---

## Design Principles

- Reusable components
- Modular structure
- Easy maintenance
- Scalable framework
- Separation of concerns
