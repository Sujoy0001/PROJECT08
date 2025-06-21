import React, { useState } from "react";
import axios from "../api/axios";

const TechnicianProfile = () => {
  const [profile, setProfile] = useState({
    technician_id: 0,
    service_category: "",
    experience_years: 0,
    work_areas: "",
    phone_or_whatsapp: "",
    about: "",
    profile_image: "",
    age: 0,
    gender: "",
    qualifications: ""
  });

  const submit = async (e) => {
    e.preventDefault();
    const payload = {
      ...profile,
      work_areas: profile.work_areas.split(",").map((a) => a.trim())
    };
    try {
      await axios.post("/technician/profile", payload);
      alert("Profile submitted!");
    } catch {
      alert("Failed to submit profile.");
    }
  };

  return (
    <form onSubmit={submit} className="p-6 max-w-xl mx-auto">
      <h2 className="text-2xl font-bold mb-4">Complete Technician Profile</h2>
      {Object.keys(profile).map((field) => (
        <input
          key={field}
          type="text"
          placeholder={field.replace(/_/g, " ").toUpperCase()}
          className="input mb-2"
          value={profile[field]}
          onChange={(e) => setProfile({ ...profile, [field]: e.target.value })}
        />
      ))}
      <button className="btn">Submit</button>
    </form>
  );
};

export default TechnicianProfile;
