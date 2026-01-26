# User Stories for Toodle Booking Project

## Must-Have

### 1. User Registration and Login
- As a user, I want to register and log in so I can book appointments and manage my bookings.
- **Acceptance Criteria:**
  - Users can sign up with a username and password.
  - Users can log in and log out securely.
  - Users see error messages for invalid login or registration.
- **Tasks:**
  - Create registration and login forms
  - Implement authentication views and templates
  - Add login/logout/signup buttons to the navbar

### 2. Book a Service/Appointment
- As a user, I want to book a service for a specific date and time so my request is recorded.
- **Acceptance Criteria:**
  - Users can view available services/resources.
  - Users can select a date and time for booking.
  - Bookings are saved and visible to the user.
- **Tasks:**
  - Create service/resource models
  - Build booking form and views
  - Display booking confirmation

### 3. View Booking History
- As a user, I want to see my past and upcoming bookings.
- **Acceptance Criteria:**
  - Users can view a list of their bookings.
  - Bookings show service, date, and status.
- **Tasks:**
  - Create booking list view and template
  - Filter bookings by user

## Should-Have

### 4. Modify or Cancel Bookings
- As a user, I want to modify or cancel my bookings within a certain timeframe.
- **Acceptance Criteria:**
  - Users can edit or delete bookings before a cutoff time.
  - Users receive feedback on successful changes.
- **Tasks:**
  - Add edit/delete booking views and templates
  - Enforce modification/cancellation rules

### 5. User Profile Management
- As a user, I want to update my profile information.
- **Acceptance Criteria:**
  - Users can edit their profile details (e.g., phone, email).
- **Tasks:**
  - Create user profile model and form
  - Add profile edit view and template

## Could-Have

### 6. Email Notifications
- As a user, I want to receive email notifications for booking confirmations and reminders.
- **Acceptance Criteria:**
  - Users receive emails after booking or changes.
- **Tasks:**
  - Integrate email backend
  - Send emails on booking actions

### 7. Admin Dashboard
- As an admin, I want to manage users, services, and bookings from a dashboard.
- **Acceptance Criteria:**
  - Admins can view and manage all bookings and users.
- **Tasks:**
  - Customize Django admin
  - Add reporting features

### 8. Responsive and Accessible UI
- As a user, I want the site to work well on all devices and be accessible.
- **Acceptance Criteria:**
  - The UI adapts to mobile and desktop.
  - Accessibility best practices are followed.
- **Tasks:**
  - Test and improve responsive design
  - Add accessibility features
