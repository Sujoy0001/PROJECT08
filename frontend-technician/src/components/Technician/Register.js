import { useState } from 'react';
import axios from '../../api/axios';

function RegisterTechnician() {
  const [form, setForm] = useState({
    id: 0,
    username: '',
    full_name: '',
    email: '',
    password: ''
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('/register/technician', form);
      alert('Registered successfully!');
    } catch (err) {
      alert('Registration failed!');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Technician Registration</h2>
      <input placeholder="Username" onChange={(e) => setForm({ ...form, username: e.target.value })} />
      <input placeholder="Full Name" onChange={(e) => setForm({ ...form, full_name: e.target.value })} />
      <input placeholder="Email" type="email" onChange={(e) => setForm({ ...form, email: e.target.value })} />
      <input placeholder="Password" type="password" onChange={(e) => setForm({ ...form, password: e.target.value })} />
      <button type="submit">Register</button>
    </form>
  );
}

export default RegisterTechnician;
