import React, { useState } from "react";
import axios from "../api/axios";

const UserSearch = () => {
  const [area, setArea] = useState("");
  const [category, setCategory] = useState("");
  const [results, setResults] = useState([]);

  const search = async () => {
    try {
      const res = await axios.get(`/technicians/search?area=${area}&category=${category}`);
      setResults(res.data.results || []);
    } catch (err) {
      alert("No results or an error occurred.");
    }
  };

  return (
    <div className="p-6 max-w-xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Search Technicians</h1>
      <input
        className="input mb-2"
        placeholder="Enter Area"
        value={area}
        onChange={(e) => setArea(e.target.value)}
      />
      <select
        className="input mb-2"
        value={category}
        onChange={(e) => setCategory(e.target.value)}
      >
        <option value="">-- Select Category --</option>
        <option>Electrician</option>
        <option>Plumber</option>
        <option>AC Repair</option>
      </select>
      <button className="btn" onClick={search}>Search</button>

      <div className="mt-4 space-y-4">
        {results.map((tech) => (
          <div key={tech.technician_id} className="p-4 bg-gray-100 rounded shadow">
            <h3 className="font-bold">
              {tech.full_name} ({tech.username})
            </h3>
            <p>Category: {tech.service_category}</p>
            <p>Areas: {tech.work_areas.join(", ")}</p>
            <p>Experience: {tech.experience_years} years</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default UserSearch;
