import React, { useState } from "react";
import axios from "../api/axios";

const TechnicianRegister = () => {
  const [form, setForm] = useState({
    id: 0,
    username: "",
    full_name: "",
    email: "",
    password: ""
  });

  const submit = async (e) => {
    e.preventDefault();
    try {
      await axios.post("/register/technician", form);
      alert("Registered successfully!");
    } catch {
      alert("Registration failed.");
    }
  };

  return (
    <form onSubmit={submit} className="p-6 max-w-xl mx-auto">
      <h2 className="text-2xl font-bold mb-4">Technician Register</h2>
      {Object.keys(form).map((field) => (
        <input
          key={field}
          type={field === "password" ? "password" : "text"}
          placeholder={field.replace("_", " ").toUpperCase()}
          className="input mb-2"
          value={form[field]}
          onChange={(e) => setForm({ ...form, [field]: e.target.value })}
        />
      ))}
      <button className="btn">Register</button>
    </form>
  );
};

export default TechnicianRegister;
