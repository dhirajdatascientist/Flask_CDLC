## Flask_WTF(L3)

---

**Question 1:** 
Create a Flask-WTF form named `RegistrationForm` with the following fields:

1. `username` - a text field with a label "Username".
2. `email` - an email field with a label "Email Address".
3. `password` - a password field with a label "Password".
4. `confirm_password` - a password field with a label "Confirm Password".

Add validators to ensure that:
- All fields are required.
- The `email` is a valid email address.
- The `password` and `confirm_password` fields match.

---

**Question 2:** 
In Flask, what purpose does `form.hidden_tag()` serve when used within a form rendered in a Jinja2 template, and why is it essential when dealing with Flask-WTF forms?

---

**Question 3:** 
Using Flask-WTF, how would you implement a CSRF protection token in your form? Explain both the backend changes (in the Flask app) and the frontend changes (in the HTML template).