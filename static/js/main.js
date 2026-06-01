document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("form");

    if (!form) return;

    form.addEventListener("submit", (event) => {

        const fullName =
            document.getElementById("id_full_name");

        if (fullName.value.trim().length < 2) {

            event.preventDefault();

            alert(
                "Please enter a valid name."
            );
        }

    });

});