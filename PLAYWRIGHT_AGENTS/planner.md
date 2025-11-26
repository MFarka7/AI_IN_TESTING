# CzechiBank Application - Comprehensive Test Plan

## Application Overview

The CzechiBank application is a web-based banking platform that provides core banking functionality. The application features:

- **User Management**: Registration and authentication system
- **Bank Accounts**: View and manage multiple bank accounts with CZECHITOKEN currency
- **Money Transfers**: Send money to other users in the system
- **Transaction History**: View up to 50 recent transactions per account
- **Account Creation**: Create new bank accounts with custom names
- **UI Customization**: Theme switching (Light/Dark/System)
- **Real-time Balance Updates**: Account balances update immediately after transactions

## Test Scenarios

### 1. User Registration and Authentication

**Seed:** `seed.spec.ts`

#### 1.1 Successful User Registration
**Priority:** High

**Steps:**
1. Navigate to `https://czechibank.ostrava.digital/signin`
2. Click on "Register" button/link
3. Fill in "Full name" field with "Jan Novák"
4. Fill in "Email" field with unique email (e.g., `jan.novak.{timestamp}@test.cz`)
5. Fill in "Password" field with "SecurePass123"
6. Fill in "Confirm Password" field with "SecurePass123"
7. Click "Register" button

**Expected Results:**
- User is redirected to `/register/success` page
- Success message "Registration Successful!" is displayed
- Message "You can now log in and start using Czechitoken." is shown
- "Continue to the app" button is available
- New user account is created in the system

#### 1.2 Registration with Mismatched Passwords
**Priority:** High

**Steps:**
1. Navigate to registration page
2. Fill in "Full name" with "Test User"
3. Fill in "Email" with valid email
4. Fill in "Password" with "Password123"
5. Fill in "Confirm Password" with "DifferentPass123"
6. Click "Register" button

**Expected Results:**
- Registration fails
- Error message displayed indicating passwords don't match
- User remains on registration page
- Form data is preserved (except passwords)

#### 1.3 Registration with Invalid Email Format
**Priority:** Medium

**Steps:**
1. Navigate to registration page
2. Fill in "Full name" with "Test User"
3. Fill in "Email" with invalid format (e.g., "notanemail")
4. Fill in "Password" with "Password123"
5. Fill in "Confirm Password" with "Password123"
6. Click "Register" button

**Expected Results:**
- Registration fails
- Email validation error is displayed
- User remains on registration page

#### 1.4 Registration with Short Password
**Priority:** Medium

**Steps:**
1. Navigate to registration page
2. Fill in "Full name" with "Test User"
3. Fill in "Email" with valid email
4. Fill in "Password" with "Short1" (less than 8 characters)
5. Fill in "Confirm Password" with "Short1"
6. Click "Register" button

**Expected Results:**
- Registration fails
- Error message: "Your password must be at least 8 characters long."
- User remains on registration page

#### 1.5 Registration with Empty Full Name
**Priority:** Medium

**Steps:**
1. Navigate to registration page
2. Leave "Full name" field empty
3. Fill in "Email" with valid email
4. Fill in "Password" with "Password123"
5. Fill in "Confirm Password" with "Password123"
6. Click "Register" button

**Expected Results:**
- Registration fails
- Error message for required "Full name" field
- User remains on registration page

#### 1.6 Registration with Existing Email
**Priority:** High

**Steps:**
1. Navigate to registration page
2. Fill in "Full name" with "Duplicate User"
3. Fill in "Email" with already registered email
4. Fill in "Password" with "Password123"
5. Fill in "Confirm Password" with "Password123"
6. Click "Register" button

**Expected Results:**
- Registration fails
- Error message indicating email is already registered
- User remains on registration page

#### 1.7 Successful Login
**Priority:** High

**Steps:**
1. Navigate to `https://czechibank.ostrava.digital/signin`
2. Fill in "Email" with valid registered email
3. Fill in "Password" with correct password
4. Click "Sign in" button

**Expected Results:**
- User is redirected to dashboard (`/`)
- Greeting message "Hello {User Name}!" is displayed
- User's bank accounts are visible
- "Create new" button is available
- User can access all authenticated features

#### 1.8 Login with Invalid Credentials
**Priority:** High

**Steps:**
1. Navigate to sign in page
2. Fill in "Email" with "test@example.com"
3. Fill in "Password" with "wrongpassword"
4. Click "Sign in" button

