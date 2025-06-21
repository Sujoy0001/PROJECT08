import { useState } from 'react';
import axios from '../../api/axios';

function SearchTechnicians() {
  const [area, setArea] = useState('');
  const [category, setCategory] = useState('');
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    try {
      const res = await axios.get(`/technicians/search?area=${area}&category=${category}`);
      setResults(res.data.results || []);
    } catch (err) {
      alert("No technicians found or error occurred.");
      setResults([]);
    }
  };

  return (
    <div>
      <h2>Find Technicians</h2>
      <input value={area} onChange={(e) => setArea(e.target.value)} placeholder="Area" />
      <select value={category} onChange={(e) => setCategory(e.target.value)}>
        <option value="">-- Select Category --</option>
        <option value="Electrician">Electrician</option>
        <option value="AC Repair">AC Repair</option>
        <option value="Carpenter">Carpenter</option>
        {/* Add more categories */}
      </select>
      <button onClick={handleSearch}>Search</button>

      <div>
        {results.map((tech) => (
          <div key={tech.technician_id} style={{ border: "1px solid #ccc", margin: "10px", padding: "10px" }}>
            <h3>{tech.full_name} ({tech.username})</h3>
            <p>Category: {tech.service_category}</p>
            <p>Area: {tech.work_areas.join(", ")}</p>
            <p>Experience: {tech.experience_years} years</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default SearchTechnicians;
