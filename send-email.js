const nodemailer = require("nodemailer");
require("dotenv").config(); // Load environment variables from .env file

module.exports = async function handler(req, res) {
    if (req.method !== "POST") {
        return res.status(405).json({ error: "Method not allowed" });
    }

    const { name, email, message } = req.body;

    // Validate input
    if (!name || !email || !message) {
        return res.status(400).json({ error: "All fields are required." });
    }

    // Email transporter configuration
    const transporter = nodemailer.createTransport({
        service: "gmail",
        auth: {
            user: process.env.EMAIL_USER,  // Your Gmail address
            pass: process.env.EMAIL_PASS,  // App password (not regular Gmail password)
        },
    });

    const mailOptions = {
        from: process.env.EMAIL_USER,
        to: process.env.RECIPIENT_EMAIL || process.env.EMAIL_USER, // Send to yourself
        subject: "New Contact Form Submission",
        text: `Name: ${name}\nEmail: ${email}\n\nMessage:\n${message}`,
    };

    try {
        await transporter.sendMail(mailOptions);
        res.status(200).json({ success: true, message: "Email sent successfully!" });
    } catch (error) {
        console.error("Email Error:", error);
        res.status(500).json({ success: false, error: "Failed to send email. Please try again later." });
    }
};
