console.log("NEW JS LOADED");

async function analyzeBug() {

    try {
        const response = await fetch("http://127.0.0.1:5000/analyze_bug", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                title: document.getElementById("bugTitle").value,
                description: document.getElementById("bugDescription").value,
                stack_trace: document.getElementById("stackTrace").value
            })
        });

        const data = await response.json();
        console.log("Response:", data);

        document.getElementById("result").innerHTML = `

<div class="report-container">

<h1 class="report-title">🤖 AI BUG ANALYSIS REPORT</h1>

<div class="status-box">
    <span>Analysis Status</span>
    <strong>${data.report.analysis_status}</strong>
</div>

<!-- Submitted Bug -->

<div class="report-card">

<h2>📝 Submitted Bug</h2>

<p><b>Title:</b> ${data.report.submitted_bug.title}</p>

<p><b>Description:</b></p>

<div class="description-box">
${data.report.submitted_bug.description}
</div>

<p><b>Stack Trace:</b></p>

<pre>${data.report.submitted_bug.stack_trace}</pre>

</div>

<!-- Triage -->

<div class="report-card">

<h2>🚦 Triage Analysis</h2>

<div class="info-grid">

<div class="info-label">Category</div>
<div class="info-value">${data.report.triage.category}</div>

<div class="info-label">Severity</div>
<div class="info-value">${data.report.triage.severity}</div>

<div class="info-label">Priority</div>
<div class="info-value">${data.report.triage.priority}</div>

<div class="info-label">Affected Module</div>
<div class="info-value">${data.report.triage.affected_module}</div>

<div class="info-label">Confidence Score</div>
<div class="info-value">${data.report.triage.confidence_score}%</div>


<div class="info-label">Reasoning</div>

<div class="info-value">
<ul class="reason-list">
<ul class="reason-list">
${(data.report.triage.reasoning || [])
    .map(item => `<li>${item}</li>`)
    .join("")}
</ul>

</div>

</div>

<!-- Log Analysis -->

<div class="report-card">

<h2>🧠 Log Analysis</h2>

<div class="info-grid">

<div class="info-label">Language</div>
<div class="info-value">${data.report.log_analysis.language}</div>

<div class="info-label">Exception</div>
<div class="info-value">${data.report.log_analysis.exception}</div>

<div class="info-label">Source File</div>
<div class="info-value">${data.report.log_analysis.file}</div>

<div class="info-label">Method</div>
<div class="info-value">${data.report.log_analysis.method}</div>

<div class="info-label">Line Number</div>
<div class="info-value">${data.report.log_analysis.line}</div>

<div class="info-label">Failure Point</div>
<div class="info-value">
${data.report.log_analysis.failure_point}
</div>

<div class="info-label">Affected Code Path</div>
<div class="info-value">
${(data.report.log_analysis.affected_code_path || []).join("<br>⬇<br>")}
</div>
</div>


<!-- Duplicate Bugs -->

<div class="report-card">

<h2>🔍 Similar Historical Bugs</h2>

<p><b>Total Similar Bugs Found:</b>
${data.report.duplicate_bugs.count}
</p>

${data.report.duplicate_bugs.matches.map((bug,index)=>`

<div class="duplicate-card">

<h3>Bug ${index+1}</h3>

<p><b>ID:</b> ${bug.bug_id}</p>

<p><b>Product:</b> ${bug.product}</p>

<p><b>Component:</b> ${bug.component}</p>

<p><b>Title:</b> ${bug.title}</p>

<p><b>Severity:</b> ${bug.severity}</p>

<p><b>Resolution:</b> ${bug.resolution}</p>

</div>

`).join("")}

</div>

<!-- Root Cause -->

<div class="report-card">

<h2>🎯 Root Cause Analysis</h2>

<p>${data.report.root_cause.root_cause}</p>

<h3>Impact</h3>

<p>${data.report.root_cause.impact}</p>

</div>

<!-- Remediation -->

<div class="report-card">

<h2>🛠 Recommended Fixes</h2>

<ul>

${data.report.remediation.recommendations.map(r=>`

<li>${r}</li>

`).join("")}

</ul>

</div>

<!-- Final Recommendation -->

<div class="report-card recommendation">

<h2>📌 Overall Recommendation</h2>

<p>

${data.report.overall_recommendation}

</p>

</div>

</div>

`;

    } catch (error) {
        console.error("Error:", error);
        document.getElementById("result").innerHTML = `

<div class="query-box">

<h3>📝 Submitted Bug</h3>

<p><b>Title:</b> ${data.query.title}</p>

<p><b>Description:</b> ${data.query.description}</p>

<p><b>Stack Trace:</b></p>

<pre>${data.query.stack_trace || "Not Provided"}</pre>

</div>

<h2 style="margin-top:20px;">🔍 Top Similar Bugs</h2>

${(data.duplicate_detection || []).map((item,i)=>`

<div class="result-card">

<h3 class="result-title">
🟢 Similar Bug #${i+1}
</h3>

<div class="info-grid">

<div class="info-label">Bug ID</div>
<div class="info-value">${item.bug_id}</div>

<div class="info-label">Product</div>
<div class="info-value">${item.product}</div>

<div class="info-label">Component</div>
<div class="info-value">${item.component}</div>

<div class="info-label">Title</div>
<div class="info-value">${item.title}</div>

<div class="info-label">Severity</div>

<div class="info-value">

<span class="badge ${
item.severity &&
item.severity.toLowerCase()=="critical"
?
"badge-critical"
:
"badge-normal"
}">
${item.severity}
</span>

</div>

<div class="info-label">Resolution</div>

<div class="info-value">

<span class="badge badge-fixed">

${item.resolution}

</span>

</div>

</div>

<h4>Description</h4>

<div class="description-box">

${(item.description || "No Description Available").substring(0,700)}

</div>

</div>

`).join("")}
`;
    }
}

document.getElementById("downloadReportBtn").addEventListener("click", function(){

    let report = document.getElementById("result").innerText;

    let file = new Blob(
        [report],
        {type:"text/plain"}
    );

    let link = document.createElement("a");

    link.href = URL.createObjectURL(file);

    link.download = "Bug_Analysis_Report.txt";

    link.click();

});

function downloadReport(){

    window.location.href =
    "http://127.0.0.1:5000/download_report";

}