import express from 'express';
import http from 'http';
import io from './socket.js';

const app = express();
const server = http.createServer(app);

// Use Railway's port in production, fallback to 4000 locally
const PORT = process.env.PORT || 4000;

// Attach socket.io to the HTTP server
io.attach(server);

server.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});


