## The Booking Table

The Booking Table is a restaurant booking website project designed to showcase full-stack web development skills using Django, HTML, CSS, Bootstrap, JavaScript, and database integration. The website provides users with a simple and convenient way to explore the restaurant menu, learn about the restaurant, and reserve tables online.

The project focuses on usability, responsive design, and efficient booking management. Users can browse menu categories, view restaurant information, and complete an online reservation form. The website is designed as an educational portfolio project demonstrating practical implementation of a booking system and CRUD functionality.

The purpose of this project is to demonstrate how a restaurant website can combine an attractive user interface with dynamic functionality through Django. The site allows users to make reservations while providing restaurant information in a clear and accessible format. It showcases skills such as database management, form handling, validation, responsive layouts, and user-focused design.

**Project Focus**

- Creating a responsive and accessible restaurant website.
- Implementing a booking system using Django forms and models.
- Practicing database management and CRUD functionality.
- Providing an intuitive user experience through clear navigation and modern design.
- Demonstrating server-side rendering and dynamic content management.

## Business Goals

- Promote the restaurant and its menu offerings.
- Provide customers with an easy online reservation process.
- Display restaurant contact information and opening hours.
- Demonstrate practical use of Django for booking management.

## User Goals

- View the restaurant menu and available dishes.
- Learn about restaurant contact details and opening hours.
- Reserve a table quickly and easily online.
- Receive confirmation after successfully submitting a reservation.

## Strategy

The strategy focuses on creating an elegant and welcoming restaurant website that encourages users to make reservations. The design prioritises simplicity, accessibility, and responsiveness across all devices. Django functionality supports form submission, booking confirmation, and database integration while maintaining a smooth user experience.

## Scope

**Must Have**

- Homepage with hero section and call-to-action button.
- Restaurant menu organised into categories.
- Online booking form connected to the database.
- Booking confirmation page displaying reservation details.
- Restaurant contact information section.
- Opening hours section.
- Responsive design using Bootstrap.

**Nice to Have**

- Booking management dashboard for administrators.
- Email confirmation after reservation submission.
- Customer account system.
- Online menu filtering and search.
- Google Maps integration showing restaurant location.
- Table availability checker.
- Customer reviews and ratings.

## Structure

The website structure guides users from discovering the restaurant to completing a reservation.

**Homepage**

- Hero image and welcome message.
- "Reserve Your Table" call-to-action button.
- Menu preview.
- Contact information.
- Opening hours.

**Booking Page**

- Reservation form.
- Customer details input.
- Date and time selection.
- Number of guests selection.
- Message require reservation.
- Form validation.

**Booking Confirmation Page**

- Confirmation message.
- Reservation details summary.
- Button to edit reservation.
- Button back to homepage.

**Footer**

- Copyright information.
- Navigation links.
- Contact details.

## Information Architecture

**Navigation**

Sticky navigation bar containing:

**Home | Menu | Contact | Book Now**

## Page Hierarchy

### Homepage

- Hero Section
- Menu Section
- Contact Information
- Opening Hours

### Booking Page

- Reservation Form
- Validation Messages

### Confirmation Page

- Booking Summary
- Return Home Button
- Edit Reservation Button

### Interaction

- Navigation links for smooth browsing.
- Form validation for reservation submissions.
- Dynamic booking confirmation page.
- Responsive menu cards with hover effects.
- Mobile-friendly navigation menu.

## Skeleton

### Priority Content**

**High Priority**

- Reserve Your Table call-to-action button.
- Online booking form.
- Restaurant menu.
- Contact information.
- Medium Priority
- Opening hours section.
- Booking confirmation page.

**Low Priority**

- Footer with additional information and navigation links.
- Future enhancements such as Google Maps and customer reviews.

## User Stories

### User Story 1: View Restaurant Overview

**Story:**

As a visitor I can view the restaurant homepage so that I can quickly understand what the restaurant offers.

**Acceptance Criteria:**

- The homepage displays restaurant name, short description, and branding.
- The homepage shows address and contact information.
- The homepage shows opening hours.
- The homepage contains a clear "Book a Table" button linking to booking page.
- The page is responsive on mobile and desktop.

### User Story 2: Submit a Booking Request

**Story:**

As a customer I can submit a booking request form so that I can request a table reservation.

**Acceptance Criteria:**

- Form includes required fields: name, email/phone, date request, time request, number of guests.
- Form includes optional field: special requests/message.
- Form cannot be submitted with empty required fields.
- Validation errors are shown if invalid data is entered.
- On successful submission, request is saved in the database.
- User sees a success message after submission and can edit reservation details.

### User Story 3: Admin View Booking Requests

**Story:**

As an admin I can view all booking requests so that I can respond and manage reservations.

**Acceptance Criteria:**

- Admin can view booking requests in Django Admin or a dashboard.
- Requests show key info: customer name, date, time, guests, message.
- Requests are ordered by newest first.

### User Story 4: Admin Update Request Status

**Story:**

As an admin I can update the request status so that I can track whether the booking is confirmed or rejected.

**Acceptance Criteria:**

- Each request has a status (Pending, Confirmed, Rejected).
- Default status is Pending when created.
- Admin can update the status manually.
- Updated status is saved and displayed correctly.

### User Story 5: Admin Manage Restaurant Info

**Story:**

As an admin I can update restaurant information so that the website stays accurate.

**Acceptance Criteria:**

- Admin can edit restaurant details (address, phone, email).
- Admin can update opening hours.
- Changes are reflected on the public website.