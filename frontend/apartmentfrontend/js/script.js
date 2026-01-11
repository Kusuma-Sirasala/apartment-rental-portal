const API_URL = "http://127.0.0.1:5000/api";

async function loadApartments() {
  try {
    const res = await fetch(`${API_URL}/apartments`);
    const apartments = await res.json();

    const container = document.getElementById("apartments");
    container.innerHTML = "";

    apartments.forEach(ap => {
      const card = document.createElement("div");
      card.className = "bg-white rounded shadow p-4";

      card.innerHTML = `
        <img src="${ap.image}" class="w-full h-40 object-cover rounded mb-3">
        <h3 class="text-lg font-bold">${ap.name}</h3>
        <p class="text-gray-600">${ap.bhk}</p>
        <p class="font-semibold text-green-600">₹${ap.rent}</p>
        <button class="bg-blue-600 text-white w-full mt-3 py-2 rounded">
          Book Now
        </button>
      `;

      container.appendChild(card);
    });

  } catch (err) {
    console.error(err);
    alert("Failed to load apartments");
  }
}

window.onload = loadApartments;