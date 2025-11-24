// ========================
// JRAVIS DASHBOARD JS
// Fetches data from backend
// ========================

async function loadSystemStatus() {
    const data = await apiGet("/dashboard/status");
    document.getElementById("system-status").innerHTML = JSON.stringify(
        data,
        null,
        2,
    );
}

async function loadEarnings() {
    const data = await apiGet("/earnings/all");
    document.getElementById("earnings").innerHTML = JSON.stringify(
        data,
        null,
        2,
    );
}

async function loadWallets() {
    const data = await apiGet("/earnings/wallets");
    document.getElementById("wallets").innerHTML = JSON.stringify(
        data,
        null,
        2,
    );
}

async function loadPayout() {
    const data = await apiGet("/payout/status");
    document.getElementById("payout").innerHTML = JSON.stringify(data, null, 2);
}

async function loadInvoices() {
    const data = await apiGet("/invoice/list");
    document.getElementById("invoices").innerHTML = JSON.stringify(
        data,
        null,
        2,
    );
}

// Load everything on startup
loadSystemStatus();
loadEarnings();
loadWallets();
loadPayout();
loadInvoices();
