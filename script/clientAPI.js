const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = 3030;

// Middleware to parse JSON
app.use(bodyParser.json());

// POST endpoint
app.post('/greet', (req, res) => {
    const { text } = req.body;
    
    if (!text) {
        return res.status(400).send('Text is required');
    }
    
    res.send(`Hello, ${text}`);
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
