import { BrowserRouter, Routes, Route } from 'react-router-dom';
import SearchTechnicians from './components/User/SearchTechnicians';
import RegisterTechnician from './components/Technician/Register';
import ProfileForm from './components/Technician/ProfileForm';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<SearchTechnicians />} />
        <Route path="/technician/register" element={<RegisterTechnician />} />
        <Route path="/technician/profile" element={<ProfileForm />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
