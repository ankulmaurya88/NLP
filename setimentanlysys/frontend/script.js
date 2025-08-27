async function analyzeSentiment() {
  const text = document.getElementById("inputText").value;
  if (!text.trim()) {
    alert("Please enter some text");
    return;
  }
// http://127.0.0.1:8000/sentiment/predict
  try {
    const response = await fetch("http://localhost:8000/sentiment/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ text })
    });

    const data = await response.json();
    document.getElementById("result").innerText =
      `Sentiment: ${data.sentiment}`;
  } catch (error) {
    document.getElementById("result").innerText = "Error connecting to backend!";
  }
}
