const API_BASE = "https://your-backend-url.onrender.com";
// Replace with actual Render backend URL

async function apiGet(path) {
    try {
        const response = await fetch(API_BASE + path);
        return await response.json();
    } catch (err) {
        console.error("API error:", err);
        return { error: true };
    }
}
