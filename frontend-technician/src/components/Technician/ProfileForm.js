import { useState } from 'react';
import axios from '../../api/axios';

function ProfileForm() {
  const [profile, setProfile] = useState({
    technician_id: 1,
    service_category: '',
    experience_years: 0,
    work_areas: [],
    phone_or_whatsapp: '',
    about: '',
    profile_image: '',
    age: 0,
    gender: '',
    qualifications: ''
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('/technician/profile', profile);
      alert('Profile created!');
    } catch (err) {
      alert('Profile already exists or error!');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Complete Your Technician Profile</h2>
      <select onChange={(e) => setProfile({ ...profile, service_category: e.target.value })}>
        <option>-- Select Category --</option>
        <option>Electrician</option>
        <option>Plumber</option>
        {/* Add more */}
      </select>
      <input placeholder="Years of Experience" type="number" onChange={(e) => setProfile({ ...profile, experience_years: parseInt(e.target.value) })} />
      <input placeholder="Areas (comma separated)" onChange={(e) => setProfile({ ...profile, work_areas: e.target.value.split(',') })} />
      <input placeholder="Phone or WhatsApp" onChange={(e) => setProfile({ ...profile, phone_or_whatsapp: e.target.value })} />
      <input placeholder="Age" type="number" onChange={(e) => setProfile({ ...profile, age: parseInt(e.target.value) })} />
      <input placeholder="Gender" onChange={(e) => setProfile({ ...profile, gender: e.target.value })} />
      <input placeholder="Qualifications" onChange={(e) => setProfile({ ...profile, qualifications: e.target.value })} />
      <textarea placeholder="About" onChange={(e) => setProfile({ ...profile, about: e.target.value })} />
      <input placeholder="Profile Image URL" onChange={(e) => setProfile({ ...profile, profile_image: e.target.value })} />
      <button type="submit">Submit Profile</button>
    </form>
  );
}

export default ProfileForm;