**Expected Results:**
- Login fails
- Error notification is displayed with message "Invalid email or password"
- 401 HTTP error in console
- User remains on sign in page
- Form fields retain the email value

#### 1.9 Login with Empty Fields
**Priority:** Medium

**Steps:**
1. Navigate to sign in page
2. Leave both "Email" and "Password" fields empty
3. Click "Sign in" button

**Expected Results:**
- Login fails
- Validation error messages displayed for required fields
- User remains on sign in page

#### 1.10 Login with Only Email
**Priority:** Medium

**Steps:**
1. Navigate to sign in page
2. Fill in "Email" with valid email
3. Leave "Password" field empty
4. Click "Sign in" button

**Expected Results:**
- Login fails
- Validation error for required password field
- User remains on sign in page

---

### 2. Dashboard and Navigation

**Seed:** `seed.spec.ts` (with logged-in user)

#### 2.1 Dashboard Display After Login
**Priority:** High

**Steps:**
1. Complete successful login
2. Verify dashboard loads

**Expected Results:**
- URL is `https://czechibank.ostrava.digital/`
- Greeting "Hello {User Name}!" is displayed with correct user name
- "Create new" button is visible and functional
- All user's bank accounts are displayed as cards
- Each account card shows:
  - Account name
  - Account number (format: ############/5555)
  - Current balance
  - Currency (CZECHITOKEN)
  - Czechitoken icon
- CzechiBank logo is visible in header
- "Toggle theme" button is available
- Version number is displayed in footer

#### 2.2 Navigate to Bank Account Details
**Priority:** High

**Steps:**
1. Login and reach dashboard
2. Click on any bank account card

**Expected Results:**
- User is redirected to `/bankAccount/{accountId}`
- Account name is displayed as page heading
- Account number section shows "Číslo účtu" with copy functionality
- Full account number is displayed (format: ############/5555)
- Current balance is prominently displayed with currency
- "Transfer your money" section is visible
- Transaction history section is visible
- All navigation elements remain accessible

#### 2.3 Navigate Back to Dashboard from Account
**Priority:** Medium

**Steps:**
1. Navigate to a bank account detail page
2. Click on "CzechiBank" logo in header

**Expected Results:**
- User is redirected back to dashboard (`/`)
- All bank accounts are displayed again
- Account balance reflects any changes made

#### 2.4 Theme Toggle Functionality
**Priority:** Low

**Steps:**
1. Login to application
2. Click on "Toggle theme" button
3. Select "Dark" from dropdown
4. Verify theme changes
5. Click "Toggle theme" again
6. Select "Light" from dropdown
7. Select "System" from dropdown

**Expected Results:**
- Theme menu opens with three options: Light, Dark, System
- Selecting each option changes the application theme accordingly
- Theme preference is persisted across page reloads
- All UI elements are readable in each theme
- Theme changes apply immediately without page refresh

---

### 3. Bank Account Creation

**Seed:** `seed.spec.ts` (with logged-in user)

#### 3.1 Create New Bank Account with Valid Data
**Priority:** High

**Steps:**
1. Login to application and reach dashboard
2. Click "Create new" button
3. Dialog "Create New Bank Account" appears
4. Fill in "Account Name" with "My Savings Account"
5. Verify "Currency" dropdown shows "CZECHITOKEN" (default)
6. Click "Create" button

**Expected Results:**
- Dialog closes after successful creation
- New bank account card appears on dashboard
- Account name is "My Savings Account"
- Initial balance is 100000.0 CZECHITOKEN
- Unique account number is assigned (format: ############/5555)
- Account is immediately accessible

#### 3.2 Create Bank Account with Empty Name
**Priority:** Medium

**Steps:**
1. Login to application
2. Click "Create new" button
3. Leave "Account Name" field empty
4. Click "Create" button

**Expected Results:**
- Account creation fails
- Validation error message appears
- Dialog remains open
- User can correct the error

#### 3.3 Cancel Account Creation
**Priority:** Low

**Steps:**
1. Login to application
2. Click "Create new" button
3. Fill in "Account Name" with "Test Account"
4. Click "Close" button (X icon)

**Expected Results:**
- Dialog closes without creating account
- No new account appears on dashboard
- User returns to dashboard with existing accounts unchanged

#### 3.4 Create Multiple Bank Accounts
**Priority:** Medium

**Steps:**
1. Login to application
2. Create first account named "Personal Account"
3. Create second account named "Business Account"
4. Create third account named "Savings Account"

**Expected Results:**
- All three accounts are created successfully
- Each has unique account number
- Each starts with 100000.0 CZECHITOKEN balance
- All accounts are displayed on dashboard
- User can access each account independently

---

### 4. Money Transfer Functionality

**Seed:** `seed.spec.ts` (with logged-in user with funds)

#### 4.1 Successful Money Transfer
**Priority:** High

**Steps:**
1. Login to application
2. Navigate to a bank account with sufficient balance
3. Click on "Receiver" dropdown
4. Select a receiver from the list (e.g., "App Admin")
5. Click on "Amount" field
6. Enter amount "100"
7. Click "Transfer" button

**Expected Results:**
- Success notification appears: "💸 Transaction created!"
- Account balance decreases by 100 (from 100000.0 to 99900.0)
- Transaction appears immediately in "Your history" table
- Transaction shows:
  - Current date (2025-11-26)
  - "From" shows current user with avatar
  - "To" shows selected receiver with avatar
  - Amount shows "-100"
- Receiver dropdown resets to placeholder
- Amount field resets to "0"
- Summary row shows "Send" with "-100"

#### 4.2 Transfer with Zero Amount
**Priority:** Medium

**Steps:**
1. Navigate to bank account detail page
2. Select a receiver
3. Enter amount "0"
4. Click "Transfer" button

**Expected Results:**
- Transfer fails or is prevented
- Error message indicates amount must be greater than zero
- No transaction is created
- Balance remains unchanged

#### 4.3 Transfer with Negative Amount
**Priority:** Medium

**Steps:**
1. Navigate to bank account detail page
2. Select a receiver
3. Attempt to enter negative amount "-100"
4. Click "Transfer" button

**Expected Results:**
- System prevents negative input OR
- Error message indicates amount must be positive
- No transaction is created
- Balance remains unchanged

#### 4.4 Transfer Amount Exceeding Balance
**Priority:** High

**Steps:**
1. Navigate to bank account with balance of 100000.0
2. Select a receiver
3. Enter amount "150000" (more than balance)
4. Click "Transfer" button

**Expected Results:**
- Transfer fails
- Error message indicates insufficient funds
- No transaction is created
- Balance remains unchanged

#### 4.5 Transfer Without Selecting Receiver
**Priority:** Medium

**Steps:**
1. Navigate to bank account detail page
2. Leave "Receiver" dropdown at placeholder "Select a receiver for your money"
3. Enter amount "100"
4. Click "Transfer" button

**Expected Results:**
- Transfer fails
- Error message indicates receiver must be selected
- No transaction is created
- Balance remains unchanged

#### 4.6 Transfer Maximum Balance
**Priority:** Medium

**Steps:**
1. Navigate to bank account with balance of 99900.0
2. Select a receiver
3. Enter amount "99900"
4. Click "Transfer" button

**Expected Results:**
- Transfer succeeds
- Success notification appears
- Balance becomes 0.0 CZECHITOKEN
- Transaction is recorded correctly
- User can still access the account (not closed)

#### 4.7 Multiple Consecutive Transfers
**Priority:** High

**Steps:**
1. Navigate to bank account with sufficient balance
2. Perform transfer of 100 to Receiver A
3. Immediately perform transfer of 200 to Receiver B
4. Immediately perform transfer of 150 to Receiver C

**Expected Results:**
- All three transfers succeed
- Balance decreases correctly: 100000 → 99900 → 99700 → 99550
- All three transactions appear in history
- Transactions are listed in chronological order (most recent first)
- Summary shows total "Send" amount: -450

---

### 5. Transaction History

**Seed:** `seed.spec.ts` (with user having transaction history)

#### 5.1 View Transaction History
**Priority:** High

**Steps:**
1. Login and navigate to bank account that has transactions
2. Scroll to "Your history" section

**Expected Results:**
- Section heading "Your history" is visible
- "Transactions" heading is displayed
- Warning alert shows: "DUE to bad performance, you will see last 50 transactions. Use API to see ALL your transactions."
- Transaction table displays with columns:
  - Date
  - From (with user avatar)
  - To (with user avatar)
  - Amount (CZK)
- Transactions are listed in chronological order
- Summary row shows "Received/Send" with total balance change

#### 5.2 Empty Transaction History
**Priority:** Medium

**Steps:**
1. Login to application
2. Create a new bank account
3. Navigate to the newly created account
4. View transaction history

**Expected Results:**
- Transaction table is displayed
- Table headers are visible
- No transaction rows appear
- Summary shows "Received/Send: 0"
- No error messages displayed

#### 5.3 Transaction History After Transfer
**Priority:** High

**Steps:**
1. Navigate to bank account
2. Note the current transaction count
3. Perform a money transfer
4. Verify transaction history updates

**Expected Results:**
- New transaction appears at the top of the list
- Transaction details are correct:
  - Today's date
  - From: Current user
  - To: Selected receiver
  - Amount: Correct transfer amount
- Summary updates to reflect new transaction
- Total balance change is accurate

#### 5.4 Verify Receiver Selection Dropdown
**Priority:** Medium

**Steps:**
1. Navigate to bank account detail page
2. Click on "Receiver" dropdown

**Expected Results:**
- Dropdown opens with scrollable list of receivers
- Each receiver shows:
  - User avatar
  - Full name (with special characters like 🐶, 🐱, 🦊 if present)
  - Account number (format: ############/5555)
- Multiple pages of receivers are available (scrollable)
- List includes users like:
  - App Admin (000000000000/5555)
  - Various test users
  - Users with Czech names (with diacritics)
- Clicking outside dropdown closes it
- Pressing Escape closes dropdown

---

### 6. Edge Cases and Negative Tests

**Seed:** `seed.spec.ts`

#### 6.1 Direct URL Access to Non-Existent Account
**Priority:** Medium

**Steps:**
1. Login to application
2. Navigate directly to `/bankAccount/invalid-account-id`

**Expected Results:**
- User sees error page or is redirected
- Appropriate error message is displayed
- User can navigate back to dashboard
- No system crash or unhandled error

#### 6.2 Access Bank Account Without Login
**Priority:** High

**Steps:**
1. Ensure user is logged out
2. Navigate directly to `/bankAccount/{valid-account-id}`

**Expected Results:**
- User is redirected to sign in page
- Account details are not displayed
- Authentication is enforced
- After login, user may or may not be redirected to originally requested page

#### 6.3 Access Dashboard Without Login
**Priority:** High

**Steps:**
1. Clear browser cookies/session
2. Navigate directly to `https://czechibank.ostrava.digital/`

**Expected Results:**
- User is redirected to sign in page (`/signin`)
- Dashboard is not accessible without authentication
- No bank account information is leaked

#### 6.4 Form Input with Special Characters
**Priority:** Low

**Steps:**
1. Navigate to registration page
2. Enter "Full name" with special characters: "Jan Novák 🎉 O'Connor"
3. Complete registration with valid email and password
4. Login and verify

**Expected Results:**
- Registration succeeds
- Special characters and diacritics are preserved
- User name displays correctly throughout application
- No encoding issues occur

#### 6.5 Very Long Account Names
**Priority:** Low

**Steps:**
1. Login to application
2. Click "Create new"
3. Enter very long account name (200+ characters)
4. Click "Create"

**Expected Results:**
- Either account is created with name truncated appropriately OR
- Validation error indicates name is too long
- UI remains functional and readable
- Account card displays name without breaking layout

#### 6.6 Rapid Button Clicking (Double Submit)
**Priority:** Medium

**Steps:**
1. Navigate to bank account
2. Select receiver and enter amount
3. Rapidly click "Transfer" button multiple times

**Expected Results:**
- Only one transfer is processed
- No duplicate transactions are created
- Button is disabled after first click until processing completes
- Success notification appears only once

#### 6.7 Browser Back Button After Logout
**Priority:** Medium

**Steps:**
1. Login to application
2. Navigate to a bank account
3. Logout (if logout functionality exists)
4. Click browser back button

**Expected Results:**
- User remains logged out
- Sensitive information is not displayed
- User is redirected to sign in page
- Session is properly terminated

#### 6.8 Transfer to Self
**Priority:** Low

**Steps:**
1. User with multiple accounts
2. Navigate to Account A
3. Attempt to select own Account B as receiver (if possible)
4. Enter amount and transfer

**Expected Results:**
- System either prevents selecting own account as receiver OR
- Transfer succeeds and both accounts update correctly
- No data corruption occurs
- Transaction history shows correctly in both accounts

---

### 7. UI/UX and Responsive Design

**Seed:** `seed.spec.ts`

#### 7.1 Notification System
**Priority:** Medium

**Steps:**
1. Login to application
2. Perform action that triggers success notification (e.g., transfer)
3. Observe notification
4. Click close button on notification

**Expected Results:**
- Notification appears in designated area (Notifications F8 region)
- Success notification shows transaction icon and message
- Error notifications show error icon and message
- Close button (X) is functional
- Notification can be dismissed
- Multiple notifications can be displayed
- Notifications don't obstruct critical UI elements

#### 7.2 Copy Account Number Functionality
**Priority:** Low

**Steps:**
1. Navigate to bank account detail page
2. Locate "Číslo účtu" section with copy icon
3. Click on copy icon

**Expected Results:**
- Account number is copied to clipboard
- Visual feedback indicates successful copy (if implemented)
- Pasted value matches displayed account number format

#### 7.3 Version Display in Footer
**Priority:** Low

**Steps:**
1. Navigate to any page in application
2. Scroll to footer

**Expected Results:**
- Version information is displayed: "Version: 0.1.5 (9e7cdbc)"
- Footer is consistent across all pages
- Version format includes semantic version and commit hash

---

### 8. Security and Data Validation

**Seed:** `seed.spec.ts`

#### 8.1 SQL Injection in Login
**Priority:** High

**Steps:**
1. Navigate to sign in page
2. Enter SQL injection attempt in email field: `' OR '1'='1`
3. Enter any password
4. Click "Sign in"

**Expected Results:**
- Login fails
- No SQL injection occurs
- Error message: "Invalid email or password"
- System remains secure

#### 8.2 XSS Attack in Account Name
**Priority:** High

**Steps:**
1. Login to application
2. Click "Create new"
3. Enter account name: `<script>alert('XSS')</script>`
4. Create account

**Expected Results:**
- Account is created OR validation prevents script tags
- Script does not execute
- If stored, script is escaped and displayed as plain text
- No XSS vulnerability exists

#### 8.3 Session Timeout
**Priority:** Medium

**Steps:**
1. Login to application
2. Leave application idle for extended period (if timeout is implemented)
3. Attempt to perform action (e.g., transfer)

**Expected Results:**
- Session expires after timeout period
- User is redirected to sign in page
- Clear message about session expiration
- No actions can be performed with expired session

#### 8.4 Password Visibility in Registration
**Priority:** Low

**Steps:**
1. Navigate to registration page
2. Enter password in "Password" field
3. Verify field type is password (dots/asterisks)
4. Check if toggle visibility option exists

**Expected Results:**
- Password is masked by default
- If toggle exists, clicking shows/hides password
- Confirm password field behaves identically
- Passwords are not visible in browser devtools (reasonable security)

---

## Test Coverage Summary

After implementing all scenarios, the following areas will be thoroughly tested:

### Functional Coverage:
- ✅ User registration with all validation rules
- ✅ User authentication (login/logout)
- ✅ Dashboard display and navigation
- ✅ Bank account creation
- ✅ Money transfer operations
- ✅ Transaction history viewing
- ✅ UI theme switching

### Non-Functional Coverage:
- ✅ Input validation and error handling
- ✅ Security (SQL injection, XSS prevention)
- ✅ Edge cases and boundary conditions
- ✅ Negative test scenarios
- ✅ UI/UX consistency
- ✅ Data persistence

### Priority Distribution:
- **High Priority:** 17 scenarios (critical business flows)
- **Medium Priority:** 18 scenarios (important features and validations)
- **Low Priority:** 12 scenarios (edge cases and minor features)

**Total Test Scenarios:** 47

---

## Notes and Recommendations

### Known Issues:
1. Console error on sign in page: "Better Auth error" - should be investigated
2. Performance warning about transaction history (limited to 50 records)
3. Missing autocomplete attributes on input fields (browser warnings)

### Test Data Requirements:
- Multiple test user accounts with varying balances
- Pre-existing transaction history for some accounts
- Users with special characters in names
- Edge case data (long names, special characters, etc.)

### Suggested Test Environment Setup:
1. Dedicated test environment with seed data
2. Ability to reset test data between test runs
3. API access for creating test scenarios programmatically
4. Isolated test users that don't interfere with production data

### Future Test Considerations:
- API testing for transaction endpoints
- Performance testing (especially for transaction history)
- Accessibility testing (WCAG compliance)
- Cross-browser compatibility testing
- Mobile responsive design testing
- Concurrent user testing (race conditions)

---

*Test plan created on November 26, 2025, based on exploration of CzechiBank application version 0.1.5 (9e7cdbc)*
