/* jshint esversion: 6 */

document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("form");

    if (!form) return;

    form.addEventListener("submit", (event) => {


        let errors = [];

        const fullName = document.getElementById("id_full_name");
        const email = document.getElementById("id_email");
        const phone = document.getElementById("id_phone");
        const bookingDate = document.getElementById("id_booking_date");
        const bookingTime = document.getElementById("id_booking_time");
        const guests = document.getElementById("id_number_of_guests");

        // Name validation
        if (fullName.value.trim().length < 4) {
            errors.push(
                "Name must contain at least 4 characters."
            );
        }

        // Email validation
        const emailPattern =
            /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (!emailPattern.test(email.value.trim())) {
            errors.push(
                "Please enter a valid email address."
            );
        }

        // Phone validation
        if (phone.value.trim() !== "") {

            const phonePattern =
                /^[0-9+\-\s()]{11,20}$/;

            if (!phonePattern.test(phone.value.trim())) {
                errors.push(
                    "Please enter a valid phone number."
                );
            }
        }

        // Date validation
        if (!bookingDate.value) {

            errors.push(
                "Please select a booking date."
            );

        } else {

            const selectedDate =
                new Date(bookingDate.value);

            const today = new Date();
            today.setHours(0, 0, 0, 0);

            if (selectedDate < today) {
                errors.push(
                    "Booking date cannot be in the past."
                );
            }

            const maxDate = new Date();
            maxDate.setMonth(
                maxDate.getMonth() + 6
            );

            if (selectedDate > maxDate) {
                errors.push(
                    "Bookings can only be made up to 6 months in advance."
                );
            }
        }

        // Time validation
        if (!bookingTime.value) {

            errors.push(
                "Please select a booking time."
            );

        } else {

            if (
                bookingTime.value < "12:00" ||
                bookingTime.value > "22:00"
            ) {
                errors.push(
                    "Bookings are available between 12:00 and 22:00 only."
                );
            }
        }

        // Guests validation
        const guestCount =
            parseInt(guests.value);

        if (
            isNaN(guestCount) ||
            guestCount < 1
        ) {
            errors.push(
                "Number of guests must be at least 1."
            );
        }

        if (guestCount > 12) {
            errors.push(
                "For parties larger than 12 guests, please contact us directly."
            );
        }

        if (errors.length > 0) {

            event.preventDefault();

            alert(errors.join("\n"));
        }

    });

});