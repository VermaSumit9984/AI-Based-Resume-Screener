const dropArea = document.getElementById("dropArea");
const fileInput = document.getElementById("fileInput");

// ---- Click to open file dialog ----
dropArea.addEventListener("click", () => fileInput.click());

// ---- Highlight drop area ----
dropArea.addEventListener("dragover", (e) => {
  e.preventDefault();
  dropArea.classList.add("dragover");
});

dropArea.addEventListener("dragleave", () => {
  dropArea.classList.remove("dragover");
});

// ---- Handle dropped files ----
dropArea.addEventListener("drop", (e) => {
  e.preventDefault();
  dropArea.classList.remove("dragover");

  let droppedFiles = Array.from(e.dataTransfer.files);
  let existingFiles = Array.from(fileInput.files);

  let allFiles = existingFiles.concat(droppedFiles);

  // Create new FileList
  const dataTransfer = new DataTransfer();
  allFiles.forEach(file => dataTransfer.items.add(file));

  fileInput.files = dataTransfer.files;

  displayFiles();
});

// ---- Show selected file names ----
fileInput.addEventListener("change", displayFiles);

function displayFiles() {
  let fileListHTML = "<strong>Selected Resumes:</strong><br>";

  for (let file of fileInput.files) {
    fileListHTML += `📄 ${file.name}<br>`;
  }

  dropArea.innerHTML = fileListHTML;
}
