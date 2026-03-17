### OpenSecret
A simple help desk portal where users can submit support tickets. The application uses JWT tokens for session management, but something seems off about how they're implemented. Can you find the security flaw?


Category: Web<br>
Difficulty: Very Easy

---

#### Flag
> HTB{0p3n_s3cr3ts_ar3_n0t_s3cr3ts}

The website allows you to submit a help desk ticket. The JWT secret key is hardcoded directly into the webpage’s source code, which is insecure because anyone can view it and forge valid tokens.

```javascript
// JWT Secret Key
const SECRET_KEY = "HTB{0p3n_s3cr3ts_ar3_n0t_s3cr3ts}";

// Helper function to convert string to Base64URL
function base64url(str) {
return btoa(str)
    .replace(/\+/g, "-")
    .replace(/\//g, "_")
    .replace(/=/g, "");
}

// Generate a JWT session token for the user
async function generateJWT() {
// Check if user already has a token
const existingToken = document.cookie
    .split("; ")
    .find((row) => row.startsWith("session_token="));

if (existingToken) {
    console.log("Session token already exists");
    return;
}

// Create a random guest username
const username = "guest_" + Math.floor(Math.random() * 10000);

// JWT Header
const header = { alg: "HS256", typ: "JWT" };

// JWT Payload
const payload = { username: username };

// Encode header and payload
const encodedHeader = base64url(JSON.stringify(header));
const encodedPayload = base64url(JSON.stringify(payload));
const data = encodedHeader + "." + encodedPayload;

// Sign with SECRET_KEY using HMAC-SHA256
const key = await crypto.subtle.importKey(
    "raw",
    new TextEncoder().encode(SECRET_KEY),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"]
);

const signature = await crypto.subtle.sign(
    "HMAC",
    key,
    new TextEncoder().encode(data)
);

// Encode signature
const encodedSignature = base64url(
    String.fromCharCode(...new Uint8Array(signature))
);

// Complete JWT token
const token = data + "." + encodedSignature;

// Store token in cookie
document.cookie = `session_token=${token}; path=/; max-age=86400`;

console.log("Generated session for:", username);
}

// Generate JWT token on page load
generateJWT();

// Handle ticket submission
document
.getElementById("submit-btn")
.addEventListener("click", async (event) => {
    event.preventDefault();

    const name = document.getElementById("ticket-name").value;
    const description =
        document.getElementById("ticket-desc").value;

    const response = await fetch("/submit-ticket", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ name, description }),
    });

    const result = await response.json();
    document.getElementById("message-display").textContent =
        result.message || "Ticket submitted successfully!";
});
```

---