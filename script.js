document.getElementById("queryForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const query = document.getElementById("query").value.trim();
    const responseBox = document.getElementById("response");
    const btn = this.querySelector(".btn");

    if (!query) return;

    btn.disabled = true;
    responseBox.classList.remove("d-none");
    responseBox.textContent = "Processing…";

    try {
        const res = await fetch("http://127.0.0.1:8000/ai-simulate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ user_input: query }) 
        });

        if (!res.ok) {
            throw new Error(`HTTP error! status: ${res.status}`);
        }

        const data = await res.json();
        responseBox.textContent = JSON.stringify(data, null, 2);

    } catch (error) {
        if (error instanceof TypeError && error.message.includes("fetch")) {
            responseBox.textContent = `Network Error: Could not connect to the server. Make sure backend is running on http://127.0.0.1:8000`;
        } else {
            responseBox.textContent = `Error: ${error.message}`;
        }
    } finally {
        btn.disabled = false;
    }
});