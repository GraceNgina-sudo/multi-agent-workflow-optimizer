document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("queryForm");
  const queryInput = document.getElementById("query");
  const responseBox = document.getElementById("response");

  form.addEventListener("submit", async (event) => {
    event.preventDefault(); // prevent refresh

    // ✅ Check empty input
    if (!queryInput.value.trim()) {
      queryInput.classList.add("is-invalid");
      return;
    }
    queryInput.classList.remove("is-invalid");

    // ✅ Prepare payload exactly like your backend expects
    const payload = {
      query: queryInput.value.trim()
    };

    try {
      responseBox.classList.remove("d-none", "alert-danger");
      responseBox.classList.add("alert-info");
      responseBox.textContent = "Processing your request...";

      // ✅ Get base URL from meta tag
      const apiBase = document.querySelector('meta[name="api-base"]').content;
      const apiUrl = `${apiBase}/ai-simulate`;

      // ✅ Call backend
      const res = await fetch(apiUrl, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({query: queryInput.value.trim()}),
      });

      if (!res.ok) {
        throw new Error(`Server error: ${res.status}`);
      }

      const data = await res.json();

      console.log("Response JSON:", data);

      // ✅ Display server response
      responseBox.classList.remove("alert-info");
      responseBox.classList.add("alert-success");
      responseBox.textContent = data.response || "No response received.";
    } catch (err) {
      console.error("error during fetch:", err);
      responseBox.classList.remove("alert-info");
      responseBox.classList.add("alert-danger");
      responseBox.textContent = "Something went wrong. Please try again.";
    }
  });
});


