document.getElementById("bugForm").addEventListener("submit", function(event) {

    // Prevent page refresh
    event.preventDefault();

    // Get form values
    const bugTitle = document.getElementById("bugTitle").value;
    const bugDescription = document.getElementById("bugDescription").value;
    const stackTrace = document.getElementById("stackTrace").value;

    // Get uploaded file
    const bugFile = document.getElementById("bugFile").files[0];

    console.log("Bug Title:", bugTitle);
    console.log("Bug Description:", bugDescription);
    console.log("Stack Trace:", stackTrace);

    if (bugFile) {
        console.log("Uploaded File:", bugFile.name);
    } else {
        console.log("No file uploaded.");
    }

    alert("Bug details captured successfully! Backend integration will be added next.");
});