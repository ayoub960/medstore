document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");
    const submitBtn = document.querySelector("button[type='submit']");

    if (!form) return;

    form.addEventListener("submit", function (e) {

        let valid = true;

        // Get fields
        const inputs = form.querySelectorAll("input, textarea, select");

        // Remove old errors
        document.querySelectorAll(".error-msg").forEach(el => el.remove());

        inputs.forEach(input => {

            if (input.hasAttribute("required") && input.value.trim() === "") {
                showError(input, "This field is required");
                valid = false;
            }

            // Mobile validation
            if (input.name === "mobile_number") {
                const pattern = /^\d{10,11}$/;

                if (!pattern.test(input.value.trim())) {
                    showError(input, "Enter valid 10-11 digit mobile number");
                    valid = false;
                }
            }
        });

        if (!valid) {
            e.preventDefault();
            return;
        }

        // Loading effect
        if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.innerText = "Placing Order...";
        }

    });

    function showError(input, message) {

        const error = document.createElement("small");
        error.classList.add("error-msg");
        error.style.color = "red";
        error.style.display = "block";
        error.style.marginTop = "-8px";
        error.style.marginBottom = "10px";
        error.innerText = message;

        input.parentNode.appendChild(error);
    }

});