passwordInput.addEventListener('input', function() {
    const password = this.value;
    let message = '';
    let strength = 0;

    if (password.length >= 8) strength++;
    if (password.match(/[a-z]+/)) strength++;
    if (password.match(/[A-Z]+/)) strength++;
    if (password.match(/[0-9]+/)) strength++;
    if (password.match(/[$@#&!]+/)) strength++;

    switch (strength) {
        case 0:
        case 1:
            message = 'Very weak';
            break;
        case 2:
            message = 'Weak';
            break;
        case 3:
            message = 'Medium';
            break;
        case 4:
            message = 'Strong';
            break;
        case 5:
            message = 'Very strong';
            break;
    }

    // Display the message (you'll need to add an element to show this)
    document.getElementById('passwordStrength').textContent = message;

    if (password.length < 8) {
        this.setCustomValidity('This is password for inventory so keep it more than 8 characters.');
    } else if (/^\d+$/.test(password)) {
        this.setCustomValidity('Password can\'t be entirely numeric.');
    } else {
        this.setCustomValidity('');
    }
});