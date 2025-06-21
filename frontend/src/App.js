import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import UserSearch from "./components/UserSearch";
import TechnicianRegister from "./components/TechnicianRegister";
import TechnicianProfile from "./components/TechnicianProfile";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<UserSearch />} />
        <Route path="/technician/register" element={<TechnicianRegister />} />
        <Route path="/technician/profile" element={<TechnicianProfile />} />
      </Routes>
    </Router>
  );
};

export default App;
