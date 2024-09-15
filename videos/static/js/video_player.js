function searchSubtitles() {
  const query = document.getElementById("search-input").value;
  const videoId = window.location.pathname.split("/").pop();

  fetch(`/search/${videoId}/?q=${encodeURIComponent(query)}`)
    .then((response) => response.json())
    .then((data) => {
      const resultsDiv = document.getElementById("search-results");
      resultsDiv.innerHTML = "";
      data.results.forEach((result) => {
        const button = document.createElement("button");
        button.textContent = `${result.timestamp}: ${result.text}`;
        button.onclick = () => {
          document.getElementById("video-player").currentTime =
            result.timestamp;
        };
        resultsDiv.appendChild(button);
      });
    });
}
