document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the form from doing the default submit (GET request)

    // Gather form data
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const message = document.getElementById('message').value;
    console.log(name,message,email,phone)
    // Send AJAX request using fetch
    fetch('store/submit-form/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCookie('csrftoken')  // Send CSRF token if required by Django
        },
        body: `name=${encodeURIComponent(name)}&email=${encodeURIComponent(email)}&phone=${encodeURIComponent(phone)}&message=${encodeURIComponent(message)}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert('Form submitted successfully!');
        } else {
            alert('Error submitting form');
        }
    })
    .catch(error => console.error('Error:', error));
});

// Function to get CSRF token if CSRF protection is enabled
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.getElementById("login-form").addEventListener("submit", function(e) {
    e.preventDefault();  // Prevent form from submitting the default way

    const email = document.getElementById("emailId").value;
    const password = document.getElementById("password").value;
    console.log("Email:", email);
    console.log("Password:", password);

    // Get CSRF token from the cookie
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    console.log("CSRF Token:", csrftoken);

    fetch('/Userauth/UserLogin/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            username: email,
            password: password
        })
    })
    .then(response => {
        console.log("Response Status:", response.status); // Log the status code
        return response.json();
    })
    .then(data => {
        console.log("Response Data:", data); // Log the response data
        if (data.success) {
            alert("Login successful");
            // Redirect or update UI
        } else {
            alert("Login failed: " + data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
