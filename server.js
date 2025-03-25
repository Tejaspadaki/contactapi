const express = require("express");
const cors = require("cors");
const sendEmail = require("./send-email"); // Import send-email function

const app = express();
app.use(express.json());
app.use(cors());

app.post("/send-email", sendEmail);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
