const API = "http://127.0.0.1:5000";


async function loadAnalysis() {

    const response = await fetch(
        `${API}/api/analysis`
    );

    const data = await response.json();

    document.getElementById("reviewCount").textContent =
        data.review_count;

    document.getElementById("themeCount").textContent =
        Object.keys(data.theme_counts).length;

    document.getElementById("featureCount").textContent =
        Object.keys(data.feature_counts).length;


    const painPoints =
        document.getElementById("painPoints");

    painPoints.innerHTML = "";

    const sortedPainPoints =
        Object.entries(data.pain_point_counts)
        .sort((a, b) => b[1] - a[1]);


    sortedPainPoints.forEach(
        ([pain, count]) => {

            const item = document.createElement("div");

            item.className = "item";

            item.innerHTML = `
                <strong>${pain}</strong>
                <p>${count} reviews</p>
                <div class="bar"
                     style="width: ${count * 10}%">
                </div>
            `;

            painPoints.appendChild(item);
        }
    );
}


async function loadPriorities() {

    const response = await fetch(
        `${API}/api/priorities`
    );

    const data = await response.json();

    const priorities =
        document.getElementById("priorities");

    priorities.innerHTML = "";


    data.forEach(
        (item, index) => {

            const div = document.createElement("div");

            div.className = "priority";

            div.innerHTML = `
                <div>
                    <strong>
                        ${index + 1}. ${item.feature}
                    </strong>

                    <p>
                        Frequency: ${item.frequency}
                        | Impact: ${item.impact}
                        | Effort: ${item.effort}
                    </p>
                </div>

                <div class="score">
                    ${item.priority_score}
                </div>
            `;

            priorities.appendChild(div);
        }
    );
}


loadAnalysis();
loadPriorities();